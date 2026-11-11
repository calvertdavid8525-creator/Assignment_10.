#import csv file
import pandas as pd
cfb_data = pd.read_csv("cfb.csv")
print(cfb_data)

#validate season choice
valid_season = False
while valid_season == False:
    user_season_choice = int(input("Choose a season to analyze: "))
    if user_season_choice >= 2013 and user_season_choice <= 2020:
        valid_season = True
    else:
        input("Invalid Season. Try again: ")

#organize teams into how many wins they had in the chosen year
    season_data = cfb_data[cfb_data["Season"]== user_season_choice][["Season", "Team", "Win"]]

    wins_10 = season_data.query("Win >= 10")[["Season", "Team", "Win"]]
    wins_89 = season_data.query("Win >= 8 and Win < 10")[["Season", "Team", "Win"]]
    wins_67 = season_data.query("Win >= 6 and Win < 8")[["Season", "Team", "Win"]]
    wins_under6 = season_data.query("Win < 6")[["Season", "Team", "Win"]]

#print results
print(f"Results for the {user_season_choice}season. ")
print()

print("10+ Wins")
print(wins_10)
print()

print("8-9 Wins")
print(wins_89)
print()

print("6-7 Wins")
print(wins_67)
print()

print("Under 6 Wins")
print(wins_under6)
print()
