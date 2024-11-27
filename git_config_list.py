# Импортируем библиотеку subprocess
import subprocess

# Определяем функцию git_config_list, которая будет выполнять команду Git 
# (нужно в консоль вывести результат работы команды git: git config --global --list)
def git_config_list():
    # Удаляем заглушку, создаем переменную result:
    try:
        # Используем subprocess.run для выполнения команды в переменной result    
        result = subprocess.run(['git', 'config', '--global', '--list'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Выводим результат выполнения команды result.stdout
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f'Error occurred: {e.stderr}')    

# вызываем git_config_list()
if __name__ == '__main__':
    git_config_list()
