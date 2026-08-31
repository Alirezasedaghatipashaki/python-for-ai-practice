students = {
    "Aarav":   [85, 90, 78],
    "Priya":   [72, 68, 75],
    "Rohan":   [45, 52, 48],
    "Sneha":   [95, 92, 98],
    "Manish":  [60, 65, 70],
}

# Variables to track overall performance and topper
total_class_score = 0
total_quizzes_count = 0
topper_name = ""
highest_avg = 0.0

print("=== Student Averages ===")

# Process each student using a loop
for name, scores in students.items():
    avg = sum(scores) / len(scores)
    
    # Track totals for class average calculation
    total_class_score += sum(scores)
    total_quizzes_count += len(scores)
    
    # Classify student
    if avg >= 80:
        status = "Topper"
    elif avg >= 60:
        status = "Pass"
    else:
        status = "Needs improvement"
        
    print(f"{name}: {avg:.2f} - {status}")
    
    # Check for topper
    if avg > highest_avg:
        highest_avg = avg
        topper_name = name

# Calculate class average across all quiz scores
class_avg = total_class_score / total_quizzes_count

print("\n=== Class Topper ===")
print(f"{topper_name} with average {highest_avg:.2f}")

print("\n=== Class Average ===")
print(f"{class_avg:.2f}")
