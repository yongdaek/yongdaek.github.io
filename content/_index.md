---
# Leave the homepage title empty to use the site title
title: 'Yongdae Kim'
date: 2025-12-26
type: landing

design:
  # Default section spacing
  spacing: '6rem'

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: me
      text: ''
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/resume.pdf
      headings:
        about: ''
        education: ''
        interests: ''
    design:
      # Use the new Gradient Mesh which automatically adapts to the selected theme colors
      background:
        gradient_mesh:
          enable: true

      # Name heading sizing to accommodate long or short names
      name:
        size: md # Options: xs, sm, md, lg (default), xl

      # Avatar customization
      avatar:
        size: medium # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded
  - block: markdown
    content:
      title: '📚 My Research'
      subtitle: ''
      text: |-
        My research focuses on discovering and analyzing security vulnerabilities in emerging systems such as cellular networks, drones, and autonomous vehicles.

        **Current Research Interests:**
        - Cellular Network Security (4G/5G/6G)
        - Autonomous Vehicle Security
        - Drone Security
        - Security Research using ML

        **Past Research Interests:**
        Blockchain Security • IoT Security • Embedded Systems Security • Network Protocol Analysis • Wireless Security • Applied Cryptography • Anonymity • Privacy • Mobile Security • Sensor Security • Software Security • System Security

        [See More →](/research)

    design:
      columns: '1'
  - block: collection
    content:
      title: Publications
      text: ''
      filters:
        folders:
          - publications
        exclude_featured: false
    design:
      view: compact
  - block: markdown
    id: awards
    content:
      title: Awards & Honors
      text: |
        **Academic Honors**
        - **Member**, National Academy of Engineering of Korea (2025)
        - **KAIST ICT Chair Professor** (2025–Present)
        - **IEEE Fellow** (2024)
        - **KAIST Chair Professor** (2013–2015)
        - **McKnight Land-Grant Professorship**, University of Minnesota (2006)
        - **NSF CAREER Award** (2005)

        **Best Paper Awards**
        - **Distinguished Paper Award**, ACM CCS 2025
        - **Best Paper Award**, ACM WiSec 2016

        **Teaching Excellence**
        - **Best Lecture Award**, KAIST Electrical Engineering (2022)
    design:
      columns: 1
---
