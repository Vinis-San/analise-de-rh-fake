from faker import Faker
import pandas as pd
import random
from datetime import date, timedelta
import os

fake = Faker('pt_BR')

departamentos = ['RH', 'Financeiro', 'Comercial', 'TI', 'Marketing', 'Operações']
cargos = {
    'RH': ['Analista de RH', 'Coordenador de RH', 'Gerente de RH'],
    'Financeiro': ['Assistente Financeiro', 'Analista Financeiro', 'Gerente Financeiro'],
    'Comercial': ['Vendedor', 'Supervisor de Vendas', 'Gerente Comercial'],
    'TI': ['Desenvolvedor', 'Analista de Dados', 'Gerente de TI'],
    'Marketing': ['Analista de Marketing', 'Designer', 'Coordenador de Marketing'],
    'Operações': ['Operador', 'Supervisor', 'Gerente de Operações']
}

funcionarios = []
avaliacoes = []
demissoes = []

for i in range(5000):
    depto = random.choice(departamentos)
    cargo = random.choice(cargos[depto])
    genero = random.choice(['Masculino', 'Feminino'])
    data_admissao = fake.date_between(start_date='-5y', end_date='today')
    salario = round(random.uniform(2000, 15000), 2)
    idade = random.randint(21, 60)
    
    funcionarios.append({
        'id_funcionario': i + 1,
        'nome': fake.name_male() if genero == 'Masculino' else fake.name_female(),
        'genero': genero,
        'idade': idade,
        'departamento': depto,
        'cargo': cargo,
        'data_admissao': data_admissao,
        'salario': salario
    })
    
    # 2 a 5 avaliações por funcionário
    for _ in range(random.randint(2, 5)):
        data_avaliacao = fake.date_between(start_date=data_admissao, end_date='today')
        nota = random.randint(1, 5)
        avaliacoes.append({
            'id_funcionario': i + 1,
            'data_avaliacao': data_avaliacao,
            'nota': nota,
            'comentario': random.choice(['Bom desempenho', 'Precisa melhorar', 'Excelente', 'Regular'])
        })

# ~20% dos funcionários desligados
demitidos = random.sample(funcionarios, k=int(len(funcionarios)*0.2))
for f in demitidos:
    demissoes.append({
        'id_funcionario': f['id_funcionario'],
        'data_demissao': fake.date_between(start_date=f['data_admissao'], end_date='today'),
        'motivo': random.choice(['Pedido de demissão', 'Desempenho', 'Corte de custos', 'Aposentadoria'])
    })

# Exportar CSVs
create_folder = 'base-dados'
if not os.path.exists(create_folder):
    os.makedirs(create_folder)

pd.DataFrame(funcionarios).to_csv(f'{create_folder}/funcionarios.csv', index=False)
pd.DataFrame(avaliacoes).to_csv(f'{create_folder}/avaliacoes.csv', index=False)
pd.DataFrame(demissoes).to_csv(f'{create_folder}/demissoes.csv', index=False)

print("✅ Arquivos gerados: base-dados/funcionarios.csv, base-dados/avaliacoes.csv, base-dados/demissoes.csv")
