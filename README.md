# Projeto de Refatoração — Sistema de Usuários

## Explicação das Mudanças Feitas

O código original foi refatorado para **melhorar a organização**, **reduzir dependências** e **aumentar a clareza**.  
As principais alterações realizadas foram:

- **Modularização:**  
  O código foi dividido em múltiplos arquivos (`user_service.py`, `email_service.py`, `api_service.py`, `logger.py` e `main.py`), cada um com uma responsabilidade específica.

- **Redução de acoplamento:**  
  As funções agora recebem parâmetros e retornam valores em vez de depender de variáveis globais, tornando o código mais independente e fácil de testar.

- **Funções mais testáveis:**  
  A lógica foi separada das interações de entrada e saída (`input()` e `print()`), permitindo que cada parte possa ser testada de forma isolada.

- **Biblioteca externa adicionada:**  
  Foi utilizada a biblioteca `requests` (para buscar dados da API externa) e `rich` (para exibir logs e mensagens coloridas no terminal).  
  Ambas são gerenciadas via **pip**, garantindo reprodutibilidade e controle de dependências.

- **Melhor visualização e registro de logs:**  
  O módulo `logger.py` utiliza o `rich` para exibir mensagens mais legíveis e salvar logs de e-mails e eventos do sistema.

- **Organização do projeto:**  
  A estrutura de diretórios foi reorganizada para facilitar a manutenção e o entendimento do código:


---

## Instruções para Executar o Código Refatorado

```bash
# Clonar o repositório
git clone https://github.com/suyane924/Clean-Code-RefatoracaoDeDependencias.git
cd projeto_usuarios

# Criar e ativar o ambiente virtual
# Windows:
python -m venv venv
venv\Scripts\activate

# Linux/macOS:
python3 -m venv venv
source venv/bin/activate

# Instalar as dependências
pip install -r requirements.txt

# Executar o sistema
python src/main.py
