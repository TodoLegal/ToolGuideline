# Lineamientos para contribuir con herramientas a TodoLegal

Crea un [Readme](https://github.com/TodoLegal/ToolGuideline#setup) que contenga:

1. Instrucciones de instalación
2. Instrucciones de ejecución
3. Un ejemplo de ejecución

Asegurate que:

1. El programa se pueda ejecutar en Debian Linux (otras distros y SOs también bienvenidos)
2. El programa reciba parametros separados por espacios (como un comando de CLI tradicional)
3. El programa devuelva su respuesta via `Stdout` en formato `JSON`

## Estilo de código de TodoLegal

Agradecemos código libre de [malos olores](https://es.wikipedia.org/wiki/Hediondez_del_c%C3%B3digo) y con una arquitectura comprensible. Hecha un vistazo a estos 4 puntos que destacan en el estilo del código de TodoLegal:

### 1. Nombres de identificadores en inglés 🙆✅

```python
def sumar(numero1, numero2):
  return numero1 + numero2
```

Pasa a ser:

```python
def sum(number1, number2):
  return number1 + number2
```


### 2. Nombres explícitos 🙆✅

```python
def check u:
  return u.tkn != None
```

Pasa a ser:

```python
def is_logged_in user:
  return user.session_token != None
```

### 3. Proceso muy largo 🙅❌

```python
def getLatestLaws(laws):
  laws_temp = laws
  laws.clear()
  for law in laws_temp:
    if law not in laws:
      laws.append(law)
  laws.sort(key=date, reverse=True)
  return laws.Take(10)
```

Pasa a ser:

```python
def removeDuplicates(list):
  list_temp = list
  list.clear()
  for item in list_temp:
    if item not in list:
      list.append(item)

def getLatestLaws(laws):
  removeDuplicates(list)
  laws.sort(key=date, reverse=True)
  return laws.Take(10)
```


### 4. Preferimos no usar comentarios 🙅❌

```python
# Now we print the user names
for user in users:
  print(user.name)
```

Pasa a ser:

```python
print_user_names(users):
  for user in users:
    print(user.name)

print_user_names users
```

## Manejo de errores

Entre mas errores logremos capturar mejor. Una explicación del error será devuelta en un objeto `JSON` con el siguiente formato:

```json
{
  "error": "invalid first parameter: integer expected and got a string"
}
```
