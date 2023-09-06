""" Написать скрипт, который принимает на вход список IP-адресов и
проверяет их доступность с помощью ping-запросов. Результаты
проверки сохраняются в отдельный файл. """

import subprocess # Библиотека для пинга

# Список IP-адресов для проверки
ips = ['192.168.20.1', '127.0.0.1', '8.8.8.8']
log_ip_scan = open('log_ip_scan.log', 'w',)
for ip in ips:
    try:
        subprocess.check_output(['ping', '-c1', ip])
        print(ip + ' Доступен')
        log_ip_scan.write( ip + ' Доступен \n')
    except subprocess.CalledProcessError:
            print(ip + ' Не доступен')
            log_ip_scan.write(ip + ' Не доступен \n')
            log_ip_scan.close