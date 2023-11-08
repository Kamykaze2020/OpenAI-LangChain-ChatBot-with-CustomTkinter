# OpenAI-LangChain-ChatBot-with-CustomTkinter
 ChatBot application with interface in CustomTkinter that uses the LangChain framework to embed and store data inside a vectorial database so that it can send it to a neural network provided by OpenAI and get the user the answers that he needs based on the files stored.

 The application uses the **OPENAI_API_KEY** that you can get from https://platform.openai.com/account/api-keys. After you make an account and get the **API_KEY** you need to insert it into the folder '**API_KEY**' inside the '**OPENAI_API_KEY.env**' file.

 You can put files like pdf, word, exel etc. inside the '**FILES_HERE**' folder. There the application will extract the text from the files in the folder, store the data inside a vector, segment it, embed it and store it into a vectorial database by using FIASS (Facebook AI Similarity Search) from the langchain package.

 The application runs on 2 threads so that the interface doesn't freeze when the langchain framework makes the request to OpenAI to get an answer. While the thread makes the reques to OpenAI a loading bar downside the textbox starts moving so that the user can know that the application is running. After the answer is written the loadbar stops.

 You can select the language in which you want the ChatBot to respond in the right corner.

# Interface

![4](https://github.com/Kamykaze2020/OpenAI-LangChain-ChatBot-with-CustomTkinter/assets/62187923/696335e7-96d3-4c37-be2c-92bc4cfe8cb7)


 # Example of running

![video-to-gif](https://github.com/Kamykaze2020/OpenAI-LangChain-ChatBot-with-CustomTkinter/assets/62187923/e78ced79-af7b-47e0-8b23-bcdc2bbaba4c)


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

