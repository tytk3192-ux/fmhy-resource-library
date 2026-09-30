import subprocess,re,json,pathlib,sys
p=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else 'fmhy-wiki-source')
current='\n'.join(f.read_text() for f in pathlib.Path('fmhy-current-source/docs').glob('*.md') if f.name not in ['storage.md','unsafe.md','posts.md','sandbox.md'])
urls=set(re.findall(r'https?://[^\s)<>]+',current))
raw=subprocess.check_output(['git','-c','core.quotePath=false','log','--format=EVENT %H %aI','--no-renames','-p','--unified=0','--','*.md'],cwd=p,text=True)
events=[];sha=date=None;minus=[];plus=[];file=''
def flush():
 added=set(re.findall(r'https?://[^\s)<>]+','\n'.join(plus)))
 for line in minus:
  if not line.startswith('*'):continue
  for u in re.findall(r'https?://[^\s)<>]+',line):
   if u in added or u in urls:continue
   if any(x in u for x in ['discord.','reddit.com','t.me/','youtube.com','x.com/']):continue
   events.append(dict(url=u,date=date,sha=sha,file=file,line=line))
for l in raw.splitlines():
 if l.startswith('EVENT '):
  flush();minus=[];plus=[];_,sha,date=l.split()
 elif l.startswith('diff --git '):
  flush();minus=[];plus=[];file=l.split(' b/')[-1]
 elif l.startswith('-') and not l.startswith('---'):minus.append(l[1:])
 elif l.startswith('+') and not l.startswith('+++'):plus.append(l[1:])
flush()
seen=set();out=[]
for e in events:
 if e['url'] not in seen:seen.add(e['url']);out.append(e)
pathlib.Path('fmhy_edit_candidates.json' if 'current' in str(p) else 'fmhy_candidates.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
from collections import Counter
print(json.dumps(dict(total=len(out),categories=Counter(e['file'] for e in out)),ensure_ascii=False))
