import requests

def churn(k):
    #Config
    db_url = "https://dsci551-173f1-default-rtdb.firebaseio.com/"

    #Curl
    url = f'{db_url}churn_data_by_ruijie.json?orderBy="Churn"&equalTo="Yes"&limitToFirst={k}&print=pretty'
    response = requests.get(url)
    filtered_data = response.json()
    result = list(filtered_data.keys())

    print(result)

if __name__ == "__main__":
    import sys
    churn(sys.argv[1])