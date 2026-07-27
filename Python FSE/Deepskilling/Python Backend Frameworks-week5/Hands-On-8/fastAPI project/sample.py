from security import get_password_hash, verify_password

password = "Archana@123"

hashed = get_password_hash(password)

print("Generated Hash:")
print(hashed)

print("\nCorrect Password:")
print(verify_password(password, hashed))

print("\nWrong Password:")
print(verify_password("WrongPassword", hashed))