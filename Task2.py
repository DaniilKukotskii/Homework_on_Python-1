sum_of_elements = input("Enter sum of elements: ")

def result (sum_of_elements):
    petr = (int(sum_of_elements)/6).__round__()
    sergey = (int(sum_of_elements)/6).__round__()
    kate = (petr + sergey) * 2

    return petr, sergey, kate

print(f"Result:\nPeter: {result(sum_of_elements)[0]} \nSergey: {result(sum_of_elements)[1]}\n"
      f"Kate: {result(sum_of_elements)[2]}")
