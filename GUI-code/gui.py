from tkinter import *
def runing():
    app=Tk()
    app.title('Predictions')
    fname=Canvas(bg="black", height=900, width=1000)
    image1=PhotoImage(file='prediction_1.png')
    image2=PhotoImage(file='prediction_2.png')
    image3=PhotoImage(file='prediction_3.png')
    image4=PhotoImage(file='prediction_4.png')
    image5=PhotoImage(file='prediction_5.png')
    image6=PhotoImage(file='prediction_6.png')
    image7=PhotoImage(file='prediction_7.png')
    image8=PhotoImage(file='prediction_8.png')
    image9=PhotoImage(file='prediction_9.png')
    def img1():
        image=fname.create_image(800, -20, anchor=NE, image=image1)
    def img2():
        image=fname.create_image(800, -20, anchor=NE, image=image2)
    def img3():
        image=fname.create_image(800, -20, anchor=NE, image=image3)
    def img4():
        image=fname.create_image(800, -20, anchor=NE, image=image4)
    def img5():
        image=fname.create_image(800, -20, anchor=NE, image=image5)
    def img6():
        image=fname.create_image(800, -20, anchor=NE, image=image6)
    def img7():
        image=fname.create_image(800, -20, anchor=NE, image=image7)
    def img8():
        image=fname.create_image(800, -20, anchor=NE, image=image8)
    def img9():
        image=fname.create_image(800, -20, anchor=NE, image=image9)
    var=IntVar()
    R1=Radiobutton(app, text='Before Lockdown', variable=var, value=1, command=img1)
    R1.pack(anchor=W)
    R2=Radiobutton(app, text='Lockdown 1', variable=var, value=2, command=img2)
    R2.pack(anchor=W)
    R3=Radiobutton(app, text='Lockdown 2', variable=var, value=3, command=img3)
    R3.pack(anchor=W)
    R4=Radiobutton(app, text='Lockdown 3', variable=var, value=4, command=img4)
    R4.pack(anchor=W)
    R5=Radiobutton(app, text='Lockdown 4', variable=var, value=5, command=img5)
    R5.pack(anchor=W)
    R6=Radiobutton(app, text='Unlockdown 1', variable=var, value=6, command=img6)
    R6.pack(anchor=W)
    R7=Radiobutton(app, text='Overall Comparison', variable=var, value=7, command=img9)
    R7.pack(anchor=W)
    R8=Radiobutton(app, text='Accuracy Percentage', variable=var, value=8, command=img8)
    R8.pack(anchor=W)
    R9=Radiobutton(app, text='Error Percentage', variable=var, value=9, command=img7)
    R9.pack(anchor=W)
    fname.pack()
    app.mainloop()
