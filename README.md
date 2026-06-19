# PlaceMux Task 2 - Job Posting with Skill Thresholds

## Objective
Build the matching feature vectors from job skill thresholds.

## Features
- Match Vector Generation
- Threshold Validation
- Competency Mapping
- Match Score Calculation
- Explainable Matching

## Project Structure

project/
│
├── data/
│   ├── students.json
│   └── jobs.json
│
├── matching.py
└── main.py

## Sample Output

Match Vector:
[1, 0, 1]

Match Score:
66.67%

Threshold Validation:
{'Python': True, 'Java': False, 'SQL': True}

Competency Levels:
Python: Advanced
Java: Intermediate
SQL: Intermediate

Match Explanation:
- Python: 80 exceeds threshold 70
- Java: 50 below threshold 60
- SQL: 70 exceeds threshold 50