# IB Investment Bank - Data Integration 🚀

Este projeto automatiza a carga e sincronização de dados de um banco de investimento utilizando **Python**, **Pandas** e **Supabase** (PostgreSQL).

## 🛠️ Funcionalidades
- **Sincronização de Produtos:** Carga automatizada de ativos financeiros via Excel.
- **Gestão de Departamentos:** Mapeamento de Business Units e Centros de Custo.
- **Gestão de Funcionários:** Upsert de colaboradores com validação de CPF único e vínculo dinâmico com departamentos.

## 🚀 Tecnologias Utilizadas
- **Python 3.12**
- **Pandas** (Tratamento de dados)
- **Supabase** (Banco de dados na nuvem / Backend)
- **Git/Github** (Versionamento)

## 📁 Estrutura do Projeto
- `setup_db.py`: Script principal de carga e tratamento.
- `connect.py`: Gerenciamento da conexão com a API do Supabase.
- `main.py`: Ponto de entrada do sistema.
