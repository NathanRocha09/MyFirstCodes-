
#Closure e funções que retornam outras funções


def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar 


primaira_saudacao = criar_saudacao("boa noite", "Bruno")
segunda_saudacao = criar_saudacao("não falamos do", "Bruno")

print(primaira_saudacao())
print(segunda_saudacao())



#Posso tbm, fazer estas funções da seguinte forma:


def greeting(welcome, name):
    def gtg():
        return f'{welcome}, {name}!'
    return gtg

good_evening = greeting('hi there')
good_nigth = greeting('by')

for name in ['Luna', 'Neith', 'Helo']:
    print(good_evening(name))
    print(good_nigth(name))

    






