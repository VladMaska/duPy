import argparse
from dupy.scanner import find_duplicates
import os
import zipfile

def main():
    parser = argparse.ArgumentParser(description="dupy - Find duplicate files")
    parser.add_argument("command", choices=["scan", "list", "delete", "zip"])
    parser.add_argument("directory", help="Target directory to scan")
    parser.add_argument("--yes", action="store_true", help="Confirm deletion automatically")
    args = parser.parse_args()

    duplicates = find_duplicates(args.directory)

    if args.command == "scan" or args.command == "list":
        if not duplicates:
            print("No duplicates found.")
            return
        print("Duplicate files:")
        for group in duplicates.values():
            print("----")
            for path in group:
                print(path)

    elif args.command == "delete":
        if not args.yes:
            confirm = input("Are you sure you want to delete duplicates? (y/N): ")
            if confirm.lower() != 'y':
                return
        for group in duplicates.values():
            for path in group[1:]:
                os.remove(path)
        print("Duplicates deleted.")

    elif args.command == "zip":
        with zipfile.ZipFile("duplicates.zip", "w") as zf:
            for group in duplicates.values():
                for path in group[1:]:
                    zf.write(path)
        print("Duplicates archived to duplicates.zip.")
