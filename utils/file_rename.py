import uuid
from pathlib import Path


class File:
    def __init__(self, filepath):
        self._filepath = filepath

    def rename(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return Path(self._filepath) / filename
