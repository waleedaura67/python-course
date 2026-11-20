temparature = int(input("Enter todays temparature in Celsius: "))
if temparature < 20:
    outfit = "jacket"
    print("It is a cold day today.")
    print("wear a",outfit)
else:
    outfit = "t-shirt"
    print("It is warm today.")
    print("wear a",outfit)
is_raining = input("is it raining today (yes/no): ")
if is_raining == "yes":
    print("bring an umbrella!")
#wind_speed = int(input("Enter the wind in km/h: "))
print("Weather check complete!")
print("Temparature:", temparature)
print("outfit chosen:", outfit)
print("raining:", is_raining)