""" Написать скрипт, который принимает на вход список IP-адресов и
проверяет их доступность с помощью ping-запросов. Результаты
проверки сохраняются в отдельный файл. """

import subprocess
from datetime import datetime
from pathlib import Path

ips = ('8.8.8.8', '8.8.4.4', '192.168.1.1')

# Форматируем дату и время для записи в файл
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Открываем файл для записи
log_ip_scan = Path("./log_ip_scan.log")
if not log_ip_scan.exists():
    log_ip_scan.touch()
with open(log_ip_scan, "a") as f:
    f.write('\n \n \n==========\n' + current_datetime)

index_ips = 0 

for ping_process in ips:
    command = ['ping', '-c2', '-w10', '-n', ips[index_ips]]
    process = subprocess.run(command, stdout=subprocess.PIPE)
    output = process.stdout.decode()
    print(output)
    log_ip_scan = open('log_ip_scan.log', 'a',)
    log_ip_scan.write( '\n==========\n' + output)
    log_ip_scan.close
    index_ips+=1