from datetime import *

def obter_hora():
    hora_atual = datetime.now().strftime("%H:%M:%S")
    return hora_atual