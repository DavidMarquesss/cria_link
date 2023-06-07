import os
PATH = "links/"
SERVER = "http://moodle2.lcad.inf.ufes.br/"
SAIDA =  "/notastreino.csv"

def criar_link(atividade):
    links = []
    alunos = os.listdir(PATH+atividade)
    for a in alunos:
        if os.path.isdir(PATH+atividade+"/"+a):
            l = SERVER+PATH+atividade+"/"+a+"/resposta.txt"
            links.append(l)

    return links

def cria_output(links,pasta):
    """
    escreve o arquivo notastreino.csv
    """
    with open(PATH+pasta+SAIDA,"w") as saida:
        for l in links:
            caminho = l.split("/")
            aluno = caminho[-2]
            saida.write(aluno+";-1;"+gera_url(l)+"\n")
            
    

def gera_url(link):
    return f"<a href='{link}'>Clique aqui!</a>"

def main():
    atividades = os.listdir(PATH)

    for a in atividades:
        if os.path.isdir(PATH+a):
            links_respostas = criar_link(a)
            cria_output(links_respostas,a)


if __name__ == '__main__':
    main()