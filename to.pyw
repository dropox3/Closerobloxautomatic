import time
import psutil
import os
import subprocess
import tkinter as tk
from PIL import Image, ImageTk
import pygame

def fechar_processo_roblox():
    for proc in psutil.process_iter(['pid', 'name']):
        if 'RobloxPlayerBeta.exe' in proc.info['name']:
            pid = proc.info['pid']
            processo = psutil.Process(pid)
            print(f"Fechando o processo RobloxPlayerBeta.exe (PID: {pid})...")
            processo.terminate()

def tocar_musica():
    pygame.mixer.init()
    pygame.mixer.music.load("hihiha.mp3")  # Substitua pelo caminho real da música
    pygame.mixer.music.play()


if __name__ == "__main__":
    while True:
        print("Aguardando o Roblox ser aberto...")
        tempo_inicial = None

        while True:
            processo_roblox = None
            for proc in psutil.process_iter(['pid', 'name']):
                if 'RobloxPlayerBeta.exe' in proc.info['name']:
                    processo_roblox = proc
                    if tempo_inicial is None:
                        tempo_inicial = time.time()
                    break

            if processo_roblox:
                # O Roblox foi aberto, verifica se já se passaram 30 segundos
                tempo_atual = time.time()
                tempo_decorrido = tempo_atual - tempo_inicial
                if tempo_decorrido >= 5:
                    print("Passaram-se 30 segundos. Fechando o RobloxPlayerBeta.exe...")
                    fechar_processo_roblox()
                    tocar_musica()
                    break

        # Intervalo de verificação para o próximo loop
        time.sleep(1)
