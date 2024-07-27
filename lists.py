marks=[23,"Rihan",45,55]
print(marks[1])
#range
print(marks[1:3])
#for loop in list
for i in marks:
    print(i)
print("----------------")
#operations in lists
#1st) append
marks.append(99)
print(marks)
print("-------------")
#2nd) insert
marks.insert(2,76)
print(marks)
print("-------------")
#3rd) in 
print(99 in marks)
#4th) len
print("-------------")
print(len(marks))
print("-------------")
#5) clear
marks.clear()
print(marks)