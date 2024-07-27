age=input("Enter your age: ")
if int(age)>=18:
    print("you are an adult")
elif int(age)>3 and int(age)<18:
    print("you are in school")
else:
    print("you are a kid")