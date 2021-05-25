import os, sys, django

from django.core.files.storage import get_storage_class

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

def upload_files(path):
    default_storage = get_storage_class()()

    for subdir, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(subdir, file)
            with open(full_path, 'rb') as data:
                default_storage.save(full_path.replace("\\","/")[len(path) + 1:], data)

if __name__ == "__main__":
    upload_files('media')