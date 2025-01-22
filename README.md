Pseudocódigo

LOOP infinito:
    SE o arquivo "pid" não existe:
        Exibir mensagem: "Arquivo 'pid' não encontrado."
        AGUARDAR 5 segundos
        CONTINUAR para a próxima iteração
    
    LER o PID do arquivo "pid"

    SE o PID corresponde a um processo ativo do Python3:
        Exibir mensagem: "1: It is alive"
    CASO CONTRÁRIO:
        Exibir mensagem: "1: It is dead"
        EXECUTAR o script Python (meu_script.py) em segundo plano
        SALVAR o novo PID no arquivo "pid"

    AGUARDAR 5 segundos antes da próxima iteração


Estrutura do Modelo Conceitual vs. Código Implementado

Aspecto	Modelo Conceitual	Código Implementado
Nível de Abstração	O modelo conceitual foca nos passos gerais do fluxo.	O código implementa detalhes técnicos como ps, os.getpid.
Iterações e Lógica	Usa pseudocódigo simples para descrever o loop e lógica.	Implementa com comandos e funções específicas (while, ps).
