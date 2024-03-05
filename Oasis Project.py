"""
Oasis Project
"""


import pandas as pd

from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players


def get_id():
    """
    Gets the player id based on the inputted player name, returns a list of 
    the ids for each player
    """
    
    team_ids = []
    
    total_players = 0
    
    # While loop should be <= 13 for each player, might need to find a better way for input
    while total_players <= 1:
          player_dictionary = players.find_players_by_full_name(input("Whos is a player on your team?\n"))
          team_ids.append(player_dictionary[0]["id"])
          total_players += 1
         
    return team_ids

    


def find_player(team_ids):
    """
    Takes in the player id and returns the data frame with all stats from 
    all years played in the NBA

    """
    dataframes = []
    
    for player_ids in team_ids:
        career = playercareerstats.PlayerCareerStats(player_id = player_ids)
        df = career.get_data_frames()[0]
        dataframes.append(df)
        
    return dataframes




# def get_stats(player_id):
#     """
    
#     """
    
#     row_index = 8
#     column_name = 'GP'
#     points = "PTS"
#     assists = "AST"
#     rebounds = "REB"
#     blocks = "BLK"
#     steals = "STL"
#     turnover = "TOR"
#     fg_made = "FGM"
#     fg_attempted = "FGA"
#     fg_missed = fg_attempted = fg_made

        
        
        
def main():
    
    team_ids = get_id()
    

    player_dataframes = find_player(team_ids)
    print(player_dataframes)



if __name__ == "__main__":
        main()









    