if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    file_name = "new_discovery.txt"
    entries = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee",
    ]

    print(f"Initializing new storage unit: {file_name}")
    f = open(file_name, "w")
    print("Storage unit created successfully...\n")

    print("Inscribing preservation data...")
    for entry in entries:
        f.write(entry)
        print(entry)
    print("")

    f.close()
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{file_name}' ready for long-term preservation.")
