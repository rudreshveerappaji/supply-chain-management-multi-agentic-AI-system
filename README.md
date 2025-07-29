# 🏗️ Multi-Agent Supply Chain System (Construction SCM) using CrewAI

This project demonstrates a **multi-agent system** for **supply chain management** in a **civil engineering/construction** use case using **CrewAI**.

---

## 📌 Overview

Agents collaborate to handle procurement, forecasting, logistics, and site material tracking.

### 🔄 Agent Interaction Flow

![Agent Flowchart](agents_flowchart.png)

- **ForecastingAgent** → predicts demand from usage data
- **ProcurementAgent** → places material orders from forecasts
- **LogisticsAgent** → schedules delivery of ordered materials
- **SiteManagerAgent** → tracks delivery and usage, updates forecast loop

---

## 📁 Project Structure

```
construction_scm_crewai/
├── agents/           # Agent definitions
├── tasks/            # Task flows
├── tools/            # Integrations (optional)
├── data/             # CSV files for mock usage and outputs
├── configs/          # Settings/config files
├── logs/             # Optional runtime logs
├── main.py           # Entry point to run CrewAI system
├── README.md         # This file
└── agent_flowchart.png # Visualization of agent interactions
```

---

## ▶️ How to Run

```bash
python main.py
```

This will:
1. Load agents from `agents/setup_agents.py`
2. Set up tasks from `tasks/setup_tasks.py`
3. Launch the CrewAI multi-agent orchestration
4. Output results in `data/` folder

---

## 📊 Sample Data

- `data/material_usage_log.csv` contains mock usage history
- Outputs like `material_forecast.csv`, `purchase_orders.csv`, `delivery_schedule.csv`, etc., are generated

---

## 🚀 Next Steps

- Add tools (e.g., Google Sheets, OCR, DB integration)
- Expand agents (ComplianceAgent, FinanceAgent, etc.)
- Deploy with a Streamlit or FastAPI interface

---

Built using ❤️ with [CrewAI](https://github.com/joaomdmoura/crewAI)