# import os
# from dotenv import load_dotenv
# from tavily import TavilyClient

# load_dotenv()

# tavily_key = os.getenv('TAVILY_API_KEY')

# tavily = TavilyClient(api_key = tavily_key)

# query = input("enter your query:")

# class SearchAgent:
#     def __init__(self):
#         pass

#     def search_net(self , query: str):
#         response = tavily.search(query=query, max_results = 5)
#         results = response['results']
#         # context = [{"url": obj["url"], "content": obj["content"]} for obj in results]
#         urls = [obj["url"] for obj in results]
#         return urls
 
#     def run(self , query : str):
#         res = self.search_net(query)
#         return res
    


# ## to test and run researchAgent individually
# # agent = SearchAgent()
# # results_url = agent.run(query)
# # print(results_url)


# langgraph agent 
import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

tavily_key = os.getenv('TAVILY_API_KEY')
tavily = TavilyClient(api_key=tavily_key)

class SearchAgent:
    def __init__(self):
        pass

    def search_net(self, query: str):
        response = tavily.search(query=query, max_results=5)
        results = response['results']
        urls = [obj["url"] for obj in results]
        return urls

    def run(self, query: str):
        return self.search_net(query)
