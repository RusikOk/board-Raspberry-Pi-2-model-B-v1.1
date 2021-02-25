# board-Raspberry-Pi-2-model-B-v1.1
полезные штуки в одном месте для удобства работы с малиной

<h1>SOFT</h1>

<h2>консоль</h2>

<h3>UART</h3>
в самом конце файла config.txt дописать следующее:<br>
# rusikok PRI3 enable UART
<br>
enable_uart=1
<br>
ссылки:<br>
<a href="https://elinux.org/RPi_Serial_Connection#Preventing_Linux_using_the_serial_port">полное описание проблемы с UART в моделях малины с блютуз модулями</a>

<h3>SSH</h3>

<h4>Включение SSH без экрана</h4>
Перейдите в каталог загрузки SD-карты с помощью файлового менеджера ОС. Пользователи Linux и macOS также могут сделать это из командной строки. Создайте новый пустой файл с именем ssh без расширения внутри загрузочного каталога.

<h4>Включение SSH из терминала</h4>
raspi-config -> Interfacing Options -> SSH -> Yes -> Entertop -> Finish

<h2>аутентификация</h2>
В Raspberry Pi OS (ранее известном как Raspbian), например, имя пользователя по умолчанию — <b>pi</b>, а пароль по умолчанию — <b>raspberry</b>, но для большинства дистрибутивов это далеко не стандарт.
<br>
Чтобы изменить пароль пользователя root в Raspberry Pi, выполните: <b>sudo passwd root</b>

<h2>мониторинг параметров HW системы</h2>
команда <b>dmesg</b> покажет сообщения ядра<br>
<a href="https://elinux.org/RPI_vcgencmd_usage">описание команд</a>
<br>
<a href="https://github.com/bamarni/pi64/issues/4#issuecomment-292707581">скрипт мониторинга</a>

<h2>выключение</h2>
Выполните команду: <b>sudo shutdown -h now</b>

<h2>для удобного переброса файлов через ZMODEM</h2>
Выполните команду: <b>sudo apt-get install lrzsz</b>

качаем последний дистрибутив <a href="https://www.segger.com/downloads/jlink/JLink_Linux_arm.tgz">J-Link utilities</a> <br>
<h2>запуск J-Link Server</h2>
роспаковуем в каталог пользователя /home/pi/JLink_Linux_V696_arm <br>
на всякий случай читаем	README.txt <br>
добавляем правила <b>sudo cp 99-jlink.rules /etc/udev/rules.d/</b><br>
теперь можно грохнуть скачаный архив <br>
ребутаем млину <br>
подключаем jLink по USB, проверяем подключение <b>./JLink_Linux_V696_arm/JLinkExe</b> -> q <br>
запускаем jLink Remote Server <b>sudo ./JLink_Linux_V696_arm/JLinkRemoteServerCLExe -Port 19020</b> -> q <br>
<br>
ссылки:<br>
<a href="https://blog.feabhas.com/2019/07/using-a-raspberry-pi-as-a-remote-headless-j-link-server/">Using a Raspberry Pi as a remote headless J-Link Server</a>
<br>
<a href="https://forum.segger.com/index.php/Thread/5693-SOLVED-J-Link-Remote-Server-on-Raspberry-Pi/">J-Link Remote Server on Raspberry-Pi</a>
<br>
<a href="">J-Link User Manual</a>

<h2>сеть</h2>
посмотреть настройки всех сетевых интерфейсов <b>ip a</b> или только LAN <b>ip addr show eth0</b><br> 
посмотреть открытые порты <b>sudo netstat -tulpn</b><br>

<h2>глянуть по свободе есть ли в этом смысл</h2>
<a href="https://github.com/pi-hole/pi-hole/#one-step-automated-install">Pi-hole</a>

<h1>HARD</h1>

<h2>pinout</h2>
<img src="https://github.com/RusikOk/board-Raspberry-Pi-2-model-B-v1.1/blob/main/1_%D1%81%D1%85%D0%B5%D0%BC%D1%8B/RaspberryPi2_pinout.png" alt="">
<br>
<a href="https://pinout.xyz/#">отличная шпора по пинам</a>

<h2>OLED на контроллере SSD1306</h2>
<a href="https://learn.adafruit.com/adafruit-pioled-128x32-mini-oled-for-raspberry-pi/usage">мануал</a>
<br>
<a href="https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples">примеры</a>

<h2>кнопки</h2>
<a href="https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/digital-i-o">примеры</a>
<br>