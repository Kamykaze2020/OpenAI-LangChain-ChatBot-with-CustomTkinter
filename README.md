# OpenAI-LangChain-ChatBot-with-CustomTkinter
### What is the application?

 ChatBot application with interface in CustomTkinter that uses the LangChain framework to embed and store data inside a vectorial database so that it can send it to a neural network provided by OpenAI and get the user the answers that he needs based on the files stored.

 The application uses the **OPENAI_API_KEY** that you can get from https://platform.openai.com/account/api-keys. After you make an account and get the **API_KEY** you need to insert it into the folder '**API_KEY**' inside the '**OPENAI_API_KEY.env**' file.

 You can put files like pdf, word, exel etc. inside the '**FILES_HERE**' folder. There the application will extract the text from the files in the folder, store the data inside a vector, segment it, embed it and store it into a vectorial database by using FIASS (Facebook AI Similarity Search) from the langchain package.

 The application runs on 2 threads so that the interface doesn't freeze when the langchain framework makes the request to OpenAI to get an answer. While the thread makes the reques to OpenAI a loading bar downside the textbox starts moving so that the user can know that the application is running. After the answer is written the loadbar stops.

 You can select the language in which you want the ChatBot to respond in the upper-left corner of the interface or you can change the UI Scaling or Theme for the interface from the lower right corner.

# Interface

![4](https://github.com/Kamykaze2020/OpenAI-LangChain-ChatBot-with-CustomTkinter/assets/62187923/696335e7-96d3-4c37-be2c-92bc4cfe8cb7)


 # Example of running

![video-to-gif](https://github.com/Kamykaze2020/OpenAI-LangChain-ChatBot-with-CustomTkinter/assets/62187923/e78ced79-af7b-47e0-8b23-bcdc2bbaba4c)

# Theory

Traditional databases store strings, numbers, and other types of scalar data in rows and columns. On the other hand, a vector database operates on vectors, so the way it’s optimized and queried is quite different.

In traditional databases, we are usually querying for rows in the database where the value usually exactly matches our query. In vector databases, we apply a similarity metric to find a vector that is the most similar to our query.

A vector database uses a combination of different algorithms that all participate in Approximate Nearest Neighbor (ANN) search. These algorithms optimize the search through hashing, quantization, or graph-based search.

These algorithms are assembled into a pipeline that provides fast and accurate retrieval of the neighbors of a queried vector. Since the vector database provides approximate results, the main trade-offs we consider are between accuracy and speed. The more accurate the result, the slower the query will be. However, a good system can provide ultra-fast search with near-perfect accuracy.

Here’s a common pipeline for a vector database:

![6](https://github.com/Kamykaze2020/OpenAI-LangChain-ChatBot-with-CustomTkinter/assets/62187923/158a61a0-a713-4e9c-b6f3-5c1b01cae5fb)

1.	**Indexing**: The vector database indexes vectors using an algorithm such as PQ, LSH, or HNSW (more on these below). This step maps the vectors to a data structure that will enable faster searching.

2.	**Querying**: The vector database compares the indexed query vector to the indexed vectors in the dataset to find the nearest neighbors (applying a similarity metric used by that index)

3.	**Post Processing**: In some cases, the vector database retrieves the final nearest neighbors from the dataset and post-processes them to return the final results. This step can include re-ranking the nearest neighbors using a different similarity measure.

More info at: https://www.pinecone.io/learn/vector-database/

# Inatallation and Packages

You will need to download the fies as .zip, extract them and then open the .py file with pycharm as a new project. You need to keep the folders '**API_KEY**' and '**FILES_HERE**' inside the project repository, otherwise the program won't work correctly.

As instructed upside, you will need to paste you **API_KEY** into the folder '**API_KEY**' inside the '**OPENAI_API_KEY.env**' file.

Files that you want the neural network to work with will be put inside '**FILES_HERE**'

This project uses multiple packages which you will need to install inside you python project for the application to run.

You can install all the needed packages by using the pip commands inside the terminal.

pip install deep-translator

pip install customtkinter

pip install python-dotenv

pip install langchain

pip install openai(or “pip install openai==0.28.1” in case it doesn’t work)

pip install PyPDF2

pip install tiktoken

pip install faiss-gpu(or “pip install faiss-cpu”)

