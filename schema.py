import pandas as pd 
df = pd.DataFrame(columns = ["Name", "subscriber_count", "number_of_views", "total_views", "joining_date", "country_of_origin"])

df.to_csv("Youtuber_data.csv")