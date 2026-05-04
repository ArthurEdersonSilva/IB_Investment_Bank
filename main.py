# main.py
from connect import get_supabase

def iniciar_sistema():
    supabase = get_supabase()
    
    if supabase:
        print("✅ Sistema iniciado e conectado ao Banco!")
        # Aqui você chama as outras funções (ex: menu, login, etc)
    else:
        print("❌ Falha crítica: O sistema não pôde conectar.")

if __name__ == "__main__":
    iniciar_sistema()