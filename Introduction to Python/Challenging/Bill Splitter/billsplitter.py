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
    pay_by_friend = {}
    total_per_friend = round(bill / (len(friends_lst) - 1), 2)
    for friend in friends_lst:
        if friend != lucky_one:
            pay_by_friend[friend] = total_per_friend
        else:
            pay_by_friend[friend] = 0
    print(pay_by_friend)


def no_lucky_friend(friends_lst, bill):
    print("No one is going to be lucky")
    pay_by_friend = dict.fromkeys(friends_lst, round(bill / len(friends_lst), 2))
    print(pay_by_friend)


main()
