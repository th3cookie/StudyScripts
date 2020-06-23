#!/usr/bin/env python3.6

def gather_info():
   height = float(input("What is your height? (inches or meters) "))
   weight = float(input("What is your Weight? (pounds or kilograms) "))
   system = input("Are your measurements in metric or imperial units? ").lower().strip()
   return (height, weight, system)

def calculate_bmi(weight, height, system='metric'):
    """
    Return the BMI for the given info
    Note: we've set default system to metric so we don't need to pass metric
    when passing metric
    """
    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi

while True:
    height, weight, system = gather_info()
    if system.startswith('i'):
        bmi = calculate_bmi(weight, system=system, height=height)
        """
        If your arguments are not positional, you can specify 
        the variable name that will match the name being passed to the function
        """
        print(f"Your BMI is {bmi}")
        break
    elif system.startswith('m'):
        bmi = calculate_bmi(weight, height) 
        """
        Since the default is defined as metric in the function, 
        we don't need to pass it, it will know to use that
        """
        print(f"Your BMI is {bmi}")
        break
    else:
        print("Error: Unknown measurement system. Please use imperial or metric.")

