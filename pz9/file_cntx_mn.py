import shutil
import os


class FileBackupManager:
    def __init__(self, filename):
        self.filename = filename
        self.backup_filename = filename + '.bak'

    def __enter__(self):
        # Проверяем, существует ли файл
        if os.path.exists(self.filename):
            # Если файл существует, создаем резервную копию
            shutil.copy(self.filename, self.backup_filename)
        else:
            # Если файл не существует, создаем новый файл
            open(self.filename, 'a').close()

        # Возвращаем открытый файл; Файл открыт для чтения и записи
        return open(self.filename, 'r+')

    def __exit__(self, exc_type, exc_value, traceback):
        # Проверяем, было ли исключение
        if exc_type is not None:
            # Если произошло исключение, восстанавливаем резервную копию
            if os.path.exists(self.backup_filename):
                # Копирует файл из backup_filename в filename
                shutil.copy(self.backup_filename, self.filename)
                os.remove(self.backup_filename)
        else:
            # Если исключение не произошло, удаляем резервную копию
            if os.path.exists(self.backup_filename):
                os.remove(self.backup_filename)
