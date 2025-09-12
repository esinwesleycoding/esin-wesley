def check_grade():
    try:
        score = float(input("Enter your exam score (0–100): "))

        if score < 0 or score > 100:
            print("Invalid score. Please enter a value between 0 and 100.")
        elif score >= 90:
            print("Grade: A — Excellent!")
        elif score >= 80:
            print("Grade: B — Very Good")
        elif score >= 70:
            print("Grade: C — Good")
        elif score >= 60:
            print("Grade: D — Fair")
        else:
            print("Grade: F — Needs Improvement")
    except ValueError:
        print("Please enter a numeric value.")

# Run the function
check_grade()
