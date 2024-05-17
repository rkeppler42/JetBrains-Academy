n = input("Enter the number of friends joining (including you):")
dict_of_friends = {}

try:
    n = int(n)
    if n <= 0:
        raise Exception

    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(n):
        dict_of_friends[input()] = 0
    total_bill = float(input("Enter the total bill value:"))
    for key in dict_of_friends:
        dict_of_friends[key] = round(total_bill / n, 2)

    print(dict_of_friends)

except (ValueError, Exception):
    print("No one is joining for the party")


