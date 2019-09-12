from tkinter import *

if __name__ == "__main__": 
  root = Tk()
  
  root.title('Calculadora')
  root.geometry("265x125")

  x = 0
  y = 0
  for number in range(1, 10):
    button_number = Button(root, text=number, height=1, width=7)
    button_number.place(x=x, y=y)
    if x == 180:
      x = 0
      y += 100
    else:
      x += 60
  '''
  zero_button = Button(root, text=0, height=1, width=7)
  zero_button.place(x=0, y=0)

  enter_button = Button(root, text='=', height=1, width=14)
  enter_button.place(x=60, y=0)
  

  root.mainloop()