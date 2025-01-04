import re
import pandas as pd 

def preprocess(data):
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

    
    messages = re.split(pattern , data)[1:]
    dates = [date.strip() for date in re.findall(pattern, data)]  # Clean trailing spaces

    # dates = re.findall(pattern , data)
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})

# convert message_date type
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y , %H-%M - ')
    df.rename(columns={'message_date': 'date'},inplace=True)

    
    # separate users and messages 
    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s',message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
    
        else:
            users.append('group_notification')
            messages.append(entry[0])
    
    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'],inplace = True)
    df.head()   
    df['date'].dt.year
    df['month'] =df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    return df
