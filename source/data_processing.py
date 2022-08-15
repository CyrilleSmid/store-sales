import pandas as pd

def combine_datasets() -> pd.DataFrame:
    df = pd.read_csv("../datasets/train.csv", parse_dates=True)
    
    print("Combining oil prices...")
    oil_df = pd.read_csv("../datasets/oil.csv")
    df = df.merge(oil_df, how="left")
    df["dcoilwtico"].interpolate(limit_direction="both", inplace=True)
    
    print("Combining store information...")
    stores_df = pd.read_csv("../datasets/stores.csv")
    df = df.merge(stores_df, how="left")
    
    df.set_index("date", drop=True, inplace=True)
    
    print("Combining events information (2min+)...")
    holidays_df = pd.read_csv("../datasets/holidays_additional_fix.csv", index_col="date", parse_dates=True)
    def if_an_event_day(group):
        date, city, state = group.name
        
        events = holidays_df.query("date == @date")
        for _, event in events.iterrows():
            if event["transferred"] == False:
                if event["type"] == "Holiday" or event["type"] == "Event":
                    if event["locale"] == "National":
                        return True
                        
                    elif event["locale"] == "Regional" and \
                            state == event["locale_name"]:
                        return True

                    elif event["locale"] == "Local" and \
                            city == event["locale_name"]:
                            return True
        return False
    df["event_day"] = df.groupby(["date", "city", "state"])["id"].transform(if_an_event_day)
    
    print("Combining non-work days information (2min+)...")
    def if_day_off(group):
        date, city, state = group.name
        date = pd.to_datetime(date)
        
        is_weekend = (date.weekday() >= 5)
        events = holidays_df.query("date == @date")
        
        for _, event in events.iterrows():
            if event["type"] != "Work Day" and event["type"] != "Event":
                if event["locale"] == "National":
                    return True
                
                elif event["locale"] == "Regional" and \
                    state == event["locale_name"]:
                    return True
                
                elif event["locale"] == "Local" and \
                    city == event["locale_name"]:
                    return True
                
            else: return False
        if is_weekend:
            return True
        return False

    df["day_off"] = df.groupby(["date", "city", "state"])["id"].transform(if_day_off)
    
    return df