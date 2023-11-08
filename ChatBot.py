import os

import dotenv
import openai
import customtkinter

from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from dotenv import load_dotenv, find_dotenv
from deep_translator import GoogleTranslator
from threading import Thread

customtkinter.set_appearance_mode("System")  # MODES: "SYSTEM" (STANDARD), "DARK", "LIGHT"
customtkinter.set_default_color_theme("blue")  # THEMES: "BLUE" (STANDARD), "GREEN", "DARK-BLUE"


# CLASS MADE FOR METHODS TO RUN ON SEPARATE THREAD
class AsyncLangChain(Thread):
    global query
    global gui_txt
    global text

    def __init__(self, url):
        super().__init__()

        self.text = None
        self.gui_txt = ''
        self.url = url

    def run(self):
        global query
        global gui_txt
        global text

        # METHOD TO GET CHARACTERS FORM PDF
        def get_pdf_data(var):
            reader = PdfReader(var)
            data = ''
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    data += text
            return data

        # METHOD TO SEGMENT TEXT FOR LABELING WITH LANGCHAIN
        def get_text_chunks(var):
            splitter = CharacterTextSplitter(
                separator="\n",
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len,
            )
            chunks = splitter.split_text(var)
            return chunks

        # CREATES VECTORIAL DATABASE USING FAISS PACKAGE
        def create_vector(var):
            embedding = OpenAIEmbeddings()
            searching = FAISS.from_texts(var, embedding)
            return searching
        
        # PATH HERE THE FILES ARE STORED IN THE ROOT
        path = r"FILES_HERE/"

        files = os.listdir(path)

        total = ''

        # TAKES TOTAL DATA FROM ALL FILES
        for i in files:
            var = path + i
            print(var)
            data = get_pdf_data(var)
            total = total + data

        # SEPARATES ALL DATA IN CHUNKS
        c = get_text_chunks(total)

        # USES LANGCHAIN FRAMEWORK TO EMBED EVERY DATA CHUNK AND STORE IT INSIDE A VECTORIAL DATABASE
        v = create_vector(c)

        vect = []
        # INITIALIZES A QUESTION-ANSWERING CHAIN USING THE OPENAI GPT-3.5
        chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")
        query = text

        info2 = v.similarity_search(query)

        # USES GOOGLE TRANSLATE TO SHOW ANSWERS IN DESIRED LANGUAGE
        global new_language_str

        translated = GoogleTranslator(source='auto', target=new_language_str).translate(
            chain.run(input_documents=info2, question=query))
        print(translated)

        # STORES ANSWER IN GLOBAL VARIABLE GUI_TXT TO SHOW IT IN TEXTBOX
        gui_txt = translated


class App(customtkinter.CTk):
    global text
    global gui_txt
    global new_language_str
    global query
    new_language_str = "en"
    text = ''  # a
    gui_txt = ''

    load_dotenv()  # remove if not using dotenv

    dotenv.load_dotenv(dotenv_path=dotenv.find_dotenv(r"API_KEY\OPENAI_API_KEY.env"))

    api_key = os.environ["OPENAI_API_KEY"]

    if "OPENAI_API_KEY" not in os.environ:
        raise Exception("Missing OPENAI_API_KEY env var")

    # METHOD USED FOR PRESSING BUTTON
    def print_method(self):
        global text
        global gui_txt
        text = ''

        # GETS TEXT FROM USER
        text = self.entry.get()
        print(text)

        # VERIFIES IF THERE IS TEXT AND STARTS PROCESS IN DIFFERENT THREAD
        if text:
            self.main_button_1['state'] = customtkinter.DISABLED

            lang_chain_thread = AsyncLangChain(text)
            lang_chain_thread.start()

            self.monitor(lang_chain_thread)
        else:
            # SHOWS IF TEXTBOX EMPTY
            self.textbox.insert("4.0", "ChatBot: \t\t" + "Please insert text!" + "\n\n")

        # SHOWS IN INTERFACE USER INPUT
        self.textbox.insert("0.0", "User: \t\t" + text + "\n\n", )
        self.textbox.insert("2.0", "\n" + "processing..." + "\n\n")

    print(text)

    def __init__(self):
        super().__init__()

        self.start_a = ''
        self.title("ChatBot.py")
        self.geometry(f"{1100}x{580}")

        # CONFIGURE GRID LAYOUT (4X4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # CREATE SIDEBAR FRAME WITH WIDGETS
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="ChatBot",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=2, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)

        # PROGRESSBAR
        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=1, column=0, padx=(0, 20), pady=(0, 0), sticky="nsew")

        self.progressbar_1.configure(mode="intermediate")

        # OPTIONS FOR INTERFACE
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Select language:", anchor="w")
        self.appearance_mode_label.grid(row=1, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_label2 = customtkinter.CTkLabel(self.sidebar_frame, text="Select Theme:", anchor="w")
        self.appearance_mode_label2.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.language_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                     values=["en", "fr", "ro"],
                                                                     command=self.change_language_mode_event)
        self.language_mode_optionemenu.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # CREATE MAIN ENTRY AND BUTTON
        self.entry = customtkinter.CTkEntry(self,
                                            placeholder_text="Hey! I am an OpenAI ChatBot. What can I help you with?")
        self.entry.grid(row=0, column=1, columnspan=1, padx=(20, 20), pady=(20, 200), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, text="Ask", fg_color="transparent", border_width=2,
                                                     text_color=("gray10", "#DCE4EE"), command=self.print_method)
        self.main_button_1.grid(row=0, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # CREATE TEXTBOX
        self.textbox = customtkinter.CTkTextbox(self, width=250, font=("Times", 16, "bold"))
        self.textbox.grid(row=1, column=1, padx=(20, 20), pady=(0, 0), sticky="nsew")

        self.appearance_mode_optionemenu.set("Dark")  #
        self.language_mode_optionemenu.set("en")  #
        self.scaling_optionemenu.set("100%")  #

    # METHOD TO CHANGE INTERFACE APPEARANCE
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # METHOD TO SCALE THE INTERFACE
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    # METHOD TO CHANGE LANGUAGE FOR ANSWERS IN INTERFACE
    def change_language_mode_event(self, new_language: str):
        global new_language_str
        new_language_str = str(new_language.replace("", ""))

    # METHODS THAT MONITORS EVERY 100MS THE THREAD TO SEE IF THE LANGCHAIN PROCESS IS STILL RUNNING
    def monitor(self, thread):
        global gui_txt

        # VERIFIES IF THREAD STARTED
        if thread.is_alive():
            # CHECK THE THREAD EVERY 100MS
            self.after(100, lambda: self.monitor(thread))
            # STARTS PROGRESS BAR
            self.progressbar_1.start()
        else:
            # INSERTS IN USER INTERFACE THE ANSWER AFTER THE THREADS FINISHES PROCESSING
            self.textbox.insert("4.0", "\n" + "ChatBot: \t\t" + gui_txt + "\n\n")

            # STOPS PROGRESS BAR IN USER INTERFACE AFTER THE PROCESS FINISHES
            self.progressbar_1.stop()

            self.main_button_1['state'] = customtkinter.NORMAL


if __name__ == "__main__":
    app = App()
    app.mainloop()
