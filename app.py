import streamlit as st
import pandas as pd
import datetime

# --- CONFIG & THEME ---
st.set_page_config(page_title="URBAN-TRACE | URBAN-TRACE", layout="wide")

# Custom CSS for the "Command Center" Aesthetic
st.markdown("""
    <style>

    /* Mega Heading for Sidebar */
    .sidebar-title {
        font-size: 3.5rem !important; /* Large Hero Size */
        font-weight: 800 !important;
        line-height: 1 !important;
        padding-top: 0px !important;
        background: linear-gradient(90deg, #2E5BFF, #1A44D4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: -10px !important;
    }
    
    .sidebar-tagline {
        font-size: 1.1rem !important;
        font-weight: 400 !important;
        color:black !important;
        opacity: 0.8;
    }  

    
    /* Main Background & Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #F8FAFC;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: skyblue !important;
        border-right: 1px solid #E2E8F0;
    }

    /* Card-style Containers */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        padding: 20px !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03) !important;
    }

    /* Button Styling */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        border: none;
        background-color: #2E5BFF;
        color: white;
        font-weight: 600;
        padding: 0.6rem 1rem;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #1A44D4;
        box-shadow: 0 10px 15px -3px rgba(46, 91, 255, 0.3);
        transform: translateY(-1px);
    }

    /* Map/Image Border Styling */
    [data-testid="stImage"] img {
        border-radius: 12px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        border: 1px solid #E2E8F0;
    }

    /* Success/Error Message Styling */
    div[data-testid="stNotification"] {
        border-radius: 10px;
    }
    
    /* Header Polish */
    h1, h2, h3 {
        color: #1E293B;
        letter-spacing: -0.02em;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: SYSTEM CONTROL ---
with st.sidebar:
    # Use Markdown with a custom class for total control over font size
    st.markdown('<p class="sidebar-title">🏙️URBAN<br>TRACE</p>', unsafe_allow_html=True)
    st.markdown('<p class="sidebar-tagline">GeoAI Verification Engine</p>', unsafe_allow_html=True)
    
    st.divider()
    selected_ward = st.selectbox("Catchment Area", ["Hebbal Valley", "Koramangala", "JP Nagar"])
    st.divider()
    # Hardcoded stats for stability
    st.metric(label="Network Integrity Score", value="68.4%", delta="-1.2%")
    st.metric(label="Critical Logic Failures", value="14 Nodes")
    
    st.divider()
    st.write("**System Status:** Operational")
    st.write("**Data Source:** Open City")

# --- MAIN LAYOUT ---
# 1. Add the Global Metrics Bar here
st.markdown("### 📊 Real-Time Network Overview")
m1, m2, m3 = st.columns(3)
m1.metric("Integrity", "68.4%", "-1.2%")
m2.metric("Hotspots", "60", "Critical")
m3.metric("Tickets", "102", "Active")

st.divider() # Adds a clean line between stats and the map
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
        st.image("ai_inference.png", caption="YOLOv8 Identification: Clogged and Waste")
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
