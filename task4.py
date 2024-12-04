import math

class NonlinearPA:
    def __init__(self, taskNum:int):
        #for tasks 1, 2
        self.interval = None
        self.tolerance = None
        
        #for task 3
        self.initial_guess = None
        self.learning_rate = None
        self.number_iterations = None
        
        #for cool i/o
        self.taskNum = taskNum
        self.taskNames = {1: "Bisection Method for Root-Finding", 
                          2: "Golden Section Method for Unimodal Function Optimization", 
                          3: "Gradient Ascent Method for Maximizing a Function"}
        
    def function1(self, x:float):
        return x**3 - 6*x**2 + 11*x - 6
    
    def function2(self, x:float):
        return (x - 2)**2 + 3
    
    def function3(self, x:float):
        return -1*x**2 + 4*x + 1
    
    def getInput(self):
        print("Task", self.taskNum, self.taskNames.get(self.taskNum))
        if(self.taskNum != 3):
            self.interval = tuple(int(x) for x in input("Initial interval: ").split())
            self.tolerance = float(input("Tolerance: "))
        else:
            self.initial_guess = float(input("Initial guess: "))
            self.learning_rate = float(input("Learning rate "))
            self.number_iterations = int(input("Number of iterations: "))
        
        
    def doTask(self):
        self.getInput()
        if(self.taskNum == 1):
            self.Bisection()
        elif(self.taskNum == 2):
            self.GoldenSection()
        elif(self.taskNum == 3):
            self.GradientAscent()
        
    #TODO
    def Bisection(self):
        pass
            
    def GoldenSection(self):
        interval = self.interval
        while(interval[1] - interval[0] > self.tolerance):
            x_1 = interval[1] - (math.sqrt(5) - 1)/2 * (interval[1] - interval[0])
            x_2 = interval[0] + (math.sqrt(5) - 1)/2 * (interval[1] - interval[0])
            if(self.function2(x_1) < self.function2(x_2)):
                interval = (interval[0], x_2)
            elif(self.function2(x_1) > self.function2(x_2)):
                interval = (x_1, interval[1])
            elif(self.function2(x_1) == self.function2(x_2)):
                interval = (x_1, x_2)
        print("Approximate x_min:", interval[0]+ (interval[1] - interval[0])/2)
        print("Approximate f(x_min)", self.function2(interval[0]+ (interval[1] - interval[0])/2))
    
    #TODO
    def GradientAscent(self):
        pass        

#use it as an example of how to call functions
#works correctly u can check)
task2 = NonlinearPA(3)
task2.doTask()