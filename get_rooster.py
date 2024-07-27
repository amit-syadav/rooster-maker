import pandas as pd
from validation import validation
import json

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

employees = ['sp yadav', 'sp sharma', 'ashok meena', 'up tyagi', 'rajendra prasad', 'pramod kumar', 'amit kumar',
             'meghnath', 'dayanand', 'yogesh kulkarni', 'gm kulkarni', 'jagnandan', 'rs meena']

duty = ['day', 'inter', 'night']



def get_exclusions():
    data = { }
    with open('input.json', 'r') as json_file:
        data = json.load(json_file)

    # Access the variables
    forced_exclusions = data["forced_exclusions"]
    forced_inclusions = data["forced_inclusions"]
    return tuple([forced_exclusions,forced_inclusions])




def get_rooster():
    forced_exclusions,forced_inclusions = get_exclusions()
    invalid_day, invalid_name, invalid_duty = validation(forced_inclusions, forced_exclusions, employees, days, duty)

    if invalid_day or invalid_name or invalid_duty:
        print(invalid_day, invalid_name, invalid_duty)
        raise Exception(invalid_day, invalid_name, invalid_duty)


    # dataframe is of form day: employees,  we show its transformed form on ui
    data = [[""] * len(employees) for _ in range(len(days))]

    df = pd.DataFrame(data, index=days, columns=employees)

    duty_i = 0

    r = 0
    c = 0

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
            # print('exclusion found')
            pass

        elif duty[duty_i] in inclusion_duty:
            duty_i += 1

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
