import random


def main():
    n = input("Enter the number of friends joining (including you):")
    try:
        n = int(n)
        if n <= 0:
            raise Exception
        friends(n)
    except (ValueError, Exception):
        print("No one is joining for the party")


def friends(n):
    friend_lst = []
    for _ in range(n):
        friend_lst.append(input())
    total_bill = float(input("Enter the total bill value:\n"))
    lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if lucky == "Yes":
        lucky_friend(friend_lst, total_bill)
    else:
        no_lucky_friend(friend_lst, total_bill)


def lucky_friend(friends_lst, bill):
    lucky_one = random.choice(friends_lst)
    print(f"{lucky_one} is the lucky one!")


def no_lucky_friend(friends_lst, bill):
    print("No one is going to be lucky")


main()



