import streamlit as st
import folium
from streamlit_folium import st_folium
from engine.inference import run_detection
from engine.audit import calculate_integrity

# 1. Page Configuration (The "Vibe")
st.set_page_config(page_title="URBAN-TRACE | GeoAI Dashboard", layout="wide")

# 2. Sidebar: Control Center
with st.sidebar:
    st.title("🛡️ URBAN-TRACE")
    st.subheader("Sutra-Audit Engine v1.0")
    selected_ward = st.selectbox("Select Catchment Area", ["Hebbal Valley", "Koramangala", "Varthur"])
    
    # Integrity Metric (The "Sutra" Score)
    integrity_score = calculate_integrity(selected_ward)
    st.metric(label="Catchment Integrity Score", value=f"{integrity_score}%", delta="-2% (Last 24h)")
    
    st.divider()
    st.write("Logged in as: **Admin (Solo-Dev)**")

# 3. Main Dashboard Layout: 2 Columns
col_map, col_audit = st.columns([2, 1])

with col_map:
    st.subheader("Interactive Logic Audit Map")
    # Base Map centered on Bengaluru
    m = folium.Map(location=[13.0489, 77.5913], zoom_start=13, tiles="CartoDB dark_matter")
    
    # TO DO: Add GeoJSON layers for Flow Accumulation
    # TO DO: Add clickable Markers for 'Red Alert Nodes'
    
    st_data = st_folium(m, width=800, height=500)

with col_audit:
    st.subheader("AI Verification Portal")
    if st_data['last_object_clicked']:
        # Trigger YOLO when a map node is clicked
        node_id = st_data['last_object_clicked']
        st.info(f"Analyzing Physical Evidence for Node: {node_id}")
        
        # Display the YOLO Inference Result
        result_img, conf = run_detection("data/sample_drain.jpg")
        st.image(result_img, caption=f"YOLOv8 Detection | Confidence: {conf}%")
        
        if st.button("Generate Maintenance Ticket"):
            st.success("Ticket #0921 created and sent to BBMP portal.")
    else:
        st.write("Click a **Red Alert Node** on the map to run GeoAI verification.")
        


st.header("📢 Citizen Engagement Portal")
st.write("Report a 'Logic Failure' in your neighborhood for AI verification.")

uploaded_file = st.file_uploader("Upload Image of Drain", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # 1. Run AI Verification on User Upload
    user_img, user_conf = run_detection(uploaded_file)
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(user_img, caption="User Submitted Image (AI Analyzed)")
    
    with col2:
        if user_conf > 70: # Verification threshold
            st.success(f"✅ VERIFIED: Blockage detected ({user_conf}%).")
            st.info("Status: Logged to Public Integrity Dashboard.")
            # Trigger Ticketing
            t = generate_ticket("Citizen_Report_01", {"label": "Blocked", "confidence": user_conf}, {"lat": 13.0, "lng": 77.5})
            st.json(t)
        else:
            st.warning("⚠️ UNVERIFIED: No significant blockage detected by GeoAI.")
