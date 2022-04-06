from datetime import datetime

birth = datetime.strptime(input("Your birth date (d.m.Y): "), "%d.%m.%Y")
age = datetime.now() - birth

print(f"You survived {age.total_seconds()} seconds")
print(datetime.now())   