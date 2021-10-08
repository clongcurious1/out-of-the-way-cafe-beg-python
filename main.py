#Imports
import math
import time
import webbrowser
#Variables
cc = 'Coffee-Cream.png'
bp = 'pancakes.png'
eb = 'eggs.png'
ft = 'frenchtoast.png'
oj = 'orange-juice.png'
st = 'sweet-tea.png'
#Functions
#Other situations
#Introduction
print("***WELCOME ADVENTURER!***")
time.sleep(1)
print('Before we begin, please make sure all browser windows are closed.')
time.sleep(2)
#About the Appalachian Trail
print('***ABOUT YOUR QUEST***')
print('You are hiking the Appalachian Trail.')
time.sleep(2)
print('//\\ //\\ //\\ //\\ //\\ //\\ //\\ //\\ //\\ //\\ //\\ //\\ //\\ //\\')
time.sleep(2)
print('The Appalachian Trail (AT) is 2200 miles long.')
time.sleep(3)
print('The Trail runs from Georgia to Maine.')
time.sleep(2)
print('***YOU ARE A THRU HIKER***')
print('Approximately 3,000 people visit sections of the trail each year.')
time.sleep(3)
print ('The most revered AT enthusiasts are the THRU HIKERS.')
time.sleep(3)
print('You are determined to hike through all FOURTEEN states.')
time.sleep(3)
print("You've trained for months to prepare for this journey.")
time.sleep(3)
print("You've got this!")
time.sleep(3)
#GeoLocation
print("***WHERE ARE YOU TODAY?***")
time.sleep(2)
print("Today, you're at Clingmans Dome, the highest point on the trail.")
time.sleep(3)
print('Elevation 6643 ft.')
time.sleep(3)
print('The nearest city is Gatlinburg, TN.')
time.sleep(3)
#About the Out of the Way Cafe
print("***FUELING THE MACHINE***")
time.sleep(2)
print('Breakfast is the most important meal of the day.')
time.sleep(2)
print("You're headed to the OUT OF THE WAY Café.")
time.sleep(3)
print('Your stomach is growling LOUDLY.')
time.sleep(2)
print("You're so hungry YOU COULD EAT A BEAR.")
time.sleep(3)
print('You walk in and take a seat at the counter.')
time.sleep(2)
print('You lean your backpack against the footrail.')
time.sleep(2)
print('Here comes the waitress.')
time.sleep(2)
#Meet Gladys
print("***MEET GLADYS***")
time.sleep(2)
print('Gladys has worked at the Out of the Way Café for decades.')
time.sleep(2)
print('Her face is as craggy as the mountains outside.')
time.sleep(2)
print('Her hair is a wreck, her uniform is wrinkled.')
time.sleep(2)
print('...but she has a kind smile.') 
time.sleep(2)
print('She pats her hair, then winks, and says:')
time.sleep(3)
#Server takes Hiker's drink order
print("Mornin' Glory! I'm Gladys.")
time.sleep(2) 
print('Welcome to the Out of the Way Café.')
time.sleep(2)
print("What can I get 'ya to wet your whistle?")
time.sleep(2)
print("We keep it pretty simple here.")
time.sleep(2)
print("The menu is LIMITED. I don't write anything down.")
time.sleep(3)
print('Your choices are coffee (cc), orange juice (oj), or sweet tea (st).')
time.sleep(2)
beverage = input("Place your order. Type cc, oj, or st: ")
time.sleep(2)
#PENDING validate answer
#TEXT - server gets beverage
print("Thanks, dear. I'll be right back with that.")
time.sleep(2)
print("Gladys walks down the counter, smiling and checking on her customers.")
time.sleep(3)
print('You rub the sleep out of your eyes and S-T-R-E-T-C-H.')
time.sleep(2)
print("In two shakes of a lamb's tail, Gladys is working her way back to you.")
time.sleep(2)
#TEST - Serve drink 
print("Here you go, sugar. That'll wake you right up!")
#Serve the beverage = display the right image 
if beverage == 'cc':
    webbrowser.open('Coffee-Cream.png')
elif beverage == 'oj':
    webbrowser.open('orange-juice.png')
else:
    webbrowser.open('sweet-tea.png')
time.sleep(4)
#PENDING How to stop statements from progressing until after brower window closes?
maintain = input('Type c to Continue or q to Quit: ')
if maintain == "c":
    #You're not from around here, are you?
    print("***SMALL TALK***")
    print('Gladys asks, "You are not from around here, are you?"')
    time.sleep(2)
    print('Nobody that comes through that door is local.')
    time.sleep(2)
    print("That's what happens when you open a diner next to the Appalachian Trail.")
    time.sleep(3)
    print("Everybody's just pasing through.") 
    time.sleep(2)
    print('So...where are you from?')
    time.sleep(2)
    print('CHOICE REQUIRED. Enter a for Albuquerque, b for Birmingham, or d for Detroit.')
    city= input("Answer the question. Type a or b or d: ")
    #PENDING validate answer
    time.sleep(2)
    if city == "a":
        print('Albuquergue! I love that place.')
        time.sleep(2)
        print('My Uncle Earl used to live out there.')
        time.sleep(2)
        print('We went to the Petroglyph National Monument.')
        time.sleep(2)
        print('I could not believe all those prehistoric drawings on the canyon walls.')
        time.sleep(2)
    elif city == 'b':
        print('Birmingham! I love that place.')
        time.sleep(2)
        print('My Aunt Alice used to live down there.')
        time.sleep(2)
        print('She was married to a man who worked in the steel industry.')
        time.sleep(2)
        print('When I was little, they took me on picnics to Vulcan Park on top of Red Mountain.')
        time.sleep(2)
    else:
        print('Detroit! I love that place.')
        time.sleep(2)
        print("My mother's best friend from nursing school was from Detroit.")
        time.sleep(2)
        print('She taught my mother how to dance...')
        time.sleep(2)
        print("She'd come to visit and we'd listen to records and have such a good time.")
        time.sleep(2)
    print('***YOU MUST BE FAMISHED***')
    time.sleep(2)
    print('Gladys sighs. "Listen to me, carrying on."')
    time.sleep(2)
    print("Meanwhile, you are WASTING AWAY right in front of my eyes.")
    time.sleep(2)
    print("What can I get you for breakfast this morning?")
    time.sleep(2)
    print('Remember, we keep it simple around here.')
    time.sleep(2)
    print('You can have eggs and bacon, french toast, or blueberry pancakes.')
    time.sleep(2)
    #Server takes Hiker's food order
    print('CHOICE REQUIRED. Enter eg for eggs, ft for french toast, or bp for pancakes.')
    time.sleep(2)
    food = input("Place your order. Type eg or ft or bp: ")
    time.sleep(2)
    #Validate response and proceed
    #Server leaves
    #Hiker waits for food
    #Hiker notes local weather looking out the window. Share Clingman rainforest precip stats.
    #Hiker checks weather back home
    #REQUIREMENT: Utilize data pulled from API 
    #Lost compass! Hiker inventories items stored in backpack. 
    #REQUIREMENT: Create list with multiple values, retrieve one value, use elsewhere in program
    #TEST - Serve food 
    print("Here you go, friend.")
    time.sleep(2)
    #Serve the beverage = display the right image 
    if food == 'eg':
        webbrowser.open('eggs.png')
    elif food == 'ft':
        webbrowser.open('frenchtoast.png')
    else:
        webbrowser.open('pancakes.png')
    time.sleep(4) 
    #PENDING How to stop statements from progressing until after brower window closes?
    maintain = input('Type c to Continue or q to Quit: ')
    if maintain == "c":
        print("Isn't that beautiful? I'll leave you to it.")
        time.sleep(2)
        print('Gladys walks away and checks on her other customers.')
        #While eating, Hiker checks local Tweets or keyword Appalachian Trail or Gatlinburg
        #Display Tweets in Terminal 
        #REQUIREMENT: import, read + display data from JSON file
        #REQUIREMENT: Visualize data in some fashion (WordCloud)
        #Server returns to clear plate
        #REQUIREMENT: Server remarks on item from list
        #How far are you going? Share Thru-Hiker stats. Will you be back this way? 
        #If YES, REQUIREMENT: countdown timer, and "Happy Trails, honey."
        #If NO, pay at the register and Happy Trails!