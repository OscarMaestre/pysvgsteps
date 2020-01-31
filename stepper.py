#!/usr/bin/python3
 
class Stepper(object):
    def __init__(self, steps=[], stepfilenameformat="step{0}.txt", stepseparator="\n"):
        super().__init__()
        self.steps=steps
        self.stepfilenameformat=stepfilenameformat
        self.stepseparator=stepseparator

    def get_array_slice(self, max_pos):
        steps=self.steps[0:max_pos+1]
        stepstext=self.stepseparator.join(steps)
        return stepstext


    def save_step(self, text, step_number):
        number=str(step_number).zfill(4)
        filename=self.stepfilenameformat.format(number)
        with open(filename, "w") as handle:
            handle.write(text)

    def save_steps(self):
        if self.steps==[]:
            return 
        max_len=len(self.steps)
        i=0
        while i<max_len:
            text=self.get_array_slice(i)
            self.save_step(text, i)
            i=i+1



if __name__ == "__main__":
    vector=["Hola", "Mundo", "Python", "Todo", "va", "bien"]
    stepper=Stepper(steps=vector, stepfilenameformat="Paso{0}.svg")
    stepper.save_steps()