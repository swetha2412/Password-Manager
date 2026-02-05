import os
from rich import print
from crypto import derive_key
from auth import setup_master, login
from storage import load_vault, save_vault
from utils import generate_password, copy_clipboard

if not os.path.exists("master.key"):
    setup_master()

if not login():
    print("[red]Access Denied[/red]")
    exit()

master_pw = input("Re-enter master password: ")
key = derive_key(master_pw)
vault = load_vault(key)

while True:
    print("\n[bold cyan]Password Manager[/bold cyan]")
    print("1. Add")
    print("2. View")
    print("3. Update")
    print("4. Delete")
    print("5. Generate Password")
    print("6. Exit")

    choice = input("> ")

    if choice == "1":
        site = input("Site: ")
        user = input("Username: ")
        pw = input("Password: ")
        vault[site] = {"user": user, "pw": pw}
        save_vault(vault, key)

    elif choice == "2":
        site = input("Site: ")
        if site in vault:
            print(vault[site])
            copy_clipboard(vault[site]["pw"])

    elif choice == "3":
        site = input("Site: ")
        if site in vault:
            vault[site]["pw"] = input("New password: ")
            save_vault(vault, key)

    elif choice == "4":
        site = input("Site: ")
        vault.pop(site, None)
        save_vault(vault, key)

    elif choice == "5":
        pw = generate_password()
        print("Generated:", pw)
        copy_clipboard(pw)

    elif choice == "6":
        break
