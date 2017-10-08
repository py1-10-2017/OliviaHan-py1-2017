def scores():
    for i in range (0,10):
        from random import randint
        score = (randint(60, 100))
        if score >= 90:
            print 'Score:',score,";", "Your grade is A!"
        elif score >=80:
            print 'Score:',score,";", "Your grade is B!"
        elif score >=70:
            print 'Score:',score,";", "Your grade is C!"
        elif score >=60:
            print 'Score:',score,";", "Your grade is D!"
    print"End of the Program. Bye!"

scores()
