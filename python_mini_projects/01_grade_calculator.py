# ============================================================
# MINI PROJECT 1 — Student Grade Calculator
# Uses: variables, lists, functions, loops, conditionals
# ============================================================

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def calculate_stats(scores):
    average = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)
    return round(average, 2), highest, lowest


def display_report(name, subjects, scores):
    print("=" * 40)
    print(f"  GRADE REPORT FOR: {name.upper()}")
    print("=" * 40)
    for subject, score in zip(subjects, scores):
        letter = get_letter_grade(score)
        print(f"  {subject:<20} {score:>3}  ({letter})")
    print("-" * 40)
    avg, high, low = calculate_stats(scores)
    print(f"  Average: {avg}")
    print(f"  Highest: {high}")
    print(f"  Lowest:  {low}")
    print(f"  Overall Grade: {get_letter_grade(avg)}")
    print("=" * 40)


# --- Sample data ---
student_name = "Abdullah"
subjects = ["Calculus", "Linear Algebra", "Physics", "Discrete Math", "Chinese"]
scores = [82, 76, 88, 71, 95]

display_report(student_name, subjects, scores)
