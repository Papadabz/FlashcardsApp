import csv

with open("cards.csv") as f:
    reader = csv.reader(f)
    next(reader) #skip header
    for row in reader:
        print("Q:", row[0])
        input("Press Enter to see the answer...")
        print("A:", row[1])
        
