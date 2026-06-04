import re

# Vulnerability patterns
patterns = {

    "Hardcoded Password":
        r'password\s*=\s*[\'"].+[\'"]',

    "SQL Injection":
        r'SELECT .* \+',

    "Command Injection":
        r'os\.system\(',

    "Eval Usage":
        r'eval\(',

    "Weak Hash Algorithm":
        r'md5\('
}

def scan_file(filename):

    print(f"\nScanning File: {filename}\n")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        vulnerabilities_found = False

        for line_number, line in enumerate(lines, start=1):

            for vulnerability, pattern in patterns.items():

                if re.search(pattern, line):

                    vulnerabilities_found = True

                    print("=" * 60)
                    print(f"[!] Vulnerability Found: {vulnerability}")
                    print(f"[!] Line Number        : {line_number}")
                    print(f"[!] Code               : {line.strip()}")
                    print("=" * 60)

        if not vulnerabilities_found:
            print("No vulnerabilities found.")

    except FileNotFoundError:
        print("File not found.")

# Target file to scan
target_file = "vulnerable_code.py"

scan_file(target_file)import re

# Vulnerability patterns
patterns = {

    "Hardcoded Password":
        r'password\s*=\s*[\'"].+[\'"]',

    "SQL Injection":
        r'SELECT .* \+',

    "Command Injection":
        r'os\.system\(',

    "Eval Usage":
        r'eval\(',

    "Weak Hash Algorithm":
        r'md5\('
}

def scan_file(filename):

    print(f"\nScanning File: {filename}\n")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        vulnerabilities_found = False

        for line_number, line in enumerate(lines, start=1):

            for vulnerability, pattern in patterns.items():

                if re.search(pattern, line):

                    vulnerabilities_found = True

                    print("=" * 60)
                    print(f"[!] Vulnerability Found: {vulnerability}")
                    print(f"[!] Line Number        : {line_number}")
                    print(f"[!] Code               : {line.strip()}")
                    print("=" * 60)

        if not vulnerabilities_found:
            print("No vulnerabilities found.")

    except FileNotFoundError:
        print("File not found.")

# Target file to scan
target_file = "vulnerable_code.py"

scan_file(target_file)