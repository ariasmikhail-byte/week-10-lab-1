def get_number_of_employees():
    while True:
        number_of_employees = int(input("Enter the number of employees: "))

        if number_of_employees >= 1:
            return number_of_employees
        else:
            print("The number of employees must be at least 1.")


def get_total_days_absent(number_of_employees):
    total_days_absent = 0

    for employee in range(1, number_of_employees + 1):
        while True:
            days_absent = int(
                input(f"Enter the days absent for Employee {employee}: ")
            )

            if days_absent >= 0:
                total_days_absent += days_absent
                break
            else:
                print("Days absent cannot be negative.")

    return total_days_absent


def calculate_average_days_absent(number_of_employees, total_days_absent):
    average_days_absent = total_days_absent / number_of_employees
    return average_days_absent


def main():
    print("EMPLOYEE ABSENCE TRACKER")

    number_of_employees = get_number_of_employees()
    total_days_absent = get_total_days_absent(number_of_employees)
    average_days_absent = calculate_average_days_absent(
        number_of_employees, total_days_absent
    )

    print("\nEMPLOYEE ABSENCE SUMMARY")
    print("Number of employees:", number_of_employees)
    print("Total days absent:", total_days_absent)
    print(f"Average days per employee: {average_days_absent:.2f}")


main()