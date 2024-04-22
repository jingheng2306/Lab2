def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    
    bmi = weight / (height * height)
    
    print("BMI = " + str(bmi))

    if bmi < 18.5:
        print("BMI Range Classification: Under Weight")
    elif 18.5 <= bmi <= 25.0: 
        print("BMI Range Classification: Normal Weight")
    else:
        print("BMI Range Classification: Over Weight")

calculate_bmi(weight=57, height=1.73)
