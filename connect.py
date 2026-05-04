# connect.py
import os
from supabase import create_client, Client

# Dados do seu projeto que pegamos nas fotos
URL = "https://zxciqhruewnolzfpsryd.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp4Y2lxaHJ1ZXdub2x6ZnBzcnlkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY1NTIwMTgsImV4cCI6MjA5MjEyODAxOH0.ZUIS-sVE-28iFomiWk15bgOPJnDlN8WDKqHBZAgBvlk" # Aquela que você mandou na foto image_6030af.png

def get_supabase() -> Client:
    try:
        supabase: Client = create_client(URL, KEY)
        return supabase
    except Exception as e:
        print(f"Erro ao conectar ao Supabase: {e}")
        return None