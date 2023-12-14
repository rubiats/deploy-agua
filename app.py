import streamlit as st 


st.header('💧 Deploy do modelo: Potability Water')

st.divider()

# Texto com sintaxe Markdown
texto_markdown = """
**O conjunto de dados neste estudo consiste em 10 variáveis, com uma variável dependente (1 = potável, 0 = não potável) e 9 variáveis independentes. As variáveis independentes são os parâmetros da água.**

Variáveis:

* Valor do pH: O pH é um parâmetro importante na avaliação do equilíbrio ácido-base da água.
* Dureza: A dureza é causada principalmente por sais de cálcio e magnésio.
* Sólidos (Sólidos dissolvidos totais - TDS): A água tem a capacidade de dissolver uma ampla gama de minerais ou sais inorgânicos e alguns orgânicos, como potássio, cálcio, sódio, bicarbonatos, cloretos, magnésio, sulfatos etc.
* Cloraminas: Cloro e cloramina são os principais desinfetantes usados em sistemas públicos de água.
* Sulfato: Os sulfatos são substâncias naturais encontradas em minerais, solo e rochas.
* Condutividade: A água pura não é um bom condutor de corrente elétrica, mas sim um bom isolante. O aumento na concentração de íons aumenta a condutividade elétrica da água.
* Organic_carbon: O carbono orgânico total (TOC) nas águas de nascente vem da matéria orgânica natural em decomposição (NOM), bem como de fontes sintéticas.
* Trihalometanos: THMs são produtos químicos que podem ser encontrados em água tratada com cloro.
* Turbidez: A turbidez da água depende da quantidade de matéria sólida presente no estado suspenso.
* Potabilidade: Indica se a água é segura para consumo humano onde 1 significa Potável e 0 significa Não potável.
"""

# Exibindo o texto formatado com Markdown
st.markdown(texto_markdown)