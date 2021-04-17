def pluralize(word): # 1. word is passed as input PARAMETER into the function...
    return word + "s" # 2. ...word is RETURNED in place at the function call with processed data.

userword = input("Word please: ")
print(pluralize(userword)) # 3. userword is a variable that's passed as an ARGUMENT to the function call.
