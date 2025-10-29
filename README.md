# 💼 Projeto People Analytics — ETL, SQL e Power BI

Simulação de um banco de dados de Recursos Humanos (RH) com **Python, Faker e Pandas**, para explorar métricas de **People Analytics** como rotatividade, desempenho e diversidade.  
O projeto cobre todo o fluxo **ETL → SQL → Power BI**, ideal para estudo e portfólio de análise de dados.

---

## 📊 **Objetivos do Projeto**

- Gerar dados fictícios de funcionários, avaliações e desligamentos usando `Faker`;
- Criar um banco SQL com os dados (SQLite ou PostgreSQL);
- Praticar consultas analíticas com **SQL**;
- Realizar análises e visualizações no **Power BI**;
- Construir um pipeline de dados de ponta a ponta (ETL completo).

---

## 🧰 **Tecnologias Utilizadas**

| Categoria | Ferramenta |
|------------|-------------|
| Linguagem | Python 3.x |
| Bibliotecas | Faker, Pandas |
| Banco de Dados | SQLite (padrão) / PostgreSQL (opcional) |
| Visualização | Power BI |
| Versionamento | Git / GitHub |

---

## ⚙️ **Instalação e Execução**

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/vinis-san/analise-de-rh-fake.git
cd analise-de-rh-fake
2️⃣ Crie o ambiente virtual (opcional, mas recomendado)
bash
Copiar código
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
3️⃣ Instale as dependências
bash
Copiar código
pip install -r requirements.txt
4️⃣ Gere os dados simulados
bash
Copiar código
python geradordedados.py
Esse script cria três arquivos CSV:

Copiar código
funcionarios.csv
avaliacoes.csv
demissoes.csv
🗄️ Carregar os Dados em SQL
Você pode usar o script carregar_sql.py para criar o banco e inserir os dados:

bash
Copiar código
python carregar_sql.py
Isso cria o arquivo people_analytics.db (SQLite).
Depois, é só abrir no DBeaver, SQLite Studio ou conectar no Power BI.

🧩 Estrutura do Repositório
bash
Copiar código
📁 analise-de-rh-fake/
│
├── geradordedados.py     # Gera os dados fictícios com Faker
├── carregar_sql.py               # Cria o banco e importa os CSVs
├── requirements.txt              # Dependências do projeto
├── README.md                     # Documentação do projeto
│
├── 📂 base-dados/
│   ├── funcionarios.csv
│   ├── avaliacoes.csv
│   └── demissoes.csv
│
└── 📊 dashboard/
    └── people_analytics.pbix     # (opcional) Dashboard Power BI
🧮 Consultas SQL de Exemplo
sql
Copiar código
-- Total de funcionários
SELECT COUNT(*) FROM funcionarios;

-- Salário médio por departamento
SELECT departamento, ROUND(AVG(salario),2) AS salario_medio
FROM funcionarios
GROUP BY departamento
ORDER BY salario_medio DESC;

-- Média de nota de avaliação por departamento
SELECT f.departamento, ROUND(AVG(a.nota),2) AS nota_media
FROM avaliacoes a
JOIN funcionarios f ON f.id_funcionario = a.id_funcionario
GROUP BY f.departamento;

-- Taxa de rotatividade
SELECT 
    (COUNT(DISTINCT d.id_funcionario) * 100.0 / COUNT(DISTINCT f.id_funcionario)) AS turnover_percentual
FROM funcionarios f
LEFT JOIN demissoes d ON f.id_funcionario = d.id_funcionario;

```
📊 Ideias de Dashboards no Power BI
📈 Turnover mensal e por departamento

💰 Salário médio e total de folha por área

🧠 Desempenho médio por departamento

👩‍💼 Distribuição de gênero e idade

🕓 Tempo médio de casa por cargo

🌟 Aprendizados e Insights
Prática completa de ETL com Python + SQL

Modelagem de dados para People Analytics

Uso de Faker para gerar datasets realistas

Criação de dashboards analíticos no Power BI

🤝 Contribuição
Sinta-se à vontade para sugerir melhorias, abrir issues ou enviar pull requests!
Esse projeto foi criado para fins de aprendizado e demonstração de habilidades em dados.

🧑‍💻 Autor
Vinicius Andrade
📧 bsbvinidesousa@gmail.com
🔗 [LinkedIn](https://linkedin.com/in/vinícius-andrade-912295234)  
🔗 [GitHub](https://github.com/vinis-san)