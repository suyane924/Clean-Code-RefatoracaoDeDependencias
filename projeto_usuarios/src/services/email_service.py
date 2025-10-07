
from src.utils.logger import log_info, salvar_log_email

def enviar_email_boas_vindas(usuario: dict):
    mensagem = f"Olá {usuario['nome']}, bem-vindo ao sistema!"
    log_info(f"[EMAIL SIMULADO] Enviando para {usuario['email']}: {mensagem}")
    salvar_log_email(usuario["email"], mensagem)
