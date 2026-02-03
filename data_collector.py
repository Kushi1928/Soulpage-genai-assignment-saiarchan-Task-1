from langchain_core.tools import tool
from tools.market_data_tool import fetch_company_data

@tool
def data_collector_agent(company: str):
    """Collects market data and recent news for a company"""
    return fetch_company_data(company)
