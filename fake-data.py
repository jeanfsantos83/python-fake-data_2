from faker import Faker

fake = Faker(locale='pt-br')
name = fake.name()
email = fake.email()
user = fake.user_name()
address = fake.address()

print(f'Name: {name}')
print(f'Email: {email}')
print(f'User: {user}')
print(f'Address: {address}')
