# Paul claudel Izabayo
# Game of 15 
# Created for fun

import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox

class game_of_15:

   def __init__ (self, master):
      self.master = master
      self.Vert1 = []
      self.Vert2 = []
      self.Vert3 = []
      self.Horiz1 =[]
      self.Horiz2 =[]
      self.Horiz3 =[]
      self.Diago1= []
      self.Diago2= []
      self.MotherList = []
      
   def Entry_boxes(self):
   
      '''Creates entry boxes'''
      button1 = button3 = ttk.Entry(self.master, font='default 100')
      button1.place (x=0, y = 0)
      self.Vert1.append(button1)
      self.Horiz1.append(button1)
      self.Diago1.append(button1)

      button3 = ttk.Entry(self.master, font='default 100')
      button3.place(x=0,y=135)
      self.Vert1.append(button3)
      self.Horiz2.append(button3)

      button2 = ttk.Entry(self.master, font='default 100')
      button2.place(x=135,y=135)
      self.Vert2.append(button2)
      self.Horiz2.append(button2)
      self.Diago1.append(button2)
      self.Diago2.append(button2)

      button4 = ttk.Entry(self.master, font='default 100')
      button4.place(x=135,y=0)
      self.Vert2.append(button4)
      self.Horiz1.append(button4)

      button5 = ttk.Entry(self.master, font='default 100')
      button5.place(x=270,y=0)
      self.Vert3.append(button5)
      self.Horiz1.append(button5)
      self.Diago2.append(button5)

      button7 = ttk.Entry(self.master, font='default 100')
      button7.place(x=270,y=135)
      self.Vert3.append(button7)
      self.Horiz2.append(button7)

      button9 = ttk.Entry(self.master, font='default 100')
      button9.place(x=0,y=270)
      self.Vert1.append(button9)
      self.Horiz3.append(button9)
      self.Diago2.append(button9)

      button8 = ttk.Entry(self.master, font='default 100')
      button8.place(x=135,y=270)
      self.Vert2.append(button8)
      self.Horiz3.append(button8)

      button6 = ttk.Entry(self.master, font='default 100')
      button6.place(x=270,y=270)
      self.Vert3.append(button6)
      self.Horiz3.append(button6)
      self.Diago1.append(button6)

   def Wrong_Entry_Type(self):
      
      wrong_entry_try = messagebox.askquestion('Wrong Entry','You can only use integers from 0 to 9 and no duplicates are allowed. Wanna try again?')
      self.master.destroy()
      if wrong_entry_try == "yes":
         main()
         
   def Won_Game (self):
      messagebox.showinfo ('Congratulations', 'Kudos, You won the Game of 15')

   def Lost_Game(self):
      try_again = messagebox.askquestion ('Aw', 'The Entries do not sum to 15. Wanna try Again?')
      self.master.destroy()
      if try_again == "yes":
         main()
   

   def Result(self):
   
      '''Creates list with all entries and makes sure we get the right entry type'''
      for i in range(0,3):
         self.Vert1[i] = int (self.Vert1[i].get())
         if 9 < self.Vert1[i] or self.Vert1[i] < 0 or self.Vert1[i] in self.MotherList:
            self.Wrong_Entry_Type()
         self.MotherList.append(self.Vert1[i])

         self.Vert2[i] = int (self.Vert2[i].get())
         if 9 < self.Vert2[i] or self.Vert2[i] < 0 or self.Vert2[i] in self.MotherList:
            self.Wrong_Entry_Type()
         self.MotherList.append(self.Vert2[i])

         self.Vert3[i] = int (self.Vert3[i].get())
         if 9 < self.Vert3[i] or self.Vert3[i] < 0 or self.Vert3 [i] in self.MotherList:
            self.Wrong_Entry_Type()
         self.MotherList.append(self.Vert3[i])

         self.Horiz1[i] = int (self.Horiz1[i].get())

         self.Horiz2[i] = int (self.Horiz2[i].get())
         
         self.Horiz3[i] = int (self.Horiz3[i].get())

         self.Diago1[i] = int (self.Diago1[i].get())

         self.Diago2[i] = int (self.Diago2[i].get())
   
      if (sum(self.Vert1) == sum(self.Vert2) 
          == sum (self.Vert3) == sum(self.Horiz1)
          ==sum(self.Horiz2) == sum(self.Horiz3)
          == sum(self.Diago1) == sum(self.Diago2) == 15):
         self.Won_Game()
      else:
         self.Lost_Game()

   def Done(self):
      done_botton = ttk.Button(self.master,text="Done", command= self.Result)
      done_botton.place(x= 300,y=410)
   def Quit(self):
      done_botton = ttk.Button(self.master,text="Quit", command= self.master.destroy)
      done_botton.place(x= 10,y=410)

def main():
   window = tk.Tk()
   window.geometry('400x450')
   window.title ("Game of 15")
   new_game = game_of_15(window)
   new_game.Entry_boxes()
   new_game.Done()
   new_game.Quit()
   window.mainloop()
main()
