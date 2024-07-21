#Write a python function which converts inches to cms

def inch_to_cm(inch):
    return (2.54*inch)

inch=float(input("Enter the measurement in inches : "))
cm=inch_to_cm(inch)
print(f"{inch} inches = {cm} cm")
    