import streamlit as st

# --- 1. Configuração da Página ---
st.set_page_config(
    page_title="Votação", 
    page_icon="🗳️", 
    layout="wide"
)

# --- 2. Estilo CSS (Com a CORREÇÃO para fontes gigantes) ---
GLOBAL_CSS = """
<style>
    /* Fundo da página PRETO */
    [data-testid="stAppViewContainer"] {
        background-color: #000000; 
    }
    footer {visibility: hidden;}

    /* --- Títulos (BRANCOS) --- */
    h1 { color: #FFFFFF; font-weight: bold; text-align: center; }
    h2 { color: #EAECEE; font-weight: normal; text-align: center; }
    h3 { color: #FFFFFF; border-bottom: 2px solid #566573; padding-bottom: 10px; text-align: center; }

    /* --- Botões Gigantes (SIM e NÃO) --- */
    div[data-testid="stHorizontalBlock"] {
        gap: 30px; 
    }

    /* Regras para o CONTAINER do botão (cor, altura, sombra) */
    .stButton > button {
        height: 400px;
        border-radius: 20px;
        border: none;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1); 
        transition: all 0.2s ease-in-out; 
    }
    
    /* ############################################################### */
    /* ### AQUI ESTÁ A CORREÇÃO QUE FAZ O TEXTO FICAR GIGANTE ### */
    /* Regras para o TEXTO <p> DENTRO do botão */
    .stButton > button p {
        font-size: 100px !important;  /* <- MUITO GRANDE */
        font-weight: 900;             /* <- BEM FORTE */
        color: white;                 /* <- COR BRANCA */
        text-shadow: 2px 2px 8px rgba(0,0,0,0.2);
    }
    /* ############################################################### */
    
    .stButton > button:hover {
        box-shadow: 0 12px 24px rgba(255,255,255,0.2); 
        transform: translateY(-5px); 
    }
    .stButton > button:active {
        transform: translateY(-1px); 
        box-shadow: 0 4px 8px rgba(255,255,255,0.1);
    }

    /* Alvo: Cor do Botão SIM (Verde) */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) .stButton > button {
        background-color: #2ECC71; 
    }
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) .stButton > button:hover {
        background-color: #28B463;
    }

    /* Alvo: Cor do Botão NÃO (Vermelho) */
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) .stButton > button {
        background-color: #E74C3C; 
    }
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) .stButton > button:hover {
        background-color: #CB4335;
    }

    /* --- Placares (Resultados) --- */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF; 
        border-radius: 15px;
        padding: 25px 20px;
        box-shadow: 0 4px 12px rgba(255,255,255,0.1);
    }
    [data-testid="stMetric"] label { color: #566573; font-size: 20px; font-weight: 500; }
    [data-testid="stMetric"] div[data-testid="stMetricValue"] { color: #2C3E50; font-size: 48px; font-weight: bold; }

    /* --- Botão Zerar (na Barra Lateral) --- */
    [data-testid="stSidebar"] [data-testid="stButton"] > button {
        background-color: #FADBD8; 
        color: #CB4335; 
        border: 1px solid #CB4335;
        width: 100%;
    }
    [data-testid="stSidebarContent"] { background-color: #0E0E0E; }
</style>
"""

# --- 3. Funções das Páginas ---

def pagina_votacao():
    """Define a página principal de votação"""
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

    # Títulos
    st.title("Você é a favor da disponibilização do TAP para venda?")
    st.subheader("Vote clicando em SIM ou NÃO")

    # Botões Gigantes
    col1, col2 = st.columns(2, gap="large")
    with col1:
        if st.button("SIM", use_container_width=True):
            st.session_state.votos_sim += 1
    with col2:
        if st.button("NÃO", use_container_width=True):
            st.session_state.votos_nao += 1

    # Separador
    st.write("<br><br>", unsafe_allow_html=True)

    # Placar: APENAS O TOTAL
    total_votos = st.session_state.votos_sim + st.session_state.votos_nao
    
    # Coloca o placar total em uma coluna central para destaque
    _, col_total, _ = st.columns([1, 1, 1], gap="large")
    with col_total:
        st.metric(label="VOTOS TOTAIS", value=total_votos)

def pagina_resultados():
    """Define a página de resultados e administração"""
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
    
    st.title("Resultados e Administração")

    # Botão de Zerar Votação
    st.header("Controle da Votação")
    st.write("Use o botão abaixo para reiniciar a contagem de votos.")
    if st.button("Zerar Votação", use_container_width=True):
        st.session_state.votos_sim = 0
        st.session_state.votos_nao = 0
        st.rerun() 
    
    # Separador
    st.write("<br><br>", unsafe_allow_html=True)

    # Resultados Detalhados
    st.header("Placar Detalhado")
    total_votos = st.session_state.votos_sim + st.session_state.votos_nao
    
    res1, res2, res3 = st.columns(3, gap="large")
    with res1:
        st.metric(label="VOTOS SIM", value=st.session_state.votos_sim)
    with res2:
        st.metric(label="VOTOS NÃO", value=st.session_state.votos_nao)
    with res3:
        st.metric(label="VOTOS TOTAIS", value=total_votos)

# --- 4. Execução Principal (Navegação) ---

# Inicializa os contadores na "memória" da sessão
if 'votos_sim' not in st.session_state:
    st.session_state.votos_sim = 0
if 'votos_nao' not in st.session_state:
    st.session_state.votos_nao = 0

# Define as páginas que estarão disponíveis no menu lateral (hambúrguer)
pg = st.navigation(
    {
        "Principal": [
            st.Page(pagina_votacao, title="Votação", icon="🗳️", default=True)
        ],
        "Administração": [
            st.Page(pagina_resultados, title="Resultados", icon="📊")
        ]
    }
)

# Executa a navegação
pg.run()