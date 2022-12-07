import pandas as pd
import time
import spotifyAPI as spot

#adds track id onto a dataframe for one year or multiple and returns that dataframe so it can be saved locally
def add_track_id(year_df):
    for index, row in year_df.iterrows():
        search_response = spot.search(search_term=row.song, music_type='track', limit=2)

        try:
            current_track_id = search_response.get('tracks').get('items')[0].get('id')
            year_df.loc[index, 'track_id'] = current_track_id

            print(f"{row.release_year}: {index}/{len(year_df)-1}")
        except:
            print("no matches found")
            year_df.loc[index, 'track_id'] = 'noid'
            continue
    return year_df

def create_audiofeatures_df(track_ids):
    audio_features_df = pd.DataFrame()
    for index, id in enumerate(track_ids):

        try:
       
            audio_features_response = spot.audio_features(track_id = id)
        
            temprow = pd.DataFrame(audio_features_response, index= [index])

            audio_features_df = pd.concat([audio_features_df, temprow])

            print(f"PROGRESS: {index}/{len(track_ids) - 1}")
        except:
            print('something went wrong finding audio features')
            continue
   
    audio_features_df = audio_features_df.reset_index(drop=True)
    return audio_features_df

