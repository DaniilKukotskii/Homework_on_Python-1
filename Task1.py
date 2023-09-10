usernum = input("Enter your number: ")

def sum_of_nums(usernum):
    result = 0
    for i in usernum:

        result += int(i)
    return result

print(f"Result: {sum_of_nums(usernum)}")
