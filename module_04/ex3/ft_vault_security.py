if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    try:
        with open("classified_data.txt", "r") as f1, open("security_protocols.txt", "r") as f2:
            print("Vault connection established with failsafe protocols\n")
            f1_data = f1.read()
            f2_data = f2.read()

            print("SECURE EXTRACTION:")
            print(f1_data)
            print("")

            print("SECURE PRESERVATION:")
            print(f2_data)
    except FileNotFoundError:
        print("ERROR: vault does not exist")
    else:
        print("Vault automatically sealed upon completion\n")
        print("All vault operations completed with maximum security")
