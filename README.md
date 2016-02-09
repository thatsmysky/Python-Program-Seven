# Python-Program-Seven
Summary of Crime Statistics based on input file
Program 7 Algorithm

Display menu: Summary by Zip, Victim Count by Offense Type, and Quit

  If they don’t choose one, ask again

Summary of Zip: 

Open incidents.csv

	Try to open, if error warn and quit

	Iterate through file

	For each line, build dictionary or zip: number of incidents

	If the zip is already in the dictionary, append

	If the zip is 0 or not there, zip = 99999

	Output 2 columns; Zip, number of crimes in zip

	Ordered numerically


Victim Count:

	Open Details.csv

	Try to open, if error warn and quit

	Iterate through file

	Sort each line into a dictionary; report number, involvement

	Open offenses.dox

	Try open, if error warn and quit

	Iterate through file

	Open incidents.csv

	Try open etc

	Iterate through file

	For each Report number in Details dictionary, replace with Offence number of report

	For each Offence number now in Details dictionary, replace with Description in offenses

	Output 2 columns; Description, Number of victims

	Ordered by number of victims (highest to lowest)
