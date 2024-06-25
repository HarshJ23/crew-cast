import os
import time
from concurrent.futures import ThreadPoolExecutor
from langgraph.graph import Graph

# Import agent classes
from agents.curator import CuratorAgent
from agents.researcher import SearchAgent

class MasterAgent:
    def __init__(self):
        # self.output_dir = f"outputs/run_{int(time.time())}"
        # os.makedirs(self.output_dir, exist_ok=True)
        pass

    def run(self, queries: list):
        # Initialize agents
        search_agent = SearchAgent()
        curator_agent = CuratorAgent()

        # Define a Langchain graph
        workflow = Graph()

        # Add nodes for each agent
        workflow.add_node("search", search_agent.run)
        workflow.add_node("curate", curator_agent.run)

        # Set up edges
        workflow.add_edge('search', 'curate')

        # Set up start and end nodes
        workflow.set_entry_point("search")
        workflow.set_finish_point("curate")

        # Compile the graph
        chain = workflow.compile()

        # Execute the graph for each query in parallel
        with ThreadPoolExecutor() as executor:
            parallel_results = list(executor.map(lambda q: chain.invoke(q), queries))

        return parallel_results

        # chain.invoke()

# Example usage
if __name__ == "__main__":
    topic_query = input("Enter your content topic query: ")
    content_type = input("Enter your content type query: ")
    
    queries = [{'query': topic_query, 'content_type': content_type}]
    
    master_agent = MasterAgent()
    results = master_agent.run(queries)
    print(results)
