def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/height ** 2
    print("BMI = " + str(bmi))

    if bmi < 18.5:
        weight = "Under Weight"
    elif 18.5 <= bmi <= 25.0:
        weight = "Normal Weight"
    else:
        weight = "Over Weight"
    print("Weight Classification = " + str(weight))

calculate_bmi(weight=57, height=1.73)

