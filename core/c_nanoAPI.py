import requests
from core import exceptions
import json


class NanoApi(object):
    def __init__(self, auth=None):
        self.auth = auth

    # ---------------------------------------------------------------
    # erstellt Nano Authentifizierungs-Token und gibt dieses zurück
    # ---------------------------------------------------------------
    def sign_in(self, username, password):
        sign_in = {"identifier": username, "password": password}
        response = requests.post("https://api.nanowrimo.org/users/sign_in", json=sign_in)
        if response:
            msg = "Login successful"
            print(msg)
            self.auth = {"Authorization": response.json()["auth_token"]}
            return True, msg
        elif response.status_code == 401:
            msg = "Wrong username/password. Try again."
            print(msg)
            return False,msg
        elif response.status_code == 404:
            msg = "Login page not found! Please contact me!"
            print(msg)
            return False, msg
        else:
            msg = "Error: Please try again later! (Status Code:" + response.status_code + ")"
            print(msg)
            return False, msg

    # setzt auth
    def log_out(self):
        self.auth = None

    def getId(self, nanoNick):
        if self.auth:
            response = requests.get("https://api.nanowrimo.org/users/" + nanoNick, headers=self.auth)
            if response:
                return response.json()["data"]["id"]
            else:
                raise exceptions.apiLoadingError("Loading data from NaNo-Api failed. Try again later")
        else:
            raise exceptions.AuthError("Authentification failed. Login first.")

    def fileFromAPI(self, url, speicherort):
        if self.auth:
            response = requests.get(url, headers=self.auth)
            if response:
                with open(speicherort + ".json", 'w') as outfile:
                    json.dump(response.json(), outfile)
            else:
                raise exceptions.apiLoadingError("Loading data from NaNo-Api failed. Try again later")
        else:
            raise exceptions.AuthError("Authentification failed. Login first.")


api = NanoApi()
