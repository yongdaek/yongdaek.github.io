---
title: 'Hiding in Plain Signal: Physical Signal Overshadowing Attack on LTE'
authors:
- Hojoon Yang
- Sangwook Bae
- Mincheol Son
- Hongil Kim
- Song Min Kim
- Yongdae Kim
date: '2019-01-01'
publication: 28th USENIX Security Symposium, USENIX Security 2019, Santa Clara, CA, USA, August 14-16, 2019
publication_types:
- '1'
abstract: ''
featured: false
links:
- name: DOI
  url: https://www.usenix.org/conference/usenixsecurity19/presentation/yang-hojoon
- name: Code
  url: https://github.com/SysSec-KAIST/sigover_injector
---

## Impact

The initial response from GSMA was disappointing as they viewed this work as only academically interesting. However, it turned out to be important for both academia and standard bodies. After it was initially discussed in 2019 Reno 97th 3GPP meeting (S3-194063), a lot of documents (and probably discussions) tried to address this attack accross multiple 3GPP meetings: TSGS3\_100Bis-e (S3-202556, S3-202738, S3-202740), TSGS3\_100e (S3-202026, S3-202109, S3-202150), TSGS3\_101e (S3-202983, S3-202984, S3-203158, S3-203160, S3-203364, S3-203447), TSGS3\_102Bis-e (S3-211345), TSGS3\_102e (S3-210131, S3-210778, S3-210783), TSGS3\_103e (S3-212351), TSGS3\_104e (S3-212748, S3-213244), TSGS3\_105e (S3-214408), and TSGS3\_107e (S3-221266). In addition, the attack is extended to sigover attack over unicast channel by us~bae2022watching, layer 2 messages by Tan et. al.~tan2021data and uplink channel by Erni et. al.~erni2022adaptover. In 5G, SA3 failed to secure these unauthenticated channels due to various technical problems. I hope to solve these problems before 6G design is complete, which will start in 2 years.

