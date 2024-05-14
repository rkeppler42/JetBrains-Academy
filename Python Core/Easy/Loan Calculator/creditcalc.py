import argparse
import math


def main():
    none_counter = 0

    parser = argparse.ArgumentParser()

    parser.add_argument("--payment", type=non_negative)
    parser.add_argument("--principal", type=non_negative)
    parser.add_argument("--periods", type=non_negative)
    parser.add_argument("--interest", type=non_negative)
    parser.add_argument("--type")

    args = parser.parse_args()

    arguments = [args.payment, args.principal, args.periods, args.interest, args.type]

    for argument in arguments:
        if argument is None:
            none_counter += 1

    if args.interest is None:
        print_error()
    elif none_counter != 1:
        print_error()
    elif args.type != "diff" and args.type != "annuity":
        print_error()
    else:
        i = float(arguments[3]) * 0.01 / 12
        if args.type == "annuity":
            if arguments[0] is None:
                p = float(arguments[1])
                n = int(arguments[2])
                calc_payment(p, n, i)
            elif arguments[1] is None:
                a = float(arguments[0])
                n = float(arguments[2])
                calc_principal(a, n, i)
            elif arguments[2] is None:
                a = float(arguments[0])
                p = float(arguments[1])
                calc_periods(a, p, i)
        else:
            p = float(arguments[1])
            n = int(arguments[2])
            diff(p, n, i)


def calc_payment(p, n, i):
    payment = math.ceil(p * ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
    print(f"Your monthly payment =  {payment}!")
    overpayment(payment, n, p)


def calc_principal(a, n, i):
    principal = math.floor(a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
    print(f"Your loan principal = {principal}!")
    overpayment(a, n, principal)


def calc_periods(a, p, i):
    periods = math.ceil(math.log((a / (a - i * p)), 1 + i))
    years = periods // 12
    months = periods % 12
    if years == 0:
        years_and_months = f"{months} months"
    elif months == 0:
        years_and_months = f"{years} years"
    else:
        years_and_months = f"{years} years and {months} months"
    print("It will take", years_and_months, "to repay this loan!")
    overpayment(a, periods, p)


def print_error():
    print("Incorrect parameters")


def non_negative(x):
    i = float(x)
    if i >= 0:
        return i


def overpayment(a, n, p):
    print(f"Overpayment = {round(n * a - p)}")


def diff(p, n, i):
    total_a = 0
    for m in range(1, n + 1):
        dm = math.ceil(p / n + i * (p - (p * (m - 1) / n)))
        total_a += dm
        print(f"Month {m}: payment is {dm}")
    print(f"Overpayment = {round(total_a - p)}")


main()
