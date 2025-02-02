from processamento_dados import Data

path_json = './data_raw/dados_empresaA.json'
path_csv = './data_raw/dados_empresaB.csv'
path_combined_data = './data_processed/dados_fusao.csv'

#Extract the data
dados_empresa_A = Data(path_json, 'json')
print(f'Colunas: {dados_empresa_A.collum_names}')
print(f'Linhas: {dados_empresa_A.size}\n')

dados_empresa_B = Data(path_csv, 'csv')
print(f'Colunas: {dados_empresa_B.collum_names}')
print(f'Linhas: {dados_empresa_B.size}\n')

#Transforming the datas
key_mapping = {
'Nome do Item': 'Nome do Produto',
'Classificação do Produto': 'Categoria do Produto',
'Valor em Reais (R$)': 'Preço do Produto (R$)',
'Quantidade em Estoque': 'Quantidade em Estoque',
'Nome da Loja': 'Filial',
'Data da Venda': 'Data da Venda'
}

dados_empresa_B.rename_collums(key_mapping)

## Joining the data
dados_fusao = Data.join(dados_empresa_A, dados_empresa_B)
print(dados_fusao.collum_names)
print(dados_fusao.size)

##Loading the data
dados_fusao.saving_data(path_combined_data)
print(f'Dados salvos em {path_combined_data}')