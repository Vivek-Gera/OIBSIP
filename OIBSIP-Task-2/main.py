
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
if height <= 3 and weight < 150:
    bmi = round(weight / height ** 2)
    if bmi < 18.5:
        print(f"Your BMI is {bmi}, you are slightly underweight.")
    elif bmi < 25:
        print(f"Your BMI is {bmi}, you are normal.")
    elif bmi < 30:
        print(f"Your BMI is {bmi}, you are overweight.")
    elif bmi < 35:
        print(f"Your BMI is {bmi}, you are Obese.")
    else:
        print(f"Your BMI is {bmi}, you are clinically obese.")
else:
    print("Input reasonable range")