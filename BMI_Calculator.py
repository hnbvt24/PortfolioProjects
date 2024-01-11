# Here we're asking the user to enter in some information about themselves: Name, Weight, Height

name = input("Enter your name: ")

weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches: "))


# Next we calculate the inputs of weight and height to get the BMI calculation

BMI = round((weight * 703) / (height * height),1)


# Then we print their respective result with a statement of wheree their BMI lies within the range of weight categories.

print("Your BMI is", BMI)
print()

if BMI > 0:
    if (BMI < 18.5):
        print(name + ', your weight is in the Underweight category for adults of your height. You may need to see your doctor to discuss your weight.')
    elif (BMI <= 24.9):
        print(name + ', your weight is in the Healthy Weight category for adults of your height. You are just right!')
    elif (BMI <= 29.9):
        print(name + ', your weight is in the Overweight category for adults of your height. Starting focusing more on your diet and becoming a little more active.')
    else:
        print(name + ', your weight is in the Above Obesity category for adults of your height. You need to exercise more and stop writing so many Python functions.')

print()
print("""
BMI is a screening measure and is not intended to diagnose disease or illness. For more information, visit About Adult BMI.(see link below)
Maintaining a weight in the healthy BMI range is one way to support overall health as you age. For more information about lifestyle approaches, visit Healthy Weight.(see link below)

About Adult BMI: https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html
Healthy Weight: https://www.cdc.gov/healthyweight/index.html
"""
     )
