marks=(98,99,54,32,98,23)
#count operation
print(marks.count(98))
print("----------")
#index
print(marks.index(32))
print("----------")
#modification in value
#converting to tuple
marks1=list(marks)
#changing/modifying value
marks1.append(54)
marks1.insert(2,76)
#changing to tuple after modification
marks=tuple(marks1)
print(marks)