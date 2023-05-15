import random
print('Enter the number of friends joining (including you):')
guest_number = int(input())
if guest_number <= 0:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line:')
    guest_list = []
    lucky_guest = {}
    while len(guest_list) < guest_number:
        guest = str(input())
        guest_list.append(guest)
    print('Enter the total bill value:')
    bill = int(input())
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    choice = input()
    if choice == 'Yes':
        select_guest = random.choice(guest_list)
        pay_round = round(bill / (guest_number - 1), 2)
        for guest in guest_list:
            if guest != select_guest:
                    lucky_guest.update({guest: pay_round})
            else:
                lucky_guest.update({guest: 0})
        print(select_guest, ' is the lucky one!')
        print(lucky_guest)
    else:
        pay_round = round(bill / guest_number, 2)
        for guest in guest_list:
            lucky_guest.update({guest: pay_round})
        print('No one is going to be lucky')
        print(lucky_guest)
      