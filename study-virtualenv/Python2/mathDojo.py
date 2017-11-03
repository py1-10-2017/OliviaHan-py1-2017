class MathDojo(object):
    def __init__(self):
        self.result = 0


    def add(self, *numbers):

        for i in range(0,len(numbers)):
            if type(numbers[i]) is list or type(numbers[i]) is tuple:
                for j in numbers[i]:
                    self.result = self.result + j
            else:
                self.result = self.result + numbers[i]
        return self

    def substract(self, *numbers):
        for i in range(0,len(numbers)):
            if type(numbers[i]) is list or type(numbers[i]) is tuple:
                for j in numbers[i]:
                    self.result = self.result - j

            else:
                self.result = self.result - numbers[i]
        return self

    def display(self):
        print "the results is " + str(self.result)
        return self



md = MathDojo()
md.add(2.1,[2,3.5]).add(2).substract(2,[1.5,1]).display()
