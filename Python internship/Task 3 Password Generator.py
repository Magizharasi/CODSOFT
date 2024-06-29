import random
import string
print("Password Generator")
def generate():
    n = int(input("Enter the required length of your password:"))
    print("Choose the complexity of the password:\n1.Easy\n2.Medium\n3.Strong\n")
    compl = int(input("Enter the number:"))
    password = ""
    if compl==1:
        for i in range (0,n):
            j = random.choice(string.ascii_letters)
            password+=j
    elif compl==2:
        for i in range (0,n):
            j = string.ascii_letters+string.digits
            password+=random.choice(j)
    elif compl==3:
        for i in range(0,n):
            j = string.ascii_letters+string.digits+string.punctuation
            password+=random.choice(j)
    print("The generated password:",password)
try:
    generate()
except ValueError:
    print("Error: Please enter integer value!")
