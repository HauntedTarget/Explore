#Imported modules
import tkinter as tkin
import pickle
import random
from datetime import datetime

#Variables
key = 0
candy = 0
coat = False
battery = 0
crystal = 0
candynow = 0
bowldown = False
pis = False
colds = False
moons = False
#Variable for the pi secret
picheck = 0
#Variable for game save area
area = 0

#The GUI class
class Game:
  def __init__(self):
    #Initializes the main window
    self.start = tkin.Tk()
    self.start.title('Explore')
    self.start.geometry("500x410")
    #Game Icons
    self.icon = tkin.PhotoImage(file = "Explore.png")
    self.icon2 = tkin.PhotoImage(file = 'Secret.png')
    self.icon3 = tkin.PhotoImage(file = 'Inventory.png')
    self.start.iconphoto(False, self.icon)
    #Initializes top frame
    self.top = tkin.Frame()
    #Background image
    self.bg = tkin.PhotoImage(file = "Intro.png")
    self.background = tkin.Label(self.top,image=self.bg)
    #Packs the background image
    self.background.pack(side='left')
    #Initializes the text label
    self.tuto = tkin.Label(self.top, text="This is a fun\nexploration\npuzzle game.\nTo play just\nhit the\nbuttons\ninteract with\nthe game.\nAlso, look out\nfor secret\nwindows.\nSecret\nwindows\ncan be found\nby doing\nsome actions\nthat are not\ndescribed\nby direct\nhints.\n")
    #Packs the label
    self.tuto.pack(side= 'top')
    #Initializes the start game button
    self.cont = tkin.Button(self.top,text='Start\nGame',command=self.enter_game)
    #Packs the start game button
    self.cont.pack(side='top')
    #Packs the top frame
    self.top.pack(side='top')
    #Initializes the main loop
    tkin.mainloop()
  #Command for the start game button
  def enter_game(self):
    #Hides the main window <--- Learnt on the tkinter website
    self.start.withdraw()
    #Initialize the inventory
    self.inventory()
    try:
      #Attempts to load data if there is any
      self.getdata()
      if area == 0:
        self.saveroom()
    except:
      #Inintialize the hallway window
      self.hallway()
  #The player inventory window
  def inventory(self):
    #Sets the window attributes
    global key
    global candy
    global crystal
    global battery
    self.inven = tkin.Toplevel()
    self.inven.geometry('150x100')
    self.inven.title('Inventory')
    self.inven.iconphoto(False, self.icon3)
    #Keys Item
    self.invenframe1 = tkin.Frame(self.inven)
    self.keys = tkin.StringVar()
    self.keytxt = tkin.Label(self.invenframe1,text='Keys: ')
    self.keytxt.pack(side='left')
    self.keytxt2 = tkin.Label(self.invenframe1,textvariable=self.keys)
    self.keys.set(key)
    self.keytxt2.pack(side='left')
    self.invenframe1.pack(side='top')
    #Candy Item
    self.invenframe2 = tkin.Frame(self.inven)
    self.candies = tkin.StringVar()
    self.candytxt = tkin.Label(self.invenframe2,text='Candies: ')
    self.candytxt.pack(side='left')
    self.candytxt2 = tkin.Label(self.invenframe2,textvariable=self.candies)
    self.candies.set(candy)
    self.candytxt2.pack(side='left')
    self.invenframe2.pack(side='top')
    #Battery Item
    self.invenframe3 = tkin.Frame(self.inven)
    self.batteries = tkin.StringVar()
    self.batterytxt = tkin.Label(self.invenframe3,text='Batteries: ')
    self.batterytxt.pack(side='left')
    self.batterytxt2 = tkin.Label(self.invenframe3,textvariable=self.batteries)
    self.batteries.set(battery)
    self.batterytxt2.pack(side='left')
    self.invenframe3.pack(side='top')
    #Crystal Item
    self.invenframe4 = tkin.Frame(self.inven)
    self.crystals = tkin.StringVar()
    self.crystaltxt = tkin.Label(self.invenframe4,text='Crystals: ')
    self.crystaltxt.pack(side='left')
    self.crystaltxt2 = tkin.Label(self.invenframe4,textvariable=self.crystals)
    self.crystals.set(crystal)
    self.crystaltxt2.pack(side='left')
    self.invenframe4.pack(side='top')
  #Updates the inventory
  def update(self):
    self.keys.set(key)
    self.candies.set(candy)
    self.batteries.set(battery)
    self.crystals.set(crystal)
  #The hallway window
  def hallway(self):
    #Inintialize the hallway window as a top level of the start window
    self.hall = tkin.Toplevel(self.start)
    self.hall.title('Main Hallway')
    self.hall.geometry('400x460')
    #Game Icon
    self.hall.iconphoto(False, self.icon)
    #Initializes the top frame
    self.top = tkin.Frame(self.hall)
    #Initializes the background image
    self.bg2 = tkin.PhotoImage(file = "Hallway.png")
    self.background2 = tkin.Label(self.top,image=self.bg2)
    #Packs the background image
    self.background2.pack(side='top')
    #Packs the top frame
    self.top.pack(side='top')
    #Initializes and packs the info text
    self.text = tkin.Frame(self.hall)
    self.info = tkin.Label(self.text,text='Main Hallway')
    self.info.pack(side='top')
    self.text.pack(side='top')
    #Initializes and packs the choice button frame
    self.choice = tkin.Frame(self.hall)
    self.lef = tkin.Button(self.choice,text = 'Left Door',command=self.halltomoon)
    self.dow = tkin.Button(self.choice,text='Down Hole',command=self.halltohedge)
    self.rig = tkin.Button(self.choice,text='Right Door',command=self.halltoclock)
    self.lef.pack(side='left')
    self.dow.pack(side='left')
    self.rig.pack(side='left')
    self.choice.pack(side='top')
  #Goes from the hallway window to the moon window
  def halltomoon(self):
    global bowldown
    #Closes the hallway window and opens the moon window or opens The Moon secret window
    if bowldown:
      self.themoon()
    else:
      self.hall.destroy()
      self.moon()
  #Sends user from the hallway to the hedge garden
  def halltohedge(self):
    self.hall.destroy()
    self.hedge()
  #Sends user to the clock room
  def halltoclock(self):
    self.hall.destroy()
    self.clocks()
  #The space window
  def moon(self):
    #Sets the window attributes and the background image
    self.robot = tkin.Toplevel(self.start)
    self.robot.title('The Moon')
    self.robot.geometry('400x460')
    self.robot.iconphoto(False, self.icon)
    #Initializes and packs the npc image
    self.image = tkin.Frame(self.robot)
    self.bg3 = tkin.PhotoImage(file = "Npc2.png")
    self.npc = tkin.Label(self.robot,image=self.bg3)
    self.npc.pack(side='top')
    self.image.pack(side='top')
    #Initializes and packs the interaction text
    self.textframe = tkin.Frame(self.robot)
    self.talk = tkin.StringVar()
    self.talk.set('Hello Biological Being')
    self.robotalk = tkin.Label(self.textframe,textvariable=self.talk)
    self.robotalk.pack()
    self.textframe.pack()
    #Initializes and packs choice buttons
    self.choice = tkin.Frame(self.robot)
    self.back = tkin.Button(self.choice,text='Hallway',command=self.moontohall)
    self.crys = tkin.Button(self.choice,text='Trade Battery for Crystal',command=self.crystal)
    self.back.pack(side='left')
    self.crys.pack(side='left')
    self.choice.pack(side='top')
  #Sends the user back to the hallway from the moon window
  def moontohall(self):
    #Closes the moon window and opens the hall window
    self.robot.destroy()
    self.hallway()
  #Takes away a battery for a crystal
  def crystal(self):
    global battery
    global crystal
    if battery > 0:
      battery -= 1
      crystal += 1
      self.talk.set('Thank You For The Power!')
      self.update()
    else:
      self.talk.set("Error! No Battery Held By Human!")
  #The moon secret
  def themoon(self):
    #Sets the window attributes and the background image
    global moons
    moons = True
    self.smoon = tkin.Toplevel(self.start)
    self.smoon.iconphoto(False, self.icon2)
    self.smoon.title('THE MOON')
    self.smoon.geometry('200x200')
    self.photo = tkin.Frame(self.smoon)
    self.secret1 = tkin.PhotoImage(file = "TheMoon.png")
    self.background = tkin.Label(self.photo,image=self.secret1)
    self.background.pack()
    self.photo.pack()
  #Hedge garden window
  def hedge(self):
    #Sets the window attributes and the background image
    self.garden = tkin.Toplevel(self.start)
    self.garden.iconphoto(False, self.icon)
    self.garden.title('Hedge Garden')
    self.garden.geometry('400x490')
    self.photo = tkin.Frame(self.garden)
    self.gard = tkin.PhotoImage(file='Hedge.png')
    self.background = tkin.Label(self.photo,image=self.gard)
    self.background.pack()
    self.photo.pack()
    self.text = tkin.Label(self.garden,text = 'The Garden')
    self.text.pack()
    self.choice = tkin.Frame(self.garden)
    self.left = tkin.Button(self.choice,text='Left Archway',command=self.hedgetotoll)
    self.back = tkin.Button(self.choice,text='Back Up Hole',command=self.hedgetohall)
    self.right = tkin.Button(self.choice,text='Right Archway',command=self.hedgetoclock)
    self.left.pack(side='left')
    self.back.pack(side='left')
    self.right.pack(side='left')
    self.choice.pack(side='top')
    self.choice2 = tkin.Frame(self.garden)
    self.up = tkin.Button(self.choice2,text='Through Window',command=self.hedgetosave)
    self.up.pack(side='top')
    self.choice2.pack(side='top')
  #Sends user to toll from hedge garden
  def hedgetotoll(self):
    self.garden.destroy()
    self.tollroad()
  #Sends user to the hallway from the hedge garden
  def hedgetohall(self):
    self.garden.destroy()
    self.hallway()
  #Sends user to the clock room from the hedge gerden
  def hedgetoclock(self):
    self.garden.destroy()
    self.clocks()
  #Sends user to the saving room from the hedge garden
  def hedgetosave(self):
    self.garden.destroy()
    self.saveroom()
  #The toll road to keep players from getting to candy without paying a key
  def tollroad(self):
    #Sets the window attributes
    self.toll = tkin.Toplevel(self.start)
    self.toll.iconphoto(False, self.icon)
    self.toll.title('Toll Road')
    self.toll.geometry('200x100')
    self.talk = tkin.StringVar()
    self.talk.set('Toll Road')
    self.pay = tkin.Label(self.toll,textvariable=self.talk)
    self.pay.pack(side='top')
    self.choice = tkin.Frame(self.toll)
    self.lock = tkin.Button(self.choice,text='Pay A Key To Go To Candy',command = self.tolltocandy)
    self.back = tkin.Button(self.choice,text='Back To The Hedge Garden',command = self.tolltohedge)
    self.lock.pack(side='top')
    self.back.pack(side='top')
    self.choice.pack(side='top')
  #Sends user to the cady bowl room from the toll road only if they have a key if not then the user is told they don't have a key
  def tolltocandy(self):
    global key
    if key > 0:
      key -= 1
      self.toll.destroy()
      self.candy()
      self.update()
    else:
      self.talk.set("Sorry! You don't have a key!")
  #Sends user to the hadge garden from the toll road
  def tolltohedge(self):
    self.toll.destroy()
    self.hedge()
  #The clock room
  def clocks(self):
    #Sets the window attributes and the background image
    self.clock = tkin.Toplevel(self.start)
    self.clock.iconphoto(False, self.icon)
    self.clock.title('Room With A Clock')
    self.clock.geometry('400x490')
    self.photo = tkin.Frame(self.clock)
    self.bg = tkin.PhotoImage(file='Clocks.png')
    self.image = tkin.Label(self.photo,image=self.bg)
    self.image.pack(side='top')
    self.photo.pack(side='top')
    self.out = tkin.StringVar()
    self.out.set('Clock Room')
    self.text = tkin.Label(self.clock,textvariable=self.out)
    self.text.pack(side='top')
    self.choice = tkin.Frame(self.clock)
    self.times = tkin.Button(self.choice,text='Check Time',command=self.timesee)
    self.floor = tkin.Button(self.choice,text='Into Ground Vent',command=self.clocktograil)
    self.times.pack(side='left')
    self.floor.pack(side='left')
    self.choice.pack(side='top')
    self.choice2 = tkin.Frame(self.clock)
    self.backha = tkin.Button(self.choice2,text='To Hallway',command = self.clocktohall)
    self.backhe = tkin.Button(self.choice2,text='To Garden',command= self.clocktohedge)
    self.backha.pack(side='left')
    self.backhe.pack(side='left')
    self.choice2.pack(side='top')
  #Displays the time to the player using the output text in the clock room
  def timesee(self):
    global picheck
    #Checks time.
    #Learnt on: www.programiz.com
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    self.out.set('Pi Clock Time: '+current_time)
    #Opens the pi secret if the time is 3:14 or if the time button has been clicked 314 times in the same visit to the window
    if picheck == 314 or current_time == '03:14' or current_time == '3:14':
      self.pi()
    else:
      picheck += 1
  #Sends user to the grail room from the clock room
  def clocktograil(self):
    #Resets the picheck variable
    global picheck
    picheck = 0
    self.clock.destroy()
    self.grail()
  #Sends user to the hallway room from the clock room
  def clocktohall(self):
    #Resets the picheck variable
    global picheck
    picheck = 0
    self.clock.destroy()
    self.hallway()
  #Sends user to the hedge garden room from the clock room
  def clocktohedge(self):
    #Resets the picheck variable
    global picheck
    picheck = 0
    self.clock.destroy()
    self.hedge()
  #The pi secret window
  def pi(self):
    #Sets the window attributes and the background image
    global pis
    pis = True
    self.pie = tkin.Toplevel(self.start)
    self.pie.iconphoto(False, self.icon2)
    self.pie.title('PI')
    self.pie.geometry('200x200')
    self.photo = tkin.Frame(self.pie)
    self.secret2 = tkin.PhotoImage(file = "Pi.png")
    self.background = tkin.Label(self.photo,image=self.secret2)
    self.background.pack()
    self.photo.pack()
  #The Grail room
  def grail(self):
    #Sets the window attributes and the background image
    self.cave = tkin.Toplevel(self.start)
    self.cave.iconphoto(False, self.icon)
    self.cave.title('Hidden Cave')
    self.cave.geometry('400x460')
    self.photo = tkin.Frame(self.cave)
    self.cup = tkin.PhotoImage(file = 'Grail.png')
    self.background = tkin.Label(self.photo,image=self.cup)
    self.background.pack()
    self.photo.pack()
    self.out = tkin.StringVar()
    self.out.set('Cave Room')
    self.text = tkin.Label(self.cave,textvariable=self.out)
    self.text.pack(side='top')
    self.choice = tkin.Frame(self.cave)
    self.back = tkin.Button(self.choice,text='Back Up',command = self.grailtoclock)
    self.keycup = tkin.Button(self.choice,text='Reach In Grail',command = self.getkey)
    self.light = tkin.Button(self.choice,text='Cave Light',command=self.grailtosplit)
    self.back.pack(side='left')
    self.keycup.pack(side='left')
    self.light.pack(side='left')
    self.choice.pack(side='top')
  #Sends user from the grail to the clock room
  def grailtoclock(self):
    self.cave.destroy()
    self.clocks()
  #Gives the user a key
  def getkey(self):
    global key
    key+=1
    self.out.set('Key Got From Grail')
    self.update()
  #Sends user from the grail to the road split
  def grailtosplit(self):
    self.cave.destroy()
    self.split()
  #The road split
  def split(self):
    #Sets the window attributes
    self.path = tkin.Toplevel(self.start)
    self.path.iconphoto(False, self.icon)
    self.path.title('Road Split')
    self.path.geometry('200x120')
    self.out = tkin.StringVar()
    self.out.set('Road With Two Paths')
    self.text = tkin.Label(self.path,textvariable=self.out)
    self.text.pack(side='top')
    self.up = tkin.Button(self.path,text='Go Up The Stairs',command=self.splittocloset)
    self.door = tkin.Button(self.path,text='Enter Door',command=self.splittoman)
    self.back = tkin.Button(self.path,text='Go Back To The Cave',command=self.blocked)
    self.up.pack(side='top')
    self.door.pack(side='top')
    self.back.pack(side='top')
  #Sends the user from the road split to the closet room
  def splittocloset(self):
    self.path.destroy()
    self.closet()
  #Sends the user from the road split to the closet room
  def splittoman(self):
    self.path.destroy()
    self.house()
  #Tells the user that the way back is blocked via the text box in split
  def blocked(self):
    self.out.set('Door Is Blocked By Rocks')
  
  def candy(self):
    #Sets the window attributes
    self.bowl = tkin.Toplevel(self.start)
    self.bowl.title('Candy Bowl')
    self.bowl.geometry('400x460')
    self.bowl.iconphoto(False, self.icon)
    #Initializes and packs the bowl image
    self.image = tkin.Frame(self.bowl)
    self.bg3 = tkin.PhotoImage(file = "Candy.png")
    self.bg4 = tkin.PhotoImage(file = "SpilledCandy.png")
    if bowldown == True:
      self.candybowl = tkin.Label(self.image,image=self.bg4)
    else:
      self.candybowl = tkin.Label(self.image,image=self.bg3)
    self.candybowl.pack(side='top')
    self.image.pack(side='top')
    #Initializes and packs the interaction text
    self.textframe = tkin.Frame(self.bowl)
    self.guilt = tkin.StringVar()
    self.guilt.set('Candy Bowl: Take One')
    self.text = tkin.Label(self.textframe,textvariable=self.guilt)
    self.text.pack()
    self.textframe.pack()
    #Initializes and packs choice buttons
    self.choice = tkin.Frame(self.bowl)
    self.back = tkin.Button(self.choice,text='Toll Road',command=self.candytotoll)
    self.crys = tkin.Button(self.choice,text='Take One Candy',command=self.getcandy)
    self.pickup = tkin.Button(self.choice,text='Pick Up Bowl',command=self.bowlup)
    self.back.pack(side='left')
    self.crys.pack(side='left')
    self.pickup.pack(side='left')
    self.choice.pack(side='top')
    if bowldown == False:
      self.pickup.pack_forget()
  #Sends the user to the toll road from the candy bowl and resets the candy now variable
  def candytotoll(self):
    global candynow
    self.bowl.destroy()
    candynow = 0
    self.tollroad()
  #Gives the user 1 candy and diplays text if they take more than one during that visit
  def getcandy(self):
    global candy
    global candynow
    global bowldown
    if candynow == 0 and bowldown == False:
      self.guilt.set('You Take One')
      candynow += 1
      candy += 1
      self.update()
    elif candynow == 1 and bowldown == False:
      self.guilt.set('You Take Another... Disgusting')
      candynow += 1
      candy += 1
      self.update()
    elif candynow == 2 and bowldown == False:
      self.guilt.set('y o u f e e l s i n s g o d o w n y o u r b a c k')
      candynow += 1
      candy += 1
      self.update()
    elif candynow == 3 and bowldown == False:
      self.guilt.set('You Took Too Many And The Bowl Fell')
      self.candybowl.configure(image=self.bg4)
      self.pickup.pack(side='left')
      bowldown = True
      candynow += 1
      candy += 1
      self.update()
    elif candynow == 4 or bowldown == True:
      self.guilt.set("LOOK AT WHAT YOU'VE DONE!!!")
  #Sets the bowl back up if over then hides the button used for the command
  def bowlup(self):
    global candynow
    global bowldown
    candynow = 0
    bowldown = False
    self.guilt.set("You pick up the bowl that's painted like a moon")
    self.candybowl.configure(image=self.bg3)
    self.pickup.pack_forget()
  #The House Window
  def house(self):
    #Sets the window attributes and the background image
    self.man = tkin.Toplevel()
    self.man.title("Person's House")
    self.man.geometry('400x460')
    self.man.iconphoto(False, self.icon)
    self.image = tkin.Frame(self.man)
    self.bg3 = tkin.PhotoImage(file = "Npc1.png")
    self.background = tkin.Label(self.image,image=self.bg3)
    self.background.pack(side='top')
    self.image.pack(side='top')
    #Initializes the npc's speach
    self.textframe =tkin.Frame(self.man)
    self.talk = tkin.StringVar()
    self.talk.set('Why are you in my house?!?')
    self.speach = tkin.Label(self.textframe,textvariable=self.talk)
    self.speach.pack(side='top')
    self.textframe.pack(side='top')
    #The window choices
    self.choice = tkin.Frame(self.man)
    self.back = tkin.Button(self.choice,text='To Split',command=self.mantosplit)
    self.trade = tkin.Button(self.choice,text='Trade Candy for Battery',command=self.battery)
    self.pastman = tkin.Button(self.choice,text='Run Past Man',command=self.mantohedge)
    self.back.pack(side='left')
    self.trade.pack(side='left')
    self.pastman.pack(side='left')
    self.choice.pack(side='top')
  #Sends user to the road split from the house
  def mantosplit(self):
    self.man.destroy()
    self.split()
  #Gives the player a battery in exchange for a candy
  def battery(self):
    global battery
    global candy
    if candy > 0:
      candy -= 1
      battery += 1
      self.talk.set('Thanks for the candy... want a battery?')
      self.update()
    else:
      self.talk.set("What are you trying to give me?")
  #Sends the player to the hedge garden from the house
  def mantohedge(self):
    self.man.destroy()
    self.hedge()
  #The closet room
  def closet(self):
    #Sets the window attributes and the background image
    self.room = tkin.Toplevel(self.start)
    self.room.title("Person's House")
    self.room.geometry('400x460')
    self.room.iconphoto(False, self.icon)
    self.image = tkin.Frame(self.room)
    self.bg3 = tkin.PhotoImage(file = "Closet.png")
    self.background = tkin.Label(self.image,image=self.bg3)
    self.background.pack(side='top')
    self.image.pack(side='top')
    self.textframe =tkin.Frame(self.room)
    self.coattext = tkin.StringVar()
    self.coattext.set('Closet Room')
    self.coatdisplay = tkin.Label(self.textframe,textvariable=self.coattext)
    self.coatdisplay.pack(side='top')
    self.textframe.pack(side='top')
    self.choice = tkin.Frame(self.room)
    self.back = tkin.Button(self.choice,text='To Split',command = self.closettosplit)
    self.coat = tkin.Button(self.choice,text='Take or Put Back Coat',command=self.takeorleave)
    self.door = tkin.Button(self.choice,text='Through Door',command=self.closettolab)
    self.back.pack(side='left')
    self.coat.pack(side='left')
    self.door.pack(side='left')
    self.choice.pack(side='top')
  #Send the player to the road split from the closet room
  def closettosplit(self):
    self.room.destroy()
    self.split()
  #Gives the user a coat if they dont have one 
  #or takes it away if they do
  def takeorleave(self):
    global coat
    if coat:
      coat = False
      self.coattext.set('You Put The Coat Back')
    else:
      coat = True
      self.coattext.set('You Put On A Coat')
  #Sends the user to the laboratory from the closet room
  def closettolab(self):
    self.room.destroy()
    self.laboratory()
  #The laboratory window
  def laboratory(self):
    #Sets the window attributes and the background image
    self.lab = tkin.Toplevel(self.start)
    self.lab.title("Volcano Laboratory")
    self.lab.geometry('400x460')
    self.lab.iconphoto(False, self.icon)
    self.image = tkin.Frame(self.lab)
    self.bg3 = tkin.PhotoImage(file = "Laboratory.png")
    self.background = tkin.Label(self.image,image=self.bg3)
    self.background.pack(side='top')
    self.image.pack(side='top')
    self.text = tkin.StringVar()
    self.text.set('Labortatory')
    self.infolabel = tkin.Label(self.lab,textvariable=self.text)
    self.infolabel.pack(side='top')
    #Choice buttons for Window
    self.choice = tkin.Frame(self.lab)
    self.back = tkin.Button(self.choice,text='Back to Room',command = self.labtocloset)
    self.teleport = tkin.Button(self.choice,text='Use Machine',command=self.randomlocal)
    self.foreward = tkin.Button(self.choice,text='Volcano',command = self.labtolava)
    self.back.pack(side='left')
    self.teleport.pack(side='left')
    self.foreward.pack(side='left')
    self.choice.pack(side='top')
  #Send the user to the closet room from the volcano lab
  def labtocloset(self):
    self.lab.destroy()
    self.closet()
  #Sends the user to a random room from the volcano lab
  def randomlocal(self):
    local = random.randint(1,10)
    if local == 1:
      self.lab.destroy()
      self.hallway()
    elif local == 2:
      self.lab.destroy()
      self.moon()
    elif local == 3:
      self.lab.destroy()
      self.hedge()
    elif local == 4:
      self.lab.destroy()
      self.clocks()
    elif local == 5:
      self.lab.destroy()
      self.grail()
    elif local == 6:
      self.lab.destroy()
      self.candy()
    elif local == 7:
      self.lab.destroy()
      self.house()
    elif local == 8:
      self.lab.destroy()
      self.closet()
    elif local == 9:
      self.lab.destroy()
      self.volcano()
    elif local == 10:
      self.text.set('The Machine Sends You Here Again.')
  #Sends the player to the volcano from the lab
  def labtolava(self):
    global coat
    if coat == True:
      self.text.set("It's Too Hot To Enter With A Coat!!!")
    else:
      self.lab.destroy()
      self.volcano()
  #The volcano Window
  def volcano(self):
    #Sets the window attributes and the background image
    self.lava = tkin.Toplevel(self.start)
    self.lava.title("The Volcano")
    self.lava.geometry('400x460')
    self.lava.iconphoto(False, self.icon)
    self.image = tkin.Frame(self.lava)
    self.bg3 = tkin.PhotoImage(file = "Volcano.png")
    self.background = tkin.Label(self.image,image=self.bg3)
    self.background.pack(side='top')
    self.image.pack(side='top')
    self.text = tkin.StringVar()
    self.text.set('Volcano')
    self.infotext = tkin.Label(self.lava,textvariable=self.text)
    self.infotext.pack(side='top')
    #Choice buttons for Window
    self.choice = tkin.Frame(self.lava)
    self.back = tkin.Button(self.choice,text='Back to Lab',command = self.lavatolab)
    self.endingdoor = tkin.Button(self.choice,text='Use Left Door',command=self.lavatoending)
    self.secrets = tkin.Button(self.choice,text='Use Right Door',command = self.lavasecret)
    self.back.pack(side='left')
    self.endingdoor.pack(side='left')
    self.secrets.pack(side='left')
    self.choice.pack(side='top')
  #Sends the user to the lab from the volcano
  def lavatolab(self):
    self.lava.destroy()
    self.laboratory()
  #Checks for secrets obtained and gives one of two endings
  def lavatoending(self):
    global moons
    global pis
    global colds
    global crystal
    if crystal >= 3:
      #crystal -= 3
      #if moons == True and colds == True and pis == True:
        self.lava.destroy()
        self.lightphoto()
      #else:
        #self.lava.destroy()
        #self.inven.destroy()
        #self.ending()
    else:
      self.text.set('The Door is Locked by 3 Crystal Slots.')
  #Opens the tundra window ONLY if the user is wearing a coat
  def lavasecret(self):
    global coat
    if coat == True:
      self.tundra()
    else:
      self.text.set("It's Too Cold In There!!!")
  #The tundra secret
  def tundra(self):
    #Sets the window attributes and the background image
    global colds
    colds = True
    self.cold = tkin.Toplevel(self.start)
    self.cold.iconphoto(False, self.icon2)
    self.cold.title('TUNDRA')
    self.cold.geometry('200x200')
    self.photo = tkin.Frame(self.cold)
    self.secret3 = tkin.PhotoImage(file = "Tundra.png")
    self.background = tkin.Label(self.photo,image=self.secret3)
    self.background.pack()
    self.photo.pack()
  #The ending Window
  def ending(self):
    #Sets the window attributes and the background image
    self.end = tkin.Toplevel(self.start)
    self.end.title("The Ending")
    self.end.geometry('400x420')
    self.end.iconphoto(False, self.icon)
    self.image = tkin.Frame(self.end)
    self.bg3 = tkin.PhotoImage(file = "AnEnding1.png")
    self.background = tkin.Label(self.image,image=self.bg3)
    self.background.pack(side='top')
    self.image.pack(side='top')
    self.infotext = tkin.Label(self.end,text='THE END')
    self.infotext.pack(side='top')
    i = open('savefile.dat','wb')
    i.close()
  #The save & quit room
  def saveroom(self):
    #Sets the save variable to 0
    global area
    area = 0
    #Sets the window attributes and the background image
    self.save = tkin.Toplevel(self.start)
    self.save.title("Save")
    self.save.geometry('400x460')
    self.save.iconphoto(False, self.icon)
    self.image = tkin.Frame(self.save)
    self.bg3 = tkin.PhotoImage(file = "SaveRoom.png")
    self.background = tkin.Label(self.image,image=self.bg3)
    self.background.pack(side='top')
    self.image.pack(side='top')
    self.text = tkin.StringVar()
    self.text.set('Save Book')
    self.infotext = tkin.Label(self.save,textvariable=self.text)
    self.infotext.pack(side='top')
    #Choice buttons for Window
    self.choice = tkin.Frame(self.save)
    self.back = tkin.Button(self.choice,text='Back To Garden',command = self.savetogarden)
    self.savegame = tkin.Button(self.choice,text='Save',command=self.savefunction)
    self.exitgame = tkin.Button(self.choice,text='Quit',command = self.quitgame)
    self.back.pack(side='left')
    self.savegame.pack(side='left')
    self.exitgame.pack(side='left')
    self.choice.pack(side='top')
  #Sends the user to the garden from the save book
  def savetogarden(self):
    self.save.destroy()
    self.hedge()
  #Saves the game for the user
  def savefunction(self):
    #Calls all inventory variables as global
    global candy
    global battery
    global key
    global crystal
    global coat
    global area
    global moons
    global pis
    global colds
    #Opens a data file to save data to
    i = open('savefile.dat','wb')
    #Sets a dictionary to save
    savedata = {}
    savedata['key'] = key
    savedata['candy'] = candy
    savedata['battery'] = battery
    savedata['crystal'] = crystal
    savedata['coat'] = coat
    savedata['area'] = area
    savedata['moon'] = moons
    savedata['pi'] = pis
    savedata['cold'] = colds
    #Pickles the data
    pickle.dump(savedata,i)
    i.close()
    self.text.set('{GAME SAVED}')

  #Closes the Game
  def quitgame(self):
    self.start.destroy()
  #Loads the save data if there is any
  def getdata(self):
    #Globalizes all inventory variables
    global candy
    global battery
    global key
    global crystal
    global coat
    global area
    global moons
    global pis
    global colds
    #Open file for binary reading
    inputfile = open('savefile.dat','rb')
    #Unpickle the next object
    savedata = pickle.load(inputfile)
    #Sets all inventory variables and runs the updat function
    candy = savedata['candy']
    battery = savedata['battery']
    key = savedata['key']
    crystal = savedata['crystal']
    coat = savedata['coat']
    area = savedata['area']
    moons = savedata['moon']
    pis = savedata['pi']
    colds = savedata['cold']
    self.update()
    #Close the file
    inputfile.close()
  #The darkroom window
  def lightphoto(self):
    self.light = True
    #Sets the window attributes and the background image
    self.dark = tkin.Toplevel(self.start)
    self.dark.title("Photo Room")
    self.dark.geometry('400x460')
    self.dark.iconphoto(False, self.icon)
    self.image = tkin.Frame(self.dark)
    self.bg3 = tkin.PhotoImage(file = "BrightDarkroom.png")
    self.background = tkin.Label(self.image,image=self.bg3)
    self.background.pack(side='top')
    self.image.pack(side='top')
    self.infotext = tkin.Label(self.dark,text='The Darkroom')
    self.infotext.pack(side='top')
    #Choice buttons for Window
    self.choice = tkin.Frame(self.dark)
    self.door = tkin.Button(self.choice,text='Go Trough Door',command = self.darktoalley)
    self.lights = tkin.Button(self.choice,text='Toggle Light',command=self.lighttoggle)
    self.tablelight = tkin.Button(self.choice,text='Look at Light',command = self.darktophoto)
    self.door.pack(side='left')
    self.lights.pack(side='left')
    self.tablelight.pack(side='left')
    self.choice.pack(side='top')
    self.tablelight.pack_forget()
  #Sends the user to the alleyway from the darkroom
  def darktoalley(self):
    print('[UNFINISHED COMMAND]')
  #Toggles the image and visibility of a button
  def lighttoggle(self):
    if self.image == True:
      img2 = tkin.PhotoImage(file = 'DarkDarkroom.png')
      self.background.configure(image=img2)
      self.background.image = img2
      self.image = False
      self.tablelight.pack(side='left')
    else:
      self.background.configure(image=self.bg3)
      self.image = True
      self.tablelight.pack_forget()
  #Either sends the user to the photo from the darkroom or opens the negetive secret
  def darktophoto(self):
    print('[UNFINISHED COMMAND]')
  


#print('[UNFINISHED COMMAND]')
#For unfinished things /\
#Makes an instance of the Game GUI
gamestart = Game()