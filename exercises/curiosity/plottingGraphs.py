"""
 Step 1 - First you would run  this command in shell "pip install matplotlib".
 Step 2 - Take advantage of methods in the lib.
"""
import matplotlib.pyplot
print("\t\tPlotting  Graphics")
print()
Title = input("Insert what you will look.\nEx: Monthy Profit\n")
titleX = input("Enter with a description.\nEx: Months\n")
print()
titleY = input("Enter with a description.\nEx: Profit\n")

matplotlib.pyplot.title(Title)
coordX = [i for i in input(f"Enter with X({titleX}) axis coordinates: \n").split()]
coordY = [int(i) for i in input(f"Enter with Y({titleY}) axis coordinates: \n").split()]
matplotlib.pyplot.xlabel(titleX)
matplotlib.pyplot.ylabel(titleY)
matplotlib.pyplot.plot(coordX,coordY)
matplotlib.pyplot.show()
