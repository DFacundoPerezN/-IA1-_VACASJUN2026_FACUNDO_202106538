#https://api.telegram.org/bot8355574792:AAE4q9NIkRYDvbxe4LAOyeGClwYTmKEX8y8/getUpdates

import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def enviar_mensaje(mensaje, chat_id = CHAT_ID):
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

def enviar_recomendaciones(listaSintomas, listaRecomendaciones, chat_id = CHAT_ID):
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

def enviar_falla(listaSintomas, falla, chat_id = CHAT_ID):
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