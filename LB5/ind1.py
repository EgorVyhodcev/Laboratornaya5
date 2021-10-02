import sys

m = int(input("Enter the number of the season "))
if m < 1 or m > 4:
    print("Illegal value of m", file=sys.stderr)
    exit(1)
if m == 1:
    print("The winter months are: December, January and February")
elif m == 2:
    print("The spring months are: March, April and May")
elif m == 3:
    print("The summer months are: June, July and August")
else:
    print("The autumn months are: September, October and November")
