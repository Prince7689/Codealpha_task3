import os
import hashlib

# Hardcoded password
password = "admin123"

# SQL Injection example
query = "SELECT * FROM users WHERE name = '" + input("Enter username: ") + "'"

# Dangerous command execution
os.system(input("Enter command: "))

# Dangerous eval
eval(input("Enter expression: "))

# Weak hash algorithm
hashlib.md5(b"password").hexdigest()