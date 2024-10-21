#!/usr/bin/python3
<<<<<<< HEAD
"""
initialize the models package
"""

from os import getenv


storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
=======
"""Instantiates a storage object.

-> If the environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
   instantiates a database storage engine (DBStorage).
-> Otherwise, instantiates a file storage engine (FileStorage).
"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
>>>>>>> 3be6b736b343528875751ac562c2e09313399515
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
