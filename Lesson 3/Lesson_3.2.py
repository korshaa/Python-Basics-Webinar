def pasport(**kwargs):
    return kwargs


pas_dict = pasport(name="Ivan", surname="Pypkin", city="Moscow", email="ivanP.mail.ru", nphone=89203244545, )
print(
    f"Имя: {pas_dict['name']}, Фамилия: {pas_dict['surname']}, город: {pas_dict['city']}, электронная почта: {pas_dict['email']}, телефон: {pas_dict['nphone']}")
