
import re

user_name = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
Email=[]
Password=[]

def isValid(email):
    if re.fullmatch(user_name, email):
      
      Email.append(email)
      

      
      return(True)
    else:
      print("Invalid email")
      return(False)
def passcode(password):

    Specialchar=['$','@','#','*']
    return_A=True
    if len(password) < 5:
        print('the length of password should be at least 5 char long')
        return_A=False
    if len(password) > 16:
        print('the length of password should be not be greater than 16')
        return_A=False
    if not any(B in Specialchar for B in password):
        print('the password should have at least one of the symbols $@#*')
        return_A=False        
    if not any(B.isdigit() for B in password):
        print('the password should have at least one digit')
        return_A=False
    if not any(B.isupper() for B in password):
        print('the password should have at least one uppercase letter')
        return_A=False
    if not any(B.islower() for B in password):
        print('the password should have at least one lowercase letter')
        return_A=False
    if return_A:
        print("registration created \n")
        Password.append(password)
        login()
       
        
        
    
    else:
      password()

def register():
  
  email=input()
  if isValid(email):
    password = input('enter the password : ')
    print(passcode(password))
    print(Email)
    print(Password)
  
 
  def login():
    print("YOU ARE IN LOGIN PAGE\n")
    Ema_il = input("Please enter your Email")
    Pass_word = input("Please enter your password")  
        
    for i in range(Email):
      if Email[i]==Ema_il:
        for j in range(Password):
          if Password[j]==Pass_word:
             print("Correct credentials!")
             print("YOU ARE LOGGED IN TO THIS PAGE")
             return True
          else:
            print("wrong Password")
            forget=int(input("Press enter forget Password"))
            if(forget==1):
              new_password=input("Enter your new password")
              login()
      else:
        register()
          
                



print("Please Enter 1 for Register\t2 for Login ")
a=int(input())
if(a==1):
  register()
else:
  login()
  







