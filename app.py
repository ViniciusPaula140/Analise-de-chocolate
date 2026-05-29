import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Dashboard Páscoa 2026", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. CARREGAMENTO DOS DADOS (Conexão Direta com o GitHub)
@st.cache_data(ttl=600) # O ttl=600 faz ele checar o github a cada 10 minutos se tem atualização
def carregar_dados():
    # URLs "Raw" do seu repositório no GitHub
    url_macro = "https://raw.githubusercontent.com/ViniciusPaula140/Analise-de-chocolate/main/dataset_projeto_pascoa.xlsx"
    url_chocolates = "https://raw.githubusercontent.com/ViniciusPaula140/Analise-de-chocolate/main/base_completa_chocolates.xlsx"
    
    # Faz o download e leitura automática via Pandas
    df_macro = pd.read_excel(url_macro)
    df_macro['Data'] = pd.to_datetime(df_macro['Data'])
    
    df_chocolates = pd.read_excel(url_chocolates)
    
    return df_macro, df_chocolates

try:
    df_macro, df_chocolates = carregar_dados()
except Exception as e:
    st.error(f"⚠️ Erro ao conectar com o GitHub. Verifique sua conexão com a internet ou se o repositório está público. Erro: {e}")
    st.stop()

# 3. CSS MÁGICO (Ajustes de espaçamento, alinhamento e contraste)
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
        text-align: left; 
        font-size: 38px; 
        font-weight: 800;
        margin-bottom: 50px; 
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
    
    .cartao-kpi { 
        background: linear-gradient(135deg, #FFFFFF, #F4EBD9);
        padding: 20px 10px; 
        text-align: center; 
        border-radius: 10px; 
        height: 120px; 
        border: 2px solid #D4A373; 
        box-shadow: 0px 6px 12px rgba(0,0,0,0.12); 
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

    hr.linha-divisoria {
        border: none;
        height: 2px;
        background-color: #B08D6A; 
        margin: 40px 0; 
    }
    </style>
""", unsafe_allow_html=True)

# 4. BARRA LATERAL (Filtros)
with st.sidebar:
    st.header("🍫 Filtros do Dashboard")
    st.markdown("---")
    ano_selecionado = st.radio(
        "Selecione o Período:",
        ["Todos os anos", "2023", "2024", "2025", "2026"]
    )
    st.markdown("---")
    st.info("💡 Pode minimizar este menu clicando no 'X' ou na setinha ( > ) no canto superior esquerdo.")

# LÓGICA DE FILTRAGEM (Alimentando os Gráficos)
if ano_selecionado == "Todos os anos":
    df_filtrado = df_macro.copy()
else:
    df_filtrado = df_macro[df_macro['Data'].dt.year == int(ano_selecionado)].copy()


# 5. TOPO PRINCIPAL: O Banner e os KPIs
st.markdown('<div class="titulo-dashboard">Análise Logística e de Custos: Especial Páscoa</div>', unsafe_allow_html=True)

# Divide o topo em 3 colunas para os cartões
k1, k2, k3 = st.columns(3)
with k1:
    st.markdown('<div class="cartao-kpi"><span class="kpi-titulo">Preço Cacau (Spot)</span><span class="kpi-valor">$ 9.850</span></div>', unsafe_allow_html=True)
with k2:
    st.markdown('<div class="cartao-kpi"><span class="kpi-titulo">Inflação de Alimentos</span><span class="kpi-valor">1.2%</span></div>', unsafe_allow_html=True)
with k3:
    st.markdown('<div class="cartao-kpi"><span class="kpi-titulo">Cotação Dólar</span><span class="kpi-valor">R$ 5,15</span></div>', unsafe_allow_html=True)

st.markdown("<hr class='linha-divisoria'>", unsafe_allow_html=True)

# 6. A GRANDE DIVISÃO DOS GRÁFICOS: Esquerda e Direita
col_esq, col_dir = st.columns(2, gap="large")

# ================= METADE ESQUERDA =================
with col_esq:
    # QUADRANTE 1: Custos e Insumos
    st.markdown('<div class="cabecalho-chocolate">CUSTOS E INSUMOS</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown('<div class="sub-caramelo">Selic, Dólar e Inflação</div>', unsafe_allow_html=True)
        
        # INJEÇÃO DO GRÁFICO 1 (Dual-Axis Plot)
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        
        # --- EIXO PRIMÁRIO (Esquerda) ---
        linha_dolar = ax1.plot(df_filtrado['Data'], df_filtrado['Dolar'], color='#27ae60', linewidth=2, linestyle='--', label='Dólar (R$)')
        linha_selic = ax1.plot(df_filtrado['Data'], df_filtrado['Selic'], color='#8e44ad', linewidth=2, linestyle=':', label='Selic (%)')
        
        ax1.set_ylabel('Cotação (R$) / Selic (%)', color='#2c3e50', fontsize=9, fontweight='bold')
        ax1.tick_params(axis='y', labelcolor='#2c3e50', labelsize=8)
        ax1.tick_params(axis='x', labelsize=8)
        ax1.grid(axis='y', linestyle='--', alpha=0.3)
        fig1.autofmt_xdate(rotation=45)
        
        # --- EIXO SECUNDÁRIO (Direita) ---
        ax2 = ax1.twinx()
        linha_inflacao = ax2.plot(df_filtrado['Data'], df_filtrado['Inflacao_Alimentos'], color='#e74c3c', linewidth=3, linestyle='-', label='Inflação (%)')
        ax2.set_ylabel('Inflação (%)', color='#e74c3c', fontsize=9, fontweight='bold')
        ax2.tick_params(axis='y', labelcolor='#e74c3c', labelsize=8)
        
        # --- CONSOLIDAÇÃO DAS LEGENDAS ---
        linhas = linha_dolar + linha_selic + linha_inflacao
        labels = [l.get_label() for l in linhas]
        ax1.legend(linhas, labels, loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=3, frameon=False, fontsize=8)
        
        # Transparência para casar com a cor do Dashboard
        fig1.patch.set_alpha(0)
        ax1.patch.set_alpha(0)
        
        st.pyplot(fig1, use_container_width=True)

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