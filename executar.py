import subprocess
import os
import sys

def iniciar_servico():
    # Define o nome do arquivo que contém a lógica principal
    script_principal = "main.py"
    
    # Encontra o caminho absoluto da pasta atual para evitar erros de diretório
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_script = os.path.join(diretorio_atual, script_principal)
    
    if not os.path.exists(caminho_script):
        print(f"Erro: O arquivo {script_principal} não foi encontrado na pasta!")
        return

    print("Iniciando o monitoramento em segundo plano...")

    try:
        # Executa o main.py de forma totalmente independente do terminal atual
        subprocess.Popen(
            [sys.executable, caminho_script],
            stdout=subprocess.DEVNULL,  # Oculta saídas padrão
            stderr=subprocess.DEVNULL,  # Oculta relatórios de erro
            start_new_session=True      # Desvincula do terminal (comportamento do nohup)
        )
        print("Serviço iniciado com sucesso nos bastidores.")
        print("Você já pode fechar esta janela do terminal.")
        
    except Exception as e:
        print(f"Falha ao iniciar o processo: {e}")

if __name__ == "__main__":
    iniciar_servico()