import webbrowser
var1 = input("What App Would You Like TO Open(For List Of MiniApps Type help without capitals And Press Enter) ")
if var1 == "help":
   var1 = webbrowser.open('https://pastebin.com/DvCNLvJy')
   var1 = input("Type Another Command ")
   
if var1 == "Help":
   var1 = input("You Dont Type Help With A Capital Theres No Capitals In Any MiniApp(Yes help Is A MiniApp) ")
if var1 == "yoftube":
   exec(open('yoftube.py').read())
   var1 = input("Now Type The Name Of Another MiniApp ")

if var1 == "armymod":
   exec(open('armymod.py').read())
   var1 = input("Now Type The Name Of Another MiniApp ")

if var1 == "yodafenry":
   webbrowser.open('https://ibb.co/Zh48QW0')
   var1 = input("Yofenry I Am ")

if var1 == "snakeisfun:)":
   exec(open('snakeminigame.py').read())
   var1 = input("Now Type Another Thing But Enjoy The Game")
