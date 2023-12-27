# board-Raspberry-Pi-2-model-B-v1.1
полезные штуки в одном месте для удобства работы с малиной

<img src="https://github.com/RusikOk/board-Raspberry-Pi-2-model-B-v1.1/blob/main/9_photo/P30417-003840.jpg"><br>
<img src="https://github.com/RusikOk/board-Raspberry-Pi-2-model-B-v1.1/blob/main/9_photo/P11228-202955.jpg"><br>

<h1>SOFT</h1>

<h2>консоль</h2>

<h3>UART</h3>
в самом конце файла <b>/boot/config.txt</b> дописать следующее:

```ini
# rusikok PRI3 enable UART
enable_uart=1
```

ссылки:<br>
<a href="https://elinux.org/RPi_Serial_Connection#Preventing_Linux_using_the_serial_port">полное описание проблемы с UART в моделях малины с блютуз модулями</a><br>
<a href="http://wikihandbk.com/wiki/Raspberry_Pi:%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0/config.txt">Raspberry Pi:Настройка/config.txt</a><br>

<h3>SSH</h3>

<h4>Включение SSH без экрана</h4>
Перейдите в каталог загрузки SD-карты с помощью файлового менеджера ОС. Пользователи Linux и macOS также могут сделать это из командной строки. Создайте новый пустой файл с именем ssh без расширения внутри загрузочного каталога.

<h4>Включение SSH из терминала</h4>
sudo raspi-config -> Interfacing Options -> SSH -> Yes -> [Entertop] -> Finish

<h2>аутентификация</h2>
В Raspberry Pi OS (ранее известном как Raspbian), например, имя пользователя по умолчанию — <b>pi</b>, а пароль по умолчанию — <b>raspberry</b>, но для большинства дистрибутивов это далеко не стандарт.
<br>
Чтобы изменить пароль пользователя root в Raspberry Pi, выполните: <b>sudo passwd root</b>

разрабы в очередной раз решили подмешать говна и заставляют теперь создавать собственную пару пользователь/пароль. если у вас нет монитора то нужно создать файлик <b>userconf.txt</b> в корне загрузочного раздела и вписать туда логин и зашифрованный пароль через двоеточие <b>pi:encrypted- password</b>
для получения зашифрованного пароля через другую расбери введите команду: <b>echo 'mypassword' | openssl passwd -6 -stdin</b>
<br>
ссылки:<br>
<a href="https://www.raspberrypi.com/news/raspberry-pi-bullseye-update-april-2022/">An update to Raspberry Pi OS Bullseye</a><br>

<h2>установка стандартного для меня софта и настроек</h2>

выключаем использование swap-памяти сейчас <b>sudo dphys-swapfile swapoff</b><br>
выключаем сервис использования swap-памяти <b>sudo systemctl disable dphys-swapfile</b><br>
удаляем swap с диска <b>sudo rm /var/swap</b><br>
синхронизации файлов описаний пакетов с репозитарием: <b>sudo apt-get update</b><br>
установка новейших версий всех установленных пакетов системы: <b>sudo apt-get upgrade</b><br>
проверить установлен пакет или нет можно командой: <b>apt-cache policy [ИмяПакета]</b><br>
Midnight Commander: <b>sudo apt-get install mc</b><br>
диспетчер задач: <b>sudo apt-get install htop</b><br>
ZMODEM: <b>sudo apt-get install lrzsz</b><br>
удаляем старые кеши и логи:

```ini
sudo rm -rf /var/cache/fontconfig/
sudo rm -rf /var/cache/apt/
sudo rm -rf /var/cache/pacman/
sudo rm -rf /var/cache/man/
sudo rm -rf /tmp/*
sudo rm -rf /var/log/*
```

в самом конце файла <b>/etc/fstab</b> дописываем строки:<br>

```ini
# rusikok пишем логи в оперативку, туда же переносим временные файлы
tmpfs           /tmp                tmpfs   defaults,noatime,nosuid                             0   0
tmpfs           /var/tmp            tmpfs   defaults,noatime,nosuid,size=30m                    0   0
tmpfs           /var/log            tmpfs   defaults,noatime,nosuid,mode=0755,size=100m         0   0
tmpfs           /var/spool/mqueue   tmpfs   defaults,noatime,nosuid,mode=0700,gid=12,size=10m   0   0
```

перезагружаемся <b>sudo reboot</b><br>
по желанию редактируем приветствие консоли <b>/etc/motd</b><br>
<br>
ссылки:<br>
<a href="https://romantelychko.com/blog/1611/">Установка и оптимизация Raspbian на Raspberry Pi</a><br>
<a href="https://zalinux.ru/?p=3047">Какие файлы можно удалить при нехватке места на диске Linux</a><br>

<h2>мониторинг параметров HW системы</h2>
команда <b>dmesg</b> покажет сообщения ядра<br>
температура SoC: <b>vcgencmd measure_temp | cut -f2 -d= | sed 's/000//'</b><br>
текущая тактовая частота SoC: <b>vcgencmd measure_clock arm | awk -F"=" '{printf ("%0.0f",$2/1000000); }'</b><br>
текущее напряжение ядра SoC: <b>vcgencmd measure_volts | cut -f2 -d= | sed 's/000//'</b><br>
состояние тротлинга ядра: <b>vcgencmd get_throttled | cut -f2 -d=</b><br>
аптайм системы: <b>uptime | awk -F'( |,|:)+' '{d=h=m=0; if($7=="min") m=$6; else { if($7~/^day/) { d=$6; h=$8; m=$9 } else if($9=="min") { h=0; m=$8 } else { h=$6; m=$7 }}} {printf("%03u days, %02u:%02u", d, h, m)}'</b><br>
<br>
ссылки:<br>
<a href="https://elinux.org/RPI_vcgencmd_usage">описание команд</a><br>
<a href="https://github.com/bamarni/pi64/issues/4#issuecomment-292707581">скрипт мониторинга</a><br>

<h2>питание</h2>
выключить сейчас: <b>sudo shutdown -h now</b><br>
выключить в 15:15: <b>sudo shutdown -h 15:15</b><br>
выключить через 15 минут: <b>sudo shutdown -h +15</b><br>
отмена запланированных действий: <b>sudo shutdown -с</b><br>
перезагрузить сейчас: <b>sudo shutdown -r now</b><br>

<h2>для удобного переброса файлов через SSH терминал</h2>
установка пакета: <b>sudo apt-get install lrzsz</b><br>
получение файла: <b>sz [filename]</b><br>
отправка файла: <b>rz</b><br>
также можно просто перетянуть файл в терминал<br>
<br>
ссылки:<br>
<a href="https://russianblogs.com/article/7328815997/">Лучший способ закачивать и скачивать файлы Linux под Windows</a><br>

<h2>запуск J-Link Remote Server УСТАРЕЛО !!!</h2>
<b>К СОЖАЛЕНИЮ НЕ РАБОТАЕТ НА Raspberry Pi 1 Segmentation Fault</b><br>
качаем последний дистрибутив <a href="https://www.segger.com/downloads/jlink/JLink_Linux_arm.tgz">J-Link utilities</a> <br>
роспаковуем в каталог пользователя /home/pi/JLink_Linux_V696_arm <br>
на всякий случай читаем	README.txt <br>
добавляем правила <b>sudo cp 99-jlink.rules /etc/udev/rules.d/</b><br>
теперь можно грохнуть скачанный архив <br>
ребутаем малину <b>sudo reboot</b><br>
подключаем J-Link <br>
проверяем J-Link в списке USB устройств <b>lsusb</b> должны увидеть что-то типа SEGGER J-Link PLUS<br>
подключаем jLink по USB, проверяем подключение <b>./JLink_Linux_V696_arm/JLinkExe</b> -> q <br>
запускаем jLink Remote Server <b>sudo ./JLink_Linux_V696_arm/JLinkRemoteServerCLExe -Port 19020</b> -> q <br>
в самом конце файла <b>/etc/rc.local</b> добавляем автозапуск программы в фоновом режиме:<br>

```ini
# rusikok jLink remote server start
/home/pi/JLink_Linux_V696_arm/JLinkRemoteServerCLExe -Port 19020 > $(date +"/var/log/jLinkRS/%Y-%m-%d_%H-%M.log") &
```
ссылки:<br>
<a href="https://blog.feabhas.com/2019/07/using-a-raspberry-pi-as-a-remote-headless-j-link-server/">Using a Raspberry Pi as a remote headless J-Link Server</a>
<br>
<a href="https://forum.segger.com/index.php/Thread/5693-SOLVED-J-Link-Remote-Server-on-Raspberry-Pi/">J-Link Remote Server on Raspberry-Pi</a>
<br>
<a href="https://github.com/RusikOk/board-Raspberry-Pi-2-model-B-v1.1/blob/main/2_datasheet/jLink%20manual%20UM08001.pdf">J-Link User Manual</a>

<h2>установка J-Link Remote Server</h2>
<b>К СОЖАЛЕНИЮ НЕ РАБОТАЕТ НА Raspberry Pi 1 Segmentation Fault</b><br>
качаем последний дистрибутив <a href="https://www.segger.com/downloads/jlink/JLink_Linux_V760g_arm.deb">32-bit Linux ARM DEB Installer</a> <br>
копируем в каталог <b>/home/pi/</b> скачанный дистрибутив<br>
синхронизация: <b>sudo apt-get update</b><br>
обновление пакетов системы: <b>sudo apt-get upgrade</b><br>
устанавливаем <b>sudo apt-get install /home/pi/JLink_Linux_V760g_arm.deb</b> -> y -> I <br>
удаляем пакет <b>rm /home/pi/JLink_Linux_V760g_arm.deb</b> <br>
подключаем J-Link по USB <br>
проверяем J-Link в списке USB устройств <b>lsusb</b> должны увидеть что-то типа SEGGER J-Link PLUS<br>
проверяем подключение <b>JLinkExe</b> -> q <br>
запускаем jLink Remote Server <b>JLinkRemoteServerCLExe -Port 19020</b> -> q <br>
запускаем jLink RTT Logger <b>JLinkRTTLoggerExe -IP 127.0.0.1 -device STM32F103CB -if SWD -speed 1000 -rttchannel 0 $(date +"/home/pi/RTT-%Y-%m-%d-%H-%M.log")</b> -> q <br>
просмотр лога RTT в реальном времени <b>log.sh RTT</b> -> ctr + c <br>

<h2>systemd автозапуск J-Link Remote Server</h2>
создаем файл <b>/etc/systemd/system/jlink.service</b> <br>

```service

```

перезагрузка <b>sudo systemctl daemon-reload</b> <br>
инсталяция сервиса <b>sudo systemctl restart jlink.service</b> <br>
автозагрузка <b>sudo systemctl enable --now jlink</b> <br>
запуск <b>sudo systemctl start jlink</b> <br>
проверка статуса службы <b>systemctl status jlink</b> <br>
ребут <b>sudo reboot</b> <br>
проверка статуса службы <b>systemctl status jlink</b> и видим, <b>ЧТО НИХРЕНА НЕ ЗАПУСТИЛОСЬ</b> <br>
перемещаем символическую ссылку /etc/systemd/system/multiuser.target.wants/jlink.service в каталог /etc/systemd/system/multi-user.target.wants/ <br>
ребут <b>sudo reboot</b> <br>
проверка статуса службы <b>systemctl status jlink</b> теперь все ОК<br>

проверка статуса службы в реальном времени <b>journalctl -S today -f -u jlink.service</b> теперь все ОК<br>

sudo chmod +x /etc/systemd/system/jwdt.sh
/bin/systemctl status --no-pager jlink | /bin/grep Rejected<br>
journalctl -u jlink<br>
systemctl list-dependencies jlink - отображение зависимостей
systemctl show jlink - Проверка свойств юнита
systemd-analyze - Выводит хронометраж процесса загрузки юнитов - сервисов, точек монтирования, устройств и сокетов<br>
systemd-analyze blame - Вывести время, которое потребовалось для загрузки каждого из юнитов<br>
systemd-analyze critical-chain - Вывести цепочку юнитов с наибольшим временем загрузки<br>

ссылки:<br>
<a href="https://habr.com/ru/post/535872/">Почему хабражители предпочитают велосипеды, вместо готовых решений? Или о systemd, part 0</a><br>
<a href="https://habr.com/ru/post/535930/">Systemd для продолжающих. Part 1 — Запуск юнитов по временным событиям</a><br>
<a href="https://habr.com/ru/post/536040/">Systemd для продолжающих. Part 2 — Триггеры на различные события</a><br>
<a href="https://habr.com/ru/company/southbridge/blog/255845/">Systemd за пять минут</a><br>
<a href="https://github.com/RusikOk/board-Raspberry-Pi-2-model-B-v1.1/blob/main/2_datasheet/systemd%20%D0%B4%D0%BB%D1%8F%20%D0%B0%D0%B4%D0%BC%D0%B8%D0%BD%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BE%D0%B2%202017.pdf">systemd для администраторов</a><br>
<a href="https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/#systemd">Run a Program On Your Raspberry Pi At Startup</a><br>
<a href="https://habr.com/ru/company/ruvds/blog/512868/">Использование таймеров systemd вместо заданий cron</a><br>
<a href="http://vladimir-stupin.blogspot.com/2013/02/systemd-2-service.html">systemd. Часть 2. service-файлы</a><br>

<h2>работа с последовательными портами</h2>
посмотреть текущие настройки порта <b>stty -F /dev/ttyUSB0 -a</b><br>
устанавливаем настройки порта <b>stty -F /dev/ttyUSB0 115200 cs8 -cstopb -parenb</b> (настройку нужно производить после открытия)<br>
перенаправляем вывод порта в файл <b>cat /dev/ttyUSB0 > "$(date +"/home/pi/ttyUSB0_%Y-%m-%d_%H-%M.log")" &</b><br>
в самом конце файла <b>/etc/rc.local</b> добавляем логирование в автозагрузку:<br>

```ini
# rusikok start logging serial port data
cat /dev/ttyUSB0 > $(date +"/home/pi/ttyUSB0_%Y-%m-%d_%H-%M.log") &
stty -F /dev/ttyUSB0 115200 cs8 -cstopb -parenb
```

ссылки:<br>
<a href="https://qastack.ru/unix/242778/what-is-the-easiest-way-to-configure-serial-port-on-linux">самый простой способ настроить последовательный порт в Linux</a><br>
<a href="https://www.cyberforum.ru/shell/thread1948807.html">Перенаправление потока в файл</a><br>

<h2>проброс последовательных портов через сеть</h2>
установка сервиса <b>sudo apt-get install ser2net</b><br>
правим конфиг <b>/etc/ser2net.conf</b> <a href="https://github.com/RusikOk/board-Raspberry-Pi-2-model-B-v1.1/blob/main/5_config/ser2net.conf">сам конфиг</a> <br>
перезагружаем службу <b>sudo service ser2net start</b><br>
подключаемся через telnet на 2000 порт с другой win машины и смотрим на вывод <b>telnet 192.168.0.7 2000</b><br>
<br>
ссылки:<br>
<a href="http://security-corp.org/os/linux/892-probros-com-portov-iz-linux-v-windows.html">Проброс COM-портов из Linux в Windows</a><br>
<a href="https://networklessons.com/network-management/raspberry-pi-as-cisco-console-server/">Raspberry Pi as Cisco Console Server</a><br>
<a href="https://linux.die.net/man/8/ser2net">ser2net(8) - Linux man page</a><br>
<a href="https://github.com/qchats/ser2net/blob/master/ser2net.conf">исходники ser2net</a><br>

<h2>сеть LAN</h2>
задаем доменное имя <b>sudo raspi-config -> System Options -> Hostname -> [Entertop] -> RPi2 -> [Entertop] -> Finish -> [Entertop]</b><br>
посмотреть настройки всех сетевых интерфейсов <b>ip a</b> или только LAN <b>ip addr show eth0</b><br> 
посмотреть открытые порты <b>sudo netstat -tulpn</b><br>
смотреть открытые порты в реальном времени <b>sudo watch netstat -tulpn</b><br>
<br>
ссылки:<br>
<a href="https://wiki.merionet.ru/servernye-resheniya/32/smotrim-otkrytye-porty-linux/">Смотрим открытые порты Linux</a><br>

<h2>сеть WLAN</h2>
подключаем USB Wi-Fi сетевой интерфейс <br>
проверяем наличие Wi-Fi адаптера в списке USB устройств <b>lsusb</b> должны увидеть что-то типа Ralink Technology, Corp. MT7601U Wireless Adapter<br>
смотрим настройки всех сетевых интерфейсов <b>ip a</b> или только WLAN <b>ip addr show wlan0</b><br> 
смотрим на список доступных AP <b>sudo iwlist wlan0 scan | grep ESSID</b><br> 
задаем региональные настройки Wi-Fi <b>sudo raspi-config -> Localisation Options -> WLAN Country -> UA Ukraine -> [Entertop] -> [Entertop] -> Finish -> [Entertop]</b><br>
задаем SSID и пароль для подключения к AP <b>sudo raspi-config -> System Options -> Wireless LAN -> [ВводимSSID] -> [Entertop] -> [ВводимПароль] -> [Entertop] -> Finish</b><br>
если все же захотелось настроить все ручками, то лазить в <b>/etc/network/interfaces</b> не стоит. на RPi это чревато отвалом всей сети. лучше поправить <b>/etc/wpa_supplicant/wpa_supplicant.conf</b><br> 
посмотреть параметры Wi-Fi подключения <b>iwconfig</b><br>
увеличим мощность передатчика до 30dBm. в файле <b>/etc/wpa_supplicant/wpa_supplicant.conf</b> меняем 3ю строчку на <b>country=BZ</b><br>
<br>
ссылки:<br>
<a href="https://vpautinu.com/wifi/raspberry-pi">Подключение и настройка интернета Wi-Fi на Raspberry Pi</a><br>
<a href="https://www.raspberrypi.com/documentation/computers/configuration.html#adding-the-network-details-to-your-raspberry-pi">Adding the Network Details to your Raspberry Pi</a><br>
<a href="https://hackware.ru/?p=4125">Как увеличить мощность (TX Power) Wi-Fi</a><br>
<a href="https://zalinux.ru/?p=411">Переход с устаревшей команды iwconfig (wireless_tools) на iw</a><br>

<h2>настройка мобильного интернета 3G</h2>
как всегда сначала <b>sudo apt-get update</b><br>
потом <b>sudo apt-get upgrade</b><br>
устанавливаем службу ppp <b>sudo apt-get install ppp</b><br>
cкачиваем утилиту sakis3g для быстрой настройки PPP соединения: <b>wget https://netix.dl.sourceforge.net/project/vim-n4n0/sakis3g.tar.gz && tar -xzvf sakis3g.tar.gz && rm sakis3g.tar.gz</b><br>
устанавливаем права на запуск бинарника <b>sudo chmod +x sakis3g</b><br>
перемещаем в рабочий каталог <b>sudo mv sakis3g /usr/bin/sakis3g</b><br>

пробуем настроить получение 3G интернета <b>sudo sakis3g --console --interactive</b><br>
подключаемся <b>Connect with 3G -> Ace&Base (www.ab.kyivstar.net) -> [Entertop] -> Cancel</b><br>
<b>Примечание ! </b>После установки 3G PPP соединения в системе сменится default route и весь трафик по умолчанию будет идти через мобильное 3G/GPRS соединение.<br>
смотрим какой  СЕРЫЙ IP мы получили от провайдера <b>ip a</b><br> 
пингонем что нибудь <b>ping google.com</b><br>
опять запускаем сакис <b>sudo sakis3g --console --interactive</b><br>
получаем строку подключения и отключаемся <b>More options... -> Generate success report -> [КопируемСтрокуПослеСловаVariables:] -> [Entertop] -> Disconnect</b><br>
у меня строка инициализации соединения получилась такой <b>--console --interactive APN="www.ab.kyivstar.net" USBDRIVER="option" MODEM="12d1:1001"</b><br>
проверяем, чтобы содинение ppp упало <b>ip a</b><br> 
устанавливаем соединение из консоли <b>sudo sakis3g connect APN="www.ab.kyivstar.net" USBDRIVER="option" MODEM="12d1:1001"</b> и ждем заветную строчку Connected.<br>
проверяем состояние подключения средствами сакиса <b>sakis3g --console status</b><br> 
посмотрим Connection Information <b>sudo sakis3g --console info</b><br> 
проверяем, чтобы содинение ppp поднялось <b>ip a</b><br> 
пингонем что нибудь <b>ping google.com</b><br>
отключаемся <b>sudo sakis3g disconnect</b><br>
<b>Примечание ! </b>После дисконнекта 3G, OpenVPN туннель тоже падает и не подымается даже если в локалке есть инет.<br>
<br>
ссылки:<br>
<a href="https://kotvaska.medium.com/internet-for-raspbery-pi-abcc46ff24f1">Internet for Raspberry Pi</a><br>
<a href="https://robocraft.ru/blog/electronics/3131.html">Raspberry Pi. Установка и настройка комплекта MTC Коннект 4 (модем Huawei E171) на Raspbian</a><br>
<a href="https://onedev.net/post/904">Настройка 3G/GPRS интернета утилитой Sakis3g на GSM модеме Huawei E1550</a><br>
<a href="https://onedev.net/post/916">Переключение режима USB модема из Mаss Storage в GSM modem в Linux</a><br>

<h2>настройка клиентского OpenVPN подключения</h2>
<h3>на стороне сервера</h3>
собственно саму настройку OpenVPN сервера оставим за скобками<br>
запускаем <b>c:\Program Files\OpenVPN\easy-rsa\EasyRSA-Start.bat</b><br>
генерируем ключ <b>./easyrsa gen-req [ИмяКлиента] nopass</b><br>
генерируем сертификат ключа <b>./easyrsa sign-req client [ИмяКлиента]</b><br>
формируем файл настроек для клиента <b>rpi2.ovpn</b><br>
формируем набор файлов для клиента <b>rpi2.ovpn</b>, <b>rpi2.key</b>, <b>rpi2.crt</b>, <b>ca.crt</b>, <b>ta.key</b>, <b>dh.pem</b> и передаем безопасным способом.
<h3>на стороне клиента</h3>
как всегда сначала <b>sudo apt-get update</b><br>
потом <b>sudo apt-get upgrade</b><br>
устанавливаем службу OpenVPN <b>sudo apt-get install openvpn</b><br>
проверяем правильность хода RTC <b>date</b><br>
настраиваем часовой пояс если нужно <b>sudo dpkg-reconfigure tzdata</b><br>
меняем текущий каталог <b>cd /etc/openvpn/client</b><br>
переносим файлы настроек в каталог <b>/etc/openvpn/client</b><br>
обязательно переименовуем файл конфига <b>sudo mv rpi2.ovpn rpi2.conf</b><br>
сменим текущий каталог <b>cd /etc/openvpn</b><br>
запускаем в ручном режиме и смотрим, нет ли ошибок <b>sudo openvpn --config /etc/openvpn/rpi2.conf</b><br>
запускаем через системный демон <b>sudo openvpn --config /etc/openvpn/rpi2.conf --daemon</b><br>
перезапускаем службу <b>sudo service openvpn restart</b><br>
смотрим запустилась служба или нет <b>service --status-all</b><br>
проверяем состояние туннеля и его IP <b>ip a</b><br>
<br>
ссылки по настройке сервера:<br>
<a href="https://github.com/RusikOk/board-Raspberry-Pi-2-model-B-v1.1/blob/main/2_datasheet/vdoc_pub_openvpn_building_and_integrating_virtual_private_networks.pdf">книга по OpenVPN</a><br>
<a href="https://winitpro.ru/index.php/2021/12/28/ustanovka-openvpn-servera-windows/">Установка и настройка OpenVPN сервера под Windows</a><br>
<a href="https://internet-lab.ru/windows_openvpn_2_5_1">OpenVPN 2.5.1 сервер на Windows</a><br>
<a href="https://habr.com/ru/post/273371/">Подробная инструкция по OpenVPN v2.3.8 на Windows server 2008R2</a><br>
<a href="https://www.linux.org.ru/forum/admin/11912037">настроить маршрутизацию для openvp</a><br>
ссылки по настройке клиента:<br>
<a href="https://openvpn.net/community-downloads/">загрузка клиент/серверных программ</a><br>
<a href="https://www.ovpn.com/en/guides/raspberry-pi-raspbian">Install OpenVPN for Raspbian</a><br>
<a href="https://openvpn.net/vpn-server-resources/connecting-to-access-server-with-linux/">Connecting to Access Server with Linux</a><br>
<a href="https://bozza.ru/art-160.html">Команды OpenVPN</a><br>

<h2>настройка клиентского L2TP подключения VPN ЕЩЕ НЕ ЗАПУСКАЛ</h2>
регистрируем бесплатный аккаунт <a href="http://lan2lan.ru">lan2lan.ru</a>, создаем пару пользователей<br>
<br>
ссылки:<br>
<a href="https://www.umgum.com/debian-linux-l2tp-ipsec">Linux Debian + L2TP + IPsec</a><br>
<a href="https://adminvps.ru/blog/ustanovka-i-nastrojka-l2tp-ipsec-na-debian-ubuntu-iphone-mac-dlya-vpn/">Установка и настройка l2tp + ipsec на Debian</a><br>

<h2>FM передатчик</h2>
подключаем проводок примерно 10см к GPIO 4<br>
скачиваем <b>wget http://omattos.com/pifm.tar.gz</b><br>
роспаковуем в каталог <b>/pifm</b><br>
запускаем трансляцию <b>./pifm sound.wav 103.0 22050 stereo</b><br>
к слову звук очень противный и не качественный. еще и полоса пропускания очень широкая занимает аж под 2МГц.<br>
<br>
ссылки:<br>
<a href="http://www.icrobotics.co.uk/wiki/index.php/Turning_the_Raspberry_Pi_Into_an_FM_Transmitter">Turning the Raspberry Pi Into an FM Transmitter</a><br>

<h2>DNS сервер Pi-hole</h2>
не особо полезная штука. <b>ФЛЕШКА СДОХЛА ЧЕРЕЗ 2 МЕСЯЦА !!!</b><br>
рекламу на ютубе не блочит, лучше пользоваться AdBlock-ом.<br>
но зато предоставляет детальную статистику запросов.<br>
<br>
управление через sqlite3:<br>
запуск <b>sudo sqlite3 /etc/pihole/gravity.db</b><br>
получить название столбцов таблицы <b>PRAGMA table_info('group');</b><br>
получить все данные из таблицы <b>SELECT * FROM "group";</b><br>
включить определенную группу  <b>UPDATE 'group' SET enabled = 1 WHERE name = 'rusikokWorkGroup';</b><br>
выключить определенную группу <b>UPDATE 'group' SET enabled = 0 WHERE name = 'rusikokWorkGroup';</b><br>
упревление группами по расписанию <b>sudo crontab -e</b> -> <b>0 7 * * * sudo sqlite3 /etc/pihole/gravity.db "UPDATE 'group' SET enabled = 1 WHERE name = 'rusikokWorkGroup';" ; /usr/local/bin/pihole restartdns reload-lists >/dev/null<br></b>
<br>
ссылки:<br>
<a href="https://interface31.ru/tech_it/2021/04/sozdaem-sobstvennyy-filtruyushhiy-dns-server-na-baze-pi-hole.html">Создаем собственный фильтрующий DNS-сервер на базе Pi-hole</a><br>
<a href="https://github.com/pi-hole/pi-hole/#one-step-automated-install">Pi-hole</a><br>
<a href="https://discourse.pi-hole.net/t/activate-group-with-cron/32660">Activate group with cron</a><br>
<a href="https://habr.com/ru/articles/468621/">Переводим на DoH домашнюю сеть, или еще один щелчок по носу фильтрации</a><br>

<h1>HARD</h1>

<h2>pinout</h2>
<img src="https://github.com/RusikOk/board-Raspberry-Pi-2-model-B-v1.1/blob/main/3_schematic/RaspberryPi2_pinout.png"><br>
<a href="https://pinout.xyz/#">отличная шпора по пинам</a><br>

<h2>OLED на контроллере SSD1306</h2>
устанавливаем какую то хрень для питона: <b>sudo apt-get install python3-pip</b><br>
устанавливаем питоновские либы для SSD1306: <b>sudo pip3 install adafruit-circuitpython-ssd1306</b><br>
запуск скрипта вручную: <b>python3 /usr/local/bin/rusikok_oled_menu.py</b><br>
в самом конце файла <b>/etc/rc.local</b> добавляем вызов скрипта в фоновом режиме после загрузки:<br>

```ini
# rusikok start OLED menu
python3 /usr/local/bin/rusikok_oled_menu.py &
```

ссылки:<br>
<a href="https://learn.adafruit.com/adafruit-pioled-128x32-mini-oled-for-raspberry-pi/usage">мануал</a><br>
<a href="https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples">примеры</a><br>

<h2>кнопки</h2>
<a href="https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/digital-i-o">примеры</a>
<br>

<h2>RTC на DS3231</h2>
проверка текущего времени: <b>timedatectl</b><br>
установка часового пояса: <b>sudo timedatectl set-timezone Europe/Kiev</b><br>
все доступные часовые пояса в системе можно подсмотреть в директории: <b>/usr/share/zoneinfo</b><br>
<img src="https://github.com/RusikOk/board-Raspberry-Pi-2-model-B-v1.1/blob/main/2_datasheet/DS3231/DS3231toRPI.webp" alt="подключение часов к RPi">
активация I2С модуля <b>sudo raspi-config -> Interfacing Options -> I2С -> Yes -> [Entertop] -> Finish</b><br>
устанавливаем софт для диагностики I2С: <b>sudo apt-get install i2c-tools</b><br>
проверка правильности подключения часов. адрес 0x68: <b>i2cdetect -y 1</b><br>
сейчас можно вычитать всю память микросхемы: <b>i2cdump -y 1 0x68</b><br>
проверить наличие драйвера: <b>/lib/modules/5.10.17-v7+/kernel/drivers/rtc/rtc-ds1307.ko</b> да! странно но для DS3231 драйвер называется именно так<br>
в самом конце файла <b>/boot/config.txt</b> добавляем загрузку драйвера RTC ядром:<br>

```ini
# rusikok RTC definition
dtoverlay=i2c-rtc,ds3231
```

ребутнем систему: <b>sudo reboot</b><br>
проверка запуска драйвера часов. адрес 0x68 -> 0xUU: <b>i2cdetect -y 1</b><br>
проверить какие конкретно модули ядра сейчас загружены: <b>lsmod</b><br>
установка поддержки датчика температуры часов: <b>sudo apt-get install lm-sensors</b><br>
проверить датчик температуры DS3231: <b>sensors</b><br>
удаляем пакет фейк часов: <b>sudo apt-get remove fake-hwclock</b><br>
удаляем сценарий инициализации: <b>sudo update-rc.d -f fake-hwclock remove</b><br>
отключаем службу фейк часов: <b>sudo systemctl disable fake-hwclock</b><br>
привести файл <b>/lib/udev/hwclock-set</b> в соответствие этому <a href="5_config/lib/udev/hwclock-set">ПРИМЕР КОНФИГА</a><br>
проверить состояние аппаратных часов: <b>sudo hwclock --verbose -r</b><br>
посмотреть время из RTC: <b>sudo hwclock</b><br>
обновить системное время данными из RTC: <b>sudo hwclock --hctosys</b><br>
записать системное время в RTC: <b>sudo hwclock --systohc</b><br>
по желанию можно отключить NTP но я не стал: <b>sudo update-rc.d ntp disable</b><br>
<br>
ссылки:<br>
<a href="https://arduinoplus.ru/rtc-raspberry-pi/">Как добавить модуль RTC к Raspberry Pi</a><br>
<a href="https://onxblog.com/2019/03/30/raspberry-pi-hw-clock-ds3231/">Часы реального времени DS3231 PI</a><br>
<a href="https://blablacode.ru/linux/581">I2c в Linux из пространства пользователя</a><br>
<a href="https://www.raspberrypi.org/forums/viewtopic.php?p=1138858&sid=78cfd3416e0f02ddfd575a98ea15198d#p1138858">ds3231 clock temperature sensor access</a><br>
<a href="https://github.com/RusikOk/board-Raspberry-Pi-2-model-B-v1.1/blob/main/2_datasheet/DS3231/DS3231_RU.pdf">DS3231 datasheet на русском</a><br>
<a href="http://wikihandbk.com/wiki/Raspberry_Pi:%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0/config.txt">Raspberry Pi:Настройка/config.txt</a><br>

<h1>BOX</h1>

<a href="https://eltis.ua/catalog/korpusa-dlya-sistem-embeddeda1ak/it-10-0012225-rmb-korpus-na-din-reyku-raspberry-pi-b-abs-seryy-kh-22-5mm/">неплохой промышленный корпус</a><br>

<img src="https://github.com/RusikOk/board-Raspberry-Pi-2-model-B-v1.1/blob/main/9_photo/box1/506415_1.webp"><br>
<img src="https://github.com/RusikOk/board-Raspberry-Pi-2-model-B-v1.1/blob/main/9_photo/box1/507079_1.webp"><br>

<a href="https://www.siver.technology/products/raspberry-pi-4-to-din-rail-mount">более универсальный вариант</a><br>

<img src="https://github.com/RusikOk/board-Raspberry-Pi-2-model-B-v1.1/blob/main/9_photo/box2/%D0%9A%D1%80%D0%B5%D0%BF%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20Raspberry%20PI%204%20%D0%BD%D0%B0%20DIN%20%D1%80%D0%B5%D0%B9%D0%BA%D1%83.100.png"><br>