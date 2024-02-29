from utils import *

def add_to_dataframe(name: str, lis: list)-> str:
    
    new_data = pd.DataFrame({
        "Name": [name], 
        "subscriber_count": [lis[0]], 
        "number_of_views": [lis[1]], 
        "total_views": [lis[2]], 
        "joining_date": [lis[3]], 
        "country_of_origin": [lis[4]]

    })
    new_data.to_csv("Youtuber_data.csv", mode='a', header=False, index=False)

    print("Data Appended")
