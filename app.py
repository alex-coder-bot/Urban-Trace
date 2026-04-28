import streamlit as st
import time
from engine.audit import calculate_integrity
from engine.ticketing import generate_ticket

# 1. Page Config
st.set_page_config(page_title="URBAN-TRACE Command Center", layout="wide")

# 2. Sidebar Stats
with st.sidebar:
    st.title("🛡️ URBAN-TRACE")
    ward = st.selectbox("Select Catchment", ["Hebbal Valley", "Koramangala"])
    score = calculate_integrity(ward)
    st.metric("Integrity Score", f"{score}%")
    st.write("---")
    st.write("**Mode:** Verification Simulation")

# 3. Main Interface
col_map, col_ai = st.columns([1.5, 1])

with col_map:
    st.subheader("📍 Catchment Logic Audit")
    # Placeholder for your Folium Map
    st.image("assets/map_placeholder.png", caption="Interactive Audit Map (Integrated with Bhuvan DEM)")
    st.info("Select a 'Red Alert' node on the map to investigate.")

with col_ai:
    st.subheader("🔍 GeoAI Verification")
    
    # Simulate a selected node
    node_id = "HB-V1-092"
    st.warning(f"ACTION REQUIRED: Logic Failure at {node_id}")
    
    # THE TRIGGER BUTTON
    if st.button("RUN AI DIAGNOSTIC"):
        with st.spinner("Accessing field camera & running YOLOv8..."):
            time.sleep(1.5) # The "Wait" adds realism and tension
            
            # Display your pre-recorded video or high-res inference image
            st.video("assets/demo_video.mp4") # Video of the AI working
            
            st.success("ANALYSIS COMPLETE: Blockage Detected (94.2%)")
            
            # Show the pre-prepared inference result
            st.image("assets/node_01_inf.jpg", caption="Physical Evidence: Siltation & Plastic Waste")

            # Generate Ticket
            if st.button("DISPATCH MAINTENANCE"):
                ticket = generate_ticket(node_id, {"conf": 94.2}, {"lat": 13.04, "lng": 77.59})
                st.table(ticket)
