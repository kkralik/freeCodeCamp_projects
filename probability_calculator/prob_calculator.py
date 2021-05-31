
import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, ** colours):
        '''
        colours: variable attributes with int value
        e.g.: Hat(yellow=15,green=1,blue=5)
        '''
        self.contents = []
        self.contents_dict = {}
        for k, v in colours.items():
            self.contents_dict[k] = v
            self.set_attribute(k, v)
            for i in range(v):
                self.contents.append(k)
    
    def set_attribute(self, k, v):
        ''' setter method for assigning variable attributes '''
        setattr(self, k, v)
    
    def get_contents(self):
        ''' getter method for self.contents '''
        return self.contents
            
    def draw(self, number):
        '''
        input: number: int
        output: list of drawn balls
        '''
        drawn = []
        if number > len(self.get_contents()):
            for i in self.get_contents():
                drawn.append(i)
            self.contents.clear()
        else:
            for n in range(number):
                d = random.randint(0, len(self.get_contents())-1)
                temp = self.contents_dict[self.contents[d]]
                setattr(self, self.get_contents()[d], temp-1)
                drawn.append(self.contents.pop(d))
        
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    '''
    performs large number of draws on a Hat class object and calculates probability of drawing expected_balls
    input:
        hat: Hat class object
        expected_balls: dictionary of the desired ball colours drawn, e.g. {"yellow":7,"blue":1}
        num_balls_drawn: int, number of drawn balls in each experiment
        num_experiments: int, number of performed balls drawing from a full hat - too small number can lead to misleading result
    output: float, probability with which expected_balls combination will be drawn out of hat in num_balls_drawn drawn balls
    '''
    count = 0
    balls_wanted = []
    for k, v in expected_balls.items():
        for i in range(v):
            balls_wanted.append(k)
    for e in range(num_experiments):
        hat_here = copy.deepcopy(hat)
        d = hat_here.draw(num_balls_drawn)
        b = copy.deepcopy(balls_wanted)
        for item in balls_wanted:
            if item not in d:
                break
            else:
                d.remove(item)
                b.remove(item)
        if len(b) == 0:
            count += 1

    return count/num_experiments
