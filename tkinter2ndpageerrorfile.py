
import tkinter as tk
page1 = tk.Tk()
page1.title("Righto Home Page")
page1.geometry("350x550")

def movepointer():
        import rightocodespace as rightocodespace
        rightocodespace.mainpage("yt")


quitbox = tk.Button(page1,text="Youtube",command=movepointer)
# checkbox = tk.Checkbutton(page1,text="Youtube",variable=YT,command=movepointer)
quitbox.pack()
page1.mainloop()
