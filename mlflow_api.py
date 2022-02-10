import requests
import json


def get_prediction_api(data_client_transformed_json):

    mlflow_uri = 'https://home-credit-advice.herokuapp.com/invocations'

    headers = {"Content-Type":"application/json"}
    response = requests.post(url=mlflow_uri, 
                            data=data_client_transformed_json,
                            headers=headers)

    prediction = json.loads(response.text)

    return prediction   

    #if (
    #response.status_code != 204 and
    #response.headers["content-type"].strip().startswith("application/json")
    #):
    #    try:
    #        prediction = json.loads(response.text)
    #        return prediction
    #    except ValueError:
    #        return "Code error"