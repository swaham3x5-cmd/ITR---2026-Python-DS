# Add input for score and handle invalid values.

score = input("Enter your score: ")

score = float(score)

if score >= 0 and score <= 100:
    if score >= 90:
        print(f"Grade: A, Score: {score}")
    elif score >= 80:
        print(f"Grade: B, Score: {score}")
    else:
        print(f"Grade: C, Score: {score}")
else:
    print("Invalid score. Please enter a value between 0 and 100.")    