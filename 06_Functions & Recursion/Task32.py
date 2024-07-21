#Write a python program using function to convert Celsius to Fahrenheit.


def Cel_to_Faren(C):
    return round((((9/5)*C)+32),2)

C=float(input("Enter the temperature in Celcius : "))
F=Cel_to_Faren(C)
print(f"{C} degree Celcius = {F} degree Farenheit")