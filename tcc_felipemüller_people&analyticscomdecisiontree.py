# -*- coding: utf-8 -*-
"""TCC_FelipeMüller_People&AnalyticscomDecisionTree.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IH8GxnBVenXGPQgwrXs7w5fsDO1ytINF
"""

#CRIANDO UM BANCO DE DADOS PARA PEOPLE ANALYTICS E APLICANDO UMA DECISION TREE

#Importando as bibliotecas
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier,export_graphviz
from sklearn.model_selection import train_test_split
from sklearn import metrics

#Tamanho da amostra - quantidade de colaboradores
colaboradores = 150

#Estabelecimento de parâmetros de funcionários RENDIMENTO BAIXO

#Intervalo de salários
SalarioMin = 1500
SalarioMax = 9500

#Dependentes
DependentesMin = 0
DependentesMax = 2

#Faltas
FaltasMin = 2
FaltasMax = 15

#Atrasos
AtrasosMin = 8
AtrasosMax = 30

#Atividades de T&D
AtivMin = 0
AtivMax = 8

#Tarefas
TarMin = 0
TarMax = 30

#Metas
MetMin = 0
MetMax = 10

#Atestados apresentados
AtestMin = 0
AtestMax = 20

#Cursos
CursosMin = 0
CursosMax = 5

#Tickets Internos atendidos
TicketsMin = 0
TicketsMax = 15

#AvaliaçõesEquipe
AvalEqMin = 0
AvalEqMax = 5

#AvaliaçõesGestor
AvalGeMin = 0
AvalGeMax = 5

#Gerando os dados

#Gerando a coluna com os nomes dos funcionários
funcionarios = ['Rafael','Lucas','Denise','Flávio','Eduardo','Eliane','Douglas','Josiane','Marcelo','Melisa','Monia','William','Rose','Itamar','Sandra','Túlio']

df0 = pd.DataFrame({'funcionarios':funcionarios})

np.random.seed(4)

#Gerando a colunas com os salários
df1 = pd.DataFrame(np.random.randint(SalarioMin,SalarioMax,size=(colaboradores,1)))

#Gerando a coluna 'Dependentes'
df2 = pd.DataFrame(np.random.randint(DependentesMin,DependentesMax,size=(colaboradores,1)))

#Gerando a coluna 'Faltas'
df3 = pd.DataFrame(np.random.randint(FaltasMin,FaltasMax,size=(colaboradores,1)))

#Gerando a coluna'atrasos'
df4 = pd.DataFrame(np.random.randint(AtrasosMin,AtrasosMax,size=(colaboradores,1)))

#Gerando a coluna 'Participação em atividades de T&D (Treinamento e Desenvolvimento)
df5 = pd.DataFrame(np.random.randint(AtivMin,AtivMax,size=(colaboradores,1)))

#Gerando a coluna 'Tarefas concluídas'
df6 = pd.DataFrame(np.random.randint(TarMin,TarMax,size=(colaboradores,1)))

#Gerando a coluna 'Metas alcançadas'
df7 = pd.DataFrame(np.random.randint(MetMin,MetMax,size=(colaboradores,1)))

#Gerando a coluna 'Atestados apresentados'
df8 = pd.DataFrame(np.random.randint(AtestMin,AtestMax,size=(colaboradores,1)))

#Gerando a coluna 'Cursos de aperfeiçoamento'
df9 = pd.DataFrame(np.random.randint(CursosMin,CursosMax,size=(colaboradores,1)))

#Gerando a coluna 'Tickets internos atendidos'
df10 = pd.DataFrame(np.random.randint(TicketsMin,TicketsMax,size=(colaboradores,1)))

#Gerando a coluna 'Avaliação da equipe'
df11 = pd.DataFrame(np.random.randint(AvalEqMin,AvalEqMax,size=(colaboradores,1)))

#Gerando a coluna 'Avaliação do gestor'
df12 = pd.DataFrame(np.random.randint(AvalGeMin,AvalGeMax,size=(colaboradores,1)))

#Juntando todas as colunas
df = pd.concat([df0,df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12],axis=1)

df.columns = ['Funcionário',
              'Salário',
              'Dependentes',
              'Faltas',
              'Atrasos',
              'Participação em atividades de T&D',
              'Tarefas concluídas',
              'Metas alcançadas',
              'Atestados apresentados',
              'Cursos de aperfeiçoamento',
              'Tickets internos atendidos',
              'Avaliação da equipe',
              'Avaliação do gestor']

dfbaixo = df

dfbaixo['Ação'] = 'Demitir'

dfbaixo

#Estabelecimento de parâmetros de funcionários RENDIMENTO MÉDIO - BAIXO

#Intervalo de salários
SalarioMin = 1500
SalarioMax = 6000

#Dependentes
DependentesMin = 0
DependentesMax = 3

#Faltas
FaltasMin = 0
FaltasMax = 10

#Atrasos
AtrasosMin = 4
AtrasosMax = 20

#Atividades de T&D
AtivMin = 2
AtivMax = 20

#Tarefas
TarMin = 10
TarMax = 50

#Metas
MetMin = 2
MetMax = 13

#Atestados apresentados
AtestMin = 2
AtestMax = 15

#Cursos
CursosMin = 2
CursosMax = 10

#Tickets Internos atendidos
TicketsMin = 5
TicketsMax = 20

#AvaliaçõesEquipe
AvalEqMin = 2
AvalEqMax = 9

#AvaliaçõesGestor
AvalGeMin = 2
AvalGeMax = 9

#Gerando os dados

#Gerando a coluna com os nomes dos funcionários
funcionarios = ['Rafael','Lucas','Denise','Flávio','Eduardo','Eliane','Douglas','Josiane','Marcelo','Melisa','Monia','William','Rose','Itamar','Sandra','Túlio']

df0 = pd.DataFrame({'funcionarios':funcionarios})

np.random.seed(6)

#Gerando a colunas com os salários
df1 = pd.DataFrame(np.random.randint(SalarioMin,SalarioMax,size=(colaboradores,1)))

#Gerando a coluna 'Dependentes'
df2 = pd.DataFrame(np.random.randint(DependentesMin,DependentesMax,size=(colaboradores,1)))

#Gerando a coluna 'Faltas'
df3 = pd.DataFrame(np.random.randint(FaltasMin,FaltasMax,size=(colaboradores,1)))

#Gerando a coluna'atrasos'
df4 = pd.DataFrame(np.random.randint(AtrasosMin,AtrasosMax,size=(colaboradores,1)))

#Gerando a coluna 'Participação em atividades de T&D (Treinamento e Desenvolvimento)
df5 = pd.DataFrame(np.random.randint(AtivMin,AtivMax,size=(colaboradores,1)))

#Gerando a coluna 'Tarefas concluídas'
df6 = pd.DataFrame(np.random.randint(TarMin,TarMax,size=(colaboradores,1)))

#Gerando a coluna 'Metas alcançadas'
df7 = pd.DataFrame(np.random.randint(MetMin,MetMax,size=(colaboradores,1)))

#Gerando a coluna 'Atestados apresentados'
df8 = pd.DataFrame(np.random.randint(AtestMin,AtestMax,size=(colaboradores,1)))

#Gerando a coluna 'Cursos de aperfeiçoamento'
df9 = pd.DataFrame(np.random.randint(CursosMin,CursosMax,size=(colaboradores,1)))

#Gerando a coluna 'Tickets internos atendidos'
df10 = pd.DataFrame(np.random.randint(TicketsMin,TicketsMax,size=(colaboradores,1)))

#Gerando a coluna 'Avaliação da equipe'
df11 = pd.DataFrame(np.random.randint(AvalEqMin,AvalEqMax,size=(colaboradores,1)))

#Gerando a coluna 'Avaliação do gestor'
df12 = pd.DataFrame(np.random.randint(AvalGeMin,AvalGeMax,size=(colaboradores,1)))

#Juntando todas as colunas
df = pd.concat([df0,df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12],axis=1)



df.columns = ['Funcionário',
              'Salário',
              'Dependentes',
              'Faltas',
              'Atrasos',
              'Participação em atividades de T&D',
              'Tarefas concluídas',
              'Metas alcançadas',
              'Atestados apresentados',
              'Cursos de aperfeiçoamento',
              'Tickets internos atendidos',
              'Avaliação da equipe',
              'Avaliação do gestor']

dfmediobaixo = df

dfmediobaixo['Ação'] = 'Manter'

dfmediobaixo

#Estabelecimento de parâmetros de funcionários RENDIMENTO MÉDIO

#Intervalo de salários
SalarioMin = 1500
SalarioMax = 5000

#Dependentes
DependentesMin = 1
DependentesMax = 3

#Faltas
FaltasMin = 0
FaltasMax = 8

#Atrasos
AtrasosMin = 2
AtrasosMax = 15

#Atividades de T&D
AtivMin = 3
AtivMax = 30

#Tarefas
TarMin = 20
TarMax = 60

#Metas
MetMin = 4
MetMax = 15

#Atestados apresentados
AtestMin = 1
AtestMax = 10

#Cursos
CursosMin = 0
CursosMax = 15

#Tickets Internos atendidos
TicketsMin = 0
TicketsMax = 25

#AvaliaçõesEquipe
AvalEqMin = 3
AvalEqMax = 10

#AvaliaçõesGestor
AvalGeMin = 3
AvalGeMax = 10

#Gerando os dados

#Gerando a coluna com os nomes dos funcionários
funcionarios = ['Rafael','Lucas','Denise','Flávio','Eduardo','Eliane','Douglas','Josiane','Marcelo','Melisa','Monia','William','Rose','Itamar','Sandra','Túlio']

df0 = pd.DataFrame({'funcionarios':funcionarios})

np.random.seed(5)

#Gerando a colunas com os salários
df1 = pd.DataFrame(np.random.randint(SalarioMin,SalarioMax,size=(colaboradores,1)))

#Gerando a coluna 'Dependentes'
df2 = pd.DataFrame(np.random.randint(DependentesMin,DependentesMax,size=(colaboradores,1)))

#Gerando a coluna 'Faltas'
df3 = pd.DataFrame(np.random.randint(FaltasMin,FaltasMax,size=(colaboradores,1)))

#Gerando a coluna'atrasos'
df4 = pd.DataFrame(np.random.randint(AtrasosMin,AtrasosMax,size=(colaboradores,1)))

#Gerando a coluna 'Participação em atividades de T&D (Treinamento e Desenvolvimento)
df5 = pd.DataFrame(np.random.randint(AtivMin,AtivMax,size=(colaboradores,1)))

#Gerando a coluna 'Tarefas concluídas'
df6 = pd.DataFrame(np.random.randint(TarMin,TarMax,size=(colaboradores,1)))

#Gerando a coluna 'Metas alcançadas'
df7 = pd.DataFrame(np.random.randint(MetMin,MetMax,size=(colaboradores,1)))

#Gerando a coluna 'Atestados apresentados'
df8 = pd.DataFrame(np.random.randint(AtestMin,AtestMax,size=(colaboradores,1)))

#Gerando a coluna 'Cursos de aperfeiçoamento'
df9 = pd.DataFrame(np.random.randint(CursosMin,CursosMax,size=(colaboradores,1)))

#Gerando a coluna 'Tickets internos atendidos'
df10 = pd.DataFrame(np.random.randint(TicketsMin,TicketsMax,size=(colaboradores,1)))

#Gerando a coluna 'Avaliação da equipe'
df11 = pd.DataFrame(np.random.randint(AvalEqMin,AvalEqMax,size=(colaboradores,1)))

#Gerando a coluna 'Avaliação do gestor'
df12 = pd.DataFrame(np.random.randint(AvalGeMin,AvalGeMax,size=(colaboradores,1)))

#Juntando todas as colunas
df = pd.concat([df0,df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12],axis=1)

df.columns = ['Funcionário',
              'Salário',
              'Dependentes',
              'Faltas',
              'Atrasos',
              'Participação em atividades de T&D',
              'Tarefas concluídas',
              'Metas alcançadas',
              'Atestados apresentados',
              'Cursos de aperfeiçoamento',
              'Tickets internos atendidos',
              'Avaliação da equipe',
              'Avaliação do gestor']

dfmed = df

dfmed['Ação'] = 'Dar aumento'

dfmed

#Estabelecimento de parâmetros de funcionários ALTO RENDIMENTO

#Intervalo de salários
SalarioMin = 1500
SalarioMax = 5000

#Dependentes
DependentesMin = 1
DependentesMax = 5

#Faltas
FaltasMin = 0
FaltasMax = 5

#Atrasos
AtrasosMin = 0
AtrasosMax = 10

#Atividades de T&D
AtivMin = 4
AtivMax = 30

#Tarefas
TarMin = 10
TarMax = 70

#Metas
MetMin = 6
MetMax = 20

#Atestados apresentados
AtestMin = 0
AtestMax = 5

#Cursos
CursosMin = 5
CursosMax = 20

#Tickets Internos atendidos
TicketsMin = 10
TicketsMax = 30

#AvaliaçõesEquipe
AvalEqMin = 6
AvalEqMax = 10

#AvaliaçõesGestor
AvalGeMin = 3
AvalGeMax = 10

#Gerando os dados

#Gerando a coluna com os nomes dos funcionários
funcionarios = ['Rafael','Lucas','Denise','Flávio','Eduardo','Eliane','Douglas','Josiane','Marcelo','Melisa','Monia','William','Rose','Itamar','Sandra','Túlio']

df0 = pd.DataFrame({'funcionarios':funcionarios})

np.random.seed(3)

#Gerando a colunas com os salários
df1 = pd.DataFrame(np.random.randint(SalarioMin,SalarioMax,size=(colaboradores,1)))

#Gerando a coluna 'Dependentes'
df2 = pd.DataFrame(np.random.randint(DependentesMin,DependentesMax,size=(colaboradores,1)))

#Gerando a coluna 'Faltas'
df3 = pd.DataFrame(np.random.randint(FaltasMin,FaltasMax,size=(colaboradores,1)))

#Gerando a coluna'atrasos'
df4 = pd.DataFrame(np.random.randint(AtrasosMin,AtrasosMax,size=(colaboradores,1)))

#Gerando a coluna 'Participação em atividades de T&D (Treinamento e Desenvolvimento)
df5 = pd.DataFrame(np.random.randint(AtivMin,AtivMax,size=(colaboradores,1)))

#Gerando a coluna 'Tarefas concluídas'
df6 = pd.DataFrame(np.random.randint(TarMin,TarMax,size=(colaboradores,1)))

#Gerando a coluna 'Metas alcançadas'
df7 = pd.DataFrame(np.random.randint(MetMin,MetMax,size=(colaboradores,1)))

#Gerando a coluna 'Atestados apresentados'
df8 = pd.DataFrame(np.random.randint(AtestMin,AtestMax,size=(colaboradores,1)))

#Gerando a coluna 'Cursos de aperfeiçoamento'
df9 = pd.DataFrame(np.random.randint(CursosMin,CursosMax,size=(colaboradores,1)))

#Gerando a coluna 'Tickets internos atendidos'
df10 = pd.DataFrame(np.random.randint(TicketsMin,TicketsMax,size=(colaboradores,1)))

#Gerando a coluna 'Avaliação da equipe'
df11 = pd.DataFrame(np.random.randint(AvalEqMin,AvalEqMax,size=(colaboradores,1)))

#Gerando a coluna 'Avaliação do gestor'
df12 = pd.DataFrame(np.random.randint(AvalGeMin,AvalGeMax,size=(colaboradores,1)))

#Juntando todas as colunas
df = pd.concat([df0,df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12],axis=1)

df.columns = ['Funcionário',
              'Salário',
              'Dependentes',
              'Faltas',
              'Atrasos',
              'Participação em atividades de T&D',
              'Tarefas concluídas',
              'Metas alcançadas',
              'Atestados apresentados',
              'Cursos de aperfeiçoamento',
              'Tickets internos atendidos',
              'Avaliação da equipe',
              'Avaliação do gestor']

dfalt = df

dfalt['Ação'] = 'Promover'

dfalt

dffuncionarios = pd.concat([dfbaixo,dfmed,dfalt,dfmediobaixo], axis=0)

dffuncionarios.sample(20)

dffuncionarios.pop("Funcionário")

dffuncionarios.sample(20)

X_train, X_test, y_train, y_test = train_test_split(dffuncionarios.drop('Ação',axis=1),dffuncionarios['Ação'],test_size=0.3)

X_train.shape,X_test.shape

clf = DecisionTreeClassifier()

clf = clf.fit(X_train,y_train)

clf.feature_importances_

resultado = clf.predict(X_test)
resultado

#Printando o score do modelo

from sklearn import metrics

print(metrics.classification_report(y_test,resultado))

#Criando um dataframe geralzão pra aplicar o modelo

#Estabelecimento de parâmetros de funcionários

colaboradores = 13


#Intervalo de salários
SalarioMin = 1500
SalarioMax = 10000

#Dependentes
DependentesMin = 0
DependentesMax = 5

#Faltas
FaltasMin = 0
FaltasMax = 15

#Atrasos
AtrasosMin = 0
AtrasosMax = 30

#Atividades de T&D
AtivMin = 0
AtivMax = 30

#Tarefas
TarMin = 0
TarMax = 70

#Metas
MetMin = 0
MetMax = 20

#Atestados apresentados
AtestMin = 0
AtestMax = 20

#Cursos
CursosMin = 0
CursosMax = 20

#Tickets Internos atendidos
TicketsMin = 0
TicketsMax = 30

#AvaliaçõesEquipe
AvalEqMin = 0
AvalEqMax = 10

#AvaliaçõesGestor
AvalGeMin = 0
AvalGeMax = 10

#Gerando os dados

#Gerando a coluna com os nomes dos funcionários
funcionarios = ['Rafael','Lucas','Denise','Flávio','Eduardo','Eliane','Douglas','Josiane','Marcelo','Melisa','Monia','William','Rose','Itamar','Sandra','Túlio']

df0 = pd.DataFrame({'funcionarios':funcionarios})

np.random.seed(5)

#Gerando a colunas com os salários
df1 = pd.DataFrame(np.random.randint(SalarioMin,SalarioMax,size=(colaboradores,1)))

#Gerando a coluna 'Dependentes'
df2 = pd.DataFrame(np.random.randint(DependentesMin,DependentesMax,size=(colaboradores,1)))

#Gerando a coluna 'Faltas'
df3 = pd.DataFrame(np.random.randint(FaltasMin,FaltasMax,size=(colaboradores,1)))

#Gerando a coluna'atrasos'
df4 = pd.DataFrame(np.random.randint(AtrasosMin,AtrasosMax,size=(colaboradores,1)))

#Gerando a coluna 'Participação em atividades de T&D (Treinamento e Desenvolvimento)
df5 = pd.DataFrame(np.random.randint(AtivMin,AtivMax,size=(colaboradores,1)))

#Gerando a coluna 'Tarefas concluídas'
df6 = pd.DataFrame(np.random.randint(TarMin,TarMax,size=(colaboradores,1)))

#Gerando a coluna 'Metas alcançadas'
df7 = pd.DataFrame(np.random.randint(MetMin,MetMax,size=(colaboradores,1)))

#Gerando a coluna 'Atestados apresentados'
df8 = pd.DataFrame(np.random.randint(AtestMin,AtestMax,size=(colaboradores,1)))

#Gerando a coluna 'Cursos de aperfeiçoamento'
df9 = pd.DataFrame(np.random.randint(CursosMin,CursosMax,size=(colaboradores,1)))

#Gerando a coluna 'Tickets internos atendidos'
df10 = pd.DataFrame(np.random.randint(TicketsMin,TicketsMax,size=(colaboradores,1)))

#Gerando a coluna 'Avaliação da equipe'
df11 = pd.DataFrame(np.random.randint(AvalEqMin,AvalEqMax,size=(colaboradores,1)))

#Gerando a coluna 'Avaliação do gestor'
df12 = pd.DataFrame(np.random.randint(AvalGeMin,AvalGeMax,size=(colaboradores,1)))

#Juntando todas as colunas
df = pd.concat([df0,df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12],axis=1)

df.columns = ['Funcionário',
              'Salário',
              'Dependentes',
              'Faltas',
              'Atrasos',
              'Participação em atividades de T&D',
              'Tarefas concluídas',
              'Metas alcançadas',
              'Atestados apresentados',
              'Cursos de aperfeiçoamento',
              'Tickets internos atendidos',
              'Avaliação da equipe',
              'Avaliação do gestor']

df

