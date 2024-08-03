
import json

class Variable:

    forced_exclusions = dict()
    forced_inclusions  = dict()
    days = []
    employees = []
    duty = []

    def __init__(self):
        # set variables from json
        with open('./input_data/input.json', 'r') as json_file:
            data = json.load(json_file)
        self.forced_exclusions = data["forced_exclusions"]
        self.forced_inclusions = data["forced_inclusions"]

        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.employees = ['sp yadav', 'sp sharma', 'ashok meena', 'up tyagi', 'rajendra prasad', 'pramod kumar', 'amit kumar',
                     'meghnath', 'dayanand', 'yogesh kulkarni', 'gm kulkarni', 'jagnandan', 'rs meena']
        self.duty = ['day', 'inter', 'night']

    def get_forced_exclusions(self):
        return self.forced_exclusions

    def get_forced_inclusions(self):
        return self.forced_inclusions

    def set_forced_exclusions(self,forced_exclusions):
        self.forced_exclusions = forced_exclusions


    def set_forced_inclusions(self,forced_inclusions):
        self.forced_inclusions = forced_inclusions

    def get_days(self):
        return self.days

    def set_days(self, new_days):
        self.days = new_days

    def get_employees(self):
        return self.employees

    def set_employees(self, new_employees):
        self.employees = new_employees

    def get_duty(self):
        return self.duty

    def set_duty(self, new_duty):
        self.duty = new_duty

