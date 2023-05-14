def calc_average_temperature():
    temp1 = float(input("Enter the first temperature: "))
    temp2 = float(input("Enter the second temperature: "))
    temp3 = float(input("Enter the third temperature: "))

    print("The three temperatures are:", temp1, temp2, temp3)

    ave_temp = (temp1 + temp2 + temp3) / 3
    print("The average temperature of the three temperatures is:", ave_temp)

    if ave_temp < 37:
        ave_temp = "Normal"
    elif ave_temp > 39:
        ave_temp = "Fever"
    else:
        ave_temp = "Hot, going to fever"
    print("You are feeling", ave_temp, "today")

calc_average_temperature()

