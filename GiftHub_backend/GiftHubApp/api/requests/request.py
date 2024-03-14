import os
import requests

class APIRequest():
    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}
        self.url = ""
        self.params = {}
        self.data = {}
        
    def set_url(self, url: str):
        if not isinstance(url, str):
            raise TypeError("Provided value is not of type str.")
        self.url = url
        
    def set_params(self, params: dict):
        """
        Use get
        """
        if not isinstance(params, dict):
            raise TypeError("Provided value is not of type dict.")
        self.params = params

    def set_data(self, data: dict):
        """
        Use post
        """
        if not isinstance(data, dict):
            raise TypeError("Provided value is not of type dict.")
        self.data = data

    def get(self):
        response = requests.get(self.url, params=self.params)
        if response.status_code == 200:
            # 요청 성공
            return response.json()  # 응답 데이터 처리
        else:
            # 요청 실패
            raise response.json()

    def post(self):
        response = requests.post(self.url, json=self.data, headers=self.headers)
        if response.status_code == 200:
            # 요청 성공
            return response.json()  # 응답 데이터 처리
        else:
            # 요청 실패
            raise response.json()