import tkinter as tk

###############################################################################
# DONE: 1. (2 pts)
#
#   For this _todo_, copy your code from your fillable form from Session 20 and
#   paste it below.
#
#   Now, create a function called print_form() that gets all the values entered
#   in your form and prints them on their own line.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# DONE: 2. (1 pt)
#
#   Now, use the command keyword to connect your "Submit" button to your
#   print_form() function.
#
#   Now, when you run your program, you should be able to type information into
#   the form and click "Submit", and it will print all the information that you
#   entered.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

window=tk.Tk()
window.title("Costum Widgets")

f1 = tk.Frame(window, bg="red", padx=5, pady=5)
f2 = tk.Frame(window, bg="yellow", padx=5, pady=5)
f3 = tk.Frame(window, bg="yellow", padx=5, pady=5)
f4 = tk.Frame(window, bg="purple", padx=5, pady=5)
f5 = tk.Frame(window, bg="green", padx=5, pady=5)
f6 = tk.Frame(window, bg="blue", padx=5, pady=5)
f7 = tk.Frame(window, bg="red", padx=5, pady=5)
f8 = tk.Frame(window, bg="red", padx=5, pady=5)

f1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
f2.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
f3.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
f4.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
f5.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
f6.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")
f7.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")
f8.grid(row=7, column=0, padx=5, pady=5, sticky="nsew")

window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], weight=1)
window.columnconfigure(0, weight=1)

l1 = tk.Label(f1, text="Name", bg="red")
l2 = tk.Label(f2, text="Address Line 1", bg="yellow")
l3 = tk.Label(f3, text="Address Line 2", bg="yellow")
l4 = tk.Label(f4, text="City", bg="purple")
l5 = tk.Label(f5, text="State", bg="green")
l6 = tk.Label(f6, text="Zip Code", bg="blue")
l7 = tk.Label(f7, text="Phone Number", bg="red")
l8 = tk.Label(f8, text="Email Address", bg="red")

l1.pack()
l2.pack()
l3.pack()
l4.pack()
l5.pack()
l6.pack()
l7.pack()
l8.pack()


entry1=tk.Entry(f1)
entry1.pack()
entry2=tk.Entry(f2)
entry2.pack()
entry3=tk.Entry(f3)
entry3.pack()
entry4=tk.Entry(f4)
entry4.pack()
entry5=tk.Entry(f5)
entry5.pack()
entry6=tk.Entry(f6)
entry6.pack()
entry7=tk.Entry(f7)
entry7.pack()
entry8=tk.Entry(f8)
entry8.pack()

def print_form():
    print(entry1.get())
    print(entry2.get())
    print(entry3.get())
    print(entry4.get())
    print(entry5.get())
    print(entry6.get())
    print(entry7.get())
    print(entry8.get())

button=tk.Button(master=window, text="submit", command=print_form)
button.grid()

window.mainloop()
