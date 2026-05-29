import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
import warnings

# Ignora os avisos de terminal do Pandas para manter o log limpo
warnings.filterwarnings('ignore')

# ==========================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Dashboard Páscoa 2026", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. CARREGAMENTO DOS DADOS (Local Seguro)
# ==========================================
@st.cache_data
def carregar_dados():
    df_macro = pd.read_excel("dataset_projeto_pascoa.xlsx")
    df_macro['Data'] = pd.to_datetime(df_macro['Data'])
    df_chocolates = pd.read_excel("base_completa_chocolates.xlsx")
    return df_macro, df_chocolates

try:
    df_macro, df_chocolates = carregar_dados()
except Exception as e:
    st.error(f"⚠️ Erro ao carregar os dados locais: {e}. Verifique se os arquivos .xlsx estão na mesma pasta do app.py.")
    st.stop()

# ==========================================
# 3. CSS MÁGICO (Estética Premium)
# ==========================================
st.markdown("""
    <style>
    .block-container {
        padding-top: 1.5rem !important; 
        padding-bottom: 1rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 95% !important;
    }
    .stApp { background-color: #FCF9F2; }

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
    
    .kpi-titulo { color: #845422; font-size: 15px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px;}
    .kpi-valor { font-size: 30px; font-weight: 900; color: #3e1f04; display: block; margin-top: 5px;}
    
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

    hr.linha-divisoria { border: none; height: 2px; background-color: #B08D6A; margin: 40px 0; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 4. BARRA LATERAL (Filtros)
# ==========================================
with st.sidebar:
    st.header("🍫 Filtros do Dashboard")
    st.markdown("---")
    ano_selecionado = st.radio(
        "Selecione o Período:",
        ["Todos os anos", "2024", "2025", "2026"]
    )
    st.markdown("---")
    st.info("💡 Pode minimizar este menu clicando na setinha ( > ) no canto superior esquerdo.")

# Lógica de Filtragem Universal
if ano_selecionado == "Todos os anos":
    df_filtrado = df_macro.copy()
else:
    df_filtrado = df_macro[df_macro['Data'].dt.year == int(ano_selecionado)].copy()

# ==========================================
# 5. TOPO PRINCIPAL: Banner e KPIs
# ==========================================
st.markdown('<div class="titulo-dashboard">Análise Logística e de Custos: Especial Páscoa</div>', unsafe_allow_html=True)

k1, k2, k3 = st.columns(3)
with k1:
    st.markdown('<div class="cartao-kpi"><span class="kpi-titulo">Preço Cacau (Spot)</span><span class="kpi-valor">$ 9.850</span></div>', unsafe_allow_html=True)
with k2:
    st.markdown('<div class="cartao-kpi"><span class="kpi-titulo">Inflação de Alimentos</span><span class="kpi-valor">1.2%</span></div>', unsafe_allow_html=True)
with k3:
    st.markdown('<div class="cartao-kpi"><span class="kpi-titulo">Cotação Dólar</span><span class="kpi-valor">R$ 5,15</span></div>', unsafe_allow_html=True)

st.markdown("<hr class='linha-divisoria'>", unsafe_allow_html=True)

# ==========================================
# 6. A GRANDE DIVISÃO DOS GRÁFICOS
# ==========================================
col_esq, col_dir = st.columns(2, gap="large")

# ================== METADE ESQUERDA ==================
with col_esq:
    # --- QUADRANTE 1: CUSTOS E INSUMOS ---
    st.markdown('<div class="cabecalho-chocolate">CUSTOS E INSUMOS</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown('<div class="sub-caramelo">Selic, Dólar e Inflação</div>', unsafe_allow_html=True)
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        df_p1 = df_filtrado.copy()
        if not df_p1.empty:
            linha_dolar = ax1.plot(df_p1['Data'], df_p1['Dolar'], color='#27ae60', linewidth=2, linestyle='--', label='Dólar (R$)')
            linha_selic = ax1.plot(df_p1['Data'], df_p1['Selic'], color='#8e44ad', linewidth=2, linestyle=':', label='Selic (%)')
            
            ax1.set_ylabel('Cotação (R$) / Selic (%)', color='#2c3e50', fontsize=9, fontweight='bold')
            ax1.tick_params(axis='y', labelcolor='#2c3e50', labelsize=8)
            ax1.tick_params(axis='x', labelsize=8)
            ax1.grid(axis='y', linestyle='--', alpha=0.3)
            fig1.autofmt_xdate(rotation=45)
            
            ax2 = ax1.twinx()
            linha_inflacao = ax2.plot(df_p1['Data'], df_p1['Inflacao_Alimentos'], color='#e74c3c', linewidth=3, linestyle='-', label='Inflação (%)')
            ax2.set_ylabel('Inflação (%)', color='#e74c3c', fontsize=9, fontweight='bold')
            ax2.tick_params(axis='y', labelcolor='#e74c3c', labelsize=8)
            
            linhas = linha_dolar + linha_selic + linha_inflacao
            labels = [l.get_label() for l in linhas]
            ax1.legend(linhas, labels, loc='upper center', bbox_to_anchor=(0.5, -0.25), ncol=3, frameon=False, fontsize=8)
            fig1.patch.set_alpha(0)
            ax1.patch.set_alpha(0)
            st.pyplot(fig1, use_container_width=True)

    with c2:
        st.markdown('<div class="sub-caramelo">Insumos x Cenário Macro</div>', unsafe_allow_html=True)
        fig2, ax3 = plt.subplots(figsize=(6, 4))
        df_p2 = df_filtrado.copy()
        if not df_p2.empty:
            alimentos = ['Cacau', 'Acucar', 'Leite', 'Soja', 'Milho', 'Trigo']
            df_p2[alimentos] = df_p2[alimentos].ffill().bfill()
            
            for item in alimentos:
                valor_inicial = df_p2[item].iloc[0]
                df_p2[f'{item}_Var'] = ((df_p2[item] / valor_inicial) - 1) * 100
                
            cores = sns.color_palette("husl", len(alimentos))
            for i, item in enumerate(alimentos):
                ax3.plot(df_p2['Data'], df_p2[f'{item}_Var'], label=item, linewidth=2, color=cores[i])

            passo = max(1, len(df_p2) // 4) 
            indices_eixo = range(0, len(df_p2), passo)
            datas_sel = df_p2['Data'].iloc[indices_eixo]
            valores_dolar = df_p2['Dolar'].iloc[indices_eixo].apply(lambda x: f'USD {x:.2f}')
            valores_selic = df_p2['Selic'].iloc[indices_eixo].apply(lambda x: f'SELIC {x:.1f}%')
            
            labels_completos = [
                f"{d.strftime('%m/%y')}\n{v}\n{s}"
                for d, v, s in zip(datas_sel, valores_dolar, valores_selic)
            ]
            
            ax3.set_xticks(datas_sel)
            ax3.set_xticklabels(labels_completos, fontsize=7, fontweight='bold')
            ax3.set_ylabel('Variação Acumulada (%)', color='#2c3e50', fontsize=9, fontweight='bold')
            ax3.axhline(0, color='black', linestyle='--', linewidth=1, alpha=0.5)
            ax3.tick_params(axis='y', labelcolor='#2c3e50', labelsize=8)
            ax3.grid(axis='y', linestyle='--', alpha=0.3)
            
            ax3.legend(loc='upper center', bbox_to_anchor=(0.5, -0.25), ncol=3, frameon=False, fontsize=8)
            fig2.patch.set_alpha(0)
            ax3.patch.set_alpha(0)
            st.pyplot(fig2, use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- QUADRANTE 3: INDÚSTRIA ---
    st.markdown('<div class="cabecalho-chocolate">INDÚSTRIA</div>', unsafe_allow_html=True)
    c3, c4 = st.columns(2)
    
    with c3:
        st.markdown('<div class="sub-caramelo">Cacau X Dólar</div>', unsafe_allow_html=True)
        fig3, ax3_1 = plt.subplots(figsize=(6, 4))
        df_p3 = df_filtrado.copy()
        if not df_p3.empty:
            df_p3[['Dolar', 'Cacau']] = df_p3[['Dolar', 'Cacau']].ffill().bfill()
            df_p3 = df_p3.tail(15) # Time Windowing
            eixo_x = df_p3['Data'].dt.strftime('%m/%y')
            
            bars = ax3_1.bar(eixo_x, df_p3['Dolar'], color='skyblue', alpha=0.7, label='Dólar (R$)')
            ax3_1.set_ylabel('Taxa de Câmbio (R$)', color='#2980b9', fontsize=9, fontweight='bold')
            ax3_1.tick_params(axis='y', labelcolor='#2980b9', labelsize=8)
            ax3_1.tick_params(axis='x', labelsize=8, rotation=45)
            
            for bar in bars:
                height = bar.get_height()
                ax3_1.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                           f'{height:.1f}', ha='center', va='bottom', fontsize=7, fontweight='bold', color='#1a5276')
                           
            ax3_2 = ax3_1.twinx()
            line = ax3_2.plot(eixo_x, df_p3['Cacau'], color='brown', marker='o', linewidth=2, label='Cacau (USD)')
            ax3_2.set_ylabel('Cacau (USD)', color='brown', fontsize=9, fontweight='bold')
            ax3_2.tick_params(axis='y', labelcolor='brown', labelsize=8)
            
            ax3_1.grid(axis='y', linestyle='--', alpha=0.3)
            linhas_legenda = [bars[0], line[0]]
            labels_legenda = ['Dólar (R$)', 'Cacau (USD)']
            ax3_1.legend(linhas_legenda, labels_legenda, loc='upper center', bbox_to_anchor=(0.5, -0.25), ncol=2, frameon=False, fontsize=8)
            
            fig3.patch.set_alpha(0)
            ax3_1.patch.set_alpha(0)
            ax3_2.patch.set_alpha(0)
            st.pyplot(fig3, use_container_width=True)

    with c4:
        st.markdown('<div class="sub-caramelo">Efeito Dominó Petróleo X Açúcar</div>', unsafe_allow_html=True)
        fig4, ax4 = plt.subplots(figsize=(6, 4))
        df_p4 = df_filtrado.copy()
        if not df_p4.empty:
            df_p4[['Petroleo_6M_Atras', 'Acucar']] = df_p4[['Petroleo_6M_Atras', 'Acucar']].ffill().bfill()
            
            scaler_p4 = MinMaxScaler(feature_range=(0, 100))
            df_p4['Pet_Norm'] = scaler_p4.fit_transform(df_p4[['Petroleo_6M_Atras']])
            df_p4['Acu_Norm'] = scaler_p4.fit_transform(df_p4[['Acucar']])
            
            ax4.plot(df_p4['Data'], df_p4['Pet_Norm'], label='Petróleo (Lag 6M)', color='#2c3e50', linewidth=3, linestyle='--')
            ax4.plot(df_p4['Data'], df_p4['Acu_Norm'], label='Açúcar (Spot)', color='#e67e22', linewidth=4)
            ax4.fill_between(df_p4['Data'], df_p4['Pet_Norm'], df_p4['Acu_Norm'], color='orange', alpha=0.1)
            
            ax4.set_ylabel('Escala Normalizada (0-100)', color='#2c3e50', fontsize=9, fontweight='bold')
            ax4.tick_params(axis='y', labelcolor='#2c3e50', labelsize=8)
            ax4.tick_params(axis='x', labelsize=8)
            ax4.grid(axis='y', linestyle='--', alpha=0.3)
            fig4.autofmt_xdate(rotation=45)
            
            ax4.legend(loc='upper center', bbox_to_anchor=(0.5, -0.25), ncol=2, frameon=False, fontsize=8)
            fig4.patch.set_alpha(0)
            ax4.patch.set_alpha(0)
            st.pyplot(fig4, use_container_width=True)

# ================== METADE DIREITA ==================
with col_dir:
    # --- QUADRANTE 2: TROCA DE MATERIAIS ---
    st.markdown('<div class="cabecalho-chocolate">TROCA DE MATERIAIS</div>', unsafe_allow_html=True)
    c5, c6 = st.columns(2)
    
    with c5:
        st.markdown('<div class="sub-caramelo">Custo de Substituição</div>', unsafe_allow_html=True)
        fig5, ax5 = plt.subplots(figsize=(6, 4))
        df_p5 = df_filtrado.copy()
        
        if not df_p5.empty:
            scaler5 = MinMaxScaler()
            cols_lag = ['Cacau_12M_Atras', 'Soja_12M_Atras', 'Milho_12M_Atras', 'Trigo_12M_Atras']
            
            df_p5[cols_lag] = df_p5[cols_lag].ffill().bfill()
            df_p5[[c + '_Norm' for c in cols_lag]] = scaler5.fit_transform(df_p5[cols_lag])
            
            ax5.plot(df_p5['Data'], df_p5['Cacau_12M_Atras_Norm'], color='#7e5109', linewidth=4, label='Cacau (Premium)')
            ax5.plot(df_p5['Data'], df_p5['Soja_12M_Atras_Norm'], color='#27ae60', linewidth=2, linestyle='--', label='Soja')
            ax5.plot(df_p5['Data'], df_p5['Milho_12M_Atras_Norm'], color='#f1c40f', linewidth=2, linestyle='--', label='Milho')
            ax5.plot(df_p5['Data'], df_p5['Trigo_12M_Atras_Norm'], color='#95a5a6', linewidth=2, linestyle='--', label='Trigo')
            ax5.fill_between(df_p5['Data'], df_p5['Cacau_12M_Atras_Norm'], df_p5['Soja_12M_Atras_Norm'], color='gray', alpha=0.1)
            
            ax5.set_ylabel('Impacto Normalizado (0-1)', color='#2c3e50', fontsize=9, fontweight='bold')
            ax5.tick_params(axis='y', labelcolor='#2c3e50', labelsize=8)
            ax5.tick_params(axis='x', labelsize=8)
            ax5.grid(axis='y', linestyle='--', alpha=0.3)
            fig5.autofmt_xdate(rotation=45)
            ax5.legend(loc='upper center', bbox_to_anchor=(0.5, -0.25), ncol=2, frameon=False, fontsize=8)
            
            fig5.patch.set_alpha(0)
            ax5.patch.set_alpha(0)
            st.pyplot(fig5, use_container_width=True)

    with c6:
        st.markdown('<div class="sub-caramelo">Gatilho Skimpflation</div>', unsafe_allow_html=True)
        fig6, ax6 = plt.subplots(figsize=(6, 4))
        df_p6 = df_filtrado.copy()
        
        if not df_p6.empty:
            scaler6 = MinMaxScaler()
            cols_gatilho = ['Cacau_12M_Atras', 'Leite']
            
            df_p6[cols_gatilho] = df_p6[cols_gatilho].ffill().bfill()
            df_p6[['Cacau_Norm', 'Leite_Norm']] = scaler6.fit_transform(df_p6[cols_gatilho])
            
            df_p6['Pressao_Dupla'] = df_p6['Cacau_Norm'] + df_p6['Leite_Norm']
            limite_critico = df_p6['Pressao_Dupla'].quantile(0.75)
            
            ax6.plot(df_p6['Data'], df_p6['Cacau_Norm'], label='Cacau (Lag 12M)', color='#8e44ad', linewidth=2.5)
            ax6.plot(df_p6['Data'], df_p6['Leite_Norm'], label='Leite (Spot)', color='#3498db', linewidth=2.5)
            
            ax6.fill_between(df_p6['Data'], 0, 1.05, 
                             where=(df_p6['Pressao_Dupla'] > limite_critico),
                             color='red', alpha=0.15, label='Alerta: Skimpflation', interpolate=True)
            
            ax6.set_ylabel('Estresse Normalizado (0-1)', color='#2c3e50', fontsize=9, fontweight='bold')
            ax6.tick_params(axis='y', labelcolor='#2c3e50', labelsize=8)
            ax6.tick_params(axis='x', labelsize=8)
            ax6.grid(axis='y', linestyle='--', alpha=0.3)
            ax6.set_ylim(0, 1.05)
            fig6.autofmt_xdate(rotation=45)
            
            ax6.legend(loc='upper center', bbox_to_anchor=(0.5, -0.25), ncol=2, frameon=False, fontsize=8)
            
            fig6.patch.set_alpha(0)
            ax6.patch.set_alpha(0)
            st.pyplot(fig6, use_container_width=True)
        
    st.markdown("<br>", unsafe_allow_html=True)

    # --- QUADRANTE 4: PREVISÃO (ESPAÇOS RESERVADOS) ---
    st.markdown('<div class="cabecalho-chocolate">PREVISÃO 2027</div>', unsafe_allow_html=True)
    c7, c8 = st.columns(2)
    with c7:
        st.markdown('<div class="sub-caramelo">Previsão de Custos</div>', unsafe_allow_html=True)
        st.markdown('<div class="grafico-falso">[Espaço do Gráfico: Projeção]</div>', unsafe_allow_html=True)
    with c8:
        st.markdown('<div class="sub-caramelo">Preço Chocolates 2027</div>', unsafe_allow_html=True)
        st.markdown('<div class="grafico-falso">[Espaço do Gráfico: Ranking 2027]</div>', unsafe_allow_html=True)