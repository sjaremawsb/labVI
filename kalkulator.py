def kalkulator():
	print("Prosty kalkulator")

	while True:
		try:
			num1 = float(input("Podaj pierwsza liczbe: "))
			operacja = input("Podaj operacje (+, -, *, /): ")
			num2 = float(input("Podaj druga liczbe: "))

			if operacja == '+':
				wynik = num1 + num2
			elif operacja == '-':
				wynik = num1 - num2
			elif operacja == '*':
				wynik = num1 * num2
			elif operacja == '/':
				if num2 != 0:
					wynik = num1 /num2

				else:
					print("Blad, dzielenie przez zero")
					continue

			else:
				print("Niedozwolona operacja")
				continue

			print (f"Wynik: {wynik}")

		except ValueError:
			print("Nieprawidlowe dane wejsciowe.")

		kontynuacja = input("Czy chcesz kontynuowac? (tak/nie): ")
		if kontynuacja.lower() != 'tak':

			breaK

kalkulator()

