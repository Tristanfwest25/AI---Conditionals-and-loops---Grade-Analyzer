scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]
# uses a dictionary to count grades
grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

for score in scores:
    if score >= 90:
        grade = 'A'
        grade_counts['A'] += 1
    elif score >= 80:
        grade = 'B'
        grade_counts['B'] += 1
    elif score >= 70:
        grade = 'C'
        grade_counts['C'] += 1
    elif score >= 60:
        grade = 'D'
        grade_counts['D'] += 1
    else:
        grade = 'F'
        grade_counts['F'] += 1


print("=" * 3 + " Grade Analyzer " + "=" * 3)

total_scores = len(scores)
print(f"Total Scores: {total_scores}")
average_score = sum(scores) / total_scores
print(f"Average Score: {average_score:.1f}")
highest_score = max(scores)
lowest_score = min(scores)
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
passing_count = grade_counts['A'] + grade_counts['B'] + grade_counts['C'] + grade_counts['D']
# show total passing grades with percentage of total passing grades using len(scores)
print(f"Total Passing Grades: {passing_count} ({passing_count / len(scores) * 100:.1f}%)")
failing_count = grade_counts['F']
print(f"Total Failing Grades: {failing_count} ({failing_count / len(scores) * 100:.1f}%)")

print(f"\nGrade Distribution:")
print(f"Total A's: {grade_counts['A']}")
print(f"Total B's: {grade_counts['B']}")
print(f"Total C's: {grade_counts['C']}")
print(f"Total D's: {grade_counts['D']}")
print(f"Total F's: {grade_counts['F']}")


print("\n" + "-" * 3 + " Add More Scores " + "-" * 3)
# Uses a while loop to let the user enter additional scores. After each entry, display the updated average. Stop when the user types "done".
while True:
    user_input = input("Enter a score (or 'done' to finish): ")
    if user_input.lower() == "done":
        break
    try:
        new_score = int(user_input)
        scores.append(new_score)
        if new_score >= 90:
            grade_counts['A'] += 1
        elif new_score >= 80:
            grade_counts['B'] += 1
        elif new_score >= 70:
            grade_counts['C'] += 1
        elif new_score >= 60:
            grade_counts['D'] += 1
        else:
            grade_counts['F'] += 1
        total_scores = len(scores)
        average_score = sum(scores) / total_scores
        print(f"Updated Average Score: {average_score:.1f}")
    except ValueError:
        print("Invalid input. Please enter a valid score or 'done'.")
print("\nFinal Average:")

print(f"Average Score: {sum(scores) / len(scores):.1f}")

    