import random

def generate_name():
  first_name=["Albert", "Charles", "Nicolas", "Michael", "Anders", "Isaac", "Stephen", "Marie", "Richard"]
  last_name=["Einstein", "Darwin", "Copernicus", "Faraday", "Celsius", "Newton", "Hawking", "Curie","Dawkins"]
  return f"{random.choice(first_name)} {random.choice(last_name)}"
for i in range(5):
  print(generate_name())

