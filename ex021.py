# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
# inicia o modulo
pygame.init()
# carrega a música
pygame.mixer.music.load('media/ex021.mp3')
# reproduz a música
pygame.mixer.music.play()
#aguarda a execução do evento para encerrar o programa
pygame.event.wait()