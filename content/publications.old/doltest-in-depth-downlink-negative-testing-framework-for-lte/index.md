---
title: 'DoLTEst: In-depth Downlink Negative Testing Framework for LTE Devices'
authors:
- CheolJun Park
- Sangwook Bae
- Beomseok Oh
- Jiho Lee
- Eunkyu Lee
- Insu Yun
- Yongdae Kim
date: '2022-01-01'
publication: 31st USENIX Security Symposium, USENIX Security 2022, Boston, MA, USA, August 10-12, 2022
publication_types:
- '1'
abstract: ''
featured: false
links:
- name: DOI
  url: https://www.usenix.org/conference/usenixsecurity22/presentation/park-cheoljun
- name: Code
  url: https://github.com/SysSec-KAIST/DoLTEst
tags:
- CVE-2019-2289
- CVE-2021-25516
- CVE-2021-25516
- CVE-2021-30826
- CVE-2021-30826
---

## Impact

This paper was discussed in a 3GPP SA3 meeting. It is currently open-sourced at https://github.com/SysSec-KAIST/DoLTEst. We uncovered 26 implementation flaws from 43 devices from 5 different baseband manufacturers by using DoLTEst. We have received 3 CVEs (CVE-2019-2289 from Qualcomm, CVE-2021-25516 from Samsung, and CVE-2021-30826 from Apple.) The Qualcomm bug allows an authentication bypass in all baseband processors manufactured by Qualcomm, requiring almost one year to finish the patch process.

