import urllib.request
import json

with urllib.request.urlopen("https://www.mercadobitcoin.net/api/BTC/ticker/") as url:
   data = json.loads(url.read())
   tb = dict(data['ticker'])
   sell = (float(tb['sell']))

valorCompra = float(input("Digite o valor de Compra: "))
qtdBTC = float(input("Digite o Quantidade de Bitcoin: "))
investimento = valorCompra * qtdBTC / 1
valorAtual = sell * qtdBTC / 1
lucroEstimado = valorAtual / investimento - 1

print ("Você investiu R$",round(investimento,2),"e o seu valor bruto atual está em R$",round(valorAtual,2),", o seu lucro estimado é",'{:.1%}'.format(lucroEstimado))
