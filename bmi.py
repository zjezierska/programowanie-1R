masa = float(input("Podaj masę:"))
wzrost = float(input("Podaj wzrost:"))

bmi = masa / (wzrost ** 2)

print(f"BMI = {bmi}")

if bmi < 18.5:
    print("niedowaga")
elif 18.5 < bmi < 25:
    print("waga prawidłowa")
elif 25 < bmi < 30:
    print("nadwaga")
else:
    print("otyłość")
