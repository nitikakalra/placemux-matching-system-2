import json

from matching import (
    generate_match_vector,
    validate_thresholds,
    competency_level,
    calculate_match_score,
    explain_match
)

with open("data/students.json") as f:
    students = json.load(f)

with open("data/jobs.json") as f:
    jobs = json.load(f)

student = students[0]
job = jobs[0]

# Generate Match Vector
vector = generate_match_vector(
    student["skills"],
    job["thresholds"]
)

print("Match Vector:")
print(vector)

# Calculate Match Score
score = calculate_match_score(vector)

print("\nMatch Score:")
print(f"{score}%")

# Validate Thresholds
validation = validate_thresholds(
    student["skills"],
    job["thresholds"]
)

print("\nThreshold Validation:")
print(validation)

# Competency Mapping
print("\nCompetency Levels:")

for skill, score in student["skills"].items():
    print(f"{skill}: {competency_level(score)}")

# Explain Match
print("\nMatch Explanation:")

for reason in explain_match(
        student["skills"],
        job["thresholds"]):
    print("-", reason)