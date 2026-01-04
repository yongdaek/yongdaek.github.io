---
title: "Cyber-Physical Systems Security"
subtitle: "Research Overview (2013-2025)"
date: 2025-01-03
type: page
---

Over the past decade, my research group has been investigating security vulnerabilities in cyber-physical systems (CPS), with a particular focus on sensor security, autonomous systems, and IoT firmware analysis.

## Research Overview

### Autonomous Systems (Drones & Vehicles)

#### Acoustic Injection Attacks

**Rocking Drones with Intentional Sound Noise on Gyroscopic Sensors (USENIX Security 2015)**

We discovered that MEMS gyroscopes are vulnerable to acoustic resonance attacks. The attack chain works as follows:

- **Acoustic resonance:** Sound waves at the gyroscope's resonant frequency induce false angular velocity readings
- **Control system feedback:** The PID control algorithm interprets corrupted sensor data as real instability and adjusts rotor speeds to compensate
- **Amplification loop:** Corrective actions amplify oscillations rather than damping them, leading to catastrophic failure

The key insight: cyber-physical vulnerabilities emerge from the interaction between sensor physics and control algorithms—neither component is vulnerable alone, but their composition creates exploitable behavior. Knowing the gyroscope's resonant frequency enables an attacker to crash the drone.

**Impact:** This work established that cyber-physical vulnerabilities emerge from component interactions, not individual components. Key influences include:

- **Defense applications:** Sandia National Laboratories' 2020 report "[Assessing the Vulnerability of Unmanned Aircraft Systems to Directed Acoustic Energy](https://www.osti.gov/biblio/1670875)" developed practical counter-UAS systems using acoustic impulses
- **Research programs:** DARPA's [FIRE (Faithful Integrated Reverse-Engineering and Exploitation)](https://www.darpa.mil/program/faithful-integrated-reverse-engineering-and-exploitation) program cites acoustic attacks on MEMS sensors as a motivating example for cyber-physical vulnerability analysis
- **Continued interest:** Acoustic weapons offer low collateral damage and effectiveness against drone swarms—a single frequency can simultaneously affect multiple drones with similar sensors

**Media:** [New York Daily](http://www.nydailynews.com/news/world/south-korea-study-proves-sound-waves-disable-drones-article-1.2318227), [Discover Magazine](http://blogs.discovermagazine.com/drone360/2015/08/05/sound-can-knock-drones-out-of-the-air/#.VgCk2iC8PRZ), [Defense Systems](https://defensesystems.com/Articles/2015/08/10/KAIST-researchers-take-out-drones-with-sound.aspx), [Techworm](http://www.techworm.net/2015/08/drone-hack-blasting-a-sound-at-a-drone-can-knock-it-out-of-the-air.html), [Slashdot](http://tech.slashdot.org/story/15/08/05/1224237/sounds-can-knock-drones-out-of-the-sky), [Network World](http://www.networkworld.com/article/2957033/sounds-can-knock-drones-out-of-the-sky.html), [Gizmodo](http://gizmodo.com/simple-soundwaves-can-knock-a-drone-out-of-the-sky-1722240688)

**Un-Rocking Drones: Foundations of Acoustic Injection Attacks and Recovery Thereof (NDSS 2023)**

We provided a comprehensive theoretical foundation for acoustic injection attacks and developed effective defenses. 

**Why attacks still work despite filters:** Modern drones have low-pass filters that should block high-frequency acoustic signals. However, sampling jitter in the analog-to-digital conversion causes these signals to alias into the measurement band, bypassing the filter.

**Defense mechanisms:** Multi-layered approach including sensor fusion, control algorithm monitoring, and acoustic signature detection to enable real-time attack detection and safe landing.

#### EMI Signal Injection Attacks

**Paralyzing Drones via EMI Signal Injection on Sensory Communication Channels (NDSS 2023)**

We discovered that EMI attacks on communication channels (I2C/SPI) between sensors and flight controllers are more effective than attacking sensors directly. This approach solves three key limitations of acoustic attacks:

- **Speed:** Attack causes failure within one control cycle (0.0025 seconds)—faster than any software-based detection or failsafe mechanism
- **Universality:** Targets the flight controller's communication bus rather than individual sensors; knowing the main board model enables a single attack frequency to crash all drones using that board, regardless of sensor types
- **Precision:** Narrow frequency spectrum (targeting specific communication clocks) minimizes collateral damage to nearby electronics

**Impact:** Demonstrated that attacking communication layers provides faster and more universal attack vectors than sensor-level attacks. Particularly effective against drone swarms using common flight controller platforms.

#### GPS Spoofing Attacks

**Tractor Beam: Safe-hijacking of Consumer Drones with Adaptive GPS Spoofing (ACM TOPS 2019)**

Prior GPS spoofing research demonstrated feasibility but failed when applied to real drones due to failsafe mechanisms. We analyzed three popular failsafe modes and developed adaptive spoofing techniques to bypass each:

- **Return-to-Home (RTH):** Gradually shift the drone's perceived home location
- **Position Hold:** Spoof incremental position changes to avoid triggering sudden movement detection
- **Emergency Landing:** Manipulate altitude readings to control descent location

This enables safe hijacking—redirecting drones to attacker-chosen locations without triggering safety mechanisms or causing crashes.

**Media:** [Electronics Weekly](https://www.electronicsweekly.com/news/research-news/tractor-beam-hijacks-drones-gps-spoofing-2019-07/)

#### Controller Security

**Security Analysis of FHSS-type Drone Controller (WISA 2015)**

We analyzed FrSky's popular FHSS (Frequency-Hopping Spread Spectrum) controller and discovered that its hopping sequence has a period of only 141 hops. This means:

- Monitoring transmissions for ~1.41 seconds reveals the complete hopping pattern
- Enables targeted jamming by following the sequence rather than broadband jamming
- Significantly reduces power requirements and collateral interference compared to wideband jamming

Note: We demonstrated jamming capability but did not implement control signal injection.

#### Drone Tracking and Identification

**GyrosFinger: Fingerprinting Drones for Location Tracking Based on the Outputs of MEMS Gyroscopes (ACM TOPS 2018)**

We discovered that manufacturing imperfections in MEMS gyroscopes create unique fingerprints that can be used to track and identify individual drones.

#### Optical Attacks on Autonomous Vehicles

**Illusion and Dazzle: Adversarial Optical Channel Exploits Against Lidars for Automotive Applications (CHES 2017)**

We discovered vulnerabilities in Velodyne lidar sensors (the most popular automotive lidar at the time) using optical attacks:

- **Illusion attacks:** Create phantom objects that appear closer than they actually are, potentially causing unnecessary braking or evasive maneuvers
- **Dazzle attacks:** Blind the sensor or hide real objects by saturating specific detection channels

These attacks exploit the time-of-flight measurement principles used by spinning lidar systems.

#### Magnetic Sensor Attacks on Vehicles

**Sampling Race: Bypassing Timing-Based Analog Active Sensor Spoofing Detection on Analog-Digital Systems (USENIX WOOT 2016)**

We demonstrated that timing-based detection mechanisms for sensor attacks can be bypassed by exploiting the sampling mechanism itself. Specifically targeting magnetic sensors in automotive speedometers:

- Attack signals are crafted to exploit the race condition between the sensor's sampling timing and the injected signal
- Carefully timed signal injection appears legitimate to timing-based defenses
- Demonstrates that defenses relying solely on timing analysis are insufficient

This work shows that sensor sampling mechanisms themselves can become attack vectors.

### Critical Infrastructure & Medical Systems

#### Medical Device Security

**Ghost Talk: Mitigating EMI Signal Injection Attacks against Analog Sensors (IEEE S&P 2013)**

My first sensor attack paper. We demonstrated that analog sensor wires can act as antennas, enabling electromagnetic signal injection that directly affects device actuation:

- **Implantable cardiac devices:** Successfully stopped pacemakers by injecting signals through EMI
- **Bluetooth headsets:** Injected audio signals directly into microphone circuits

This work established the fundamental vulnerability of analog sensors to intentional electromagnetic interference and motivated my move to KAIST's electrical engineering department to continue sensor security research with EE students.

**Media:** [The Register](https://www.theregister.com/2013/11/01/analog_sensors_hack/)

**This Ain't Your Dose: Sensor Spoofing Attack on Medical Infusion Pump (USENIX WOOT 2016)**

Demonstrated laser-based attacks on infusion pump drop sensors enabling over-infusion or under-infusion while the display shows correct dosage.

#### Fire Detection Systems

**The System That Cried Wolf: Sensor Security Analysis of Wide-area Smoke Detectors for Critical Infrastructure (ACM TOPS 2020)**

Comprehensive analysis of commercial wide-area photoelectric smoke detectors used in critical infrastructure. Demonstrated remote false alarm attacks and real fire suppression using laser light with minimal equipment.

#### Photoelectric Sensor Defense

**Lightbox: Sensor Attack Detection for Photoelectric Sensors via Spectrum Fingerprinting (ACM TOPS 2023)**

Defense-focused work. Each photoelectric sensor has unique spectral response characteristics, enabling real-time attack detection by distinguishing legitimate signals from attacker-injected light.

#### Power Grid Security

**Revisiting GPS Spoofing in Phasor Measurement: Real-World Exploitation and Practical Detection in Power Grids (ACM TOPS 2025)**

Phasor Measurement Units (PMUs) are critical for power grid monitoring. Prior research suggested arbitrary time manipulation through GPS spoofing could disrupt grid operations. We challenged this assumption:

- **Specification analysis:** Detailed analysis of IEEE Standard C37.118.x revealed that arbitrary time manipulation triggers GPS holdover mode, alerting operators and invalidating synchrophasor data
- **Real-world testbed:** Collaboration with KEPCO (Korea) and Hydro-Québec (Canada) using commercial PMUs confirmed our analysis
- **Attack requirements:** Successful attacks require two specific conditions:
  - Seamless takeover of GPS control without triggering alarms
  - Gradual time manipulation within acceptable bounds to avoid holdover
- **Practical detection:** Developed detection mechanisms based on understanding these specific attack constraints

This work demonstrates that effective attacks on critical infrastructure require precise understanding of operational specifications, not just proof-of-concept demonstrations.

### Systematic Analysis & Foundations

**SoK: A Minimalist Approach to Formalizing Analog Sensor Security (IEEE S&P 2020)**

We developed the first unified framework for systematizing analog sensor security research:

- **Modeling framework:** Created a minimalist model that captures the essential properties of sensor attacks across different domains (acoustic, optical, EMI, etc.)
- **Attack taxonomy:** Analyzed existing sensor attacks and classified them into a coherent taxonomy based on attack principles
- **Defense analysis:** Evaluated existing defense mechanisms and identified gaps in protection strategies
- **Future predictions:** Used the framework to predict new classes of sensor attacks that had not yet been demonstrated

This work established a principled foundation for understanding sensor security, enabling researchers to reason about attacks and defenses systematically rather than addressing each sensor type in isolation.

**A Systematic Study of Physical Sensor Attack Hardness (IEEE S&P 2024)**

The first systematic study to quantify the difficulty of launching physical sensor attacks by analyzing various factors including required equipment, expertise, and proximity.

### IoT & Firmware Security

**FirmAE: Towards Large-Scale Emulation of IoT Firmware for Dynamic Analysis (ACSAC 2020) / Enabling the Large-Scale Emulation of Internet of Things Firmware With Heuristic Workarounds (IEEE Security & Privacy 2021)**

We developed FirmAE, a fully-automated framework for large-scale IoT firmware emulation and vulnerability analysis. Prior state-of-the-art tool (Firmadyne) could only emulate 16.28% of firmware images due to discrepancies between real and emulated environments.

**Key innovations:**
- **Arbitrated emulation:** Systematized heuristic workarounds to address common emulation failures
- **Dramatic improvement:** Increased emulation success rate from 16.28% to 79.36% (≈4.8x improvement) on 1,124 firmware images from top eight vendors
- **Five arbitration techniques:** Boot, network, NVRAM, kernel, and configuration arbitrations to handle environment mismatches
- **Automated vulnerability discovery:** Developed dynamic analysis tools that infer web service information from filesystem and kernel logs

**Results:**
- Successfully emulated 892 of 1,124 wireless router and IP camera firmware images
- Validated 320 known vulnerabilities (306 more than Firmadyne)
- Discovered 12 new 0-day vulnerabilities affecting 23 devices across four vendors

**CVEs:** CVE-2018-19986, CVE-2018-19987, CVE-2018-19988, CVE-2018-19989, CVE-2018-19990, CVE-2018-20114, CVE-2019-11399, CVE-2019-11400, CVE-2019-20082, CVE-2019-20084, CVE-2019-6258

The IEEE Security & Privacy 2021 magazine article provides an accessible overview of the FirmAE approach. [GitHub repository](https://github.com/pr0v3rbs/FirmAE)

**Dissecting Customized Protocols: Automatic Analysis for Customized Protocols based on IEEE 802.15.4 (WiSec 2016) 🏆 Best Paper Award**

We developed WASp, a tool for automatically analyzing customized IoT protocols built on top of IEEE 802.15.4. Many IoT devices use proprietary protocols layered over standard wireless protocols, making security analysis difficult. WASp enables automated extraction and analysis of these customized protocol implementations without requiring access to specifications or source code.
