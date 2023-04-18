import re

#Limpar String do Trabalho

def limpar_string(string):
    nova_string = re.sub(r"<[\w\s\=\"\-\/]*>", " ", string)
    final_string = re.sub(r"\s{2,}", " ", nova_string)
    print(f"\n{final_string}\n")

# exemplo de uso
string = '<article class="question-text"><strong>Assinale a alternativa correta onde consta o relatório contábil em que são apresentados os recursos próprios e de terceiros:</strong></article>'

limpar_string(string)