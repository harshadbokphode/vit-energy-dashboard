import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="VIT Smart Energy Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- LOAD DATA ----------------
df = pd.read_csv("energy_data.csv")

# ---------------- TITLE ----------------
st.title("⚡ VIT Campus Smart Energy Utility Dashboard")
st.caption("Department & floor-wise energy monitoring for sustainability planning")

# ---------------- KPI CONTAINER ----------------
with st.container():
    col1, col2, col3 = st.columns(3)

    total_energy = df["Total_kWh"].sum()
    total_floors = df.shape[0]
    total_departments = df["Department"].nunique()

    col1.metric("🔌 Total Energy (kWh/day)", total_energy)
    col2.metric("🏢 Floors Monitored", total_floors)
    col3.metric("🎓 Departments", total_departments)

st.divider()

# ---------------- FILTERS ----------------
with st.sidebar:
    st.header("🔍 Filters")
    selected_dept = st.selectbox(
        "Select Department",
        ["All"] + list(df["Department"].unique())
    )

if selected_dept != "All":
    df = df[df["Department"] == selected_dept]

# ---------------- GRAPHS CONTAINER ----------------
with st.container():
    col1, col2 = st.columns(2)

    # -------- Department-wise Energy --------
    with col1:
        st.subheader("🏢 Department-wise Energy")

        dept_energy = df.groupby("Department")["Total_kWh"].sum()

        fig, ax = plt.subplots(figsize=(4, 3))
        dept_energy.plot(kind="bar", ax=ax)
        ax.set_ylabel("kWh/day")
        ax.set_xlabel("")
        plt.xticks(rotation=30)

        st.pyplot(fig, use_container_width=True)

    # -------- Floor-wise Energy --------
    with col2:
        st.subheader("🏬 Floor-wise Energy")

        fig2, ax2 = plt.subplots(figsize=(4, 3))
        ax2.bar(df["Floor"], df["Total_kWh"])
        ax2.set_ylabel("kWh/day")
        ax2.set_xlabel("")

        st.pyplot(fig2, use_container_width=True)

st.divider()

# ---------------- COMPONENT ANALYSIS ----------------
with st.container():
    col1, col2 = st.columns([1, 1])

    # -------- Component Pie --------
    with col1:
        st.subheader("🔌 Component-wise Energy")

        components = df[["Classroom_kWh", "Washroom_kWh", "Water_kWh"]].sum()

        fig3, ax3 = plt.subplots(figsize=(4, 3))
        ax3.pie(
            components,
            labels=components.index,
            autopct="%1.1f%%",
            startangle=90
        )
        ax3.axis("equal")

        st.pyplot(fig3, use_container_width=True)

    # -------- Sustainability Box --------
    with col2:
        st.subheader("🌍 Sustainability Indicators")

        carbon = total_energy * 0.82
        solar_offset = total_energy * 0.40

        st.info(f"**Estimated CO₂ Emissions:** {carbon:.2f} kg/day")
        st.success(f"**Potential Solar Offset:** {solar_offset:.2f} kWh/day")

        st.write("✔ Based on standard Indian grid emission factors")
        st.write("✔ Supports long-term green campus planning")

st.divider()

# ---------------- DATA TABLE ----------------
with st.container():
    st.subheader("📋 Energy Data Snapshot")
    st.dataframe(df, use_container_width=True)

# ---------------- FOOTER ----------------
st.success("Dashboard UI optimized and running successfully ✅")

st.divider()

# ---------------- SMART ENERGY SOLUTIONS ----------------
st.header("💡 Smart Energy Solutions")

solutions_col1, solutions_col2, solutions_col3 = st.columns(3)

with solutions_col1:
    st.subheader("🔆 Smart Lighting Systems")
    st.write("Use LED lights and motion sensors to reduce electricity usage.")

with solutions_col2:
    st.subheader("☀️ Solar Energy Integration")
    st.write("Install rooftop solar panels to offset campus energy demand.")

with solutions_col3:
    st.subheader("🤖 AI-Based Energy Optimization")
    st.write("Analyze energy data to predict peak loads and improve efficiency.")

st.divider()

solutions_col4, solutions_col5, solutions_col6 = st.columns(3)

with solutions_col4:
    st.subheader("❄️ Smart HVAC Control")
    st.write("Automated temperature control based on occupancy.")

with solutions_col5:
    st.subheader("🚨 Real-Time Energy Alerts")
    st.write("Notify administrators when energy consumption exceeds limits.")

with solutions_col6:
    st.subheader("📊 Department Energy Benchmarking")
    st.write("Compare department-wise usage to identify high consumption areas.")
