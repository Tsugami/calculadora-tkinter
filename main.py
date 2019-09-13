from tkinter import *

delete_button = '➡'
delete_all_button = 'c'

expressions = ['+','-','*','/']

class Calculadora:
  def __init__ (self, root):
    self.root = root
    self.operator = ''
    self.add_hud()
    self.add_buttons()

    self.operator_label = Label()
    self.operator_label.place(x=0, y=102)

    self.result_label = Label(font=("Arial", 18))
    self.result_label.place(x=0, y=125)

  def add_hud (self):
    self.root.title('Calculadora')
    self.root.geometry('300x150')

  def add_buttons (self):
  	self._add_button(1, 0, 0, lambda: self.press_button(1))
  	self._add_button(2, 60, 0, lambda: self.press_button(2))
  	self._add_button(3, 120, 0, lambda: self.press_button(3))

  	self._add_button('+', 180, 0, lambda: self.press_button('+'))
  	self._add_button('-', 240, 0, lambda: self.press_button('-'))

  	self._add_button(4, 0, 25, lambda: self.press_button(4))
  	self._add_button(5, 60, 25, lambda: self.press_button(5))
  	self._add_button(6, 120, 25, lambda: self.press_button(6))

  	self._add_button('*', 180, 25, lambda: self.press_button('*'))
  	self._add_button('/', 240, 25, lambda: self.press_button('/'))

  	self._add_button(7, 0, 50, lambda: self.press_button(7))
  	self._add_button(8, 60, 50, lambda: self.press_button(8))
  	self._add_button(9, 120, 50, lambda: self.press_button(9))

  	self._add_button(delete_button, 180, 50, lambda: self.press_button(delete_button))
  	self._add_button(delete_all_button, 240, 50, lambda: self.press_button(delete_all_button))

  	self._add_button(0, 0, 75, lambda: self.press_button(0))
  	self._add_button('=', 60, 75, width=33, command=lambda: self.press_button('='))
 

  def _add_button (self, text, x, y, command, height=1, width=7):
  	button = Button(self.root, text=text, height=height, width=width, command= command)
  	button.place(x=x, y=y)

  def press_button (self, button):
    if  button == delete_button:
    	self.operator = self.operator[:-1]
    elif button == delete_all_button:
    	self.operator = ''
    elif button == '=':
    	self.operator = eval(self.operator)
    else:
    	if len(self.operator) > 0 and str(button) == str(self.operator[-1]) and str(button) in expressions:
    		return
    	self.operator = self.operator + str(button)
    self.update()

  def update (self):
    try:
      self.operator_label.config(text=self.operator)
      self.result_label.config(text=eval(self.operator))
    except:
  	  pass


root = Tk()
App = Calculadora(root)
root.mainloop()