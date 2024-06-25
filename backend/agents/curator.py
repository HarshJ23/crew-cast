# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# import bs4
# from langchain import hub
# from langchain_chroma import Chroma
# from langchain_community.document_loaders import WebBaseLoader
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnablePassthrough
# from langchain_openai import OpenAIEmbeddings
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_core.prompts import ChatPromptTemplate


# load_dotenv()
# fcontent = input("enter your content requirement:")


# groq_api_key = os.getenv('GROQ_API_KEY')
# openai_key = os.getenv('OPENAI_API_KEY')
# llm = ChatGroq(model="mixtral-8x7b-32768" , groq_api_key = groq_api_key)
# sources =['https://www.anthropic.com/news/claude-3-5-sonnet', 'https://www.anthropic.com/claude', 'https://www.theverge.com/2024/6/20/24181961/anthropic-claude-35-sonnet-model-ai-launch', 'https://arstechnica.com/information-technology/2024/06/anthropics-latest-best-ai-model-is-twice-as-fast-and-still-terrible-at-dad-jokes/', 'https://venturebeat.com/ai/anthropic-claude-3-5-sonnet-surges-to-top-of-ai-rankings-challenging-industry-giants/']

# class CuratorAgent():
#     def __init__(self):
#         pass


#     def scrape_rag(self , sources:list):

#         loader = WebBaseLoader(sources)
#         docs = loader.load()
#         docs1 = "\n\n".join(doc.page_content for doc in docs)

#         text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
#         splits = text_splitter.split_documents(docs1)
#         vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings(openai_api_key = openai_key ))
        
#         # Retrieve and generate using the relevant snippets of the blog.
#         retriever = vectorstore.as_retriever()
#         system_prompt = (
#         "You are an assistant for generating content for a twitter , linkedin and tik-tok content creator."
#         "Use the following pieces of retrieved context to create the content according to user requirements."
#         "If you are not able to create specified type of content , say that you"
#         "don't know."
#         "while generating content ,from the given context , include a bit of history , numbers and insights too."
#         "content should be engaging and sound and look insightful.Use human like language and tone"
#         "\n\n"
#         "{context}"
#         )

#         prompt = ChatPromptTemplate.from_messages(
#         [
#         ("system", system_prompt),
#         ("human", "{input}"),
#         ]
#         )

#         rag_chain = (
#         {"context": retriever, "input": RunnablePassthrough()}
#         | prompt
#         | llm
#         | StrOutputParser()
#         )

#         response = rag_chain.invoke(fcontent)
#         return response
    
#     def run(self , query:str):
#         content = self.scrape_rag(query)
#         return content
    

# agent = CuratorAgent()
# res = agent.run(fcontent)
# print(res)


# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain import hub
# from langchain_chroma import Chroma
# from langchain_community.document_loaders import WebBaseLoader
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnablePassthrough
# from langchain_openai import OpenAIEmbeddings
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_core.prompts import ChatPromptTemplate

# load_dotenv()

# fcontent = input("Enter your content requirement: ")

# groq_api_key = os.getenv('GROQ_API_KEY')
# openai_key = os.getenv('OPENAI_API_KEY')

# llm = ChatGroq(model="mixtral-8x7b-32768", groq_api_key=groq_api_key)

# sources = [
#     'https://www.anthropic.com/news/claude-3-5-sonnet',
#     'https://www.anthropic.com/claude',
#     'https://www.theverge.com/2024/6/20/24181961/anthropic-claude-35-sonnet-model-ai-launch',
#     'https://arstechnica.com/information-technology/2024/06/anthropics-latest-best-ai-model-is-twice-as-fast-and-still-terrible-at-dad-jokes/',
#     'https://venturebeat.com/ai/anthropic-claude-3-5-sonnet-surges-to-top-of-ai-rankings-challenging-industry-giants/'
# ]

# class CuratorAgent:
#     def __init__(self):
#         pass

#     def scrape_rag(self, sources: list):
#         loader = WebBaseLoader(sources)
#         docs = loader.load()

#         text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
#         splits = text_splitter.split_documents(docs)
        
#         vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings(openai_api_key=openai_key))
        
#         retriever = vectorstore.as_retriever()
        
#         system_prompt = (
#             "You are an assistant for generating content for a Twitter, LinkedIn, and TikTok content creator. "
#             "Use the following pieces of retrieved context to create the content according to user requirements. "
#             "If you are not able to create specified type of content, say that you don't know. "
#             "While generating content from the given context, include a bit of history, numbers, and insights too. "
#             "Content should be engaging and sound and look insightful. Use human-like language and tone.\n\n"
#             "{context}"
#         )

#         prompt = ChatPromptTemplate.from_messages(
#             [
#                 ("system", system_prompt),
#                 ("human", "{input}")
#             ]
#         )

#         rag_chain = (
#             {"context": retriever, "input": RunnablePassthrough()}
#             | prompt
#             | llm
#             | StrOutputParser()
#         )

#         response = rag_chain.invoke(fcontent)
#         return response

#     def run(self, query: str):
#         content = self.scrape_rag(sources)
#         return content



# ## to test and run researchAgent individually
# # Create an instance of CuratorAgent and run the process
# # agent = CuratorAgent()
# # res = agent.run(fcontent)
# # print(res)


# langgraph agent
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')
openai_key = os.getenv('OPENAI_API_KEY')

llm = ChatGroq(model="mixtral-8x7b-32768", groq_api_key=groq_api_key)

class CuratorAgent:
    def __init__(self):
        pass

    def scrape_rag(self, sources: list, content_type: str):
        loader = WebBaseLoader(sources)
        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(docs)
        
        vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings(openai_api_key=openai_key))
        
        retriever = vectorstore.as_retriever()
        
        system_prompt = (
            "You are an assistant for generating content for a Twitter, LinkedIn, and TikTok content creator. "
            "Use the following pieces of retrieved context to create the content according to user requirements. "
            "If you are not able to create specified type of content, say that you don't know. "
            "While generating content from the given context, include a bit of history, numbers, and insights too. "
            "Content should be engaging and sound and look insightful. Use human-like language and tone.\n\n"
            "{context}"
        )

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}")
            ]
        )

        rag_chain = (
            {"context": retriever, "input": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )

        response = rag_chain.invoke(content_type)
        return response

    def run(self, query: dict):
        sources = query['urls']
        content_type = query['content_type']
        return self.scrape_rag(sources, content_type)
