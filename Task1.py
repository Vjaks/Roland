class calc:
    def __init__(self,userinput):
       self.a = userinput
  
    def add(self):
       
        if "+" in self.a:
           print('Lets Start Addition')
           fl,sl= self.a.split("+")
           print("Ans : ",int(fl) + int(sl))


    def sub(self):
        
        if "-" in self.a:
         print('Lets Start Subtraction')
         fl,sl= self.a.split("-")
         print("Ans : ",int(fl) - int(sl) )

    def mul(self):
        
        if "*" in self.a:
         print('Lets Start Multiplication')
         fl,sl= self.a.split("*")
         print("Ans : ",int(fl) * int(sl) )

    def div(self):
        
        if "/" in self.a:
         print('Lets Start Division')
         fl,sl= self.a.split("/")
         print("Ans : ",int(fl) / int(sl) ) 

      

obj = calc(userinput =input("Enter Values For Calculate : "))
obj.add()
obj.sub()
obj.mul()
obj.div()