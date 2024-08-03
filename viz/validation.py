def validation(app_variables):
    forced_exclusions = app_variables.get_forced_exclusions()
    forced_inclusions = app_variables.get_forced_inclusions()
    days = app_variables.get_days()
    employees = app_variables.get_employees()
    duty = app_variables.get_duty()

    invalid_day = []
    invalid_name = []
    invalid_duty = []
    error_str = ""



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

    if invalid_day:
        error_str += "Found invalid day {}".format(invalid_day)
    if invalid_name:
        error_str += "Found invalid name {}".format(invalid_name)
    if invalid_duty:
        error_str += "Found invalid duty {}".format(invalid_duty)
    return error_str
