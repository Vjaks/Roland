class homepage :
    def __init__(self):
      user = input("""
      Hai What Do You Open Now ?
                   
      Youtube - type yt
      Local Host - type lh
      """)
      import rightocodespace as rightocodespace
      if user == "yt":
        rightocodespace.mainpage(user)
      
      elif user == "lh":
          rightocodespace.mainpage(user)
       
      else:
         print("yt or lh")
homepage()
