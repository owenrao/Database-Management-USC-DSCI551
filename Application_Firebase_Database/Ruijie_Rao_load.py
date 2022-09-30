import requests
import json
import pandas as pd

#Config
db_url = "https://dsci551-173f1-default-rtdb.firebaseio.com/"
data_path = "WA_Fn-UseC_-Telco-Customer-Churn.csv"

#Data Preparation
churn_raw_data = pd.read_csv(data_path)
churn_raw_data = churn_raw_data.set_index("customerID")
churn_seniors_data = churn_raw_data[churn_raw_data["SeniorCitizen"]==1]
churn_seniors_dict = churn_seniors_data.to_dict("index")

#Upload Data
url = db_url+"churn_data_by_ruijie.json"
payload = json.dumps(churn_seniors_dict)
response = requests.put(url,payload)
message = response.json()

if response.status_code == 200:
    print("Upload Complete!")
else:
    print(message)