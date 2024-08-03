import pandas as pd
from viz.validation import validation
from  datetime import datetime




def get_rooster(app_variables):
    forced_exclusions = app_variables.get_forced_exclusions()
    forced_inclusions = app_variables.get_forced_inclusions()
    days = app_variables.get_days()
    employees = app_variables.get_employees()
    duty = app_variables.get_duty()


    if validation(app_variables) != "":
        raise ValueError(validation(app_variables))




    # dataframe is of form day: employees,  we show its transformed form on ui
    data = [[""] * len(employees) for _ in range(len(days))]

    df = pd.DataFrame(data, index=days, columns=employees)

    duty_i = 0

    r = 0
    c = datetime.now().second

    # iterate all days
    while r < df.shape[0]:

        # satisfy all forced inclusions for this day
        inclusion_emp = []
        inclusion_duty = []


        if df.index[r] in forced_inclusions:
            for duty_requested in forced_inclusions.get(df.index[r]):
                for emp in duty_requested:
                    df.at[df.index[r], emp] = duty_requested[emp]
                    inclusion_emp.append(emp)
                    inclusion_duty.append(duty_requested[emp])

        # print(df.columns[c % df.shape[1]], df.index[r])

        # check if exclusion exists for the emp
        if df.columns[c % df.shape[1]] in forced_exclusions and df.index[r] in forced_exclusions[
            df.columns[c % df.shape[1]]]:
            # print('Exclusion found!! Employee does not want duty on this day')
            pass

        elif duty[duty_i] in inclusion_duty:
            duty_i += 1
            c -= 1 #do not increment counter in this case

        elif df.columns[c % df.shape[1]] in inclusion_emp:
            pass

        else:  # already assigend as forced inclusion
            df.iloc[r, c % df.shape[1]] = duty[duty_i]
            duty_i += 1

        c += 1

        if duty_i == 3:  # all duties allocated for the given day
            duty_i = 0
            # print(df.iloc[r])
            r += 1

    # print(df.to_html())

    final_table = df.transpose().to_html(classes='text-center table table-striped table-bordered ')

    # print(df.transpose())
    return final_table
