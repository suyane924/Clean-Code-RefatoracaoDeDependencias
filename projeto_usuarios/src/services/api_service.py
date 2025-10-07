
import requests
from src.utils.logger import log_info, log_error, log_warning

def buscar_usuario_api(user_id: int):
    try:
        r = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}", timeout=5)
        if r.status_code == 200:
            dados = r.json()
            log_info(f"Usuário encontrado: {dados['name']} ({dados['email']})")
            return dados
        else:
            log_warning("Usuário não encontrado na API.")
            return None
    except Exception as e:
        log_error(f"Erro ao buscar usuário: {e}")
        return None
