"""
Oasis Project
"""


import pandas as pd

from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonallplayers

all_players = commonallplayers.CommonAllPlayers(is_only_current_season=1)

# Get the data frame containing information about all players
all_players_data = all_players.get_data_frames()[0]

# Extract the player names from the data frame
all_players = all_players_data['DISPLAY_FIRST_LAST'].tolist()


def get_id():
    """
    Gets the player id based on the inputted player name, returns a list of 
    the ids for each player
    """
    
    team_ids = []
    player_names = []
    
    total_players = 0
    
    # While loop should be <= 13 for each player, might need to find a better way for input
    # while total_players <= 0:
    #       player_dictionary = players.find_players_by_full_name(input("Who is a player on your team you want to compare?\n"))
    #       # team_ids.append(player_dictionary[0]["id"])
    #       # player_names.append(player_dictionary[0]["full_name"])
    #       total_players += 1
          
    # if player_dictionary in all_players:
    #     team_ids.append(player_dictionary[0]["id"])
    #     player_names.append(player_dictionary[0]["full_name"])
    # else:
    #     print("wrong")
        
    while True:
        player_input = input("Enter the name of an NBA player: \n")
        if player_input in all_players:
            player_dictionary = players.find_players_by_full_name(player_input)
            print("Player found:", player_input)
            team_ids.append(player_dictionary[0]["id"])
            player_names.append(player_dictionary[0]["full_name"])
            break 
        else:
            print("Player not found. Please enter a valid NBA player.")
            # Prompt for another input
            continue
 
    return team_ids, player_names
    
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

                                      

def get_stats(dataframes):
    """
    Given a list of dataframes returns a dataframe of the averages of each
    statistic that affects players fantasy points for all players
    """

  
    # df_current_season = []
    
    
    for df in dataframes:
        current_season_data = df.iloc[-1]
        games_played = current_season_data['GP']
        points = current_season_data['PTS']
        rebounds = current_season_data['REB']
        assists = current_season_data['AST']
        blocks = current_season_data['BLK']
        steals = current_season_data['STL']
        turnovers = current_season_data['TOV']
        fg_made = current_season_data['FGM']
        fg_attempted = current_season_data['FGA']
        fg_missed = fg_attempted - fg_made
        
        
        data_frame = {
"Points" : [round(points/games_played, 1)], "Rebounds" : [round(rebounds/games_played, 1)],
"Assists" : [round(assists/games_played, 1)], "Blocks" : [round(blocks/games_played, 1)], 
"Steals" : [round(steals/games_played, 1)], "Turnovers" : [round(turnovers/games_played, 1)],
"FG Missed" : [round(fg_missed/games_played, 1)]

}
    
        df = pd.DataFrame(data_frame)
        
        
        # df_current_season.append(df)
        
        {"Jayson Tatum": df, "Jaylen Brown": df}
        

    return df
        
        
        
def main():
    
     # list of team_ids and player names
     team_ids1, player_names1 = get_id()
     team_ids2, player_names2 = get_id()
    
     # Career statistics dataframe
     player_dataframes1 = find_player(team_ids1)
     player_dataframes2 = find_player(team_ids2)
    # print(player_dataframes)
    
     # Current season statistic dataframe
     season_data1 = get_stats(player_dataframes1)
     season_data2 = get_stats(player_dataframes2)
     print(season_data1)
     print(season_data2)



if __name__ == "__main__":
        main()









    
