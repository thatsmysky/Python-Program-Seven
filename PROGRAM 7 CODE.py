# Lucy Kull
# CS 101
# Professor Hare
# Program 7 Algorithm

Incidents_Dict = {}
Arrests_Dict = {}
Offense_Dict = {}
End_Dict = {}
End_List = {}
Correct_Inputs = ["1", "2", "Q"]


def try_open(file):
    try:
        open(file)
    except IOError:
        print("ioerror")
        return False
    except:
        print("wtf")
        return False
    return True


def read_incident_file(file):
    readfile = open(file, 'r')
    readfile.readline()
    # For each line, build dictionary of zip: number of incidents
    for line in readfile:
        line = line.split(",")
        # If the zip is 0 or not there, zip = 99999
        if line[4] == "\n" or line[4] == "0":
            line[4] = 99999
        line[4] = int(line[4])
        if line[4] in Incidents_Dict.keys():
            Incidents_Dict[line[4]] += 1
        else:
            Incidents_Dict[line[4]] = 1
    # Ordered numerically
    # Output 2 columns; Zip, number of crimes in zip
    print('{0:<10} {1:>12}'.format("Zipcode", "Crimes"))
    print("=======================")
    for k in sorted(Incidents_Dict.keys()):
        print('{0:<10} {1:>12}'.format(k, Incidents_Dict[k]))


def read_detail_file(file):
    readfile = open(file, 'r')
    readfile.readline()
    # Sort each line into a dictionary; report number, involvement
    for line in readfile:
        line = line.split(",")
        line[0] = int(line[0])
        if line[0] in Arrests_Dict.keys():
            Arrests_Dict[line[0]] += 1
        else:
            Arrests_Dict[line[0]] = 1


def read_offenses_file(file):
    # Open incidents file
    incidents = open("incidents.csv")
    readfile = open(file)
    # Iterate through file
    incidents.readline()
    for line in incidents:
        line = line.split(",")
        line[0] = int(line[0])
        line[3] = int(line[3])
        Offense_Dict[line[0]] = line[3]
    # For each Report number in Arrests dictionary, replace with Offence number of report
    readfile.readline()
    for line in readfile:
        line = line.split(",")
        line[0] = int(line[0])
        line[1] = line[1].strip()
        End_Dict[line[0]] = 0
        End_List[line[0]] = line[1]
    # For each Offence number now in Details dictionary, replace with Description in offenses
    for k in Offense_Dict.keys():
        End_Dict[Offense_Dict[k]] += Arrests_Dict[k]
    Final_Dict = dict((End_List[key], value) for (key, value) in End_Dict.items())
    Last_Dict = {Final_Dict[v]: v for v in Final_Dict}
    # Ordered by number of victims (highest to lowest)
    # Output 2 columns; Description, Number of victims
    print('{0:<25} {1:>12}'.format("Offense", "Victims"))
    print("======================================")
    for k in sorted(Last_Dict.keys(), reverse=True):
        print('{0:<25} {1:>12}'.format(Last_Dict[k], k))


Running = True
while Running:
    # Display menu: Summary by Zip, Victim Count by Offense Type, and Quit
    print("\nKCPD CRIME STATISTICS \n")
    print("1.  Summary by Zipcode")
    print("2.  Victim Count by Offence Type")
    print("Q.  Quit")
    RunProgram = input("---> ")
    RunProgram = RunProgram.upper()
    # If they don’t choose one, ask again
    if "Q" in RunProgram:
        break
    if RunProgram not in Correct_Inputs:
        print("you're bad at this")
        continue
    if "1" in RunProgram:
        # Summary of Zip:
        if not try_open("incidents.csv"):
            # Try to open, if error warn and quit
            print("I'm sorry, there was an error \n")
            break
        # Open incidents.csv
        if try_open("incidents.csv"):
            # Iterate through file
            read_incident_file("incidents.csv")

    if "2" in RunProgram:
        # Victim Count:
        if not try_open("details.csv"):
            # Try to open, if error warn and quit
            print("I'm sorry, there was an error")
            break
        # Open Details.csv
        if try_open("details.csv"):
            # Iterate through file
            read_detail_file("details.csv")
        if not try_open("offenses.csv"):
            # Try open, if error warn and quit
            print("I'm sorry, there was an error")
            break
        if not try_open("offenses.csv"):
            print("I'm sorry, there was an error")
            break
        # Open offenses.doc
        if try_open("offenses.csv"):
            # Iterate through file
            read_offenses_file("offenses.csv")
