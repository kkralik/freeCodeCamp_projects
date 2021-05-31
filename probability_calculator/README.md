## Introduction
This is my submitted code for finishing one of the projects on <a href = https://www.freecodecamp.org/> freeCodeCamp.org </a>

* Certification name: Scientific Computing with Python
* Task name: <b> Probability Calculator </b>
* My code in the provided test settings: https://replit.com/@kkralik/boilerplate-probability-calculator-1#prob_calculator.py

## Brief description:
The code contains a class 'Hat' with several methods and a function 'experiment', which returns probability of drawing a specific combination of balls from a hat in a specified number of draws.

example:

```
hat1 = Hat(yellow=5,red=1,green=3,blue=9,test=1)
e = experiment(hat=hat1, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=5)
print(e)
```

would lead to output:
```
1.0
```
