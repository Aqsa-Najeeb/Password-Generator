import secrets
import string


print("+========================================================+")
print("|           P A S S W O R D  G E N E R A T O R           |")
print("+========================================================+\n")

while True:
    passwordLength = int(input("\n>  What should the Password Length:  "))

    if passwordLength > 7:
        break

    print("Password lenght should be of 8 or above letters")

while True:
    includeNum = input("\n>  Should the Password include a Numeric Character (y/n):  ")

    if includeNum =='y' or includeNum == 'n':
        break

    print("Enter 'y' or 'n' ")

while True:
    includeChar = input("\n>  Should the Password include a Special Character (y/n):  ")

    if includeChar == 'y' or includeChar == 'n':
        break

Selection = ""   # including all the characters the password will be formed from

if includeNum == "y":
    Selection = Selection + string.digits

if includeChar == "y":
    Selection = Selection + string.punctuation

Selection = Selection + string.ascii_letters

Password = ''.join(secrets.choice(Selection) for _ in range(passwordLength))

print("\n")
print("----------------------------------------------------------")
print(f"            P A S S W O R D  :         {Password}      ")
print("----------------------------------------------------------")
