import subprocess # Библиотека для пинга

# Список IP-адресов для проверки
ips = ['192.168.20.1', '127.0.0.1', '8.8.8.8']

for ip in ips:
    try:
        subprocess.check_output(['ping', '-c1', ip])
        print(ip + ' Доступен')
    except subprocess.CalledProcessError:
            print(ip + ' Не доступен')