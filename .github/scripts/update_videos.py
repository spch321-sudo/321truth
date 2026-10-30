#!/usr/bin/env python3
"""每天抓 YouTube 播放清單最新影片（RSS，免金鑰），依標題「真理點心NNN」寫入 data/videos.json。"""
import json, re, sys, urllib.request, xml.etree.ElementTree as ET
LIST = 'PLid55ck_AyA26gNybAlSVfPZPZd9eg7hF'
URL = 'https://www.youtube.com/feeds/videos.xml?playlist_id=' + LIST
PATH = 'data/videos.json'
NS = {'a': 'http://www.w3.org/2005/Atom', 'y': 'http://www.youtube.com/xml/schemas/2015'}
RE = re.compile(r'真理[點点]心\s*[#＃No.第]*\s*0*(\d{1,4})')

def fetch(path=None):
    if path: return open(path, 'rb').read()
    req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0 (321truth video sync)'})
    return urllib.request.urlopen(req, timeout=30).read()

def main(src=None):
    root = ET.fromstring(fetch(src))
    vids = json.load(open(PATH, encoding='utf-8'))
    added = []
    for e in root.findall('a:entry', NS):
        vid = e.findtext('y:videoId', namespaces=NS)
        title = e.findtext('a:title', namespaces=NS) or ''
        m = RE.search(title)
        if not vid or not m: continue
        n = str(int(m.group(1)))
        if vids.get(n) != vid:
            if n not in vids: added.append(n)
            vids[n] = vid
    if added or '--force' in sys.argv:
        out = {k: vids[k] for k in sorted(vids, key=lambda x: int(x))}
        open(PATH, 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, separators=(',', ':')))
    print('added:', ' '.join(added) if added else 'none')

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('--') else None)
