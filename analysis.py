import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("students.csv")

# Calculate average marks
data['Average'] = data[['Maths', 'Science', 'English']].mean(axis=1)

# Display data
print("Student Data:\n", data)

# Top performer
top_student = data.loc[data['Average'].idxmax()]
print("\nTop Performer:\n", top_student)

# Plot graph
data.plot(x='Name', y=['Maths', 'Science', 'English'], kind='bar')
plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()