class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки, объект "{self.title}"')


class Pen(Stationery):
    def draw(self):
        print(f'Начинаем отрисовку ручкой, объект: "{self.title}"')


class Pencil(Stationery):
    def draw(self):
        print(f'Отрисовка карандашом, объект: "{self.title}"')


class Handle(Stationery):
    def draw(self):
        print(f'Малюем маркером, объект: "{self.title}"')


title_1 = Stationery('Монитор')
title_1.draw()
title_2 = Pen('Банан')
title_2.draw()
title_3 = Pencil('Луна')
title_3.draw()
title_4 = Handle("КОнь")
title_4.draw()
