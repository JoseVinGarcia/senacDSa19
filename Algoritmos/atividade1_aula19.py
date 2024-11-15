# ATIVIDADE 1

import pandas as pd
import numpy as np
import os

# 1. Coletando Dados
try:
    tb_vendas = pd.read_csv("tb_Vendas2017_Miranda.csv", sep=";", encoding="iso-8859-1")
    tb_produtos = pd.read_csv("tb_CadastroProdutos2017_Miranda.csv", sep=";", encoding="iso-8859-1")

    df_vendas = tb_vendas[["ID Produto", "Quantidade Vendida"]]
    df_produtos = tb_produtos[["ID Produto", "Preco Unitario"]]
    
    # convertendo preco unitario para numero
    df_produtos.loc[:, "Preco Unitario"] = df_produtos["Preco Unitario"].str.replace(",",".").astype(float)
    
    # NAO USADO - Convertendo arquivos
    # df_produtos.loc[:, "ID Produto"] = df_produtos["ID Produto"].astype(str)
    # df_vendas.loc[:, "ID Produto"] = df_vendas["ID Produto"].astype(str)
    # df_vendas.loc[:, "Quantidade Vendida"] = df_vendas["Quantidade Vendida"].astype(int)

    # Unindo os dados das duas tabelas
    df_vendasprodutos = pd.merge(df_vendas, df_produtos, on="ID Produto")

    # Descobrindo o valor total vendido
    df_vendasprodutos["Valor Total"] = df_vendasprodutos["Quantidade Vendida"] * df_vendasprodutos["Preco Unitario"]

    # Print de teste
    print(df_vendasprodutos)

except Exception as e:
    print(f"Erro {e}")
    exit()

# 2. Interpretando Dados
try:

    
except Exception as e:
    print(f"Erro {e}")
