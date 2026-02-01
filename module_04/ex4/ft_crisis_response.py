def print_error(file_name: str, error: str, status: str) -> None:
    print(f"CRISIS ALERT: Attempting access to '{file_name}'\n"
        f"RESPONSE: {error}\n"
        f"STATUS: Crisis handled, {status}\n"
          )


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    files = [
        "lost_archive.txt",
         "classified_archive.txt",
         "standard_archive.txt"
        ]
    for file in files:
        try:
            with open(file, "r") as f:
                data = f.read()
        except FileNotFoundError:
            print_error(file,
                        "Archive not found in storage matrix",
                        "system stable")
        except PermissionError:
            print_error(file, "Security protocols deny access", "security maintained")
        else:
            print(f"ROUTINE ACCESS: Attempting access to '{file}'...\n"
                "SUCCESS: Archive recovered - ``Knowledge preserved to humanity``\n"
                "STATUS: Normal operations resumed\n")
    print("All crisis scenarios handled successfully. Archive secure.")
