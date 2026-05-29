import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Dashboard Páscoa 2026", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. CSS MÁGICO (Ajustes de espaçamento, alinhamento e contraste)
st.markdown("""
    <style>
    .block-container {
        padding-top: 1.5rem !important; 
        padding-bottom: 1rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 95% !important;
    }

    .stApp {
        background-color: #FCF9F2;
    }

    /* Cabeçalho Maior, Alinhado à Esquerda e mais distante dos cartões */
    .titulo-dashboard {
        background: linear-gradient(135deg, #4b2e13, #845422);
        color: #F4EBD9;
        padding: 25px 30px; 
        border-radius: 12px;
        text-align: left; /* Mudança para a esquerda */
        font-size: 38px; /* Fonte aumentada */
        font-weight: 800;
        margin-bottom: 50px; /* Margem aumentada para afastar dos cartões */
        box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .cabecalho-chocolate { 
        background-color: #5C3A21; 
        color: #F4EBD9; 
        padding: 12px; 
        text-align: center; 
        border-radius: 8px; 
        font-size: 20px; 
        font-weight: bold; 
        margin-bottom: 15px;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
    }
    
    .sub-caramelo { 
        background-color: #D4A373; 
        color: #4A3018; 
        padding: 8px; 
        text-align: center; 
        border-radius: 6px; 
        font-size: 15px; 
        font-weight: 600;
        margin-bottom: 10px;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Cartões com bordas mais evidentes e sombras mais fortes */
    .cartao-kpi { 
        background: linear-gradient(135deg, #FFFFFF, #F4EBD9);
        padding: 20px 10px; 
        text-align: center; 
        border-radius: 10px; 
        height: 120px; 
        border: 2px solid #D4A373; /* Borda adicionada para destacar */
        box-shadow: 0px 6px 12px rgba(0,0,0,0.12); /* Sombra mais destacada */
        border-bottom: 6px solid #5C3A21;
    }
    
    .kpi-titulo {
        color: #845422;
        font-size: 15px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .kpi-valor {
        font-size: 30px;
        font-weight: 900;
        color: #3e1f04;
        display: block;
        margin-top: 5px;
    }
    
    .grafico-falso { 
        background-color: #FFFFFF; 
        border: 1px dashed #D4A373; 
        height: 320px; 
        border-radius: 8px; 
        display: flex; 
        align-items: center; 
        justify-content: center; 
        color: #B08D6A; 
        font-style: italic;
        box-shadow: inset 0px 0px 10px rgba(0,0,0,0.02);
    }

    /* Linha divisória mais escura e marcante */
    hr.linha-divisoria {
        border: none;
        height: 2px;
        background-color: #B08D6A; /* Marrom mais escuro */
        margin: 40px 0; /* Mais espaço em cima e embaixo */
    }
    </style>
""", unsafe_allow_html=True)

# 3. BARRA LATERAL (Filtros)
with st.sidebar:
    st.header("🍫 Filtros do Dashboard")
    st.markdown("---")
    ano_selecionado = st.radio(
        "Selecione o Período:",
        ["Todos os anos", "2023", "2024", "2025", "2026"]
    )
    st.markdown("---")
    st.info("💡 Pode minimizar este menu clicando no 'X' ou na setinha ( > ) no canto superior esquerdo.")

# 4. TOPO PRINCIPAL: O Banner e os KPIs
st.markdown('<div class="titulo-dashboard">Análise Logística e de Custos: Especial Páscoa</div>', unsafe_allow_html=True)

# Divide o topo em 3 colunas para os cartões
k1, k2, k3 = st.columns(3)
with k1:
    st.markdown('<div class="cartao-kpi"><span class="kpi-titulo">Preço Cacau (Spot)</span><span class="kpi-valor">$ 9.850</span></div>', unsafe_allow_html=True)
with k2:
    st.markdown('<div class="cartao-kpi"><span class="kpi-titulo">Inflação de Alimentos</span><span class="kpi-valor">1.2%</span></div>', unsafe_allow_html=True)
with k3:
    st.markdown('<div class="cartao-kpi"><span class="kpi-titulo">Cotação Dólar</span><span class="kpi-valor">R$ 5,15</span></div>', unsafe_allow_html=True)

# Aplica a nova linha divisória mais escura
st.markdown("<hr class='linha-divisoria'>", unsafe_allow_html=True)

# 5. A GRANDE DIVISÃO DOS GRÁFICOS: Esquerda e Direita
col_esq, col_dir = st.columns(2, gap="large")

# ================= METADE ESQUERDA =================
with col_esq:
    # QUADRANTE 1: Custos e Insumos
    st.markdown('<div class="cabecalho-chocolate">CUSTOS E INSUMOS</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="sub-caramelo">Selic, Dólar e Inflação</div>', unsafe_allow_html=True)
        st.markdown('<div class="grafico-falso">[Espaço do Gráfico 1]</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="sub-caramelo">Insumos x Cenário Macro</div>', unsafe_allow_html=True)
        st.markdown('<div class="grafico-falso">[Espaço do Gráfico 2]</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # QUADRANTE 3: Industria
    st.markdown('<div class="cabecalho-chocolate">INDÚSTRIA</div>', unsafe_allow_html=True)
    c3, c4 = st.columns(2)
    with c3:
        st.markdown('<div class="sub-caramelo">Cacau X Dólar</div>', unsafe_allow_html=True)
        st.markdown('<div class="grafico-falso">[Espaço do Gráfico 3]</div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="sub-caramelo">Efeito Dominó Petróleo</div>', unsafe_allow_html=True)
        st.markdown('<div class="grafico-falso">[Espaço do Gráfico 4]</div>', unsafe_allow_html=True)

# ================= METADE DIREITA =================
with col_dir:
    # QUADRANTE 2: Troca de materiais
    st.markdown('<div class="cabecalho-chocolate">TROCA DE MATERIAIS</div>', unsafe_allow_html=True)
    c5, c6 = st.columns(2)
    with c5:
        st.markdown('<div class="sub-caramelo">Custo de Substituição</div>', unsafe_allow_html=True)
        st.markdown('<div class="grafico-falso">[Espaço do Gráfico 5]</div>', unsafe_allow_html=True)
    with c6:
        st.markdown('<div class="sub-caramelo">Gatilho Skimpflation</div>', unsafe_allow_html=True)
        st.markdown('<div class="grafico-falso">[Espaço do Gráfico 6]</div>', unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)

    # QUADRANTE 4: Previsão
    st.markdown('<div class="cabecalho-chocolate">PREVISÃO 2027</div>', unsafe_allow_html=True)
    c7, c8 = st.columns(2)
    with c7:
        st.markdown('<div class="sub-caramelo">Previsão de Custos</div>', unsafe_allow_html=True)
        st.markdown('<div class="grafico-falso">[Espaço do Gráfico: Projeção]</div>', unsafe_allow_html=True)
    with c8:
        st.markdown('<div class="sub-caramelo">Preço Chocolates 2027</div>', unsafe_allow_html=True)
        st.markdown('<div class="grafico-falso">[Espaço do Gráfico: Ranking 2027]</div>', unsafe_allow_html=True)