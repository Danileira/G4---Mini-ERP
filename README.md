# G4 Mini - Sistema de Gestão ERP 🚀

O **G4 Mini** é um sistema compacto de Planejamento de Recursos Empresariais (ERP) desenvolvido como projeto prático de estudos. O software permite o controle essencial de um fluxo comercial, englobando o cadastro de produtos, gerenciamento de clientes, emissão de orçamentos e registro de vendas com baixa automática de estoque.

A interface conta com uma estilização moderna, limpa e responsiva em modo escuro (*Dark Mode*), implementada de forma otimizada.

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python 3 & Flask (Arquitetura de rotas e processamento de requisições GET/POST)
* **Frontend:** HTML5 & Jinja2 (Renderização de templates dinâmicos e controle de loops no navegador)
* **Estilização:** Water.css (Framework *classless* para design responsivo e minimalista)
* **Controle de Versão:** Git & GitHub

---

## 💡 Funcionalidades do Sistema

* **Gestão de Produtos:** Cadastro, listagem, edição e exclusão de itens com controle de preço e estoque.
* **Gestão de Clientes:** Cadastro completo e gerenciamento de base de clientes (Nome e E-mail).
* **Módulo de Orçamentos:** Geração de propostas comerciais atrelando clientes e produtos cadastrados, mantendo o status inicial como `PENDENTE`.
* **Módulo de Vendas:** Validação de estoque disponível, cálculo automático do valor total e abatimento automático da quantidade vendida direto no estoque real do produto.

---

## 📁 Estrutura do Projeto

```text
📁 G4-Mini-ERP/
│
├── 📄 app.py            # Código principal com a lógica de negócios e rotas Flask
├── 📄 .gitignore        # Bloqueio de arquivos temporários do Python (__pycache__)
├── 📄 README.md         # Documentação do projeto
│
└── 📁 templates/        # Arquivos de interface (HTML + Jinja2)
    ├── 📄 index.html
    ├── 📄 produtos.html
    ├── 📄 editar_produto.html
    ├── 📄 clientes.html
    ├── 📄 editar_cliente.html
    ├── 📄 orcamentos.html
    └── 📄 vendas.html
