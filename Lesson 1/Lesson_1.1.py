
name = "Андрей"
age = 31
city = "Тверь"

print(f"Привет, меня зовут {name} мне {age} лет(год), я живу в городе {city}.")

user_name = input("А как зовут Вас?:  ")
user_city = input("Из какого Вы города?:  ")

print(f"{user_name}, рад нашему знакомству =), {user_city} классный город =)")

user_ex = int(input("Сколько лет Вы знакомы с языком Python?:  "))
if user_ex <= 1:
    print("Твой уровень Junior")
elif (user_ex > 1) and (user_ex <= 3):
    print("Твой уровень Middle")
else:
    print("Твой уровень Senior")

print("Goodbye!")
