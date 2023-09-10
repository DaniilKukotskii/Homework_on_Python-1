ticket = input("Enter your number of ticket: ")

def lucky_ticket(ticket):
    first_3num = 0
    second_3num = 0
    for i in ticket:
        num = int(i)
        first_3num += num if num < 3 else 0
        second_3num += num if num >= 3 else 0
    return True if first_3num == second_3num else False

print(f"Lucky ticket(false or true): {lucky_ticket(ticket)}")