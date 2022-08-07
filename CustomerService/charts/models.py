import os

from django.core.files.storage import FileSystemStorage
from django.db import models

fs = FileSystemStorage(location='/media/files')

class FileName(models.Model):
    files = models.FileField(storage=fs)

    def filename(self):
        return os.path.basename(self.files.name)