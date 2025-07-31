import streamlit as st

#Employee profiles example
employees = {
    "Amal Ali": {
        "Role": "Data Analyst",
        "Department": "Data Science Dept.",
        "Skills": ["Python", "SQL", "Excel"],
        "Performance": 78,
        "Engagement": 65,
        "Risk": "Medium"
    },
    "Faisal Rahman": {
        "Role": "Marketing Specialist",
        "Department": "Marketing & Communications Dept.",
        "Skills": ["SEO", "Content Creation", "Analytics"],
        "Performance": 70,
        "Engagement": 72,
        "Risk": "Low"
    },
    "Sara Hussain": {
        "Role": "HR Officer",
        "Department": "Human Resources Dept.",
        "Skills": ["Recruitment", "Payroll", "Compliance"],
        "Performance": 82,
        "Engagement": 58,
        "Risk": "High"
    }
}


risk_levels = ["Low", "Medium", "High"]


st.title("Digital Twin – Employee Simulation Demo")


selected = st.selectbox("Select an Employee", list(employees.keys()))
emp = employees[selected]

#Employee profile display
st.subheader("👤 Employee Profile")
st.write(f"**Name:** {selected}")
st.write(f"**Role:** {emp['Role']}")
st.write(f"**Department:** {emp['Department']}")
st.write(f"**Skills:** {', '.join(emp['Skills'])}")
st.write(f"**Current Performance Score:** {emp['Performance']}")
st.write(f"**Current Engagement Level:** {emp['Engagement']}%")
st.write(f"**Current Attrition Risk:** {emp['Risk']}")

#What-If Simulations
st.subheader("🔁 Apply Simulations")
scenarios = st.multiselect("Select one or more changes to simulate:", [
    "Give a promotion",
    "Add AI/ML skill",
    "Change to toxic manager",
    "No raise this year",
    "Enroll in training program",
    "Transfer to supportive manager",
    "Reduce workload by 10%",
    "Delay in bonus payment",
    "Assign to cross-functional team"
])

#apply effects after selecting scenarios and calculating new values
performance = emp['Performance']
engagement = emp['Engagement']
risk_index = risk_levels.index(emp['Risk'])

for option in scenarios:
    if option == "Give a promotion":
        performance += 10
        engagement += 8
        risk_index = max(0, risk_index - 1)
    elif option == "Add AI/ML skill":
        performance += 7
        risk_index = max(0, risk_index - 1)
    elif option == "Change to toxic manager":
        engagement -= 20
        risk_index = min(2, risk_index + 1)
    elif option == "No raise this year":
        engagement -= 15
        risk_index = min(2, risk_index + 1)
    elif option == "Enroll in training program":
        performance += 5
        engagement += 6
    elif option == "Transfer to supportive manager":
        engagement += 10
        risk_index = max(0, risk_index - 1)
    elif option == "Reduce workload by 10%":
        engagement += 7
    elif option == "Delay in bonus payment":
        engagement -= 10
        risk_index = min(2, risk_index + 1)
    elif option == "Assign to cross-functional team":
        performance += 6
        engagement += 5

#New values after applying scenarios
performance = min(100, max(0, performance))
engagement = min(100, max(0, engagement))
risk = risk_levels[risk_index]


st.subheader("📊 Simulation Results")
st.write(f"**New Performance Score:** {performance}")
st.write(f"**New Engagement Level:** {engagement}%")
st.write(f"**New Attrition Risk:** {risk}")

#run 'streamlit run Demo.py' in terminal to start the app