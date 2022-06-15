import requests
import json

URL = "http://127.0.0.1:8000/student/"

def get_data(user_id=None):
    data = {}
    if id is not None:
        data = {"user_id": user_id}
    print(f'Data is -------------->',data)
    json_data = json.dumps(data)
    print(f'JSON Data -------------->',json_data)
    final = requests.get(url = URL , data = json_data)
    print(f'R Data -------------->',final)
    # data = r.json()

get_data()