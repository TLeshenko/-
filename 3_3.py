Kil = (input("Введите массу конфет в кг "))
Kil = Kil.replace(",", ".")
Kil = float(Kil)
Price = (input("Введите цену конфет "))
Price = Price.replace(",", ".")
Price = float(Price)
Cost = Kil * Price
print("Стоимость", Kil, "килограмм конфет равна", round(Cost,2))