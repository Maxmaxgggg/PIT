import tempfile
import os


class TempFileManager:
    def __enter__(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        return self.temp_file

    def __exit__(self, exc_type, exc_value, traceback):
        self.temp_file.close()
        os.unlink(self.temp_file.name)
