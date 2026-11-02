
def calculate_energy_charge(units):
    if units <= 100:
        energy_charge = units * 3
    elif units <= 200:
        energy_charge = (100 * 3) + ((units - 100) * 5)
    else:
        energy_charge = (100 * 3) + (100 * 5) + ((units - 200) * 8)

    return energy_charge


def generate_bill(consumer_name, units):
    if units < 0:
        print("Invalid units. Enter a non-negative number.")
        return

    fixed_charge = 50
    energy_charge = calculate_energy_charge(units)
    tax = 0.05 * (energy_charge + fixed_charge)
    total_bill = energy_charge + fixed_charge + tax

    print("\n========== ELECTRICITY BILL ==========")
    print("Consumer Name :", consumer_name)
    print("Units Consumed:", units)
    print(f"Energy Charge : Rs. {energy_charge:.2f}")
    print(f"Fixed Charge  : Rs. {fixed_charge:.2f}")
    print(f"Tax (5%)      : Rs. {tax:.2f}")
    print("--------------------------------------")
    print(f"Total Bill    : Rs. {total_bill:.2f}")
    print("======================================")


# Main Program
try:
    consumer_name = input("Enter consumer name: ")
    units = float(input("Enter units consumed: "))

    if units < 0:
        print("Invalid units. Enter a non-negative number.")
    else:
        generate_bill(consumer_name, units)

except ValueError:
    print("Invalid input. Please enter a valid number.")