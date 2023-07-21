class HonestCalk:
    def __init__(self):
        self.user_input = None
        self.msg_0 = "Enter an equation"
        self.msg_1 = "Do you even know what numbers are? Stay focused!"
        self.msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
        self.msg_3 = "Yeah... division by zero. Smart move..."
        self.msg_4 = "Do you want to store the result? (y / n):"
        self.msg_5 = "Do you want to continue calculations? (y / n):"
        self.msg_6 = " ... lazy"
        self.msg_7 = " ... very lazy"
        self.msg_8 = " ... very, very lazy"
        self.msg_9 = "You are"
        self.msg_10 = "Are you sure? It is only one digit! (y / n)"
        self.msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
        self.msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
        self.oper = ['+', '-', '*', '/']
        self.memory = 0.0
        self.result = None

    def check_number(self):
        if self.user_input[0] == 'M':
            self.user_input[0] = self.memory
        if self.user_input[2] == 'M':
            self.user_input[2] = self.memory
        try:
            v1 = float(self.user_input[0])
            v2 = float(self.user_input[2])
            v3 = self.user_input[1]
            msg = ''
            if (v1 % 1 == 0) and (v2 % 1 == 0):
                if (-10 < v1 < 10) and (-10 < v2 < 10):
                    msg += self.msg_6
            if (v1 == 1.0 or v2 == 1.0) and v3 == '*':
                msg += self.msg_7
            if (v1 == 0.0 or v2 == 0.0) and v3 in ['*', '+', '-']:
                msg += self.msg_8
            if msg != '':
                msg = self.msg_9 + msg
                print(msg)
        except ValueError:
            print(self.msg_1)
        else:
            return 'OK'

    def check_oper(self):
        if self.user_input[1] not in self.oper:
            print(self.msg_2)
        elif self.user_input[1] == '/' and float(self.user_input[2]) == 0.0:
            print(self.msg_3)
        else:
            return 'OK'

    def calculations(self):
        if self.user_input[1] == '/':
            self.result = float(self.user_input[0]) / float(self.user_input[2])
        elif self.user_input[1] == '*':
            self.result = float(self.user_input[0]) * float(self.user_input[2])
        elif self.user_input[1] == '-':
            self.result = float(self.user_input[0]) - float(self.user_input[2])
        elif self.user_input[1] == '+':
            self.result = float(self.user_input[0]) + float(self.user_input[2])
        print(self.result)
        self.choices()

    def choices(self):
        print(self.msg_4)
        choice_msg_4 = input()
        if choice_msg_4 == 'y':
            if (self.result % 1 == 0) and (-10 < self.result < 10):
                self.annoying_text()
            else:
                self.memory = self.result
        print(self.msg_5)
        choice_msg_5 = input()
        if choice_msg_5 == 'y':
            self.user_input = None
            self.start()


    def annoying_text(self):
        print(self.msg_10)
        answer1 = input()
        if answer1 == 'y':
            print(self.msg_11)
            answer2 = input()
            if answer2 == 'y':
                print(self.msg_12)
                answer3 = input()
                if answer3 == 'y':
                   self.memory = self.result


    def start(self):
        while True:
            print(self.msg_0)
            self.user_input = input().split()
            if self.check_number() == 'OK' and self.check_oper() == 'OK':
                self.calculations()
                break


calculator = HonestCalk()
calculator.start()
