if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    file_name = "ancient_fragment.txt"
    try:
        print(f"Accessing Storage Vault: {file_name}")
        f = open(file_name, "r")
        data = f.read()
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(data)
    except FileNotFoundError:
       print("ERROR: Storage vault not found.")
    finally:
        f.close()
    print("")
    print("Data recovery complete. Storage unit disconnected")
