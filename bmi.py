name1 = 'A'
height_m1 = 1.7526
weight_kg1 = 76

name2 = "A's sister"
height_m2 = 1.8
weight_kg2 = 70

name3 = "A's brother"
height_m3 = 2.5
weight_kg3 = 160

def bmi_calc(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print('bmi: ')
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"
      
result1 = bmi_calc(name1, height_m1, weight_kg1)
result2 = bmi_calc(name2, height_m2, weight_kg2)
result3 = bmi_calc(name3, height_m3, weight_kg3)

print(result1)
print(result2)
print(result3)
