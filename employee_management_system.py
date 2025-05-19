import streamlit as st

# Employee Class Hierarchy
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        return f"**🆔 ID:** {self.emp_id} | **👤 Name:** {self.name} | 💰 **Salary:** ${self.salary}"

    def calculate_bonus(self):
        return self.salary * 0.1

class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department

    def display_info(self):
        return f"{super().display_info()} | 🏢 **Department:** {self.department}"

    def calculate_bonus(self):
        return self.salary * 0.2

class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language

    def display_info(self):
        return f"{super().display_info()} | 💻 **Tech Stack:** {self.programming_language}"

    def calculate_bonus(self):
        return self.salary * 0.5

# Initialize session state for employees
if "employees" not in st.session_state:
    st.session_state.employees = []

# Streamlit UI
st.title("💼 Employee Management System")

# Sidebar Navigation
menu = ["🏠 Dashboard", "➕ Add Employee", "📋 View Employees"]
choice = st.sidebar.selectbox("📌 Select an Option", menu)

if choice == "🏠 Dashboard":
    st.subheader("📊 Employee Dashboard")
    total_employees = len(st.session_state.employees)
    total_salary = sum(emp.salary for emp in st.session_state.employees)
    avg_salary = total_salary / total_employees if total_employees else 0

    st.metric("👥 Total Employees", total_employees)
    st.metric("💰 Total Salary Expense", f"${total_salary}")
    st.metric("📊 Average Salary", f"${round(avg_salary, 2)}")

elif choice == "➕ Add Employee":
    st.subheader("➕ Add a New Employee")
    name = st.text_input("👤 Employee Name")
    emp_id = st.text_input("🆔 Employee ID")
    salary = st.number_input("💰 Salary", min_value=0.0, step=500.0)

    emp_type = st.radio("🏢 Choose Employee Type", ["Regular Employee", "Manager", "Developer"])

    if emp_type == "Manager":
        department = st.text_input("🏢 Department")
    elif emp_type == "Developer":
        programming_language = st.text_input("💻 Programming Language")

    if st.button("✅ Add Employee"):
        if name and emp_id and salary:
            if emp_type == "Regular Employee":
                st.session_state.employees.append(Employee(name, emp_id, salary))
            elif emp_type == "Manager" and department:
                st.session_state.employees.append(Manager(name, emp_id, salary, department))
            elif emp_type == "Developer" and programming_language:
                st.session_state.employees.append(Developer(name, emp_id, salary, programming_language))
            else:
                st.error("⚠️ Please fill all required fields!")
            st.success(f"🎉 Employee '{name}' added successfully!")
        else:
            st.error("⚠️ Please enter all details!")

elif choice == "📋 View Employees":
    st.subheader("📋 Employee List")
    if not st.session_state.employees:
        st.warning("⚠️ No employees added yet.")
    else:
        search_query = st.text_input("🔍 Search by Employee ID or Name").lower()
        for emp in st.session_state.employees:
            emp_info = emp.display_info()
            if search_query in emp.emp_id.lower() or search_query in emp.name.lower():
                st.write(emp_info)
                st.write(f"💰 **Bonus:** ${emp.calculate_bonus()}")
                st.markdown("---")
