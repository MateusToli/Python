# importar base de dados
import os 
import pandas as pd
import win32com.client as win32
tabela_vendas = pd.read_excel('vendas.xlsx')

# visualizar a base de dados
os.system('cls')
pd.set_option('display.max_columns', None)
print(tabela_vendas)

# calcular o faturamento por loja

faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)
print('\n\n')

# quantidade de produtos vendidos por loja

quantidade_vendidos = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade_vendidos)
print('\n\n')

# ticket médio (faturamento/quantidade de produtos vendidos por loja)

ticket_medio = (faturamento['Valor Final'] / quantidade_vendidos['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
print(ticket_medio)
print('\n\n')

# enviar email com relatório

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'mateusareas11@gmail.com'
mail.Subject = 'Relatório de Vendas'
mail.HTMLBody = f'''
<p>Prezados,</p> 

<p>Segue o Relatório de Vendas por Loja.</p> 

<p>Faturamento:</p>  
{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade Vendida:</p> 
{quantidade_vendidos.to_html()}

<p>Ticket Médio por Loja:</p> 
{ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

<p>Qualquer dúvida estou à disposição.</p> 

<p>Att.,</p> 
<p>Mateus</p> 
'''

mail.Send()