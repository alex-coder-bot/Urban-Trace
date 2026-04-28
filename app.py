import streamlit as st
import pandas as pd
import datetime

# --- CONFIG & THEME ---
st.set_page_config(page_title="URBAN-TRACE | URBAN-TRACE", layout="wide")

# Custom CSS for that professional 'Sutra' look
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_content_usage=True)

# --- SIDEBAR: SYSTEM CONTROL ---
with st.sidebar:
    st.title("🛡️ URBAN-TRACE")
    st.subheader("GeoAI Verification Engine")
    
    selected_ward = st.selectbox("Catchment Area", ["Hebbal Valley (Pilot)", "Koramangala", "Varthur"])
    
    st.divider()
    # Hardcoded stats for stability
    st.metric(label="Network Integrity Score", value="68.4%", delta="-1.2%")
    st.metric(label="Critical Logic Failures", value="14 Nodes")
    
    st.divider()
    st.write("**System Status:** Operational")
    st.write("**Data Source:** Open City")

# --- MAIN LAYOUT ---
col_left, col_right = st.columns([1.5, 1])

with col_left:
    st.subheader("📍 Topographical Logic Audit Map")
    # Using your high-fidelity network map image
    st.image("map_placeholder.png", use_container_width=True, caption="Layer: Natural Flow Accumulation vs. Infrastructure")
    
    st.info("💡 **Logic Analysis:** Drainage segments in RED indicate elevation traps where the natural slope contradicts the current physical pipe network.")

with col_right:
    st.subheader("🔍 GeoAI Physical Verification")
    
    # Simulation Logic
    node_id = "HB-V1-092"
    st.error(f"ALERT: Logic Failure at Node {node_id}")
    
    # Feature 1: The 'Static' AI Verification
    with st.expander("View AI Diagnostic Evidence", expanded=True):
        st.image("ai_inference.png", caption="YOLOv8 Identification: Siltation (94%) & Waste (88%)")
        st.caption(f"Last Scanned: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")

    # Feature 2: Automated Ticketing
    if st.button("Generate Maintenance Ticket"):
        st.success(f"Ticket #TR-BK-{node_id} Dispatched!")
        ticket_data = {
            "Field": ["Status", "Priority", "Assigned Crew", "GPS"],
            "Details": ["OPEN", "CRITICAL", "Ward-21 Maintenance", "13.0489, 77.5913"]
        }
        st.table(pd.DataFrame(ticket_data))

# --- FEATURE 3: CITIZEN REPORTING (Simple Version) ---
st.divider()
st.subheader("📢 Citizen Transparency Portal")
with st.expander("Submit a Field Report"):
    c1, c2 = st.columns(2)
    with c1:
        st.file_uploader("Upload Image of Clogged Drain")
    with c2:
        st.text_input("Location/Landmark")
        if st.button("Submit for AI Validation"):
            st.info("Processing... Image queued for YOLOv8 batch verification.")
