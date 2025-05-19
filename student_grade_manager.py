import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def calculate_grades(scores):
    grades = [
        "A" if score >= 90 else
        "B" if score >= 80 else
        "C" if score >= 70 else
        "D" if score >= 60 else
        "F"
        for score in scores
    ]
    return grades

def main():
    st.title("📚 Student Grade Manager")
    
    # Input field for scores
    student_scores = st.text_input("Enter student scores separated by commas:")
    
    # Button to process scores
    if st.button("Submit"):
        try:
            scores = [int(score.strip()) for score in student_scores.split(",")]
            grades = calculate_grades(scores)
            
            # Filter Passing and Failing Students
            passing_students = [score for score in scores if score >= 60]
            failing_students = [score for score in scores if score < 60]
            
            # Display Results
            st.subheader("📊 Student Grades")
            data = {"Student": [f"Student {i+1}" for i in range(len(scores))],
                    "Score": scores,
                    "Grade": grades}
            df = pd.DataFrame(data)
            st.dataframe(df)
            
            # Visualization
            st.subheader("📈 Grade Distribution")
            plt.figure(figsize=(6, 4))
            plt.hist(grades, bins=5, color='skyblue', edgecolor='black')
            plt.xlabel("Grades")
            plt.ylabel("Number of Students")
            plt.title("Grade Distribution Chart")
            st.pyplot(plt)
            
            # Display Pass/Fail
            st.subheader("✅ Passing & ❌ Failing Students")
            st.write(f"Passing Students: {passing_students}")
            st.write(f"Failing Students: {failing_students}")
            
            # Option to download results
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download Results", data=csv, file_name="student_grades.csv", mime="text/csv")
        
        except ValueError:
            st.error("❗ Please enter valid numerical scores separated by commas.")

if __name__ == "__main__":
    main()
