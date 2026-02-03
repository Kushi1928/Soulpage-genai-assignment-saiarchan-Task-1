from langgraph.graph import StateGraph
from agents.data_collector import data_collector_agent
from agents.analyst import analyst_agent

from typing import TypedDict

class AgentState(TypedDict):
    company: str
    market_data: dict
    analysis: str


def collect_data(state: AgentState):
    company = state["company"]
    state["market_data"] = data_collector_agent.invoke(company)
    return state

def analyze_data(state: AgentState):
    state["analysis"] = analyst_agent(state["market_data"])
    return state


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("collector", collect_data)
    graph.add_node("analyst", analyze_data)

    graph.set_entry_point("collector")
    graph.add_edge("collector", "analyst")
    graph.set_finish_point("analyst")

    return graph.compile()

