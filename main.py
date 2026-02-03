from dotenv import load_dotenv
load_dotenv()

from graph.orchestrator import build_graph

if __name__ == "__main__":
    app = build_graph()

    company_name = "Infosys"

    result = app.invoke({
        "company": company_name
    })

    print("\n📌 Company Intelligence Report\n")
    print("Company:", company_name)
    print("\n📊 Market Data:\n", result["market_data"])
    print("\n📈 Analysis:\n", result["analysis"])
