# OpenAI-LangChain-ChatBot-with-CustomTkinter
 ChatBot application with interface in CustomTkinter that uses the LangChain framework to embed and store data inside a vectorial database so that it can send it to a neural network provided by OpenAI and get the user the answers that he needs based on the files stored.

 The application uses the OPENAI_API_KEY that you can get from https://platform.openai.com/account/api-keys. After you make an account and get the API_KEY you need to insert it into the folder 'API_KEY' inside the 'OPENAI_API_KEY.env' file.

 You can put files like pdf, word, exel etc. inside the 'FILES_HERE' folder. There the application will extract the text from the files in the folder, store the data inside a vector, segment it, embed it and store it into a vectorial database by using FIASS (Facebook AI Similarity Search) from the langchain package.

# Interface

![5](https://github.com/Kamykaze2020/OpenAI-LangChain-ChatBot-with-CustomTkinter/assets/62187923/2a77aab8-0cfa-42ef-9348-83cb40115ee1)

 # Example of running

![4](https://github.com/Kamykaze2020/OpenAI-LangChain-ChatBot-with-CustomTkinter/assets/62187923/d18d979b-05c1-4a1c-88c3-86c8235271f5)

# Inatallation and Packages

You will need to download the fies as .zip, extract them and then open the .py file with pycharm as a new project. You need to keep the folders 'API_KEY' and 'FILES_HERE' inside the project repository, otherwise the program won't work correctly.

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

