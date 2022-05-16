'''
A demonstration of how well I understood the basic syntax and semantics of the Python programming language
by computing for the general weighted average of a user based on their input of grades and units for one
semester with only 5 subjects allowed to be enrolled, as well as using what a university in the Philippines
use as their grading scale and latin grade honor range for reference.
'''

print("This program computes your General Weighted Average (GWA) on 5 subjects for a whole semester.")
grade1 = float(input("\nEnter grade:\n"))
units1 = float(input("Enter number of units:\n"))

grade2 = float(input("Enter grade:\n"))
units2 = float(input("Enter number of units:\n"))

grade3 = float(input("Enter grade:\n"))
units3 = float(input("Enter number of units:\n"))

grade4 = float(input("Enter grade:\n"))
units4 = float(input("Enter number of units:\n"))

grade5 = float(input("Enter grade:\n"))
units5 = float(input("Enter number of units:\n"))

total_units = units1 + units2 + units3 + units4 + units5
GWA = ((grade1 * units1) + (grade2 * units2) + (grade3 * units3) + (grade4 * units4) + (grade5 * units5)) / total_units
print("GWA:", GWA)

if GWA <= 1.20:
    print("If you can maintain your GWA, you can graduate summa cum laude.")
elif GWA > 1.20 and GWA <= 1.45:
    print("If you can maintain your GWA, you can graduate magna cum laude.")
elif GWA <= 1.75 and GWA > 1.45:
    print("If you can maintain your GWA, you can graduate cum laude.")
else:
    print("Improve your GWA to receive latin honors.")