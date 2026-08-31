# Exercise 1: Student Quiz Score Tracker

## Problem Statement
You are tracking quiz scores for students in a Python cohort. Each student has taken 3 quizzes, and your goal is to calculate individual averages, classify students based on their performance, identify the class topper, and compute the overall class average.

### Input Data
students = {
    "Aarav":   [85, 90, 78],
    "Priya":   [72, 68, 75],
    "Rohan":   [45, 52, 48],
    "Sneha":   [95, 92, 98],
    "Manish":  [60, 65, 70],
}

### Classification Rules
- Average >= 80: "Topper"
- Average 60 to 79: "Pass"
- Average < 60: "Needs improvement"

### Expected Output
=== Student Averages ===
Aarav: 84.33 - Topper
Priya: 71.67 - Pass
Rohan: 48.33 - Needs improvement
Sneha: 95.00 - Topper
Manish: 65.00 - Pass

=== Class Topper ===
Sneha with average 95.00

=== Class Average ===
72.87
