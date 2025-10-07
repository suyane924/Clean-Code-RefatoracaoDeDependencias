
from typing import List, Dict
from src.services.email_service import enviar_email_boas_vindas
from src.utils.logger import log_info, log_warning

class UserService:
    def __init__(self):
        self.usuarios: List[Dict] = []

    def adicionar_usuario(self, nome: str, email: str):
        usuario = {
            "id": len(self.usuarios) + 1,
            "nome": nome,
            "email": email,
            "ativo": True
        }
        self.usuarios.append(usuario)
        enviar_email_boas_vindas(usuario)
        log_info(f"Usuário {nome} adicionado com sucesso!")
        return usuario

    def listar_usuarios(self):
        if not self.usuarios:
            log_warning("Nenhum usuário cadastrado.")
            return
        for u in self.usuarios:
            status = "Ativo" if u["ativo"] else "Inativo"
            log_info(f"{u['id']}: {u['nome']} ({u['email']}) - {status}")

    def desativar_usuario(self, user_id: int):
        for u in self.usuarios:
            if u["id"] == user_id:
                u["ativo"] = False
                log_warning(f"Usuário {u['nome']} desativado.")
                return True
        log_warning("Usuário não encontrado.")
        return False
