from random import randint

class Training:
    def __init__(self, low, up, exList):
        self.low = low
        self.up = up
        self.exList = exList
        self.pakli = []
        for ex in self.exList:
            temp = [ex+" - "+str(x) for x in range(self.low, self.up + 1)]
            self.pakli += temp

    def play(self):
        pakli = self.pakli.copy()
        print("Press ENTER to pull a new exercise!")
        while len(pakli) > 0:
            input()
            index = randint(0, (len(pakli)-1))
            print(pakli[index])
            pakli.pop(index)

if __name__ == "__main__":
    repMin = int(input("Minumum rep: "))
    repMax = int(input("Maximum rep: "))
    exNum = int(input("Number of exercises: "))
    exercises = []
    for i in range(exNum):
        exercises.append(input("{}. Exercise name: ".format(i+1)))
    
    workout = Training(repMin, repMax, exercises)
    workout.play()
