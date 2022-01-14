import Tkinter

top = Tkinter.Tk()

canvas = Tkinter.Canvas(width=1300, height=100, bg='grey')
canvas.pack()

photo = Tkinter.PhotoImage(file="D:\\Winter sem\\ITE1015\\J component\\image.gif")

canvas.create_image(0,0, image=photo, anchor=Tkinter.NW)

w = Tkinter.Scale(top, from_=0, to=100, orient=Tkinter.HORIZONTAL, length=200)
w.pack()
label = Tkinter.Label(text="Blur")
label.pack()

w = Tkinter.Scale(top, from_=0, to=100, orient=Tkinter.HORIZONTAL, length=200)
w.pack()
label = Tkinter.Label(text="Sharpening")
label.pack()

c = Tkinter.Checkbutton(top, text = "Median Filter")
c.pack()

s = Tkinter.Button(top, text = "Submit")
s.pack()

top.mainloop()
