# Parte 1: Celsius para Fahrenheit
celsius = [22.5, 40, 13, 29, 34]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print("Temperaturas em Fahrenheit:")
print(fahrenheit)

# Parte 2: Fahrenheit para Kelvin + média
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
kelvin = [(temp - 32) * 5/9 + 273.15 for temp in fahrenheit]
media_kelvin = sum(kelvin) / len(kelvin)

print("\nTemperaturas em Kelvin:")
print(kelvin)
print(f"\nMédia das temperaturas em Kelvin: {media_kelvin:.2f}")
