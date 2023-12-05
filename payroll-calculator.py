import csv
import constant
from collections import defaultdict

infile = open('bookings-corrected.csv', mode='r')
reader = csv.reader(infile)

bookings_dict = {header: [] for header in constant.DESIRED_HEADERS}

for idx_row, row in enumerate(reader):
    if idx_row == 0:
        headers = row
    else:
        for idx, value in enumerate(row):
            if headers[idx] in constant.DESIRED_HEADERS:
                bookings_dict[headers[idx]].append(value)

infile.close()


def calculate_salary_based_on_appointment_type(appointment_name):
    total_value = 0.0
    for key, value in constant.TIER_ONE_SALARY.items():
        if key in appointment_name:
            total_value = float(duration) / 30 * float(value)
            break
    return total_value


new_dict = defaultdict(float)  # Use float as the default type for total values

for team_member, duration, appointment_name in zip(
    bookings_dict["Team Member Name"],
    bookings_dict["Duration"],
    bookings_dict["Appointment Name"]
):
    total_value = calculate_salary_based_on_appointment_type(appointment_name)
    new_dict[team_member] += total_value

# If you want to convert the defaultdict to a regular dictionary
summed_dict = dict(new_dict)

print(summed_dict)
