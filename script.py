import os
import time

# Nome do arquivo que armazenará o PID
PID_FILE = "pid"

def main():
    # Obtém o próprio PID do processo
    current_pid = os.getpid()

    # Escreve o PID no arquivo
    with open(PID_FILE, "w") as f:
        f.write(str(current_pid))

    # Loop de 3 iterações
    for i in range(3):
        print("2: I am alive")
        time.sleep(2)  # Aguarda 2 segundos entre as iterações

    # Mensagem final
    print("2: I gonna die now, bye")

if __name__ == "__main__":
    main()

