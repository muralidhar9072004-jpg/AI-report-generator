# Raw notes from daily operations
notes = [
    "Checked battery station performance",
    "2 stations reported low SOC",
    "1 station under maintenance review",
    "Overall weekly operations stable"
]

# Convert notes into report
report = f"""
WEEKLY OPERATIONS REPORT

Summary:
- {notes[0]}
- {notes[1]}
- {notes[2]}
- {notes[3]}

Conclusion:
System performance remained stable with minor issues requiring follow-up.
"""

print(report)

# Save report
with open("weekly_report.txt", "w") as file:
    file.write(report)

print("Report saved as weekly_report.txt")
