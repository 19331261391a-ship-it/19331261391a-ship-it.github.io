from pathlib import Path
import re, base64, mimetypes
root=Path(__file__).resolve().parent
raw=(root/'index.html').read_text(encoding='utf-8')
def embed(m):
    src=m.group(2)
    if src.startswith(('data:','http:','https:','//')):return m.group(0)
    p=root/src
    return m.group(1)+'data:'+mimetypes.guess_type(p.name)[0]+';base64,'+base64.b64encode(p.read_bytes()).decode()+m.group(3)
raw=re.sub(r'(<img\b[^>]*?\bsrc=")([^"]+)(")',embed,raw,flags=re.I)
(root/'Sam-Ge-Webpage-R19.html').write_text(raw,encoding='utf-8')
print('Updated Sam-Ge-Webpage-R19.html')
