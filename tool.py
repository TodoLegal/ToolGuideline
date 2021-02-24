import sys
import json

if len(sys.argv) < 3:
  json.dump({
    'error': "Wrong number of parameters"
  }, sys.stdout)
  exit()

number1 = int(sys.argv[1])
number2 = int(sys.argv[2])

response = {
    'sum': number1 + number2
}

json.dump(response, sys.stdout)