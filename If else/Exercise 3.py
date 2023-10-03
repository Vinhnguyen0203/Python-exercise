gender = input("Are you male or female? ")
hmgValue = float(input("Input your hemoglobin value (g/l): "))
if gender == "male":
    if hmgValue < 134:
        print("Your hemoglobin value is low")
    elif hmgValue > 167:
        print("Your hemoglobin value is high")
    else:
        print("Your hemoglobin value is normal")
else:
    if hmgValue < 117:
        print("Your hemoglobin value is low")
    elif hmgValue > 155:
        print("Your hemoglobin value is high")
    else:
        print("Your hemoglobin value is normal")
