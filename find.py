import os


def check_files_in_project(project_dir):
    # os.walk() возвращает кортеж (root, dirs, files), но dirs мы не используем
    for root, _, files in os.walk(project_dir):
        for file in files:
            if file.endswith('.py'):  # Только Python файлы
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        f.read()
                except UnicodeDecodeError as e:
                    print(f"Ошибка в файле: {os.path.join(root, file)} - {e}")


# Укажите путь к вашему проекту
check_files_in_project(r"D:\AQA")
