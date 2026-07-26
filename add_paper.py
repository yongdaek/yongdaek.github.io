#!/usr/bin/env python3
"""
새 논문 하나 추가하는 대화형 스크립트.
repo 루트(yongdaek.github.io)에서 실행:  python3 add_paper.py

제목/저자/학회/연도/링크를 물어보고:
  - content/publications/<slug>/index.md 생성 (기존 형식과 동일)
  - 새 공저자는 data/authors/<slug>.yaml 자동 생성 (이름 대문자 표시용)
Impact / Media / CVE 는 선택 입력 (엔터로 건너뜀, 나중에 md 직접 편집도 가능).
"""
import os, re, sys, unicodedata

PUB = "content/publications"
AUTH = "data/authors"

def ascii_fold(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')

def paper_slug(title):
    s = ascii_fold(title).lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s[:60].strip('-')

def author_slug(name):
    s = ascii_fold(name).lower().replace('.', '')
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

def ask(prompt, required=True):
    while True:
        v = input(prompt).strip()
        if v or not required:
            return v
        print("  (필수 항목입니다)")

def main():
    if not os.path.isdir(PUB):
        sys.exit(f"'{PUB}' 폴더가 없습니다. repo 루트에서 실행하세요.")

    print("\n=== 새 논문 추가 ===\n")
    title = ask("제목: ")
    print("저자 (쉼표로 구분, 예: Alice Kim, Bob Lee, Yongdae Kim)")
    authors = [a.strip() for a in ask("저자: ").split(',') if a.strip()]
    venue = ask("학회/저널 (전체 표기): ")
    year = ask("연도 (예: 2026): ")

    t = ask("종류 [c=학회 / j=저널] (기본 c): ", required=False).lower()
    pub_type = '2' if t.startswith('j') else '1'

    # 링크 (여러 개 가능)
    links = []
    print("링크 입력 (없으면 엔터). 예: DOI, 학회 페이지, PDF ...")
    url = ask("  첫 링크 URL (없으면 엔터): ", required=False)
    if url:
        name = ask("  링크 이름 (기본 DOI): ", required=False) or "DOI"
        links.append((name, url))
        while True:
            u2 = ask("  추가 링크 URL (없으면 엔터): ", required=False)
            if not u2:
                break
            n2 = ask("  추가 링크 이름: ", required=False) or "Link"
            links.append((n2, u2))

    # 선택 섹션
    abstract = ask("초록 (선택, 엔터로 건너뜀): ", required=False)
    impact = ask("Impact (선택, 엔터로 건너뜀): ", required=False)
    media = [m.strip() for m in ask("Media 매체명 (쉼표 구분, 선택): ", required=False).split(',') if m.strip()]
    cve = ask("CVE (선택, 예: CVE-2026-1234): ", required=False)

    slug = paper_slug(title)
    folder = os.path.join(PUB, slug)
    if os.path.isdir(folder):
        if not ask(f"\n'{slug}' 폴더가 이미 있습니다. 덮어쓸까요? [y/N]: ", required=False).lower().startswith('y'):
            sys.exit("취소했습니다.")
    os.makedirs(folder, exist_ok=True)

    # frontmatter
    q = lambda s: s.replace("'", "''")  # YAML single-quote escape
    fm = ["---", f"title: '{q(title)}'", "authors:"]
    fm += [f"- {a}" for a in authors]
    fm += [
        f"date: '{year}-01-01'",
        f"publication: '{q(venue)}'",
        "publication_types:",
        f"- '{pub_type}'",
        f"abstract: '{q(abstract)}'" if abstract else "abstract: ''",
        "featured: false",
    ]
    if links:
        fm.append("links:")
        for name, u in links:
            fm.append(f"- name: {name}")
            fm.append(f"  url: {u}")
    fm.append("---")

    body = ["", ""]
    if impact:
        body += ["## Impact", "", impact, ""]
    if media:
        body += ["## Media Coverage", ""] + [f"- {m}" for m in media] + [""]
    if cve:
        body += ["## CVE", "", cve, ""]

    with open(os.path.join(folder, "index.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(fm) + "\n" + "\n".join(body))

    # 새 저자 YAML
    created_authors = []
    os.makedirs(AUTH, exist_ok=True)
    for a in authors:
        aslug = author_slug(a)
        ypath = os.path.join(AUTH, f"{aslug}.yaml")
        if not os.path.exists(ypath):
            with open(ypath, "w", encoding="utf-8") as f:
                f.write(f"name:\n  display: {a}\n")
            created_authors.append(aslug)

    print(f"\n✅ 생성: {folder}/index.md")
    if created_authors:
        print(f"✅ 새 저자 YAML {len(created_authors)}개:", ", ".join(created_authors))
    print("\n다음 단계:")
    print("  hugo server        # 로컬 확인 (Ctrl+C 종료)")
    print("  git add -A")
    print(f"  git commit -m 'Add paper: {title[:50]}'")
    print("  git push")

if __name__ == "__main__":
    main()
