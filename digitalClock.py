from tkinter import Tk,Label
window = Tk()
window.title("Reloj Digital - Digital Clock")
window.geometry("600x300")
window.configure(bg="steelblue")
label = Label(window,font=("Arial Black",78,"bold"), bg="steelblue" , fg="blue")
label.pack(pady=100)
window.mainloop()