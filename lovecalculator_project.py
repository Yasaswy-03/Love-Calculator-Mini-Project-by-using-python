print("Welcome to Love Calculator")
name1 = str(input("Enter your name : ")).lower()
name2 = str(input("Enter his/her name :")).lower()
name = name1 + name2 
t=name.count("t")
r=name.count("r")
u=name.count("u")
e=name.count("e")
x=str(t+r+u+e)
l=name.count("l")
o=name.count("o")
v=name.count("v")
e=name.count("e")
y=str(l+o+v+e)
percent = int(x+y)
print(f"{x}{y} is the percent ")
print("Calculating Love ")
if percent < 10:
    print("Low love score")
elif 10 <= percent < 40 :
    print("You need to build more with your partner ")
elif 40 <= percent < 90:
    print("A strong bond")  
else:
    print("A very strong bond")      

    
    
 