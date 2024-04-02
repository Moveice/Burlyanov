import random
size_uch = [random.randint(120, 180) for _ in range(30)]
uch_highest_10 = sum(1 for size in size_uch if size > 170)
if uch_highest_10 >= 5:
    print(f'Из 30 учеников, {uch_highest_10} учеников выше 170см. Можно сформировать команду из 5 '
          f'человек и более.')
else:
    print(
        f'Из 30 учеников, всего лишь {uch_highest_10} имеют рост выше 170см. Нельзя сформировать команду из 5 '
        f'человек и более.')