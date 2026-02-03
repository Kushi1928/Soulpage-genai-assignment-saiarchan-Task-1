import streamlit as st
from graph.orchestrator import build_graph

st.set_page_config(
    page_title="Multi-Agent Company Intelligence System",
    page_icon="🤖",
    layout="centered"
)

st.markdown(
    """
    <style>
    .stApp {
    background: linear-gradient(135deg, #e0f7ff, #cceeff, #b3e5ff);
    color: #0b1f33;
    }


    .card {
        background-color: rgba(255, 255, 255, 0.08);
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }

    h1, h2, h3 {
        color: #00f5d4;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align:center;'>🚀 AgentIQ</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>Multi-Agent Company Intelligence System</h3>", unsafe_allow_html=True)

st.write("")

company = st.text_input("🏢 Enter Company Name", "Infosys")


if st.button("🔍 Generate Intelligence Report"):
    app = build_graph()
    result = app.invoke({"company": company})

  
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("## 📊 Market Data (Data Collector Agent)")
    st.write(f"💰 **Stock Price:** {result['market_data']['stock_price']}")
    st.write(f"📈 **Market Trend:** {result['market_data']['market_trend']}")

    st.markdown("📰 **Recent News:**")
    for news in result["market_data"]["news"]:
        st.write(f"• {news}")
    st.markdown("</div>", unsafe_allow_html=True)


    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("## 🧠 Analysis & Insights (Analyst Agent)")
    st.write(result["analysis"])
    st.markdown("</div>", unsafe_allow_html=True)


    st.markdown(
        "<p style='text-align:center; opacity:0.7;'>Powered by LangGraph • Agentic AI</p>",
        unsafe_allow_html=True
    )
