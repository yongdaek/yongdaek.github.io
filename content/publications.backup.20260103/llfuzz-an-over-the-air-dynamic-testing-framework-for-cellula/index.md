---
title: 'LLFuzz: An Over-the-Air Dynamic Testing Framework for Cellular Baseband Lower Layers'
authors:
- Tuan Dinh Hoang
- Taekkyung Oh
- CheolJun Park
- Insu Yun
- Yongdae Kim
date: '2025-01-01'
publication: 34th USENIX Security Symposium, USENIX Security 2025, Seattle, WA, USA, August 13-15, 2025
publication_types:
- '1'
abstract: ''
featured: false
links:
- name: DOI
  url: https://www.usenix.org/conference/usenixsecurity25/presentation/hoang
- name: Code
  url: https://github.com/SysSec-KAIST/LLFuzz
tags:
- CVE-2025-21477
- CVE-2025-21477
- CVE-2024-23385
- CVE-2024-23385
- CVE-2024-20076
- CVE-2024-20076
- CVE-2024-20077
- CVE-2024-20077
- CVE-2025-20659
- CVE-2025-20659
- CVE-2025-26780
- CVE-2025-26780
- CVE-2024-27870
- CVE-2024-27870
- CVE-2025-21477
---

## Impact

LLFuzz uncovered 11 previously unknown vulnerabilities across 15 commercial smartphones from major vendors including Qualcomm, MediaTek, Samsung, and Apple. Seven of these vulnerabilities have been assigned CVE identifiers and patched by vendors, while four remain undisclosed due to patch delays. The CVEs include: itemize Qualcomm: CVE-2025-21477, CVE-2024-23385 -- affecting over 90 chipsets. MediaTek: CVE-2024-20076, CVE-2024-20077, CVE-2025-20659 -- affecting over 80 chipsets. Samsung: CVE-2025-26780 -- affecting Exynos 2400 series and Modem 5400. Apple: CVE-2024-27870 -- equivalent to CVE-2025-21477 in Qualcomm modems. itemize LLFuzz revealed systemic flaws in how lower-layer baseband logic is implemented across vendors. In one test, a single malformed MAC-layer packet immediately disabled a device during data streaming. These results demonstrate that lower layers remain a blind spot in mobile security. LLFuzz is open-sourced at https://github.com/SysSec-KAIST/LLFuzz.

