from flask import Flask, render_template, request, redirect, url_for #Importando a biblioteca Flask, render_template, request, redirect, url_for

app = Flask(__name__) #Cria o objeto Flask

#Banco de dados temporário
produtos_cadastrados = [ #Array "[" de dicionários "{"
    {"nome": "Notebook", "preco": 3500.00, "quantidade": 5},
    {"nome": "Mouse", "preco": 50.00, "quantidade": 10}
]

#Banco de dados de clientes
clientes_cadastrados = [
    {"nome": "João Silva", "email": "joao@gmail.com"},
    {"nome": "Maria Souza", "email": "maria@gmail.com"}
]

#Banco de dados de orçamentos
orcamentos_gerados = [

]

#Banco de dados de vendas
vendas_realizadas = [

]

#Página inicial (Rotas de Navegação)
@app.route("/")
def home():
    return render_template ("index.html")
                           
#Rota de Produtos
@app.route("/produtos", methods=["GET", "POST"])
def produtos():
    #Se o usuário preencheu o formulário e clicou em enviar
    if request.method == "POST":
        nome = request.form.get("nome_produto") #Pega valor do input 'nome_produto'
        preco = request.form.get("preco_produto") #Pega valor do input 'preco_produto'
        quantidade = request.form.get("quantidade_produto") #Pega valor do input 'quantidade_produto'

        #Criamos um novo dicionário e adicionamos na lista
        novo_produto = {"nome": nome, "preco": float(preco), "quantidade": int(quantidade)}

        #Adicionando o dicionário à lista global
        produtos_cadastrados.append(novo_produto)

        #Depois de salvar, recarrega a pagina
        return redirect("/produtos")
    
    #Se ele apenas acessou a página, mostra a lista atual
    return render_template("produtos.html", produtos=produtos_cadastrados)

#Rota para editar produto
@app.route("/editar_produto/<int:indice>", methods=["GET", "POST"])
def editar_produto(indice):
    #Se o usuário clicou em 'Salvar' no formulário de edição
    if request.method == "POST":
        nome = request.form.get("nome_produto")
        preco = float(request.form.get("preco_produto"))
        quantidade = int(request.form.get("quantidade_produto"))

        #Atualiza os dados na posição especificada da lista
        produtos_cadastrados[indice] = {
        "nome" :nome,
        "preco" : preco,
        "quantidade" : quantidade,
        }
        return redirect(url_for("produtos"))
    
    produto = produtos_cadastrados[indice]
    return render_template("editar_produto.html", produto=produto, indice=indice)
    
#Rota para excluir um produto
@app.route("/excluir_produto/<int:indice>")
def excluir_produto(indice):
    #Utilizando pop para remover um item da lista baseado na posição (indice)
    if indice < len(produtos_cadastrados):
        produtos_cadastrados.pop(indice)
    
    #Depois de excluir, volta para a pagina de produtos
    return redirect(url_for("produtos"))

#Rota de Clientes
@app.route("/clientes", methods=["GET", "POST"])
def clientes():
    #Se o usuário enviou o formulário (POST)
    if request.method == "POST":
        nome = request.form.get("nome_cliente")
        email = request.form.get("email_cliente")

        #Criando o dicionário do novo cliente
        novo_cliente = {"nome": nome, "email": email}

        #Adicionando na lista
        clientes_cadastrados.append(novo_cliente)

        return redirect(url_for("clientes"))

    #Se for apenas acesso visual (GET), renderiza o HTML passando a lista
    return render_template("clientes.html", clientes=clientes_cadastrados)

#Rota para editar cliente
@app.route("/editar_cliente/<int:indice>", methods=["GET", "POST"])
def editar_cliente(indice):
    #Se o usuário salvou as alterações (POST)
    if request.method == "POST":
        clientes_cadastrados[indice] = {
            "nome": request.form.get("nome_cliente"),
            "email": request.form.get("email_cliente")
        }
        return redirect(url_for("clientes")) #Volta para a pagina de clientes, importante dar o recuo depois do if para a página não ficar em loop

    #Buscando o cliente para exibir no editar_cliente.html
    cliente = clientes_cadastrados[indice]
    return render_template ("editar_cliente.html", cliente=cliente, indice=indice)

#Rota para excluir um cliente
@app.route("/excluir_cliente/<int:indice>")
def excluir_cliente(indice):
    clientes_cadastrados.pop(indice)
    return redirect(url_for("clientes"))

#Orçamentos
@app.route("/orcamentos", methods=["GET", "POST"])
def orcamentos():
    if request.method == "POST":
        #Pegando os dados do formulário HTML
        indice_cliente = int(request.form.get("cliente"))
        indice_produto = int(request.form.get("produto"))
        qtd_venda = int(request.form.get("quantidade_venda"))

        #localizando o cliente e produto nas listas globais
        cliente = clientes_cadastrados[indice_cliente]
        produto = produtos_cadastrados[indice_produto]
        
        #Calcula o valor total do produto
        valor_total = produto["preco"] * qtd_venda

        #Dicionário do novo orçamento
        novo_orcamento = {
            "cliente": cliente["nome"],
            "produto": produto["nome"],
            "quantidade": qtd_venda,
            "total": valor_total,
            "status": "PENDENTE" #Diferencial do orçamento
        }

        #Adicionando ao banco de dados (lista global de orcamentos)
        orcamentos_gerados.append(novo_orcamento)

        return redirect(url_for("orcamentos"))
    
    #Se ele apenas acessou a página, mostra a lista atual no GET
    return render_template("orcamentos.html",
                           orcamentos=orcamentos_gerados,
                           produtos=produtos_cadastrados,
                           clientes=clientes_cadastrados)

#Vendas
@app.route("/vendas", methods=["GET", "POST"])
def vendas():
    if request.method == "POST":
        #Pegando o índice do cliente, produto e quantidade selecionados no <select> do HTML
        indice_cliente = int(request.form.get("cliente"))
        indice_produto = int(request.form.get("produto"))
        qtd_venda = int(request.form.get("quantidade_venda"))

        #Localizando os objetos reais (cliente e produto) nas nossas listas
        cliente = clientes_cadastrados[indice_cliente]
        produto = produtos_cadastrados[indice_produto]

        #Lógica simples de estoque: verifica se a quantidade vendida não é maior que o estoque atual
        if qtd_venda <= produto["quantidade"]:
            #Calcula o valor total
            valor_total = produto["preco"] * qtd_venda

            #Cria o registro da venda
            nova_venda = {
                "cliente": cliente["nome"],
                "produto": produto["nome"],
                "quantidade": qtd_venda,
                "total": valor_total
            }

            #Adiciona a venda na lista
            vendas_realizadas.append(nova_venda) #Salva a venda no histórico
            produto["quantidade"] -= qtd_venda #Diminui a quantidade do estoque real do produto
            return redirect(url_for("vendas")) #Recarrega a página após a venda
    
        else:
            #Aqui podemos enviar uma mensagem de erro,
            #Por enquanto apenas não registra a venda se não houver estoque suficiente.
            return redirect(url_for("vendas"))

    #No GET, passamos a linha de produtos e clientes para o HTML
    return render_template("vendas.html",
                           vendas=vendas_realizadas,
                           produtos=produtos_cadastrados,
                           clientes=clientes_cadastrados)

#INICIALIZAÇÃO DO SERVIDOR - deve ser a ultima linha do arquivo
if __name__ == "__main__":
    app.run(debug=True) #Habilita o modo debug e inicia o servidor na porta 5000
