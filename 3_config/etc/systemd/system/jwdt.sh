#!/bin/bash
#
# (c) 2022-02-04 RusikOk

# путь к файлу лога
LOG=/var/log/rusikok_jlink_jwdt.log

# активируем сторожевой таймер
/bin/systemd-notify --ready;

# получаем статус выполнения команды в текстовую переменную
RET=$(/bin/systemctl status --no-pager jlink | /bin/grep Rejected);

# сразу же выводим полученные данные в консоль
echo $RET;

# если строка вывода пустая
if [[ -z $RET ]]; then 
    # сбрасываем сторожевой таймер
    /bin/systemd-notify --status=WATCHDOG=1; 
    echo "WATCHDOG -> OK";
else
    echo "WATCHDOG -> ERROR";
    # запрашиваем полный лог статуса сервиса
    RET=$(/bin/systemctl status --no-pager jlink);
    # пишем в файл вывод статуса
    echo >> $LOG;
    echo $(date +"%Y-%m-%d %H:%M:%S") >> $LOG;
    echo $RET >> $LOG;
fi