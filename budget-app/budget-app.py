class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        
    def get_name(self):
        ''' getter method for self.name '''
        return self.name
    
    def deposit(self, amount, description = ""):
        '''
        adds money to the balance
        input: amount: int
               description: str
        output: None
        '''
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
        
    def withdraw(self, amount, description = ""):
        '''
        subtracts money from the balance
        input: amount: int
               description: str
        output: True if the subtraction was possible
                False if the balance was lower that the subtracted amount
        '''
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": 0-amount, "description": description})
            self.balance -= amount
            return True
        else:
            return False
 
    def get_balance(self):
        ''' getter method for self.balance '''
        return self.balance
        
    def transfer(self, amount, target):
        '''
        transfers money from the current category to another
        input: amount: int
               target: different Category object
        output: True if the trnasfer was possible
                False if the balance was lower that the transferred amount
        '''
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": 0-amount, "description": "Transfer to "+str(target.get_name())})
            self.balance -= amount
            target.ledger.append({"amount": amount, "description": "Transfer from "+str(self.get_name())})
            target.balance += amount
            return True
        else:
            return False
        
    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True
    
    def __str__(self):
        ''' pretty print '''
        to_print = '{0:*^30}'.format(self.get_name())
        for i in range(len(self.ledger)):
            to_print += '\n{0:<23}{1:>7.2f}'.format(self.ledger[i]["description"][0:23], self.ledger[i]["amount"])
        to_print += '\nTotal: {0}'.format(self.get_balance())
        return to_print
    
    def __repr__(self):
        return str(self.get_name())


def create_spend_chart(categories):
    '''
    Creates an easy-to-read spend chart.
    input: list of 'Category' objects
    output: chart as a string
    '''
     # calculates how much was spent in which category
    totals = []
    total = 0
    for c in range(len(categories)):
        cat_spent = 0
        for item in categories[c].ledger:
            if item["amount"] < 0:
                cat_spent -= item["amount"]
        totals.append(cat_spent)
    total = sum(totals)
    
    # calculates what percentage of all spending was spent in each category
    perc = {}
    cat_names = []
    for t in range(len(totals)):
        perc[categories[t]] = int(totals[t]/(total/100))
        cat_names.append(categories[t])
    
    # construction of the result string
    chart = "Percentage spent by category"
    # construction of the result string - graph part
    counter = 100
    for i in range(11):
        chart += "\n{0:>3}| ".format(str(counter))
        for j in range(len(categories)):
            if perc[categories[j]] >= counter:
                chart += "o  "
            else:
                chart += "   "
        counter -= 10
    chart += "\n{0:4}{0:->{num}}".format('', num = len(categories*3)+1)
    
    # construction of the result string - names of categories
    cat_list = str(cat_names).split('[')[1].split(']')[0].split(', ')
    longest_cat = max(cat_list, key = len)
    for i in range(len(longest_cat)):
        chart += "\n{0:5}".format('')
        for j in range(len(categories)):
            letter = ''
            if len(cat_list[j]) > i:
                # print('debug: i: '+str(i)+', j: '+str(j), 'len of str: '+str(len(cat_list[j])))
                letter = cat_list[j][i]
            chart += "{0:<3}".format(letter)

    return chart
