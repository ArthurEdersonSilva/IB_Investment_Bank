import pandas as pd
from connect import get_supabase 

supabase = get_supabase()

def upload_product():
    # 1. Carrega o arquivo Excel de Product
    df_product = pd.read_excel("C:/Users/ferna/Desktop/Arthur/Projetos/IB/Dados Tabelas/product.xlsx")
    print("🚀 Iniciando sincronização de Produtos...")

    for index, row in df_product.iterrows():
        dados = {
            "name_product": row["name_product"],
            "type": row["type"],
            "risk": row["risk"],
            "currency": row["currency"],
            "external_code": row["external_code"],
            "price": float(row["price"])
        }
        
        # O 'upsert' evita duplicados baseando-se no 'external_code'
        supabase.table('product').upsert(dados, on_conflict="external_code").execute()
        print(f"✅ Produto {row['name_product']} sincronizado!")
    
    print("\n--- Tabela Product finalizada ---\n")

def upload_department():
    # 2. Carrega o arquivo Excel de Department
    df_department = pd.read_excel("C:/Users/ferna/Desktop/Arthur/Projetos/IB/Dados Tabelas/department.xlsx")
    print("🚀 Iniciando sincronização de Departamentos...")

    for index, row in df_department.iterrows():
        dados = {
            "name_department": row['name_department'],
            "business_unit": row['business_unit'],
            "cost_center": row['cost_center']
        }
        
        # Usando 'cost_center' como chave única para evitar duplicados
        supabase.table('department').upsert(dados, on_conflict="cost_center").execute()
        print(f"✅ Depto {row['name_department']} ({row['business_unit']}) sincronizado!")
        
    print("\n--- Tabela Department finalizada ---")

def upload_employees():
    df_employees = pd.read_excel("C:/Users/ferna/Desktop/Arthur/Projetos/IB/Dados Tabelas/employees.xlsm")
    print("🚀 Iniciando sincronização de Funcionários...")

    for index, row in df_employees.iterrows():
        try:
            dados = {
                "name": row['name'],
                "email": row['email'],
                "cpf": str(row['cpf']).strip(),
                "address": row['address'],
                "salary": float(row['salary']),
                "hire_date": str(row['hire_date']),
                "status": row['status'],
                "job_position": row['job_position'],
                "id_department": int(row['id_department'])
            }
            
            # O upsert garante a lógica de "se não está lá, incrementa; se está, ignora/atualiza"
            supabase.table('employee').upsert(dados, on_conflict="cpf").execute()
            print(f"✅ Funcionário {row['name']} sincronizado!")
            
        except Exception as e:
            print(f"❌ Erro ao sincronizar {row['name']}: {e}")
            continue # Pula para o próximo funcionário em caso de erro

    print("\n--- Tabela Employee finalizada ---")

# Bloco principal para executar as funções
if __name__ == "__main__":
    upload_product()
    upload_department()
    upload_employees()