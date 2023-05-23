from tkinter import *
from speedtest import Speedtest 

def Speed_check():
    sp =  Speedtest()     # To fetch speed by class of Speedtest class  
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+" Mbps"
    up = str(round(sp.upload()/(10**6),3))+" Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)


# Create a Window of tkinter
sp= Tk()

# Title
sp.title("Internet Speed Test")
# dimension
sp.geometry("500x600")

# Background Colour
sp.config(bg="Blue")

# Creating Label
lab= Label(sp,text="Internet Speed Test",font=("Time New Roman",20,"bold"),bg="Blue",fg="White",)
lab.place(x=60,y=40,height=50,width=380)

# Creating Label Downloading Speed
lab= Label(sp,text="Downloading Speed",font=("Time New Roman",20,"bold"))
lab.place(x=60,y=130,height=50,width=380)

# Label for value of Downloading Speed
lab_down= Label(sp,text="00",font=("Time New Roman",20,"bold"))
 
lab_down.place(x=60,y=200,height=50,width=380)

# Creating Label Uploading Speed
lab= Label(sp,text="Uploading Speed",font=("Time New Roman",20,"bold"))

lab.place(x=60,y=290,height=50,width=380)

# Label for value of Uploading Speed
lab_up= Label(sp,text="00",font=("Time New Roman",20,"bold"))

lab_up.place(x=60,y=360,height=50,width=380)

# Creating Button
button = Button(sp,text="Check Speed",font=("Time New Roman",20,"bold"),relief=RAISED,bg="Green",cursor="arrow",command=Speed_check)

# Dimension of Button
button.place(x=60,y=460,height=50,width=380)




sp.mainloop()