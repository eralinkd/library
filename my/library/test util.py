import re
from django.core.files.base import ContentFile
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
filepath = os.path.join(BASE_DIR, "media")
files = os.listdir(filepath)
print(list(sorted(files)))

"""
    Returns a list of all names of encyclopedia entries.
    """
#a, filenames = default_storage.listdir("media")
    #return list(sorted(re.sub(r"\.md$", "", filename)
                #for filename in filenames if filename.endswith(".md")))
#print(a)