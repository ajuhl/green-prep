def macros(weight, weightType, heightType, heightTens, heightUnits, age, sex, job, goal):
    carbs = 0
    protein = 0
    fats = 0
    calories = 0
    if (heightType == "feet"):
        height = (heightTens * 30.48) + (heightUnits * 2.54)
    elif(heightType == "meter"):
        height = heightTens * 100 + heightUnits
    if (weightType == "pounds"):
        weight *= 0.453592
    if (sex == "M"):
        calories = (weight * 10) + (height * 6.25) - (age * 5) + 5
    else:
        calories = (weight * 10) + (height * 6.25) - (age * 5) - 161

    if (job == "L"):
        calories = round(calories * 1.1)
    elif (job == "M"):
        calories = round(calories * 1.3)
    elif (job == "V"):
        calories = round(calories *1.5)
    elif (job == "E"):
        calories = round(calories * 1.7)

    if(goal == "fat-loss"):
        if (calories <= 2000): calories = round(0.9 * calories);
        if (calories > 2000): calories = round(0.8 * calories);
        carbs = round(0.40 * calories / 4);
        protein = round(0.40 * calories / 4);
        fats = round(0.20 * calories / 9);
    elif(goal == "maintain"):
        carbs = round(0.45 * calories / 4);
        protein = round(0.30 * calories / 4);
        fats = round(0.25 * calories / 9);
    elif(goal == "gain"):
        calories += 500;
        carbs = round(0.45 * calories / 4);
        protein = round(0.30 * calories / 4);
        fats = round(0.25 * calories / 9);
    return calories, carbs, protein, fats

##print the ouput to test the function against online claculator
print(macros(150, "pounds", "feet", 5, 6, 25, "F", "M", "maintain"))
