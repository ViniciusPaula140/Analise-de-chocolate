import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrap_extremo_chocolates(marca):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }
    
    # Lista de termos para varrer todas as categorias
    termos = ["ovo de pascoa", "caixa de bombom", "barra de chocolate", "pacote atacado"]
    produtos_da_marca = []

    for termo in termos:
        url = f"https://lista.mercadolivre.com.br/{termo}-{marca}"
        print(f"🕵️ Varrendo: {marca} + {termo}...")
        
        try:
            response = requests.get(url, headers=headers, timeout=15)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Pegamos os 15 primeiros de cada categoria para ter volume
            items = soup.find_all('li', class_='ui-search-layout__item', limit=15)
            if not items:
                items = soup.find_all('div', class_='ui-search-result__wrapper', limit=15)

            for item in items:
                try:
                    nome = item.find(['h2', 'h3']).text.strip()
                    
                    # Filtro de segurança: garantir que a marca está no nome
                    if marca.lower() not in nome.lower():
                        continue

                    preco_container = item.find('span', class_='andes-money-amount__fraction')
                    preco_inteiro = preco_container.text.replace('.', '').replace(',', '')
                    
                    try:
                        preco_centavos = item.find('span', class_='andes-money-amount__cents').text
                    except:
                        preco_centavos = "00"

                    valor_float = float(f"{preco_inteiro}.{preco_centavos}")

                    produtos_da_marca.append({
                        'Marca': marca.capitalize(),
                        'Produto': nome,
                        'Preco_Hoje': valor_float,
                        'Fonte': 'Mercado Livre'
                    })
                except:
                    continue
            time.sleep(1) # Pausa entre termos para evitar block
        except Exception as e:
            print(f"❌ Erro em {marca} {termo}: {e}")
            
    return produtos_da_marca

# --- Execução em Massa ---
marcas_lideres = ["Lacta", "Nestle", "Garoto", "Ferrero", "Hershey"]
base_gigante = []

for marca in marcas_lideres:
    dados = scrap_extremo_chocolates(marca)
    base_gigante.extend(dados)

if base_gigante:
    df_final = pd.DataFrame(base_gigante)
    
    # Remove produtos duplicados (caso apareçam em mais de uma busca)
    df_final = df_final.drop_duplicates(subset=['Produto', 'Preco_Hoje'])
    
    df_final.to_excel('base_completa_chocolates.xlsx', index=False)
    
    print(f"\n✅ Mapeamento concluído! {len(df_final)} produtos capturados.")
    print(df_final.groupby('Marca').size())
else:
    print("\n❌ Falha na extração em massa.")