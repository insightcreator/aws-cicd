import json
import pandas as pd
import requests

def lambda_handler(event, context):
    print("event Data-->",event)
    response=requests.get("https://www.goggle.com/")
    print("Google Response:",response.text)
    # TODO implement
    di={'col1':[1,2],'col2':[3,4]}
    df=pd.DataFrame(di)
    print(df)
    print("Code Execution Completed")