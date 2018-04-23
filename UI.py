import tkinter as ttk
#disallow same team to be picked
    
def setup():
    #Create Tk object
    root = ttk.Tk()
    root.title("Choose Features")


    #Setup Window
    window = ttk.Frame(root)
    window.grid(column=0,row=0)
    window.columnconfigure(0, weight = 1)
    window.rowconfigure(0, weight = 1)
    window.pack(pady = 20, padx = 20)
     
    #Setup Boxes
    hteam = ttk.StringVar(root)
    vteam = ttk.StringVar(root)
    day = ttk.StringVar(root)
    time = ttk.StringVar(root)

    teams = []
    teamDict = {}
    teams = []
    with open("teamCodeList.txt") as file:
        for line in file:
            e = line.strip().split(" = ")
            teams.append(e[1])
            teamDict[e[1]] = e[0]
            
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    times = ['Day','Night']

    #Set Default Options
    hteam.set("Home Team")
    vteam.set('Visiting Team') 
    day.set('Day of the Week')
    time.set('Time of Game')

    #create dropdown boxes
    hteamMenu = ttk.OptionMenu(window, hteam, *teams)
    ttk.Label(window, text="Home Team").grid(row = 1, column = 1)
    hteamMenu.grid(row = 1, column =3)

    vteamMenu = ttk.OptionMenu(window, vteam, *teams)
    ttk.Label(window, text="Visiting Team").grid(row = 2, column = 1)
    vteamMenu.grid(row = 2, column =3)

    dayMenu = ttk.OptionMenu(window, day, *days)
    ttk.Label(window, text="Day of the Week").grid(row = 3, column = 1)
    dayMenu.grid(row = 3, column =3)

    timeMenu = ttk.OptionMenu(window, time, *times)
    ttk.Label(window, text="Time of Game").grid(row = 4, column = 1)
    timeMenu.grid(row = 4, column =3)

    ttk.Label(window, text = "").grid(row = 6,column = 2)

    def avoid_same_team(*args):
        tempTeams = teams[:teams.index(hteam.get())]+teams[teams.index(hteam.get())+1:]
        vteamMenu = ttk.OptionMenu(window, vteam, *tempTeams)
        ttk.Label(window, text="Visiting Team").grid(row = 2, column = 1)
        vteamMenu.grid(row = 2, column =3)

    def avoid_same_team2(*args):
        tempTeams = teams[:teams.index(vteam.get())]+teams[teams.index(vteam.get())+1:]
        hteamMenu = ttk.OptionMenu(window, hteam, *tempTeams)
        ttk.Label(window, text="Home Team").grid(row = 1, column = 1)
        hteamMenu.grid(row = 1, column =3)

    hteam.trace('w', avoid_same_team)
    vteam.trace('w', avoid_same_team2)

    return root, window, [hteam,vteam,day,time], [teams,days,times], teamDict

def checkValues(values, choices:
    return values[0] not in choices[0] or values[1] not in choices[0] or values[2] not in choices[1] or values[3] not in choices[2]

root, window, objects, choices, teamDict = setup()

#When button is pressed
def do_stuff(*args):
    values = [objects[0].get(),objects[1].get(),objects[2].get(),objects[3].get()]
    if checkValues(values,choices):
        label = ttk.Label(window, text="Must Select All Boxes")# if not selected something
        label.place(x=60,y=150)
        return
    print(teamDict[values[0]], teamDict[values[1]], values[2][:3],values[3][:1]) #Do Regression Here
    root.destroy()

#create button to confirm answers
button = ttk.Button(window, text="OK",command=do_stuff)
button.grid(row = 5, column = 2)

root.mainloop()

