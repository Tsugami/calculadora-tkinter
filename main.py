from tkinter import *

delete_button = '➡'
delete_all_button = 'c'

buttons = [1,2,3,'+','-',4,5,6,'*','/',7,8,9,delete_button,delete_all_button,222]

class Calculadora:
  def __init__ (self, root):
    self.root = root
    self.operator = ''
    self.add_hud()
    self.add_buttons()

  def add_hud (self):
    self.root.title('Calculadora')
    self.root.geometry('300x150')

  def add_buttons (self):
    x = 0
    y = 0

    for b in buttons:
      button_name = f'button_{b}'
      button = Button(self.root, text=b, height=1,width=7, command = lambda: print(button_name))
      button.place(x=x, y=y)

      if x >= 240:
        x = 0
        y += 25
      else:
        x += 60

    enter_button = Button(root, text='=', height=1, width=33)
    enter_button.place(x=60, y=y)


def add (x):
  global operator
  if x == delete_button:
    operator = operator[:-1]
  elif x == delete_all_button:
    operator = ''
  else:
    operator = operator + x
  print(operator, x)

root = Tk()
App = Calculadora(root)
root.mainloop()
