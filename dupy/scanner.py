import os
from dupy.file_utils import file_hash

def find_duplicates(directory, ignore_hidden=True):
    files_by_size = {}
    duplicates = {}

    for root, _, files in os.walk(directory):
        for name in files:
            if ignore_hidden and name.startswith('.'):
                continue
            path = os.path.join(root, name)
            try:
                size = os.path.getsize(path)
                files_by_size.setdefault(size, []).append(path)
            except Exception:
                continue

    for size, paths in files_by_size.items():
        if len(paths) < 2:
            continue
        hashes = {}
        for path in paths:
            try:
                h = file_hash(path)
                hashes.setdefault(h, []).append(path)
            except Exception:
                continue
        for h, paths in hashes.items():
            if len(paths) > 1:
                duplicates[h] = paths

    return duplicates
