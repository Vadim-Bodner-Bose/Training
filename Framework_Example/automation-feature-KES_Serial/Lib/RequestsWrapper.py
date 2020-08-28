"""
File contains a wrapper class for Requests package
"""

import requests


class RequestsWrapper:
    """
    Class is a wrapper for requests calls for reporting to REST API's
    """

    def __init__(self):
        """
        Class initialization
        """
        self.headers = {'Content-Type': 'application/json',
                        'Accept': 'application/json'}

    def put_request(self, url, payload, token=None):
        """
        Wrapper function for PUT request
        """
        if isinstance(token, str):
            self.headers["Authorization"] = 'auth_token ' + token
            put_request = requests.request("PUT", url, headers=self.headers, data=payload)

        if isinstance(token, tuple):
            put_request = requests.request("PUT", url, headers=self.headers, data=payload, auth=token)

        print(put_request.status_code)
        put_response = put_request.text.encode('utf8')
        return put_response

    def get_request(self, url, token=None):
        """

        """
        if isinstance(token, str):
            self.headers["Authorization"] = 'auth_token ' + token
            get_request = requests.request("GET", url, headers=self.headers)

        if isinstance(token, tuple):
            get_request = requests.request("GET", url, headers=self.headers, auth=token)

        print(get_request.status_code)
        get_response = get_request.text.encode('utf8')
        return get_response

    def post_request(self, url, payload, token=None):
        """

        """
        if isinstance(token, str):
            self.headers["Authorization"] = 'auth_token ' + token
            post_request = requests.request("POST", url, headers=self.headers, data=payload)

        if isinstance(token, tuple):
            post_request = requests.request("POST", url, headers=self.headers, data=payload, auth=token)

        if token == None :
            post_request = requests.request("POST", url, headers=self.headers, data=payload)

        print(post_request.status_code)
        post_response = post_request.text.encode('utf8')
        return post_response

    def post_request_file(self, url, token, file):
        """
        Wrapper function for file sending through POST
        """
        headers = {'Authorization': 'auth_token ' + token}
        payload = {}
        post_request = requests.request("POST", url, headers=headers, data=payload, files=file)
        return post_request

    def delete_request(self, url, token):
        """
        Wrapper function for delete call
        """

        self.headers['Authorization'] = 'auth_token ' + token

        delete_request = requests.delete(url, headers=self.headers)
        return delete_request