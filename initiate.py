import os
import subprocess
import sys
import venv

#
# Fluxo para iniciar o projeto
# 1. Instalar o ambiente
# 2. Iniciar o ambiente
#

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
VENV_DIR = os.path.join(PROJECT_DIR, '.venv')

def run(cmd, check=True):
    print(f'\033[94mExecutando:\033[0m {cmd}')
    subprocess.run(cmd, shell=True, check=check)

def main():
    print('📦 Iniciando setup do projeto Django...')

    # 1. Criar ambiente virtual
    if not os.path.exists(VENV_DIR):
        print('🔧 Criando ambiente virtual...')
        venv.create(VENV_DIR, with_pip=True)
    else:
        print('⚠️ Ambiente virtual já existe.')

    # 2. Ativar ambiente virtual (só funciona em subprocess)
    python_bin = os.path.join(VENV_DIR, 'Scripts' if os.name == 'nt' else 'bin', 'python')

    # 3. Instalar dependências
    print('📦 Instalando dependências...')
    run(f'"{python_bin}" -m pip install -r requirements.txt')

    # 4. Criar DB SQLite (automático na migração)
    print('🗃️ Fazendo migrações...')
    run(f'"{python_bin}" manage.py migrate')
    run(f'"{python_bin}" manage.py runserver')

    print('\n✅ Projeto iniciado com sucesso!')

if __name__ == '__main__':
    try:
        main()
    except subprocess.CalledProcessError:
        print('\n❌ Ocorreu um erro durante o processo.')
        sys.exit(1)
