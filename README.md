<p align="center">
  <img src="header.svg" alt="Herman Doronin — Marine Engineer" width="100%"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Experience-3%2B_years_ship_power_plants-1b263b?style=flat-square" alt="Experience">
  <img src="https://img.shields.io/badge/Location-Germany-1b263b?style=flat-square" alt="Location">
  <img src="https://img.shields.io/badge/Status-Open_to_Work-2d6a4f?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Latest-NautilusQuant_v0.1.0_pre--silicon-c47700?style=flat-square" alt="Latest">
</p>

<p align="center">
  <strong>Marine engineer building the AI — and now the silicon — that runs in the engine room.</strong><br>
  <em>From engine room to ASIC. From J1939 to LLM inference.</em>
</p>

---

### About

3+ years hands-on in commercial marine power plants — medium-speed and high-speed 4-stroke diesel engines, mechanical fuel-injection systems (Bosch P-pump rebuilds), turbocharger overhaul and dynamic balancing, fuel-injector pressure testing, scavenge-space and piston-ring inspection, auxiliary genset servicing, planned-maintenance-system execution. The kind of detail you only learn with grease on your hands.

Hands-on with both legacy mechanically-governed engines (Bosch P-pump + pneumatic / Woodward governors) and modern ECU-controlled repower projects (Caterpillar ADEM, Cummins CM-series, J1939 telemetry).

Every project I build came from a problem I saw on board. I solve it at the layer where it actually needs to be solved — sometimes Python, sometimes a Rust crate over J1939, sometimes SystemVerilog targeting Skywater 130 nm.

| Problem on board                                    | What I built                                                                |
|-----------------------------------------------------|-----------------------------------------------------------------------------|
| Confined-space inspections are expensive and risk lives | **ARGOS** — autonomous inspection robot (edge AI + TRIZ reasoning)           |
| Unplanned engine failure stops the ship                | **POSEIDON-DIAG** — real-time J1939 / NMEA 2000 diagnostics + AI anomaly detection |
| Time-based PMS replaces parts that are still healthy  | **TRITON-ML** — RUL prediction 2–4 weeks ahead of classical alarms            |
| Operators ignore alarms past 500+ params              | **AEGIS-MONITOR** — 3D ship dashboard with intelligent prioritization         |
| IMO 2030/2050 demands radical engineering R&D         | **SYNIZ** — 50 TRIZ agents debating contradictions to compress R&D cycles     |
| Satellite uplink is 64–512 kbps, cloud AI doesn't fit | **NautilusQuant** — deterministic KV-cache compression, ROM-LUT instead of a stored matrix |

---

### Ecosystem

```mermaid
graph TD
    A["AEGIS-MONITOR<br/><i>Operator Dashboard</i><br/>Live telemetry · 3D model · Alerts"] --> B
    B["ARGOS<br/><i>Inspection Robot</i><br/>Vision · Navigation · Edge AI"] --> C
    B --> D
    B --> E
    C["SYNIZ<br/><i>TRIZ Engine</i><br/>50 agents reason<br/>about the unknown"]
    D["TRITON-ML<br/><i>Predictive Maintenance</i><br/>Fault detection + RUL"]
    E["POSEIDON-DIAG<br/><i>Ship Interface</i><br/>J1939 · NMEA 2000 · CAN"]
    D --> F["NautilusQuant<br/><i>Edge Compression + Custom ASIC</i><br/>24-opcode ISA · 1.9 KB LUT<br/>RTL skeleton · Yosys · OpenLane MPW path"]

    style A fill:#0d4a6b,stroke:#1e88a8,color:#e2e8f0
    style B fill:#6b2d0d,stroke:#a8571e,color:#e2e8f0
    style C fill:#2d6b0d,stroke:#4a8a1e,color:#e2e8f0
    style D fill:#4a0d6b,stroke:#7a1ea8,color:#e2e8f0
    style E fill:#0d4a6b,stroke:#1e88a8,color:#e2e8f0
    style F fill:#6b5a0d,stroke:#a8901e,color:#e2e8f0
```

The robot sees. The ML predicts. TRIZ reasons about the unknown. NautilusQuant fits inference into the satellite pipe — and now into custom silicon. The human makes the final call.

**[Read the full engineering vision: from protocol layer to autonomous systems →](VISION.md)**

---

### Projects

| Project | Status | Problem it solves | Stack |
|---------|--------|-------------------|-------|
| [**NautilusQuant**](https://github.com/hermandoronin/NautilusQuant) | 🧪 research · v0.1.0 · 247 tests | Satellite uplink 64–512 kbps — shipboard AI without cloud dependency. 1.9 KB ROM-LUT instead of a stored rotation matrix; 24-opcode ISA and an RTL skeleton on the OpenLane path. Benchmarks incl. the negative result are in the repo. | Python · PyTorch · Triton · SystemVerilog · Yosys · OpenLane |
| [**ARGOS**](https://github.com/hermandoronin/ARGOS) | 🧪 prototype | Hull and tank inspections are expensive and put humans at risk. Edge AI + TRIZ reasoning for confined spaces. | Python · ONNX · OpenCV · CAN |
| [**POSEIDON-DIAG**](https://github.com/hermandoronin/POSEIDON-DIAG) | 🔄 active | Unplanned engine failure is the most expensive event at sea. J1939 / NMEA 2000 decoding as a Rust workspace — protocol layer works, tests green. | Rust · J1939-71 · NMEA 2000 · SocketCAN |
| [**TRITON-ML**](https://github.com/hermandoronin/TRITON-ML) | 🔄 active | Time-based maintenance replaces parts that are still healthy. ML on vibration/thermal/operational features estimates true condition instead. | Python · XGBoost · PyTorch · SHAP · ONNX |
| [**SYNIZ**](https://github.com/hermandoronin/SYNIZ) | 🧪 prototype | IMO 2030/2050 demands radical engineering. A swarm of TRIZ agents debates contradictions instead of one model guessing. Interface and prompts are Russian for now. | Python · FastAPI · Neo4j · React |
| [**AEGIS-MONITOR**](https://github.com/hermandoronin/AEGIS-MONITOR) | 🔄 active | 500+ parameters cause alarm fatigue. 3D ship dashboard with prioritised alarms; runs on a mock data server. | React 19 · TypeScript · Three.js · Vite |

#### Cross-domain / experimental

| Project | Status | Problem it solves | Stack |
|---------|--------|-------------------|-------|
| [**arc-computer**](https://github.com/hermandoronin/arc-computer) | 🧪 experiment | Engineering knowledge that works without internet or subscription. This repo publishes the knowledge-base pipeline only. | Python · offline knowledge base |

---

### Tech Stack

**Hardware & Silicon**
<p>
  <img src="https://img.shields.io/badge/SystemVerilog-1f6feb?style=flat-square" alt="SystemVerilog">
  <img src="https://img.shields.io/badge/Verilator-FF6B35?style=flat-square" alt="Verilator">
  <img src="https://img.shields.io/badge/Yosys-2D5F2D?style=flat-square" alt="Yosys">
  <img src="https://img.shields.io/badge/OpenLane2-1b263b?style=flat-square" alt="OpenLane2">
  <img src="https://img.shields.io/badge/SymbiYosys-formal-4a0d6b?style=flat-square" alt="SymbiYosys">
  <img src="https://img.shields.io/badge/Skywater_130nm-PDK-c47700?style=flat-square" alt="Skywater PDK">
  <img src="https://img.shields.io/badge/RTL_to_GDS-1f6feb?style=flat-square" alt="RTL-to-GDS">
</p>

**ML / AI / Robotics**
<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch">
  <img src="https://img.shields.io/badge/Triton-GPU_kernels-76B900?style=flat-square&logo=nvidia&logoColor=white" alt="Triton">
  <img src="https://img.shields.io/badge/ONNX-005CED?style=flat-square&logo=onnx&logoColor=white" alt="ONNX">
  <img src="https://img.shields.io/badge/XGBoost-1f8b4c?style=flat-square" alt="XGBoost">
  <img src="https://img.shields.io/badge/SHAP-explainability-4a0d6b?style=flat-square" alt="SHAP">
</p>

**Marine Engine Systems**
<p>
  <img src="https://img.shields.io/badge/Medium--speed_marine_diesel-4--stroke-0d1b2a?style=flat-square" alt="Medium-speed">
  <img src="https://img.shields.io/badge/High--speed_marine_diesel-4--stroke-0d1b2a?style=flat-square" alt="High-speed">
  <img src="https://img.shields.io/badge/Bosch_P--pump-Mechanical_injection-0d1b2a?style=flat-square" alt="Bosch P-pump">
  <img src="https://img.shields.io/badge/Woodward-Governor_UG-0d1b2a?style=flat-square" alt="Woodward">
  <img src="https://img.shields.io/badge/Turbocharger-Overhaul_%26_balancing-0d1b2a?style=flat-square" alt="Turbocharger">
  <img src="https://img.shields.io/badge/Caterpillar-ADEM_A4-0d1b2a?style=flat-square" alt="Cat ADEM">
  <img src="https://img.shields.io/badge/Cummins-CM--series_ECU-0d1b2a?style=flat-square" alt="Cummins CM">
</p>

**Marine Automation & Industrial Protocols**
<p>
  <img src="https://img.shields.io/badge/J1939--71-Marine_CAN-0d1b2a?style=flat-square" alt="J1939">
  <img src="https://img.shields.io/badge/NMEA_2000-Navigation_Bus-0d1b2a?style=flat-square" alt="NMEA">
  <img src="https://img.shields.io/badge/Modbus_RTU-Industrial-0d1b2a?style=flat-square" alt="Modbus">
  <img src="https://img.shields.io/badge/OPC_UA-Unified_Architecture-0d1b2a?style=flat-square" alt="OPC UA">
  <img src="https://img.shields.io/badge/IEC_61131--3-PLC-0d1b2a?style=flat-square" alt="PLC">
  <img src="https://img.shields.io/badge/Class_society-survey_support-0d1b2a?style=flat-square" alt="Class survey">
</p>

**Edge & Systems**
<p>
  <img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust">
  <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux">
  <img src="https://img.shields.io/badge/Jetson-edge_GPU-76B900?style=flat-square&logo=nvidia&logoColor=white" alt="Jetson">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" alt="Git">
</p>

**Web & Visualization**
<p>
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Three.js-000000?style=flat-square&logo=three.js&logoColor=white" alt="Three.js">
  <img src="https://img.shields.io/badge/D3.js-F9A03C?style=flat-square&logo=d3.js&logoColor=white" alt="D3">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Neo4j-008CC1?style=flat-square&logo=neo4j&logoColor=white" alt="Neo4j">
</p>

---

### Domain Knowledge

```
Ship Power Plants     ██████████  Marine Diesel Engines
Propulsion Systems    █████████░  Overhaul & Diagnostics
Auxiliary Machinery   █████████░  Pumps · Compressors · Heat Exchangers
Engine Control        ████████░░  ECU · Governor · Fuel Injection
Dry-dock Operations   ████████░░  Inspection · Repair · Reporting
```

---

### Education & Certifications

**Operation of Ship Power Plants** — 4-year diploma program · graduated **2022**.
Thermodynamics · marine diesel engines · steam turbines · auxiliary machinery · ship electrical systems · automation & control.

**STCW International**: ISPS · Basic Safety Training (fire prevention, survival, personal safety) · Proficiency in Medical First Aid · Security Awareness Training.

**Languages**:
<p>
  <img src="https://img.shields.io/badge/English-Working_proficiency-1b263b?style=flat-square" alt="English">
  <img src="https://img.shields.io/badge/Deutsch-Working_proficiency-1b263b?style=flat-square" alt="Deutsch">
  <img src="https://img.shields.io/badge/Русский-Native-1b263b?style=flat-square" alt="Russian">
</p>

---

### Open to

**Maritime / Marine Automation**
- Marine Automation Engineer
- Vessel Performance / Condition Monitoring Engineer
- Embedded Systems Engineer (Maritime)
- Naval Systems Integration Engineer

**Hardware / ML systems** *(marine-domain expertise as differentiator)*
- Hardware/Software Co-design Engineer
- FPGA / ASIC Engineer (LLM inference acceleration)
- ML Inference Optimization Engineer
- Pre-silicon Verification Engineer

---

<p align="center">
  <em>"Most software engineers have never touched a marine diesel.<br>
  Most marine engineers have never written a GPU kernel.<br>
  Most GPU engineers have never designed the silicon underneath.<br>
  Three layers. One engineer."</em>
</p>
