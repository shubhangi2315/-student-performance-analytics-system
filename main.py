
import pandas as pd

# 1. Read student dataset
students = pd.read_csv("students.csv")

# 2. Subjects
subjects = [
    "Python",
    "Mathematics",
    "Electronics",
    "Communication"
]

# 3. Calculate total marks
students["Total_Marks"] = students[subjects].sum(axis=1)

# 4. Calculate average marks
students["Average_Marks"] = (
    students[subjects].mean(axis=1).round(2)
)

# 5. Assign grades
def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

students["Grade"] = students["Average_Marks"].apply(
    assign_grade
)

# 6. Check Pass or Fail
def check_result(marks):
    if all(mark >= 35 for mark in marks):
        return "Pass"
    return "Fail"

students["Result"] = students[subjects].apply(
    lambda row: check_result(row.tolist()),
    axis=1
)

# 7. Display student performance report
print("\n" + "=" * 65)
print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("=" * 65)

columns = [
    "Student_ID",
    "Name",
    "Department",
    "Total_Marks",
    "Average_Marks",
    "Grade",
    "Result"
]

print(students[columns].to_string(index=False))

# 8. Class analysis
print("\n" + "=" * 40)
print("CLASS PERFORMANCE ANALYSIS")
print("=" * 40)

class_average = round(students[subjects].to_numpy().mean(), 2)
print("Total Students:", len(students))
print("Class Average:", class_average)
print("Pass Students:", (students["Result"] == "Pass").sum())
print("Fail Students:", (students["Result"] == "Fail").sum())

# 9. Top 3 students
print("\n" + "=" * 40)
print("TOP 3 STUDENTS")
print("=" * 40)

top_students = students.nlargest(3, "Average_Marks")

print(
    top_students[
        ["Name", "Department", "Average_Marks", "Grade"]
    ].to_string(index=False)
)

# 10. Subject-wise average
print("\n" + "=" * 40)
print("SUBJECT-WISE AVERAGE")
print("=" * 40)

print(students[subjects].mean().round(2).to_string())

# 11. Save report
students.to_csv("student_performance_report.csv", index=False)

print("\nReport saved as student_performance_report.csv")
print("Student analytics completed successfully!")

