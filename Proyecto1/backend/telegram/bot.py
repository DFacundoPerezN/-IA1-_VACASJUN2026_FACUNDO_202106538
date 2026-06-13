#https://api.telegram.org/bot8355574792:AAE4q9NIkRYDvbxe4LAOyeGClwYTmKEX8y8/getUpdates

import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

class TelegramBot:
    def __init__(self):
        self.token = TOKEN
        self.chat_id = CHAT_ID

    def cambiar_chat(self, chat: str):
        self.chat_id = chat
        print(f" Se cambio el chat_id a :{self.chat_id}")

    def cambiar_token(self, tk: str):
        self.token = tk
        print(f" Se cambio el token a :{self.chat_id}")

    def enviar_mensaje(self, mensaje):
        chat_id = self.chat_id
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        #print(url)
        payload ={
            "chat_id": chat_id,
            "text": mensaje
        }

        response = requests.post(url, json=payload)

        if response.status_code == 200:
            print("enviado con extio")
        else:
            print("Error al enviar el mensaje: ", response.text)

    #enviar_mensaje("D-frag es el mejor manga que traduces")

    def enviar_recomendaciones(self, listaSintomas, listaRecomendaciones, chat_id = CHAT_ID):
        chat_id = self.chat_id
        texto = "Se analizaron los sintomas dados: \n"
        for sintoma in listaSintomas:
            texto += "  * "+ sintoma.replace("_", " ") +"\n"
        texto += "\n\nY aplicando logica inferencial se dan las siguientes recomendaciones:\n"
        
        for recomendacion in listaRecomendaciones:
            texto += "  * "+ recomendacion.replace("_", " ") +"\n"
        texto += "\n\nEsperamos que su equipo mejore pronto :)"

        
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        #print(url)
        payload ={
            "chat_id": chat_id,
            "text": texto
        }

        response = requests.post(url, json=payload)

        if response.status_code == 200:
            print("Mensaje en telegram enviado con extio")
        else:
            print("Error al enviar el mensaje: ", response.text)

    def enviar_falla(self, listaSintomas, falla, chat_id = CHAT_ID):
        chat_id = self.chat_id
        texto = "Se analizaron los sintomas dados: \n"
        for sintoma in listaSintomas:
            texto += "  * "+ sintoma +"\n"
        texto += "\n\nY aplicando logica inferencial se concluyo que lo más probable es que el equipo tenga:\n"
        
        texto += falla.replace("_", " ")

        
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        #print(url)
        payload ={
            "chat_id": chat_id,
            "text": texto
        }

        response = requests.post(url, json=payload)

        if response.status_code == 200:
            print("Mensaje en telegram enviado con extio")
        else:
            print("Error al enviar el mensaje: ", response.text)