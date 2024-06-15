def operaciones_matematicas():
  """
  Función que solicita al usuario dos números y realiza una operación matemática con ellos.

  Args:
    No recibe argumentos.

  Returns:
    No retorna nada.
  """
  # Solicitar operación al usuario
  operacion = int(input("¿Qué operación deseas realizar? (1: suma, 2: resta, 3: multiplicación, 4: división): "))

  # Solicitar números al usuario
  numero1 = float(input("Introduce el primer número: "))
  numero2 = float(input("Introduce el segundo número: "))

  # Realizar la operación matemática
  if operacion == 1:
    resultado = numero1 + numero2
    operacion_simbolo = "+"
  elif operacion == 2:
    resultado = numero1 - numero2
    operacion_simbolo = "-"
  elif operacion == 3:
    resultado = numero1 * numero2
    operacion_simbolo = "*"
  elif operacion == 4:
    if numero2 == 0:
      print("No se puede dividir por cero.")
      return
    else:
      resultado = numero1 / numero2
      operacion_simbolo = "/"
  else:
    print("Operación no válida.")
    return

  # Mostrar el resultado
  print(f"{numero1} {operacion_simbolo} {numero2} = {resultado}")

# Llamar a la función
operaciones_matematicas()