{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Projeto.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "mount_file_id": "1GffC7i-y3I9s465fgBjlwtaGAFQPJ7Lw",
      "authorship_tag": "ABX9TyPCi1UXvDVpT/xRFJGh/cOh"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QhOuXBW76kGi"
      },
      "source": [
        "**Passo a passo de construção de código**:\r\n",
        "*   Passo 1. - Importar base de dados\r\n",
        "*   Passo 2. - Calcular o faturamento de cada loja\r\n",
        "*   Passo 3. - Calcular a quantidade de produtos vendidos de cada loja\r\n",
        "*   Passo 4. - Calcular o ticket médio dos produtos de cada loja\r\n",
        "*   Passo 5. - Enviar Email para a diretoria\r\n",
        "*   Passo 6. - Enviar Email para cada loja"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9PFtP5av5ttG"
      },
      "source": [
        "importei o Pandas as pd para ler a tabela em excel.\r\n",
        "\r\n",
        "\r\n",
        "\r\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "A_arL3QCz36q"
      },
      "source": [
        "import pandas as pd\r\n",
        "\r\n",
        "tabela_vendas = pd.read_excel(\"/content/drive/MyDrive/Colab Notebooks/Vendas.xlsx\")\r\n",
        "display(tabela_vendas)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3t0802ES8MeE"
      },
      "source": [
        "tabela_faturamento = tabela_vendas[[\"ID Loja\", \"Valor Final\"]].groupby(\"ID Loja\").sum(\"Valor Final\")\r\n",
        "tabela_faturamento = tabela_faturamento.sort_values(by=\"Valor Final\", ascending=True)\r\n",
        "display(tabela_faturamento)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3g9LOYBwCzw3"
      },
      "source": [
        "tabela_quantidade = tabela_vendas [[\"ID Loja\", \"Quantidade\"]].groupby(\"ID Loja\").sum()\r\n",
        "display(tabela_quantidade)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 855
        },
        "id": "I489GMbsDKhk",
        "outputId": "bc332434-18d9-4ef9-e41f-61e9609565f4"
      },
      "source": [
        "ticket_medio = (tabela_faturamento[\"Valor Final\"] / tabela_quantidade[\"Quantidade\"]).to_frame()\r\n",
        "ticket_medio = ticket_medio.rename(columns={0: \"Ticket Médio\"})\r\n",
        "display(ticket_medio)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Ticket Médio</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>ID Loja</th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Bourbon Shopping SP</th>\n",
              "      <td>194.754598</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Center Shopping Uberlândia</th>\n",
              "      <td>193.453228</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Iguatemi Campinas</th>\n",
              "      <td>197.248909</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Iguatemi Esplanada</th>\n",
              "      <td>198.098019</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Norte Shopping</th>\n",
              "      <td>189.923231</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Novo Shopping Ribeirão Preto</th>\n",
              "      <td>191.775226</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Palladium Shopping Curitiba</th>\n",
              "      <td>189.321307</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Parque Dom Pedro Shopping</th>\n",
              "      <td>194.519552</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Passei das Águas Shopping</th>\n",
              "      <td>191.345324</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Ribeirão Shopping</th>\n",
              "      <td>193.441586</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Rio Mar Recife</th>\n",
              "      <td>194.377299</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Rio Mar Shopping Fortaleza</th>\n",
              "      <td>190.044758</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Salvador Shopping</th>\n",
              "      <td>189.323868</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Shopping Barra</th>\n",
              "      <td>191.375666</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Shopping Center Interlagos</th>\n",
              "      <td>189.105014</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Shopping Center Leste Aricanduva</th>\n",
              "      <td>188.282614</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Shopping Eldorado</th>\n",
              "      <td>189.025232</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Shopping Ibirapuera</th>\n",
              "      <td>187.442394</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Shopping Iguatemi Fortaleza</th>\n",
              "      <td>194.092479</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Shopping Midway Mall</th>\n",
              "      <td>193.814404</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Shopping Morumbi</th>\n",
              "      <td>186.464974</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Shopping Recife</th>\n",
              "      <td>189.357767</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Shopping SP Market</th>\n",
              "      <td>192.871401</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Shopping União de Osasco</th>\n",
              "      <td>190.580756</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Shopping Vila Velha</th>\n",
              "      <td>187.680724</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                                  Ticket Médio\n",
              "ID Loja                                       \n",
              "Bourbon Shopping SP                 194.754598\n",
              "Center Shopping Uberlândia          193.453228\n",
              "Iguatemi Campinas                   197.248909\n",
              "Iguatemi Esplanada                  198.098019\n",
              "Norte Shopping                      189.923231\n",
              "Novo Shopping Ribeirão Preto        191.775226\n",
              "Palladium Shopping Curitiba         189.321307\n",
              "Parque Dom Pedro Shopping           194.519552\n",
              "Passei das Águas Shopping           191.345324\n",
              "Ribeirão Shopping                   193.441586\n",
              "Rio Mar Recife                      194.377299\n",
              "Rio Mar Shopping Fortaleza          190.044758\n",
              "Salvador Shopping                   189.323868\n",
              "Shopping Barra                      191.375666\n",
              "Shopping Center Interlagos          189.105014\n",
              "Shopping Center Leste Aricanduva    188.282614\n",
              "Shopping Eldorado                   189.025232\n",
              "Shopping Ibirapuera                 187.442394\n",
              "Shopping Iguatemi Fortaleza         194.092479\n",
              "Shopping Midway Mall                193.814404\n",
              "Shopping Morumbi                    186.464974\n",
              "Shopping Recife                     189.357767\n",
              "Shopping SP Market                  192.871401\n",
              "Shopping União de Osasco            190.580756\n",
              "Shopping Vila Velha                 187.680724"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kTs-RjYFFJuv"
      },
      "source": [
        "def enviar_email(\"nome_da_loja, tabela\"):\r\n",
        "import smtplib\r\n",
        "import email.message\r\n",
        "\r\n",
        "server = smtplib.SMTP('smtp.gmail.com:587')  \r\n",
        "corpo_email = f\"\"\"\r\n",
        "<p>Prezados,</p>\r\n",
        "<p>Segue relatório de Vendas</p>\r\n",
        "{tabela.to_html()}\r\n",
        "<p>Qualquer dúvida estou a disposição.</p>\r\n",
        "\"\"\"\r\n",
        "msg = email.message.Message()\r\n",
        "msg['Subject'] = f\"Relatório de Vendas - {nome_da_loja}\"\r\n",
        "msg['From'] = 'seuemail@gmail.com'\r\n",
        "msg['To'] = 'teste@teste.com'\r\n",
        "password = \"MinhaSenha\"\r\n",
        "msg.add_header('Content-Type', 'text/html')\r\n",
        "msg.set_payload(corpo_email )\r\n",
        "  \r\n",
        "s = smtplib.SMTP('smtp.gmail.com: 587')\r\n",
        "s.starttls()\r\n",
        "# Credenciais de Login para enviar emails.\r\n",
        "s.login(msg['From'], password)\r\n",
        "s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))\r\n",
        "print('Email enviado')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xkbYP3K_KLkf"
      },
      "source": [
        "tabela_completa = tabela_faturamento.join(tabela_quantidade).join(ticket_medio)\r\n",
        "enviar_email(\"Diretoria\", tabela_completa)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Axlpp0gILm7y"
      },
      "source": [
        "listas_lojas = tabela_vendas[\"ID Loja\"].unique()\r\n",
        "for loja in lista_lojas\r\n",
        "  tabela_loja = tabela_vendas.loc[tabela_vendas[\"ID Loja\"] == loja, [\"ID Loja\", \"Quantidade\", \"Valor Final\"]]\r\n",
        "  tabela_loja = tabela_loja.groupby(\"ID Loja\").sum()\r\n",
        "  tabela_loja[\"Ticket Medio\"] = tabela_loja[\"Valor Final\"] / tabela_loja[\"Quantidade\"]\r\n",
        "\r\n",
        "enviar_email(loja, tabela_loja)"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}