import os
import json
import requests
from langchain.tools import tool

class SerachTools():
    @tool("search the internet")
    def search_internet(query):
        'To serch the internet'
        top_result_to_return = 1
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})

        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        results = response.json()#['organic']
        organic_results = results.get('organic', [])

        string = []
        for result in organic_results[:top_result_to_return]:

            try:
                string.append('\n'.join([
                    f"Title: {result['title']}", f"Link: {result['link']}",
                    f"Snippet: {result['snippet']}", "\n-----------------"
                ]))
            except KeyError:
                next

        return '\n'.join(string)