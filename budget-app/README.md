## Introduction
This is my submitted code for finishing one of the projects on <a href = https://www.freecodecamp.org/> freeCodeCamp.org </a>

* Certification name: Scientific Computing with Python
* Task name: <b> Budget app </b>
* My code in the provided test settings: https://replit.com/@kkralik/boilerplate-budget-app-1#budget.py

## Brief description:
The code contains a class Category with several methods, which keep track of the budget and offer easy-to-read format as a result.

example:

```
# initialising 'Food' category and a few budget operations
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

# initialising 'Clothing' category and a few budget operations
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)

# initialising 'Auto' category and a few budget operations
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(create_spend_chart([food, clothing, auto]))
```

would lead to output:
```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```
