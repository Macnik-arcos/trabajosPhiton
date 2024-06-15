def calcular_media_aritmetica():
  """
  Función que calcula la media aritmética de notas introducidas por el usuario.

  Args:
    No recibe argumentos.

  Returns:
    La media aritmética de las notas.
  """
  numero_notas = int(input("¿Cuántas notas deseas introducir?: "))
  suma_notas = 0

  for _ in range(numero_notas):
    nota = float(input("Introduce una nota: "))
    suma_notas += nota

  if numero_notas == 0:
    return None

  media_aritmetica = suma_notas / numero_notas
  return media_aritmetica

# Ejemplo de uso
media = calcular_media_aritmetica()
if media is not None:
  print(f"La media aritmética de las notas es: {media}")
else:
  print("No se introdujeron notas.")
