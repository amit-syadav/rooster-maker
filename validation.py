def validation(forced_inclusions, forced_exclusions, employees, days, duty):
    invalid_day = []
    invalid_name = []
    invalid_duty = []



    for day in forced_inclusions.keys():
        if day not in days:
            invalid_day.append(day)
        else:
            for emp_duty_dict in forced_inclusions[day]:
                emp = list(emp_duty_dict.keys())[0]
                duty_inner = emp_duty_dict[emp]
                if emp not in employees:
                    invalid_name.append(emp)
                    print(emp,employees)
                if duty_inner not in duty:
                    invalid_duty.append(duty_inner)

    for emp in forced_exclusions.keys():
        if emp not in employees:
                invalid_name.append(emp)
                print(emp,employees)
        else:
            for day in forced_exclusions[emp]:
                if day not in days:
                    invalid_day.append(day)

    return tuple([invalid_day,
                 invalid_name,
                 invalid_duty])
