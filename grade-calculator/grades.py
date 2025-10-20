def calculate_final(current: float, desired: float, share: float) -> float:
    share_fraction = share / 100
    needed = (desired - current * (1 - share_fraction)) / share_fraction
    return needed

def write_message(final_needed: float) -> str:
    if final_needed > 100:
        return "That's over 100%. Extra credit?"
    elif final_needed >= 90:
        return "That's an A."
    elif final_needed >= 80:
        return "That's a B."
    elif final_needed >= 70:
        return "That's a C."
    elif final_needed >= 60:
        return "That's a D."
    else:
        return "That's an F."

if __name__ == "__main__":
    grades_needed = {}

    while True:
        course_name = input("What is the course name? ")
        current_grade = input("What is your current grade? ")
        current_grade = float(current_grade)
        desired_grade = input("What grade do you want? ")
        desired_grade = float(desired_grade)
        final_share = input("What percent of your grade is your final? ")
        final_share = float(final_share)

        final_needed = calculate_final(current_grade, desired_grade, final_share)
        print("You need a " + str(final_needed) + ".")

        message = write_message(final_needed)
        print(message)

        grades_needed[course_name] = final_needed

        again = input("Calculate another score? y/n ")
        if again == "n":
            break

    replayed_final = input("Which final do you want to see again? ")
    print(grades_needed[replayed_final])

    print("To recap, you need:")
    for course, grade in grades_needed.items():
        print(str(grade) + " in " + course + ". ", end=" ")
        message = write_message(grade)
        print(message)

__all__ = ["calculate_final", "write_message"]