import tkinter as tk

class mainpage():
    def __init__(self,input):
       
# Youtube

       if input == "yt":  
            def submit():
        
              import os
              urlyt=f"https://www.youtube.com/results?search_query={entry.get()}"
              os.startfile(urlyt)
           
            root = tk.Tk()
            root.title("Righto")
            root.geometry("300x100")
    
            text = tk.Label(root, text="Search On Youtube : ")
            text.place(x=0, y=55)
    
            image = tk.PhotoImage(file="C:\\xampp\\htdocs\\Geek\\pythonprojects\\Logo_of_YouTube.png")
            image = image.subsample(10,10)
            label = tk.Label(root, image=image)
            label.place(x=0, y=0)
    
            entry = tk.Entry(root)
            entry.place(x=115, y=57)
    
            button = tk.Button(root, text="Submit", command=submit)
            button.place(x=250, y=52)
    
            root.mainloop()
 
# Local host

       elif input == "lh":  
            def submit():
        
              import os
              
              urlyt=f"https://localhost/{entry.get()}/"
              os.startfile(urlyt)
           
            root = tk.Tk()
            root.title("Righto")
            root.geometry("300x100")
    
            text = tk.Label(root, text="Search On LocalHost : ")
            text.place(x=0, y=65)
    
            image = tk.PhotoImage(file="C:\\xampp\\htdocs\\Geek\\pythonprojects\\dx-localhost.png")
            image = image.subsample(4,4)
            label = tk.Label(root, image=image)
            label.place(x=0, y=0)
    
            entry = tk.Entry(root)
            entry.place(x=122, y=67)
    
            button = tk.Button(root, text="Submit", command=submit)
            button.place(x=250, y=63)
    
            root.mainloop()
       else:
           print("DOneyyy")
mainpage("yt")
mainpage("lh")