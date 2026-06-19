def generate_match_vector(student_skills, job_thresholds):

    vector = []

    for skill, threshold in job_thresholds.items():

        score = student_skills.get(skill, 0)

        if score >= threshold:
            vector.append(1)
        else:
            vector.append(0)

    return vector


def validate_thresholds(student_skills, job_thresholds):

    results = {}

    for skill, threshold in job_thresholds.items():

        score = student_skills.get(skill, 0)

        results[skill] = score >= threshold

    return results


def competency_level(score):

    if score <= 40:
        return "Beginner"

    elif score <= 70:
        return "Intermediate"

    else:
        return "Advanced"


def calculate_match_score(match_vector):

    total = len(match_vector)

    matched = sum(match_vector)

    return round((matched / total) * 100, 2)


def explain_match(student_skills, job_thresholds):

    reasons = []

    for skill, threshold in job_thresholds.items():

        score = student_skills.get(skill, 0)

        if score >= threshold:
            reasons.append(
                f"{skill}: {score} exceeds threshold {threshold}"
            )
        else:
            reasons.append(
                f"{skill}: {score} below threshold {threshold}"
            )

    return reasons