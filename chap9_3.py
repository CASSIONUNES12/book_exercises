import csv

with open("movies.csv", "w", newline='') as f:
    m = csv.writer(f, delimiter=",")
    m.writerow(["Top Gun", "Risky Business", "Minority Report"])
    m.writerow(["Titanic", "The Revenant", "Inception"])
    m.writerow(["Training Day", "Man on Fire", "Flight"])