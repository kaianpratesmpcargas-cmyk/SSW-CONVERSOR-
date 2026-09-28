# MP CARGAS — Conversor SSW

Aplicativo desktop profissional em Python para converter dados copiados diretamente do sistema **SSW** em formato de tabela Markdown/texto delimitado para planilhas **Excel (.xlsx)** com relatórios gerenciais, indicadores de atraso e agrupamento por destino.

---

## 🚀 Funcionalidades

- **Área de Colagem Ampla**: Permite colar tabelas diretamente com `Ctrl + V` ou através do botão dedicado **"Colar da Área de Transferência"**.
- **Parser Confiável e Inteligente**:
  - Limpeza automática de links Markdown `[CTRC](URL)`.
  - Remoção de tags HTML (`<br>`, `&#xA0;`, `&nbsp;`, etc.), negritos (`**`) e espaços duplicados.
  - Normalização de valores monetários no formato brasileiro (`R$ 1.250,50` ou `8.500,00`) e pesos em decimais.
  - Interpretação inteligente da coluna **Atraso**:
    - Maior que 0: **ATRASADO**
    - Igual a 0: **NO PRAZO**
    - Vazio ou ausente: **SEM INFORMAÇÃO**
  - Descarte seguro de separadores Markdown, cabeçalhos residuais, botões de paginação (`×`) e rodapés de sistema.
- **Dashboard e Tabela Interativa (Tkinter)**:
  - Cards com indicadores: **Total de CT-RCs**, **Atrasados**, **No Prazo**, **Sem Informação**, **Peso Total** e **Frete Total**.
  - Tabela com rolagem vertical e horizontal.
  - Busca rápida em tempo real por CTRC, Nota Fiscal, Remetente, Destinatário ou Destino.
  - Filtros combinados por **Situação** e **Destino**.
  - Cores dinâmicas para fácil visualização de entregas em atraso ou no prazo.
- **Exportação Profissional para Excel (.xlsx)**:
  - **Aba Acompanhamento**: Cabeçalho azul marinho estilizado, congelamento da 1ª linha (`freeze_panes`), autofiltro ativado, largura de coluna automática, formatação de moeda brasileira (`R$ #,##0.00`), peso numérico e destaque condicional de linhas/situações.
  - **Aba RESUMO**: Indicadores consolidados e tabela gerencial agrupada por **Destino** (Quantidade, Atrasados e Peso).
  - Diálogo padrão de salvamento com nome sugerido `MP_CARGAS_SSW_YYYY-MM-DD.xlsx` e confirmação antes de sobrescrever.
- **100% Local**: Não utiliza IA, não depende de banco de dados.

---

## 📂 Estrutura do Projeto

```text
CONVERSOR SSW/
├── main.py             # Interface gráfica principal e fluxo do aplicativo
├── parser_ssw.py       # Limpeza profunda, extração e validação dos dados do SSW
├── excel_export.py     # Geração e estilização profissional da planilha Excel (OpenPyXL)
├── dashboard.py        # Dashboard de métricas, cards e tabela filtrável (Tkinter)
├── requirements.txt    # Dependências mínimas do projeto
└── README.md           # Instruções e documentação
```

---

## 🛠️ Requisitos e Instalação

### 1. Pré-requisitos
- **Python 3.10** ou superior instalado no Windows.
- As bibliotecas `tkinter` já vêm instaladas por padrão no instalador oficial do Python para Windows.

### 2. Instalação das Dependências

Abra o prompt de comando (PowerShell ou CMD) na pasta do projeto e execute:

```powershell
pip install -r requirements.txt
```

---

## ▶️ Como Executar

Execute o comando:

```powershell
python main.py
```

### Passo a Passo de Uso:
1. Abra a consulta no sistema SSW e copie os dados da tabela.
2. No aplicativo **MP CARGAS**, clique no botão **"Colar da Área de Transferência"** ou pressione `Ctrl + V` na área de texto.
3. Clique em **"PROCESSAR TABELA"**.
4. Veja os indicadores nos cards e visualize a tabela com filtros de busca.
5. Clique em **"EXPORTAR EXCEL (.xlsx)"** e selecione o local desejado para salvar a planilha.
