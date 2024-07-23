import tkinter as tk

root = tk.Tk()

#madhesia  e hapsires se window, titulli i appit
root.geometry('500x500')
root.title("Jon Calculator")

root["bg"] = "#B9E47A"
#label si titull, me.pack() e kena vendos ne window
label = tk.Label(root,text="Welcome to Calculator" , font=("Times New Roman",20))
label.pack(padx=20, pady=20)

#input i nje shkrimi permes .Text
textbox = tk.Text(root, height=3)
#me .pack() e kemi vendos ne window
textbox.pack()




buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

#krijimi i butonave
btn1 = tk.Button(buttonframe, text="1", font=("Times New Roman",16))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
btn1.config(bg="#D4F5A4")
buttonframe.pack(fill= "x")

#krijimi i butonave
btn2 = tk.Button(buttonframe, text="2", font=("Times New Roman",16))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
btn2.config(bg="#D4F5A4")
buttonframe.pack(fill= "x")

#krijimi i butonave
btn3 = tk.Button(buttonframe, text="3", font=("Times New Roman",16))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
btn3.config(bg="#D4F5A4")
buttonframe.pack(fill= "x")

#butoni per +
btnplus = tk.Button(buttonframe, text="+", font=("Times New Roman",16))
btnplus.grid(row=0, column=3, sticky=tk.W+tk.E)

buttonframe.pack(fill= "x")

#krijimi i butonave
btn4 = tk.Button(buttonframe, text="4", font=("Times New Roman",16))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)
btn4.config(bg="#D4F5A4")
buttonframe.pack(fill= "x")


#krijimi i butonave
btn5 = tk.Button(buttonframe, text="5", font=("Times New Roman",16))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)
btn5.config(bg="#D4F5A4")
buttonframe.pack(fill= "x")

#krijimi i butonave
btn6 = tk.Button(buttonframe, text="6", font=("Times New Roman",16))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)
btn6.config(bg="#D4F5A4")
buttonframe.pack(fill= "x")

#btnminus
btnminus = tk.Button(buttonframe, text="-", font=("Times New Roman",16))
btnminus.grid(row=1, column=3, sticky=tk.W+tk.E)

buttonframe.pack(fill= "x")

#krijimi i butonave
btn7 = tk.Button(buttonframe, text="7", font=("Times New Roman",16))
btn7.grid(row=2, column=0, sticky=tk.W+tk.E)
btn7.config(bg="#D4F5A4")
buttonframe.pack(fill= "x")

#krijimi i butonave
btn8 = tk.Button(buttonframe, text="8", font=("Times New Roman",16))
btn8.grid(row=2, column=1, sticky=tk.W+tk.E)
btn8.config(bg="#D4F5A4")
buttonframe.pack(fill= "x")

#krijimi i butonave
btn9 = tk.Button(buttonframe, text="9", font=("Times New Roman",16))
btn9.grid(row=2, column=2, sticky=tk.W+tk.E)
btn9.config(bg="#D4F5A4")
buttonframe.pack(fill= "x")

#butoni oer *
btnprodhimi = tk.Button(buttonframe, text="*", font=("Times New Roman",16))
btnprodhimi.grid(row=2, column=3, sticky=tk.W+tk.E)

buttonframe.pack(fill= "x")

root.mainloop()
