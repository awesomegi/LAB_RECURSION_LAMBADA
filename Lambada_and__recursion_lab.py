

#Q1
def recursion_fun(vow_test):

    if vow_test == "":
        return 0

    char = vow_test[0].lower()
    
    if char in "aeiou":
        return 1 + recursion_fun(vow_test[1:])
    else:
        return recursion_fun(vow_test[1:])
    
print(recursion_fun("I LOvE PythoN"))
        








#Q2
numbers = [40, 35, 10, 15, 20]
list_multiplied = list(map(lambda num: num * 2,numbers))
print(list_multiplied)