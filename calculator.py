from tkinter import *
import math
root = Tk()
root.geometry('325x394')
root.title('Calculator')
root.configure(bg= '#868DAE')
root.resizable(0,0)


disp = Frame(root, height = 40, width = 300, borderwidth = 4, relief = SUNKEN)
disp.place(x = 20, y = 15)

calc = Frame(root, borderwidth = 3, relief = GROOVE)
calc.place(x = 8, y = 105)

class CalcButtons():
    button_column = 0
    button_row = 4
    display_text = '0.0'
    current_number = ''
    previous_number = ''
    operation = ''
    solved = False
    display = Label(disp,text = display_text, height = 2, width = 22, bg ='#757B97', fg ='white', anchor = 'e')
    display.configure(font=('Arial',15,'bold'))
    display.grid(column = 0, row = 0, columnspan = 6)
    display.grid_propagate(False)
    def __init__(self,number):
        self.number = number
    def make_button(self, button_column, button_row):
        
        
        self.button = Button(calc,text = (self.number),command=self.button_click, height= 2, width = 4, bg = '#868DAE', fg = 'white', border =3)
        self.button.configure(font=('Arial',15))
        self.button.grid(column = button_column, row = button_row)
        
    def button_click(self):
        if CalcButtons.solved and self.number not in ['+','-','x','/','+/-','sq','sqrt']:
            CalcButtons.current_number = ''
            CalcButtons.solved = False
        if self.number =='delete':
            if len(CalcButtons.current_number)>0:
                CalcButtons.current_number=CalcButtons.current_number[:-1]
                CalcButtons.display['text'] = CalcButtons.current_number
        elif self.number.lower() =='c':
            CalcButtons.current_number = ''
            CalcButtons.previous_number = ''
            CalcButtons.display['text'] = CalcButtons.display_text
        elif self.number == '+/-':
            if CalcButtons.current_number == '':
                CalcButtons.current_number+=('-')
            elif '-' in CalcButtons.current_number: 
                CalcButtons.current_number = CalcButtons.current_number[1:]
            else:
                CalcButtons.current_number = '-' + CalcButtons.current_number
            
            CalcButtons.display['text'] = CalcButtons.current_number
        elif self.number == '-' and CalcButtons.previous_number == '' and CalcButtons.current_number == '':
            CalcButtons.current_number+=('-')
            CalcButtons.display['text'] = CalcButtons.current_number
        elif self.number == 'sq':
            CalcButtons.current_number = str(float(CalcButtons.current_number) * float(CalcButtons.current_number))
            CalcButtons.display['text']= CalcButtons.current_number
            CalcButtons.previous_number = ''
            CalcButtons.operation = ''
        elif self.number == 'sqrt': 
            if CalcButtons.current_number.startswith('-'):
                CalcButtons.display['text'] = 'Error'
                CalcButtons.current_number = ''
            else:
                CalcButtons.current_number = str(math.sqrt(float(CalcButtons.current_number)))
                CalcButtons.display['text'] = CalcButtons.current_number 
                CalcButtons.previous_number = ''
                CalcButtons.operation = ''
        elif self.number not in ['1','2','3','4','5','6','7','8','9','0','+','-','x','/','=','.']:
            pass

        elif self.number == '=':
            if CalcButtons.current_number =='':
                pass
            else:
                if CalcButtons.operation == '+':
                    CalcButtons.current_number = str(float(CalcButtons.current_number) + float(CalcButtons.previous_number))
                elif CalcButtons.operation == '-':
                    CalcButtons.current_number = str(float(CalcButtons.previous_number) - float(CalcButtons.current_number))
                elif CalcButtons.operation == 'x':
                    CalcButtons.current_number = str(float(CalcButtons.current_number) * float(CalcButtons.previous_number))
                elif CalcButtons.operation == '/':
                    if CalcButtons.current_number == '0':
                        CalcButtons.current_number = ''
                    else:
                        CalcButtons.current_number = str(float(CalcButtons.previous_number) / float(CalcButtons.current_number))
            
            
                CalcButtons.display['text'] = CalcButtons.current_number
                CalcButtons.previous_number = ''
                CalcButtons.operation = ''
                CalcButtons.solved = True
                return CalcButtons.current_number
        elif self.number =='.':
            if '.' not in CalcButtons.current_number:
                CalcButtons.current_number+=(self.number)
                CalcButtons.display['text'] = CalcButtons.current_number
        elif self.number not in list(map(str,range(10))):
            if CalcButtons.previous_number == '':
                CalcButtons.previous_number = CalcButtons.current_number
            else:
                CalcButtons.previous_number = CalcButtons('=').button_click()
            CalcButtons.current_number = ''
            if self.number in ['+','-','x','/']:
                CalcButtons.operation = self.number
        
            
        else:
            CalcButtons.current_number+=(self.number)
            CalcButtons.display['text'] = CalcButtons.current_number


def key_press(k):
    CalcButtons(k.char).button_click()
def solve(enter):
    CalcButtons('=').button_click()
def delete(delete):
    CalcButtons('delete').button_click()


button_column = 0
button_row = 4
for num in range(10):
    if num == 1:
        button_row = 3 
    elif num == 0:
        button_column = 0
        button_row=4
    elif button_column == 2:
        button_column = 0
        button_row-=1
    else:
        button_column +=1
    CalcButtons(str(num)).make_button(button_column, button_row)
    
CalcButtons('.').make_button(1,4)
CalcButtons('=').make_button(2,4)
CalcButtons('+').make_button(3,4)
CalcButtons('-').make_button(3,3)
CalcButtons('x').make_button(3,2)
CalcButtons('/').make_button(3,1)
CalcButtons('sqrt').make_button(5,1)
CalcButtons('sq').make_button(5,2)
CalcButtons('+/-').make_button(5,3)
CalcButtons('C').make_button(5,4)


root.bind("<BackSpace>",delete)
root.bind("<Return>",solve)    
root.bind("<KeyPress>", key_press)

root.mainloop()