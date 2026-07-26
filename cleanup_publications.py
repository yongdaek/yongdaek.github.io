#!/usr/bin/env python3
"""
EE/homepage publications 정리 스크립트.
repo 루트(yongdaek.github.io)에서 실행하세요:  python3 cleanup_publications.py

수행 작업:
  A) 동명이인(다른 Yongdae Kim) 논문 폴더 4개 삭제
  B) 저자 이름의 LaTeX 액센트 복원 (K\"olndorfer -> Kölndorfer, Mazi\'eres -> Mazières)
  C) \_ 이스케이프 제거 (DOI 링크 및 Impact 본문)
  D) 인용 키 잔여물(~citekey) 제거
"""
import os, re, glob, shutil

PUB = "content/publications"

WRONG = [
    "design-and-control-of-a-two-degree-of-freedom-haptic-device-",
    "integrating-an-eclipse-based-scenario-modeling-environment-w",
    "security-requirements-of-certificate-validation-in-web-secur",
    "voice-coil-motor-nano-stage-with-an-eddy-current-damper",
]

ACCENTS = {
    r'\\"o':'ö', r'\\"u':'ü', r'\\"a':'ä', r'\\"O':'Ö', r'\\"U':'Ü', r'\\"A':'Ä',
    r"\\'e":'é', r"\\'a":'á', r"\\'o":'ó', r"\\'i":'í', r"\\'u":'ú', r"\\'c":'ć',
    r"\\'E":'É', r"\\'A":'Á',
    r'\\`e':'è', r'\\`a':'à', r'\\`o':'ò',
    r'\\\^o':'ô', r'\\\^e':'ê', r'\\\^a':'â',
    r'\\~n':'ñ', r'\\~a':'ã',
}

# 소스 오타 교정 (acute -> 실제 표기)
NAME_FIX = {"David Maziéres": "David Mazières"}

def fix_text(t):
    for pat, rep in ACCENTS.items():
        t = re.sub(r'\{' + pat + r'\}', rep, t)
        t = re.sub(pat, rep, t)
    t = t.replace(r'\_', '_')
    for wrong, right in NAME_FIX.items():
        t = t.replace(wrong, right)
    return t

def strip_cites(t):
    out = []
    for line in t.split('\n'):
        if line.strip().startswith('url:') or 'http' in line:
            out.append(line); continue
        out.append(re.sub(r'~[A-Za-z][A-Za-z0-9]*', '', line))
    return '\n'.join(out)

deleted = []
for s in WRONG:
    p = os.path.join(PUB, s)
    if os.path.isdir(p):
        shutil.rmtree(p); deleted.append(s)

changed = []
for md in glob.glob(os.path.join(PUB, "*/index.md")):
    orig = open(md, encoding='utf-8').read()
    new = strip_cites(fix_text(orig))
    if new != orig:
        open(md, 'w', encoding='utf-8').write(new); changed.append(md)

print(f"삭제된 폴더: {len(deleted)}")
for d in deleted: print("  -", d)
print(f"수정된 파일: {len(changed)}")
print("\n완료. `git diff` 로 검토 후 커밋하세요.")
