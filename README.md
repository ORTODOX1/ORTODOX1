<h1 align="center">
  <br>
  <img src="https://img.shields.io/badge/Marine_Engineer-Automation_&_Embedded_Systems-0d1b2a?style=for-the-badge&labelColor=1b263b" alt="Title">
</h1>

<p align="center">
  <strong>Herman Doronin</strong><br>
  <em>Bridging ship machinery and digital systems</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Experience-3+_Years_Ship_Repair-1b263b?style=flat-square" alt="Experience">
  <img src="https://img.shields.io/badge/Location-Germany-1b263b?style=flat-square" alt="Location">
  <img src="https://img.shields.io/badge/Status-Open_to_Work-2d6a4f?style=flat-square" alt="Status">
</p>

---

### About

Marine engineer with **3+ years** in ship power plant maintenance: main engine overhaul, turbocharger balancing, fuel injector testing, piston ring and scavenge port inspection, auxiliary diesel servicing, planned maintenance system (PMS) execution.

I build software that solves the problems I encountered hands-on — condition-based maintenance instead of fixed intervals, automated inspection of confined spaces, intelligent alarm prioritization instead of alarm fatigue.

**Rust** for CAN bus protocols (J1939, NMEA 2000). **Python** for ML, computer vision, edge inference. **TypeScript** for real-time monitoring dashboards.

### Education

**Operation of Ship Power Plants** (4 years)
Marine power plant operation, maintenance, and diagnostics.
Core curriculum: thermodynamics, marine diesel engines, steam turbines, auxiliary machinery, ship electrical systems, automation and control systems.

**STCW International Certifications**
- ISPS Code — International Ship and Port Facility Security
- Basic Safety Training (BST) — fire prevention & firefighting, personal survival techniques, personal safety & social responsibilities
- Proficiency in Medical First Aid
- Security Awareness Training

---

### Domain Knowledge

```
Ship Power Plants     ██████████  Marine Diesel Engines
Propulsion Systems    █████████░  Overhaul & Diagnostics
Auxiliary Machinery   █████████░  Pumps, Compressors, Heat Exchangers
Engine Control        ████████░░  ECU, Governor, Fuel Injection
Dry-dock Operations   ████████░░  Inspection, Repair, Reporting
```

### Maritime Protocols & Automation

<p>
  <img src="https://img.shields.io/badge/J1939--76-Marine_CAN-0d1b2a?style=flat-square" alt="J1939">
  <img src="https://img.shields.io/badge/NMEA_2000-Navigation_Bus-0d1b2a?style=flat-square" alt="NMEA">
  <img src="https://img.shields.io/badge/Modbus-Industrial_Protocol-0d1b2a?style=flat-square" alt="Modbus">
  <img src="https://img.shields.io/badge/OPC_UA-Unified_Architecture-0d1b2a?style=flat-square" alt="OPC UA">
  <img src="https://img.shields.io/badge/CAN_Bus-Controller_Area_Network-0d1b2a?style=flat-square" alt="CAN">
  <img src="https://img.shields.io/badge/K--Line-ISO_9141-0d1b2a?style=flat-square" alt="K-Line">
  <img src="https://img.shields.io/badge/IEC_61131--3-PLC_Programming-0d1b2a?style=flat-square" alt="PLC">
</p>

### Software & Tools

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux">
  <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" alt="Git">
</p>

---

### Projects

| Project | Problem It Solves | Stack |
|---------|-------------------|-------|
| [**ARGOS**](https://github.com/ORTODOX1/ARGOS) | Hull and tank inspections cost $50-100K and put humans at risk. ARGOS automates inspection in confined spaces with edge AI and TRIZ reasoning | Python, Rust, ROS 2, ONNX |
| [**POSEIDON-DIAG**](https://github.com/ORTODOX1/POSEIDON-DIAG) | Unplanned engine failure costs $50K-500K/day. Real-time CAN bus diagnostics with AI anomaly detection catch failures before they happen | Rust, Tauri, React, CAN |
| [**TRITON-ML**](https://github.com/ORTODOX1/TRITON-ML) | Time-based maintenance wastes 30-50% of budget. ML predicts actual equipment condition 2-4 weeks before traditional alarms | Python, XGBoost, PyTorch, SHAP |
| [**SYNIZ**](https://github.com/ORTODOX1/SYNIZ) | IMO 2030/2050 requires radical engineering innovation. 50 TRIZ agents debate contradictions to accelerate R&D cycles | Python, FastAPI, Neo4j, D3.js |
| [**AEGIS-MONITOR**](https://github.com/ORTODOX1/AEGIS-MONITOR) | Operators monitor 500+ parameters with alarm fatigue. Dashboard with 3D ship model and intelligent alerting reduces response time | React, TypeScript, Three.js |
| [**NautilusQuant**](https://github.com/ORTODOX1/NautilusQuant) | Satellite bandwidth is 64-512 kbps. 4x deterministic compression enables shipboard AI without cloud dependency | Python, PyTorch, Triton GPU |

### Ecosystem

```mermaid
graph TD
    A["AEGIS-MONITOR<br/><i>Operator Dashboard</i><br/>Live telemetry · 3D model · Alarms"] --> B
    B["ARGOS<br/><i>Inspection Robot</i><br/>Vision · Navigation · Edge AI"] --> C
    B --> D
    B --> E
    C["SYNIZ<br/><i>TRIZ Engine</i><br/>50 agents solve<br/>the unknown"]
    D["TRITON-ML<br/><i>Predictive Maintenance</i><br/>Fault detection + RUL"]
    E["POSEIDON-DIAG<br/><i>Ship Interface</i><br/>J1939 · NMEA · CAN"]
    D --> F["NautilusQuant<br/><i>Edge Compression</i><br/>3-bit · 512-byte LUT"]

    style A fill:#0d4a6b,stroke:#1e88a8,color:#e2e8f0
    style B fill:#6b2d0d,stroke:#a8571e,color:#e2e8f0
    style C fill:#2d6b0d,stroke:#4a8a1e,color:#e2e8f0
    style D fill:#4a0d6b,stroke:#7a1ea8,color:#e2e8f0
    style E fill:#0d4a6b,stroke:#1e88a8,color:#e2e8f0
    style F fill:#6b5a0d,stroke:#a8901e,color:#e2e8f0
```

The robot sees. The ML classifies. TRIZ reasons about the unknown. The human makes the final call.

**[Read the full engineering vision: from fundamental physics to autonomous systems →](VISION.md)**

---

### Target Roles

- Marine Automation Engineer
- Vessel Performance / Condition Monitoring Engineer
- Embedded Systems Engineer (Maritime)
- Naval Systems Integration Engineer

---

<p align="center">
  <em>"Most software engineers have never touched a marine diesel.<br>Most marine engineers have never written a GPU kernel.<br>I do both."</em>
</p>
