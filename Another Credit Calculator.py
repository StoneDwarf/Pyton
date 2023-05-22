import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str, help='indicates the type of payment: annuity or differentiated')
parser.add_argument('--payment', type=int, help='indicates the sum of monthly payment')
parser.add_argument('--principal', type=int, help='indicates the sum of loan principal')
parser.add_argument('--periods', type=int, help='indicates the amount of months to pay')
parser.add_argument('--interest', type=float, help='indicates the interest %')
args = parser.parse_args()


def month_number():
    log_inside = annuity_payment / (annuity_payment - (interest * loan_principal))
    log_base = 1 + interest
    period_nbr = math.ceil(math.log(log_inside, log_base))
    paysum = (annuity_payment * period_nbr)
    if period_nbr // 12 - period_nbr / 12 == 0:
        print(f'It will take {int(period_nbr / 12)} years to repay this loan!')
    elif math.ceil(period_nbr / 12) - math.floor(period_nbr / 12) > 0:
        print(f'It will take {int(period_nbr // 12)} years and {int(period_nbr % 12)} months to repay this loan!')
    else:
        print(f'It will take {int(period_nbr % 12)} months to repay this loan!')
    print(f'Overpayment = {paysum - loan_principal}')
    return ()


def calc_annuity_payment():
    upper = interest * pow(1 + interest, period_nbr)
    lower = pow(1 + interest, period_nbr) - 1
    annuity_payment = math.ceil(loan_principal * (upper / lower))
    paysum = (annuity_payment * period_nbr)
    print(f'Your monthly payment = {annuity_payment}!')
    print(f'Overpayment = {paysum - loan_principal}')
    return ()


def calc_loan_principal():
    principal = round(
        annuity_payment / ((interest * pow(1 + interest, period_nbr)) / (pow(1 + interest, period_nbr) - 1)))
    print(f'Your loan principal = {principal} !')
    return ()


def differentiated():
    paysum = 0
    for i in range(1, period_nbr + 1):
        current_period = i
        payment = math.ceil((loan_principal / period_nbr) + interest * (
                    loan_principal - ((loan_principal * (current_period - 1)) / period_nbr)))
        print(f'Month {i}: payment is {payment}')
        i += 1
        paysum += payment
    print()
    print(f'Overpayment = {paysum - loan_principal}')
    return ()


def inside_calculations():
    if operation_type != "annuity" and operation_type != "diff":
        print('Incorrect parameters')
    elif operation_type == "diff":
        if annuity_payment:
            print('Incorrect parameters')
        else:
            differentiated()
    else:
        if annuity_payment:
            if period_nbr:
                calc_loan_principal()
            elif loan_principal:
                month_number()
            else:
                print('Incorrect parameters')
        elif loan_principal:
            if period_nbr:
                calc_annuity_payment()
            else:
                print('Incorrect parameters')
        else:
            print('Incorrect parameters')
    return ()

try:
    operation_type = args.type
    loan_principal = args.principal
    annuity_payment = args.payment
    period_nbr = args.periods
    interest = float(args.interest / 1200)
    inside_calculations()
except TypeError:
    print('Incorrect parameters')
