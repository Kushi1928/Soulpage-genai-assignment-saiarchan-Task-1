🤖 AgentIQ – Multi-Agent Company Intelligence System

AgentIQ is a **LangGraph-based multi-agent AI system** designed to generate structured company intelligence reports. The project demonstrates how **agentic AI architectures** can be used to decompose complex analytical workflows into independent, collaborative agents operating on a shared state.

The system focuses on modularity, scalability, and reproducibility, making it suitable for academic projects, portfolio demonstrations, and extensible real-world applications.

📌 About the Project

Traditional AI applications often use monolithic pipelines where data collection, processing, and analysis are tightly coupled. AgentIQ adopts an **agent-based design**, where each agent has a well-defined responsibility and communicates through a controlled execution graph.

The project showcases:

* Multi-agent orchestration using **LangGraph**
* Stable data contracts between agents and UI
* Optional integration of **Gemini Generative AI** for advanced reasoning
* Interactive visualization using **Streamlit**


🏗️ System Architecture

AgentIQ follows a **graph-based agent orchestration model**.

🔹 High-Level Architecture Flow

User (Streamlit UI)
        │
        ▼
LangGraph Orchestrator
        │
        ▼
Data Collector Agent
        │
        ▼
Analyst Agent (Gemini / Mock Logic)
        │
        ▼
Final Structured Output
        │
        ▼
Streamlit Dashboard

🔹 Agent Responsibilities

**Data Collector Agent**

* Fetches company market data
* Structures data into a stable schema
* Can operate in mock mode or API-based mode

Analyst Agent

* Consumes structured market data
* Generates analytical insights and trends
* Can be powered by Gemini API or fallback logic


 🔹 Shared State Schema (Example)

python
{
  "company": "Infosys",
  "stock_price": "₹3245",
  "predicted_price": "₹3310",
  "market_trend": "Bullish",
  "news": [ ... ],
  "analysis": "Generated insights"
}



## 📁 Project Structure


Soulpage-genai-assignment-saiarchan/
│
├── app.py                     # Streamlit UI
├── main.py                    # CLI runner
│
├── graph/
│   └── orchestrator.py        # LangGraph orchestration
│
├── agents/
│   ├── data_collector.py      # Data Collector Agent
│   └── analyst.py             # Analyst Agent
│
├── tools/
│   └── market_data_tool.py    # Market data & prediction logic
│
├── requirements.txt
└── README.md


⚙️ Setup Instructions

 1️⃣ Prerequisites

* Python **3.9 or higher**
* pip
* Internet connection (optional, for APIs)



2️⃣ Create Virtual Environment (Recommended)

bash
python -m venv venv


Activate it:

**Windows**

bash
venv\Scripts\activate


**macOS / Linux**

bash
source venv/bin/activate



 3️⃣ Install Dependencies

bash
pip install -r requirements.txt



 4️⃣ (Optional) Set Gemini API Key

The project works **without API keys** (mock mode).

If Gemini integration is required:

bash
setx GEMINI_API_KEY "your_api_key_here"   # Windows
```


## ▶️ Example Usage

### 🖥️ Running the Streamlit App (Recommended)

bash
streamlit run app.py


**Steps:**

1. Open the app in browser
2. Enter a company name (e.g., *Infosys*)
3. Click **Generate Intelligence Report**
4. View market data, prediction, and analysis


### 💻 Running via Command Line

bash
python main.py


**Sample Output (Console):**

text
Company: Infosys
Stock Price: ₹3245
Predicted Price: ₹3310
Market Trend: Bullish
Analysis: Positive outlook driven by earnings growth


### 🧪 Using the Market Data Tool Directly

```python
from tools.market_data_tool import fetch_company_data

data = fetch_company_data("Infosys")
print(data)
```


🔒 Design Highlights

* Agent-based modular architecture
* Stable data contracts (prevents runtime errors)
* API-agnostic and fault-tolerant design
* UI decoupled from agent logic
* Easily extensible with ML models or LLMs


 ⚠️ Disclaimer

> This project is for **educational purposes only**.
> Stock prices and predictions do **not** constitute financial advice.

