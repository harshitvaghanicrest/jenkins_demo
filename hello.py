import datetime
version = "1.0.0"
with open('result.txt', 'w') as file:
    file.write(f'VERSION: {version}\n')
    file.write(f"Hello World! @ {datetime.datetime.now()}")
