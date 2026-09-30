import json,re,pathlib,datetime,collections,concurrent.futures,urllib.parse,urllib.request,sys
edit=len(sys.argv)>1
a=json.load(open('fmhy_edit_candidates.json' if edit else 'fmhy_candidates.json'));docs=pathlib.Path('fmhy-current-source/docs')
previous=json.load(open('fmhy_page_checks.json')) if edit else []
checked_urls={e['url'] for e in previous}
current='\n'.join(p.read_text() for p in docs.glob('*.md') if p.name not in ['storage.md','unsafe.md','posts.md','sandbox.md'])
current_hosts=set(urllib.parse.urlsplit(u).netloc.lower().removeprefix('www.') for u in re.findall(r'https?://[^\s)<>]+',current))
unsafe=(docs/'unsafe.md').read_text()
groups=collections.defaultdict(list)
for e in a:
 try:host=urllib.parse.urlsplit(e['url']).netloc.lower().removeprefix('www.')
 except ValueError:e['malformed_url']=True;continue
 e['same_host_in_current']=host in current_hosts
 e['unsafe_exact_match']=e['url'] in unsafe
 if e['url'] in checked_urls:continue
 if edit and ('/posts/' in e['file'] or '/.vitepress/' in e['file'] or e['file'] in ['docs/unsafe.md','docs/unsafesites.md','.github/README.md']):continue
 if host in ['github.com','raw.githubusercontent.com','rentry.co','pastebin.com','apps.apple.com','play.google.com','greasyfork.org']:continue
 if host in current_hosts or e['unsafe_exact_match']:continue
 groups[e['file']].append(e)
selected=[];seen=set()
for category,items in groups.items():
 ordered=sorted(items,key=lambda e:('⭐' not in e['line'] and '🌐' not in e['line'],e['date']<'2025'),reverse=False)
 for e in ordered:
  host=urllib.parse.urlsplit(e['url']).netloc.lower().removeprefix('www.')
  if host in seen:continue
  seen.add(host);selected.append(e)
  if sum(x['file']==category for x in selected)>=(8 if edit else 12):break
def check(e):
 e=e.copy();e['checked_at']=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat(timespec='seconds')
 try:
  req=urllib.request.Request(e['url'],headers={'User-Agent':'Mozilla/5.0 FMHY-resource-audit/1.0'})
  with urllib.request.urlopen(req,timeout=6) as r:
   status=r.status;final=r.url;data=r.read(160000).decode('utf-8',errors='replace')
  m=re.search(r'<title[^>]*>(.*?)</title>',data,re.I|re.S)
  e.update(http_status=status,final_url=final,title=re.sub(r'\s+',' ',m.group(1)).strip() if m else '',validation_level='page_only',core_function_verified=False)
 except Exception as ex:e.update(error=type(ex).__name__,validation_level='unconfirmed',core_function_verified=False)
 return e
out=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
 for e in pool.map(check,selected):out.append(e)
pathlib.Path('fmhy_edit_page_checks.json' if edit else 'fmhy_page_checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
pathlib.Path('fmhy_edit_candidates.json' if edit else 'fmhy_candidates.json').write_text(json.dumps(a,ensure_ascii=False,indent=2))
print(json.dumps({'checked':len(out),'categories':len(groups),'http_2xx':sum(200<=e.get('http_status',0)<300 for e in out)},ensure_ascii=False))
