scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]
count_A = 0
count_B = 0
count_C = 0
count_D = 0
count_F = 0
for score in scores:
    if score >= 90:
        grade = 'A'
        count_A += 1
    elif score >= 80:
        grade = 'B'
        count_B += 1
    elif score >= 70:
        grade = 'C'
        count_C += 1
    elif score >= 60:
        grade = 'D'
        count_D += 1
    else:
        grade = 'F'
        count_F += 1


print("=" * 3 + " Grade Analyzer " + "=" * 3)

total_scores = len(scores)
print(f"Total Scores: {total_scores}")
average_score = sum(scores) / total_scores
print(f"Average Score: {average_score:.1f}")
highest_score = max(scores)
lowest_score = min(scores)
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
passing_count = count_A + count_B + count_C + count_D
print(f"Total Passing Grades: {passing_count}")
failing_count = count_F
print(f"Total Failing Grades: {failing_count}")

print(f"\nGrade Distribution:")
print(f"Total A's: {count_A}")
print(f"Total B's: {count_B}")
print(f"Total C's: {count_C}")
print(f"Total D's: {count_D}")
print(f"Total F's: {count_F}")


print("\n" + "-" * 3 + " Add More Scores " + "-" * 3)
# Uses a while loop to let the user enter additional scores. After each entry, display the updated average. Stop when the user types "done".
while True:
    user_input = input("Enter a score (or 'done' to finish): ")
    if user_input.lower() == "done":
        break
    try:
        new_score = int(user_input)
        scores.append(new_score)
        total_scores = len(scores)
        average_score = sum(scores) / total_scores
        print(f"Updated Average Score: {average_score:.1f}")
    except ValueError:
        print("Invalid input. Please enter a valid score or 'done'.")
print("\nFinal Average:")

print(f"Average Score: {sum(scores) / len(scores):.1f}")

    