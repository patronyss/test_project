import requests


class Parser:
    def true_response(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False

    def parse_count_of_info(self, url, info):
        response = requests.get(url).text
        return response.count(info)
