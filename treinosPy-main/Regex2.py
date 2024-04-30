import re

def limpar_tags(string):
    """
    Remove todas as tags HTML da string.
    """
    nova_string = re.sub(r"(<[\w\s\=\"\-\/\;\:\.]*>)|(&\w*;)", " ", string)
    final_string = re.sub(r"\s{2,}", " ", nova_string)
    return final_string

def limpar_numeracao(string):
    """
    Remove a numeração presente na string.
    """
    final_string = re.sub(r"(I{1,3}\. )|(IV\. )", "\n", string)
    return final_string

def limpar_data(string):
    """
    Remove a data presente na string.
    """
    final_string = re.sub(r"[a-zA-Zà-úÀ-Ú]* \d*\/\d* \- ", "", string)
    return final_string

def limpar_string(string):
    """
    Limpa a string removendo tags HTML, numeração e data.
    """
    string_sem_tags = limpar_tags(string)
    string_sem_numeracao = limpar_numeracao(string_sem_tags)
    string_sem_data = limpar_data(string_sem_numeracao)
    return string_sem_data

# Exemplo de uso
string = '<div data-ordem="2" class="show"><div><i class="icon-arrow-left" style="font-size: 1.2em; cursor: pointer; margin-right: 10px;"></i><span tabindex="0" class="title">Questão 2/10 - Análise de Crédito e Risco</span><i class="icon-arrow-right" style="font-size: 1.2em; cursor: pointer; margin-left: 10px;"></i></div><article tabindex="0" class="question-text"><p><strong>Conforme </strong><strong>os conteúdos </strong><strong>do (livro-base Gestão de Crédito e Riscos, p. 4 p. 5), do Tema Análise de Crédito Pessoa Física e Jurídica, analise as assertivas que seguem e marque V para as asserções verdadeiras, e F para as asserções falsas.</strong></p><div class="row"></div></article><article class="question-text">I. ( ) É muito comum na pessoa física a validação do crédito por meio de métricas de pontuação. Essa métricas são encaixadas nas modelagens de credit score.<br>II. ( )Técnicas como análise discriminante, regressão linear, árvores de decisão, programação matemática, redes neurais, entre outras, foram evoluindo ao longo do tempo para procurar medir, com maior precisão, fatores que envolviam qualidade e comportamento. (Salanek Filho, 2018)<br><p>III. (&nbsp; ) <em>Behaviour Score</em> ferramenta que estabelece uma espécie de pontuação de crédito, sendo muito utilizado pelas entidades financeiras.<br>IV. ( ) Na pessoa jurídica, utiliza-se muito a análise com base nas informações de balanço.</p><p>&nbsp;</p><p>Agora, assinale a alternativa que apresenta a sequência correta:</p></article><table><tbody><tr class="question-choice"><td class="question-choice-input"><input type="radio" name="questao2935444" id="alternativa10796959" value="10796959" data-idquestao="2935444" data-idalternativa="10796959" data-letra="A" data-idhistorico="620384652"></td><td class="question-choice-label">A</td><td><article class="question-choice-body">V – F – V – F</article></td></tr><tr class="question-choice"><td class="question-choice-input"><input type="radio" name="questao2935444" id="alternativa10796960" value="10796960" data-idquestao="2935444" data-idalternativa="10796960" data-letra="B" data-idhistorico="620384652"></td><td class="question-choice-label">B</td><td><article class="question-choice-body">V – F – V – V</article></td></tr><tr class="question-choice"><td class="question-choice-input"><input type="radio" name="questao2935444" id="alternativa10796961" value="10796961" data-idquestao="2935444" data-idalternativa="10796961" data-letra="C" data-idhistorico="620384652"></td><td class="question-choice-label">C</td><td><article class="question-choice-body">F – V – V – F</article></td></tr><tr class="question-choice"><td class="question-choice-input"><input type="radio" name="questao2935444" id="alternativa10796962" value="10796962" data-idquestao="2935444" data-idalternativa="10796962" data-letra="D" data-idhistorico="620384652"></td><td class="question-choice-label">D</td><td><article class="question-choice-body">V – V – F – V</article></td></tr></tbody></table><hr class="hide"></div>'

nova_string = limpar_string(string)

print(f"\n{nova_string}\n")
