cost = float(input("Введите цену еды: "))
percent = float(input("Введите процент чаевых: "))
tip_amount = (cost * percent) / 100
total = cost + tip_amount