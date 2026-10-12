import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Viswas.ai | Enterprise Intelligence Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- PROFESSIONAL CSS STYLING ---
st.markdown("""
    <style>
    /* Main Theme Colors & Font */
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
        font-family: 'Inter', sans-serif;
    }
    
    /* Header Styling */
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #4f46e5, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    
    .sub-header {
        color: #9ca3af;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    /* Card Containers */
    .metric-card {
        background-color: #1f2937;
        border: 1px solid #374151;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }

    /* Chat Styling */
    .stChatMessage {
        background-color: #1f2937;
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 10px;
    }
    
    /* Custom Footer */
    .footer {
        text-align: center;
        color: #6b7280;
        margin-top: 4rem;
        font-size: 0.85rem;
        border-top: 1px solid #374151;
        padding-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR CONFIGURATION ---
with st.sidebar:
    st.markdown("### ⚡ Viswas.ai")
    st.caption("v2.4.0 Enterprise Edition")
    st.divider()
    
    st.markdown("#### 🛠️ Model Configuration")
    selected_model = st.selectbox(
        "Engine", 
        ["Viswas-Enterprise-Alpha", "Viswas-Standard-v2", "Viswas-Code-Gen"]
    )
    
    temperature = st.slider("Temperature", 0.0, 1.0, 0.3, 0.1, help="Lower values are more deterministic; higher values are more creative.")
    max_tokens = st.slider("Max Response Tokens", 256, 4096, 2048, 128)
    
    st.divider()
    st.markdown("#### 🔒 Authentication")
    api_key = st.text_input("API Key", type="password", placeholder="vws_live_xxxxxxxx...")
    
    st.divider()
    st.markdown("#### 👨‍💻 Platform Architect")
    st.info("**Vishveshwar Ray**\n\nFounder & Principal AI Architect")
    
    if st.button("Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# --- MAIN INTERFACE HEADER ---
st.markdown("<h1 class='main-header'>Viswas.ai</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Next-generation enterprise AI platform architected by <b>Vishveshwar Ray</b>.</p>", unsafe_allow_html=True)

# --- METRIC SUMMARY CARDS ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("<div class='metric-card'><h3>99.9%</h3><p>Uptime SLA</p></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='metric-card'><h3>< 120ms</h3><p>Latency</p></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='metric-card'><h3>SOC 2</h3><p>Compliant</p></div>", unsafe_allow_html=True)
with col4:
    st.markdown("<div class='metric-card'><h3>256-bit</h3><p>Encryption</p></div>", unsafe_allow_html=True)

st.write("")
st.write("")

# --- CHAT INTERFACE SESSION STATE ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am **Viswas.ai**, engineered by **Vishveshwar Ray**. How can I assist your enterprise workflow today?"}
    ]

# Display historical messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("Message Viswas.ai..."):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # Professional simulation / Integration Hook
        with st.spinner("Processing request through Viswas Neural Core..."):
            time.sleep(1) # Simulated network delay
            
            response_text = f"**[Viswas Core Output]**\n\nThank you for your query, processed via `{selected_model}` (Temp: `{temperature}`).\n\nYou asked: *\"{prompt}\"*.\n\nAs an enterprise solution designed under the leadership of **Vishveshwar Ray**, Viswas.ai is optimized for high-throughput reasoning, security, and precision. \n\n*(To connect this code to a live backend, replace this simulation block with your OpenAI, Anthropic, or custom endpoint API call).* "
            
            message_placeholder.markdown(response_text)
            
    # Save assistant response to session state
    st.session_state.messages.append({"role": "assistant", "content": response_text})

# --- PROFESSIONAL FOOTER ---
st.markdown("""
    <div class='footer'>
        <p>© 2026 Viswas.ai Inc. All rights reserved. Architected and Developed by <b>Vishveshwar Ray</b>.</p>
    </div>
""", unsafe_allow_html=True)
