import requests

cep = "6 5 0 , 6 7 1 9. 7........"
cep = cep.replace("-", "").replace(" ", "").replace(".", "").replace(",", "")
if len(cep) == 8:
    link = f"https://viacep.com.br/ws/{cep}/json/"
    requisicao = requests.get(link)

    print(requisicao)

    dicio_json = requisicao.json()
    uf = dicio_json["uf"]
    cidade = dicio_json["localidade"]
    bairro = dicio_json["bairro"]
    print(uf, cidade, bairro)
else:
    print("CEP Inválido!")

