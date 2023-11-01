import customtkinter as ct
import numpy as np
import matplotlib.pyplot as plt

ct.set_appearance_mode('dark')
ct.set_default_color_theme('green')

root= ct.CTk()
root.geometry('400x300')

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
   # plt.hist(house_prices,200)
    plt.polar(house_prices)
    plt.show()

my_button = ct.CTkButton(root,text='Graph It', command=graph)
my_button.pack()

root.mainloop()