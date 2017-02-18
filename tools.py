"""
    Work flow

    Attempt to connect
    Parse
"""
import requests


class DatabaseHelper:
    def __init__(self):
        pass

    @staticmethod
    def load_data():
        some_data = {'a': 'b', 'c': 'd', 'e': 'f' }
        return some_data  # dict

    def add_data(self):
        pass


# class Employee(Base):
#
# 	__tablename__ = 'employee'
# 	name = Column(String(250), nullable = False)
# 	id = Column(Integer, primary_key = True)

class Connections:

    def __init__(self):
        pass

    @staticmethod
    def format_post(user_details):
        payload = {
            "username": user_details.keys()[0],
            "password": user_details.values()[0],
            'dst':'http://canvas.oauife.edu.ng/advert',
            'popup':'true'

        }

        headers = {
            # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            # "Accept-Encoding": "gzip, deflate",
            # "Accept-Language": "en-US,en;q=0.8",
            # "Cache-Control": "max-age=0",
            # "Connection": "keep-alive",
            # "Content-Length": "88",
            # "Content-Type": "application/x-www-form-urlencoded",
            # "Host": "gateway.oauife.edu.ng",
            # "Origin": "http://gateway.oauife.edu.ng",
            # "Referer": "http://gateway.oauife.edu.ng/start.html",
            # "Upgrade-Insecure-Requests": "1",
            # "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
            #  (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"

            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Length": "100",
            "Content-Type":"application/x-www-form-urlencoded",
            "Host": "gateway.oauife.edu.ng",
            "Origin": "https://gateway.oauife.edu.ng",
            "Referer": "https://gateway.oauife.edu.ng/start.html",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36\
             (KHTML, like Gecko) Chrome/56.0.2924.76 Mobile Safari/537.36"

#              Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
# Accept-Encoding:gzip, deflate, br
# Accept-Language:en-US,en;q=0.8
# Cache-Control:max-age=0
# Connection:keep-alive
# Content-Length:88
# Content-Type:application/x-www-form-urlencoded
# Cookie:__utma=135605487.788700159.1481619800.1483540398.1483825883.5; __utmz=135605487.1481619800.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)
# Host:gateway.oauife.edu.ng
# Origin:https://gateway.oauife.edu.ng
# Referer:https://gateway.oauife.edu.ng/start.html
# Upgrade-Insecure-Requests:1
# User-Agent:Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Mobile Safari/537.36

        }

        return {"payload": payload, "headers": headers}

    def post(self, user_detail=None):
        if not user_detail:
            raise ValueError("User Detail Expected")

        formatted_post = self.format_post(user_detail)
        response = None
        # session = requests.Session()
        # response = session.post('https://gateway.oauife.edu.ng/login',
        #                     data=formatted_post.get('payload'),
        #                     headers=formatted_post.get('headers'),
        #                     verify=False)
        # print response.text
        # response = session.get('http://canvas.oauife.edu.ng/advert')
        try:
            session = requests.Session()
            response = session.post('https://gateway.oauife.edu.ng/login',
                            data=formatted_post.get('payload'),
                            headers=formatted_post.get('headers'),
                            verify=False)
            # response = session.get('http://canvas.oauife.edu.ng/advert')
            # print response.text
        except exception as e:
            raise e
        finally:
            if not response:
                return False
            return response.text.lower()

    # def parse_response(self, response):
    #     server_reply = response.text.lower()
    #     if not response:
    #         return False
    #     else:
    #         if 'invalid' in server_reply:
    #             return 'invalid'
    #         elif 'radius' in server_reply:
    #             return 'radius'
    #         elif 'confirm' in server_reply:
    #             return 'expired'
    #         elif 'maximum' in server_reply:
    #             return 'expired'
    #         elif 'logged in' in server_reply:
    #
    #         else:
    #             if self.is_active():
    #                 return 'success'
    #             else:
    #                 raise TypeError("Unhandled exception!\n" + server_reply)

    @staticmethod
    def is_active():
        try:
            requests.get('https://www.python.org')
            return True
        except requests.ConnectionError:
            return False

if __name__ == '__main__':
    test = Connections()
    test.post({'a': 'apple', 'b': 'ball', 'c': 'cup'})
