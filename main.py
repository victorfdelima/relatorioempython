import pandas as pd

# Utilizei caminho do documento, no caso no Google Drive
tabela_vendas = pd.read_excel("/content/drive/MyDrive/Colab Notebooks/Vendas.xlsx")

tabela_faturamento = tabela_vendas[["ID Loja", "Valor Final"]].groupby("ID Loja").sum("Valor Final")
tabela_faturamento = tabela_faturamento.sort_values(by="Valor Final", ascending=True)
tabela_quantidade = tabela_vendas [["ID Loja", "Quantidade"]].groupby("ID Loja").sum()
ticket_medio = (tabela_faturamento["Valor Final"] / tabela_quantidade["Quantidade"]).to_frame()
ticket_medio = ticket_medio.rename(columns={0: "Ticket Médio"})


def enviar_email("nome_da_loja, tabela"):
  import smtplib
  import email.message

  server = smtplib.SMTP('smtp.gmail.com:587')  
  corpo_email = f"""
  <p>Prezados,</p>
  <p>Segue relatório de Vendas</p>
  {tabela.to_html()}
  <p>Qualquer dúvida estou a disposição.</p>
  """
  msg = email.message.Message()
  msg['Subject'] = f"Relatório de Vendas - {nome_da_loja}"
  msg['From'] = 'seuemail@gmail.com'
  msg['To'] = 'teste@teste.com'
  password = "MinhaSenha"
  msg.add_header('Content-Type', 'text/html')
  msg.set_payload(corpo_email )
  
  s = smtplib.SMTP('smtp.gmail.com: 587')
  s.starttls()
  # Credenciais de Login para enviar emails.
  s.login(msg['From'], password)
  s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
  # Caso tenha mais de 1000000 de linhas, retirar o print('Email enviado')
  print('Email enviado')

# Função de enviar email
tabela_completa = tabela_faturamento.join(tabela_quantidade).join(ticket_medio)
enviar_email("Diretoria", tabela_completa)

# Função de automatizar processo de envio de email

listas_lojas = tabela_vendas["ID Loja"].unique()
for loja in lista_lojas
  tabela_loja = tabela_vendas.loc[tabela_vendas["ID Loja"] == loja, ["ID Loja", "Quantidade", "Valor Final"]]
  tabela_loja = tabela_loja.groupby("ID Loja").sum()
  tabela_loja["Ticket Medio"] = tabela_loja["Valor Final"] / tabela_loja["Quantidade"]

enviar_email(loja, tabela_loja)
  
  
  
