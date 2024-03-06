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
    player_names = []
    
    total_players = 0
    
    # While loop should be <= 13 for each player, might need to find a better way for input
    while total_players <= 1:
          player_dictionary = players.find_players_by_full_name(input("Whos is a player on your team?\n"))
          team_ids.append(player_dictionary[0]["id"])
          player_names.append(player_dictionary[0]["full_name"])
          total_players += 1
 
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

  
    df_current_season = []
    
    
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
        
        
        df_current_season.append(df)
        
        {"Jayson Tatum": df, "Jaylen Brown": df}
        

    return df_current_season
    
    
    
    
    
    

        
        
        
def main():
    
    # list of team_ids and player names
    team_ids, player_names = get_id()
    print(player_names)
    
    # Career statistics dataframe
    player_dataframes = find_player(team_ids)
   # print(player_dataframes)
    
    # Current season statistic dataframe
    season_data = get_stats(player_dataframes)
    print(season_data)



if __name__ == "__main__":
        main()









    
