# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
aa = name1.lower()
aa = aa.count("t")
aa = aa + name1.count("r")
aa = aa + name1.count("u")
aa = aa + name1.count("e")


bb = name2.lower()
bb = bb.count("t")
bb = bb + name2.count("r")
bb = bb + name2.count("u")
bb = bb + name2.count("e")

true= str(aa + bb)


cc = name1.lower()
cc = cc.count("l")
cc = cc + name1.count("o")
cc = cc + name1.count("v")
cc = cc + name1.count("e")


dd = name2.lower()
dd = dd.count("l")
dd = dd + name2.count("o")
dd = dd + name2.count("v")
dd = dd + name2.count("e")
love = str(cc + dd)
merged = true + love
#print(f"Your score is {merged}%")
merged = int(merged)

if merged < 10 or merged > 90:
  print(f"Your score is {merged}%, you go together like coke and mentos.")
elif merged > 40 and merged < 50:
  print(f"Your score is {merged}%, you are alright together.")
else:
  print(f"Your score is {merged}%.")
  