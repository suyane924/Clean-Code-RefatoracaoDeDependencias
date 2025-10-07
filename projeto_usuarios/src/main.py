
from src.services.user_service import UserService
from src.services.api_service import buscar_usuario_api
from src.utils.logger import log_info, log_error

def menu():
    service = UserService()

    while True:
        print("\n=== Sistema de Usuários ===")
        print("1 - Adicionar usuário")
        print("2 - Listar usuários")
        print("3 - Desativar usuário")
        print("4 - Buscar usuário na API")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                nome = input("Nome: ")
                email = input("Email: ")
                service.adicionar_usuario(nome, email)
            elif opcao == "2":
                service.listar_usuarios()
            elif opcao == "3":
                user_id = int(input("ID do usuário: "))
                service.desativar_usuario(user_id)
            elif opcao == "4":
                user_id = int(input("ID para buscar na API: "))
                buscar_usuario_api(user_id)
            elif opcao == "0":
                log_info("Saindo do sistema...")
                break
            else:
                log_error("Opção inválida.")
        except Exception as e:
            log_error(f"Erro: {e}")

if __name__ == "__main__":
    menu()
