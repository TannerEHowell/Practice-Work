####First Lab Assignment
##master_list = []
##
##for i in range(3):
##    person_info = []
##    
##    name = input("Enter name: ")
##    person_info.append(name)
##
##    age = input("Enter age: ")
##    person_info.append(age)
##
##    hmtwn = input("Enter your hometown: ")
##    person_info.append(hmtwn)
##
##    person_info.insert(0, person_info.pop(1))
##    master_list.append(person_info)
##
##
##master_list.sort()
##
##print(master_list)
##
##print("Name", "\tAge", "\tHometown")
##print("-" * 25)
##
##for lst in master_list:
##


##Second Assignment

num_lst = str(input("Please enter numbers divided by commas: "))
num_lst = num_lst.split(",")

print(num_lst)

for i in range(len(num_lst) - 1):
    if i > i+1:
        i = i+1

print(num_lst)
