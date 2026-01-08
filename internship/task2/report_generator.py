import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Read data from CSV
data = pd.read_csv("data.csv")

# Analysis
average_marks = data["Marks"].mean()
highest_marks = data["Marks"].max()
lowest_marks = data["Marks"].min()

# Create PDF
file_name = "output_report.pdf"
pdf = canvas.Canvas(file_name, pagesize=A4)
width, height = A4

# Title
pdf.setFont("Helvetica-Bold", 18)
pdf.drawString(50, height - 50, "Automated Student Report")

# Subtitle
pdf.setFont("Helvetica", 12)
pdf.drawString(50, height - 80, "Generated using Python")

# Data Section
pdf.setFont("Helvetica-Bold", 14)
pdf.drawString(50, height - 130, "Student Marks Data:")

y_position = height - 160
pdf.setFont("Helvetica", 12)

for index, row in data.iterrows():
    pdf.drawString(60, y_position, f"{row['Name']} : {row['Marks']}")
    y_position -= 20

# Analysis Section
pdf.setFont("Helvetica-Bold", 14)
pdf.drawString(50, y_position - 20, "Analysis Summary:")

pdf.setFont("Helvetica", 12)
pdf.drawString(60, y_position - 50, f"Average Marks: {average_marks:.2f}")
pdf.drawString(60, y_position - 70, f"Highest Marks: {highest_marks}")
pdf.drawString(60, y_position - 90, f"Lowest Marks: {lowest_marks}")

# Footer
pdf.setFont("Helvetica-Oblique", 10)
pdf.drawString(50, 40, "CODTECH Internship | Task 2 – Automated Report Generation")

pdf.save()

print("PDF Report Generated Successfully!")
