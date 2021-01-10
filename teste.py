diretorio = 'C:/users/user/desktop/teste.txt'

def escrever_arquivo(texto):
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open (diretorio, 'a')
    arquivo.write (texto)
    arquivo.close()

def ler_arquivo (nome_arquivo):
    arquivo = open (nome_arquivo, 'r') 
    texto = arquivo.read ()   
    print(texto)

if __name__ == "__main__":
    #escrever_arquivo('Primeira Linha \n')
    #atualizar_arquivo('Terceira Linha \n')
    #ler_arquivo('C:/users/user/desktop/teste.txt')
    
    