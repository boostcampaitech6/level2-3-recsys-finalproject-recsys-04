import os
import requests

class APIRequest():
    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}
        
    def url(self, url: str):
        if not type(str):
            raise TypeError("Provided value is not of type str.")
        self.url = url
        
    def params(self, params: dict):
        if not type(params):
            raise TypeError("Provided value is not of type dict.")
        self.params = params

    def data(self, data: dict):
        if not type(data):
            raise TypeError("Provided value is not of type dict.")
        self.data = data

    def get(self):
        response = requests.get(self.url, params=self.params)
        if response.status_code == 200:
            # 요청 성공
            return response.json()  # 응답 데이터 처리
        else:
            # 요청 실패
            return {'error': 'Request failed'}

    def post(self):
        response = requests.post(self.url, json=self.data, headers=self.headers)
        if response.status_code == 200:
            # 요청 성공
            return response.json()  # 응답 데이터 처리
        else:
            # 요청 실패
            return {'error': 'Request failed'}