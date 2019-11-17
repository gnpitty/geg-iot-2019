from time import sleep
from omxplayer.player import OMXPlayer

def play1():
    player = OMXPlayer("speech.mp3")
    sleep(20)
    player.quit()
    player = OMXPlayer("timbre.mp3")
    sleep(4)
    player.quit()

play1()
