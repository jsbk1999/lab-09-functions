userstring = input("Number please: ")
usernum = int(userstring)

def factorial(n):
    userinput = 1
    for i in range(1, usernum + 1):
            userinput *= i
    return userinput
print(factorial(usernum))
