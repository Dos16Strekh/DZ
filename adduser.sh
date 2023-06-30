#!bin/bash

#Написать Bash-скрипт который будет создавать пользователя по переданным аргументам:
#./script.sh user_name home_folder ssh_access enable
#можно использовать user_name= home_folder= ssh_access= enable=
#можно -user_name -home_folder -ssh_access -enable

# Проверка колличества аргументов. Должно быть 4.
if [ -n "$4" ];
    then
        echo "==============="
        echo "Вы ввели имя пользователя: $1"
        echo "Вы ввели имя папки: $2"
        echo "Вы ввели ssh_access: $3"
        echo "Вы ввели enable: $4"
        echo "==============="
    else
        echo "Должно быть 4 аргумента! Аргументы должны быть вида <имяпользователя> <папка> <ssh_access_on> <enable_on> "
        echo "Если ssh_acces не нужен - <ssh_access_off>"
        echo "Если enable не нужен <enable_off>"
fi

#проверка аргументов на ложность

if [ $3 = ssh_access_on ] || [ $3 = ssh_access_off ];
    then
        echo "Атрибут ssh_access введен верно. "
    else
        echo "Аргумент ssh_access должен иметь вид: <ssh_access_on> или <ssh_access_off>"
        exit 1
fi

if [ $4 = enable_on ] || [ $4 = enable_off ];
    then
        echo "Атрибут enable введен верно."
    else
        echo "Аргумент enable должен иметь вид: <enable_on> или <enable_off>"
        exit 1
fi

echo "==============="

#создаем пользователя по заданым параметрам

user_name=$1
home_folder=$2
ssh_access=$3
enable=$4

#пользователь

echo "Пользователь с именем $1 создан."
echo "==============="
#папка пользователя

echo "Папка пользователя с именем $2 создан."
echo "==============="
#ssh_access

if [ $ssh_access = ssh_access_on ];
    then
        echo "ssh_ access включен."
    else
        echo "ssh_ access не включен."
fi
echo "==============="

#enable


if [ $enable = enable_on ];
    then
        echo "enable включен."
    else
        echo "enable не включен."
fi
echo "==============="
