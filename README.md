# Github, kivy & Data Analysis tasks
As instruções a seguir são uma lista de implementação para exercitar tarefas básicas com github kivy, numpy, pandas e matplotlib.

## 1. Clonar o repositório
Clone este repositório `test-repo` para sua máquina.

```bash
git clone git@github.com:jvianna07/test-repo.git
```
## 2. Criar ambiente virtual
Dentro do diretório `test-repo` crie um ambiente virtual (use o conda ou pyenv com python 3.10) e dê um nome a sua escolha.

Ative o ambiente virtual e instale as seguintes dependências:
* kivy
* numpy
* pandas
* matplotlib
* ipykernel

Crie o arquivo `.gitignore` e coloque nele todos arquivos que devem ser ignorados (env/, /\_pycache\_/, etc.).


## 3. Criar diretórios e arquivos
Crie dois diretórios: `data_science` (com o arquivo `data_analysis.ipynb`); e `kivy_app` (com os arquivos `main.py` e `myapp.kv`). A estrutura final do diretório com os arquivos (incluindo o `README.md`) deve ser a seguinte:
```bash
test-repo/
├── data_science/
│   └── data_analysis.ipynb
├── kivy_app/
│   ├── main.py
│   └── myapp.kv
└── README.md
```

Copie os códigos seguintes para os arquivos.

- Arquivo `data_analysis.ipynb`:
```python
# Importar bibliotecas 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

```python
# Importar o dataset
df=pd.read_csv("https://raw.githubusercontent.com/jvianna07/popular_datasets/refs/heads/main/calories.csv")
df.head()
```


- Arquivo `main.py`:
```python
# Importar bibliotecas 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


# Classe de widgets 
class MyWidget(BoxLayout):
    texto = StringProperty("Hello World!")

    def atualizar_texto(self, novo_texto):
        self.texto = f"Você digitou: {novo_texto}"


# Classe principal do app 
class MyApp(App):
    def build(self):
        return MyWidget()


# Run
if __name__ == '__main__':
    MyApp().run()
```

- Arquivo `myapp.kv`:
```kivy
<MyWidget>:
    orientation: 'vertical'
    padding: 20
    spacing: 10

    TextInput:
        id: entrada
        hint_text: "Digite qualquer coisa..."
        multiline: False
        on_text_validate: root.atualizar_texto(self.text)

    Button:
        text: "Atualizar"
        on_press: root.atualizar_texto(entrada.text)

    Label:
        text: root.texto
        font_size: 24

```

## 4. Explorar o dataset com tarefas de análise de dados básicas

Use o arquivo `data_analysis.ipynb` para exercitar tarefas de análise de dados básicas com pandas, numpy e matplotlib.

### I. Pandas (manipulação de dataframes)
a) Limpeza de Dados

* Verificar valores ausentes (`NaN`) e tratá-los (ex: com `dropna()` ou `fillna()`).
* Verificar tipos de dados e convertê-los adequadamente (`astype()`).
* Identificar e remover duplicatas (`drop_duplicates()`).
* Verificar e tratar outliers (ex: usando `describe()` ou visualizações).
* Corrigir valores inconsistentes (ex: `Pulse` maior que `Maxpulse`, `Duration` negativa etc.).

b) Análise Estatística

* Estatísticas descritivas com `describe()`.
* Média, mediana, moda, desvio padrão, variância de cada coluna.
* Distribuição de frequência de valores de `Duration`, `Pulse`, etc.
* Contar quantas sessões têm duração maior que X minutos.
* Média de calorias queimadas por duração.

c) Agrupamentos e Agregações

* Agrupar por `Duration` e calcular média de `Calories`.
* Agrupar por faixas de `Pulse` ou `Maxpulse`.

d) Análise de Correlação**

* Matriz de correlação com `.corr()`
* Análise da relação entre `Pulse` e `Calories`.
* Identificar colunas mais fortemente correlacionadas.

e) Transformações e Criação de Novas Colunas

* Calcular `Calories` por minuto: `Calories/Duration`.
* Criar coluna booleana: sessões com `Pulse` acima de 120.
* Normalizar ou padronizar colunas para análise posterior (padronizar com valores entre 0 e 1).

f) Exportar Dados

* Exportar o dataset limpo no formato `.csv` (escolha as colunas a incluir).


### II. Numpy (Arrays)
a) Tranforme o dataset em um array numpy

b) Calcule as seguintes estatiticas das colunas: Média, mediana, desvio padrão, variância

### III. Matplotlib (Visualização)
a) Com o matplotlib, crie as seguintes visualizações:

* Histograma da distribuição de `Calories`.
* Gráfico de dispersão entre `Pulse` e `Calories`.
* Boxplot de `Calories` por faixas de `Duration`.
* Gráfico de linha para `Calories` ao longo das sessões.

## 5. Ficheiro de dependências
Crie o arquivo `requirements.txt`. Ele será responsável por guardar todas as dependências que devem ser instaladas para quem for usar este repositório.

```bash
pip freeze> requirements.txt
```

No final a estrutura do diretório `test-repo` com o arquivo `requirements.txt` deverá ser a seguinte:

```bash
test-repo/
├── data_science/
│   └── data_analysis.ipynb
├── kivy_app/
│   ├── main.py
│   └── myapp.kv
├── README.md
└── requirements.txt
```

## 6. Salvar as alterações no repositório remoto
Faça o commit de todas as alterações com a mensagem "versão final".

Salve no repositório remoto `test-repo` com o comando `git push`.


