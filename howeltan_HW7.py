##8.40
##I guess I didn't quite understand how to do just number 8.40 without doing number 8.20
##Since 8.40 is fixing issues in 8.20, so I went ahead and did
class BankAccount(object):
        def __init__(self, amount):
            try:
                self.acc_balance = amount
            
                if amount < 0:
                    raise ValueError

            except ValueError:
                print('Invalid Account Balance')
            
            

        def withdraw(self, amount):
            try:
                
                if amount < 0:
                    raise ValueError
                
                if amount > self.acc_balance:
                    raise ValueError

                self.acc_balance = self.acc_balance - amount
            
                print('You now have $', self.acc_balance, ' left in your account.\n')
                
            except ValueError:
                print('Invalid Withdrawal Amount')
            

        def deposit(self, amount):
            try:
                if amount < 0:
                    raise ValueError
                
                self.acc_balance = self.acc_balance + amount
                
                print('You now have $', self.acc_balance, ' left in your account.\n')

            except ValueError:
                print('Invalid Deposit Amount')

        def balance(self):
            
            return float(self.acc_balance)

    


##8.35

##class Stack(object):
##    def __init__(self):
##        self.seq = []
##
##    def isEmpty(self):
##        return self.length() == 0  
##
##    def push(self, item):
##        self.seq.append(item)
##        return(self.seq)
##        
##    def pop(self):
##        return self.seq.pop()  
##
##    def length(self):
##        return len(self.seq)  
##
####I don't really know what to do to just pritn the whole s sequence on its own, this is what I thought I had to do but it doesn't work
####I tried to just type s before but it wouldn't help either, feedback?
####    def s(self):
####        print(self.seq)  
##
##
####s = Stack()
####s.push('plate 1')
####s.push('plate 2')
####s.push('plate 3')








##8.40


