class CoffeeMachine:
    def __init__(self):
        self.coffee_bank = {'water': 400, 'milk': 540, 'coffee_beans': 120, 'cups': 9, 'money': 550}


    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        receipt_list = [{'water': 250, 'milk': 0, 'coffee_beans': 16, 'price': 4},
        {'water': 350, 'milk': 75, 'coffee_beans': 20, 'price': 7},
        {'water': 200, 'milk': 100, 'coffee_beans': 12, 'price': 6}]
        choice = input()
        if choice == 'back':
            return
        else:  
            rec_choise = int(choice) - 1
            receipt = receipt_list[rec_choise]
            self.resource_check(receipt)


    def resource_check(self, receipt):
        check_sum = 0
        if self.coffee_bank['water'] >= receipt['water']:
            check_sum += 1    
        if self.coffee_bank['milk'] >= receipt['milk']:
            check_sum += 1 
        if self.coffee_bank['coffee_beans'] >= receipt['coffee_beans']:
            check_sum += 1 
        if self.coffee_bank['cups'] >= 1:   
            check_sum += 1 
        if check_sum == 4:
            self.bank_update(receipt)
        else:
            print('Sorry, not enough resources')        


    def bank_update(self, receipt):    
        self.coffee_bank['water'] -= receipt['water']
        self.coffee_bank['milk'] -= receipt['milk']
        self.coffee_bank['coffee_beans'] -= receipt['coffee_beans']
        self.coffee_bank['cups'] -= 1
        self.coffee_bank['money'] += receipt['price']
        print('I have enough resources, making you a coffee!')    


    def fill(self):
        fill = ["Write how many ml of water you want to add:", 
                "Write how many ml of milk you want to add:", 
                "Write how many grams of coffee beans you want to add:", 
                "Write how many disposable cups you want to add:"]
        print(fill[0])
        self.coffee_bank['water'] += int(input())
        print(fill[1])
        self.coffee_bank['milk'] += int(input())
        print(fill[2])
        self.coffee_bank['coffee_beans'] += int(input())
        print(fill[3])
        self.coffee_bank['cups'] += int(input())


    def status(self):
        print(f"""
The coffee machine has:
{self.coffee_bank['water']} ml of water
{self.coffee_bank['milk']} ml of milk
{self.coffee_bank['coffee_beans']} g of coffee beans
{self.coffee_bank['cups']} disposable cups
${self.coffee_bank['money']} of money""")


    def start(self):
        while True:
            print('\nWrite action (buy, fill, take, remaining, exit):')
            action = input()
            if action == 'exit':
                break
            if action == 'fill':
                self.fill()
            elif action == 'take':
                print(f"I gave you ${self.coffee_bank['money']}")
                self.coffee_bank['money'] = 0
            elif action == 'buy':
                self.buy()
            elif action == 'remaining':
                self.status()


coffee_machine = CoffeeMachine()
coffee_machine.start()
