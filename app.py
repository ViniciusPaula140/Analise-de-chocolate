import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Dashboard Páscoa 2026", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. CSS MÁGICO (Otimizado para aproveitar o máximo da tela e dar espaço ao topo)
st.markdown("""
    <style>
    /* Estica o dashboard para as bordas e controla o topo */
    .block-container {
        padding-top: 2rem !important; 
        padding-bottom: 1rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 95% !important;
    }
    
    .cabecalho-laranja { background-color: #d97726; color: white; padding: 10px; text-align: center; border-radius: 15px; font-size: 20px; font-weight: bold; margin-bottom: 15px;}
    .sub-azul { background-color: #92d3f5; color: black; padding: 8px; text-align: center; border-radius: 10px; font-size: 16px; margin-bottom: 10px;}
    .cartao-amarelo { background-color: #ffcc00; color: black; padding: 25px 10px; text-align: center; border-radius: 10px; font-size: 20px; font-weight: bold; height: 130px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);}
    
    /* Aumentei a altura de 200px para 320px para preencher a tela toda */
    .grafico-falso { background-color: white; border: 1px dashed #bbb; height: 320px; border-radius: 10px; display: flex; align-items: center; justify-content: center; color: #888; font-style: italic;}
    
    /* Classe para dar o espaço do futuro cabeçalho */
    .espaco-cabecalho { margin-bottom: 60px; }
    </style>
""", unsafe_allow_html=True)

# 3. BARRA LATERAL (Filtros)
with st.sidebar:
    st.header("Filtros do Dashboard")
    st.markdown("---")
    ano_selecionado = st.radio(
        "Selecione o Período:",
        ["Todos os anos", "2023", "2024", "2025", "2026"]
    )
    st.markdown("---")
    st.info("💡 Pode minimizar este menu clicando no 'X' ou na setinha ( > ) no canto superior esquerdo.")

# 4. TOPO PRINCIPAL: Título e KPIs
st.title("Dashboard")

# Espaço em branco garantido para o futuro cabeçalho
st.markdown('<div class="espaco-cabecalho"></div>', unsafe_allow_html=True)

# Divide o topo em 3 colunas para os cartões
k1, k2, k3 = st.columns(3)
with k1:
    st.markdown('<div class="cartao-amarelo">PREÇO CACAU<br><br>XXXX</div>', unsafe_allow_html=True)
with k2:
    st.markdown('<div class="cartao-amarelo">INFLAÇÃO<br><br>XXXX</div>', unsafe_allow_html=True)
with k3:
    st.markdown('<div class="cartao-amarelo">DOLAR<br><br>XXXX</div>', unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

# 5. A GRANDE DIVISÃO DOS GRÁFICOS: Esquerda e Direita (Maximizados)
col_esq, col_dir = st.columns(2, gap="large")

# ================= METADE ESQUERDA =================
with col_esq:
    # QUADRANTE 1: Custos e Insumos
    st.markdown('<div class="cabecalho-laranja">Custos e insumos</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="sub-azul">Selic, dolar e inflação</div>', unsafe_allow_html=True)
        st.markdown('<div class="grafico-falso">[Espaço do Gráfico 1]</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="sub-azul">Insumos x Cenário macroeconômico</div>', unsafe_allow_html=True)
        st.markdown('<div class="grafico-falso">[Espaço do Gráfico 2]</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # QUADRANTE 3: Industria
    st.markdown('<div class="cabecalho-laranja">Industria</div>', unsafe_allow_html=True)
    c3, c4 = st.columns(2)
    with c3:
        st.markdown('<div class="sub-azul">Cacau X Dólar</div>', unsafe_allow_html=True)
        st.markdown('<div class="grafico-falso">[Espaço do Gráfico 3]</div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="sub-azul">Efeito dominó Petróleo</div>', unsafe_allow_html=True)
        st.markdown('<div class="grafico-falso">[Espaço do Gráfico 4]</div>', unsafe_allow_html=True)

# ================= METADE DIREITA =================
with col_dir:
    # QUADRANTE 2: Troca de materiais
    st.markdown('<div class="cabecalho-laranja">Troca de materiais</div>', unsafe_allow_html=True)
    c5, c6 = st.columns(2)
    with c5:
        st.markdown('<div class="sub-azul">Selic, dolar e inflação</div>', unsafe_allow_html=True)
        st.markdown('<div class="grafico-falso">[Espaço do Gráfico 5]</div>', unsafe_allow_html=True)
    with c6:
        st.markdown('<div class="sub-azul">Gatilho Skimpflation</div>', unsafe_allow_html=True)
        st.markdown('<div class="grafico-falso">[Espaço do Gráfico 6]</div>', unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)

    # NOVO QUADRANTE 4: Previsão
    st.markdown('<div class="cabecalho-laranja">Previsão</div>', unsafe_allow_html=True)
    c7, c8 = st.columns(2)
    with c7:
        st.markdown('<div class="sub-azul">Previsão de Custos</div>', unsafe_allow_html=True)
        st.markdown('<div class="grafico-falso">[Espaço do Gráfico: Projeção]</div>', unsafe_allow_html=True)
    with c8:
        st.markdown('<div class="sub-azul">Preço Chocolates 2027</div>', unsafe_allow_html=True)
        st.markdown('<div class="grafico-falso">[Espaço do Gráfico: Ranking 2027]</div>', unsafe_allow_html=True)