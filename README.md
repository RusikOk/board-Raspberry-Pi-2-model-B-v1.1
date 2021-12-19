# board-Raspberry-Pi-2-model-B-v1.1
полезные штуки в одном месте для удобства работы с малиной

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
raspi-config -> Interfacing Options -> SSH -> Yes -> Entertop -> Finish

<h2>аутентификация</h2>
В Raspberry Pi OS (ранее известном как Raspbian), например, имя пользователя по умолчанию — 
` pi `
, а пароль по умолчанию — 

` raspberry`

, но для большинства дистрибутивов это далеко не стандарт.
<br>
Чтобы изменить пароль пользователя root в Raspberry Pi, выполните: <b>sudo passwd root</b>

<h2>установка стандартного для меня софта</h2>
синхронизации файлов описаний пакетов с репозитарием: <b>sudo apt-get update</b><br>
установка новейших версий всех установленных пакетов системы: <b>sudo apt-get upgrade</b><br>
проверить установлен пакет или нет можно командой: <b>apt-cache policy [ИмяПакета]</b><br>
Midnight Commander: <b>sudo apt-get install mc</b><br>
диспетчер задач: <b>sudo apt-get install htop</b><br>
ZMODEM: <b>sudo apt-get install lrzsz</b><br>
: <b>sudo apt-get install </b><br>

<h2>мониторинг параметров HW системы</h2>
команда <b>dmesg</b> покажет сообщения ядра<br>
<a href="https://elinux.org/RPI_vcgencmd_usage">описание команд</a>
<br>
<a href="https://github.com/bamarni/pi64/issues/4#issuecomment-292707581">скрипт мониторинга</a>

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
также можно просто перетянуть файл в терминал
<br><br>
ссылки:<br>
<a href="https://russianblogs.com/article/7328815997/">Лучший способ закачивать и скачивать файлы Linux под Windows</a><br>

<h2>запуск J-Link Server</h2>
качаем последний дистрибутив <a href="https://www.segger.com/downloads/jlink/JLink_Linux_arm.tgz">J-Link utilities</a> <br>
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
<a href="https://github.com/RusikOk/board-Raspberry-Pi-2-model-B-v1.1/blob/main/2_datasheet/jLink%20manual%20UM08001.pdf">J-Link User Manual</a>

<h2>проброс последовательных портов через сеть</h2>
установка сервиса <b>sudo apt-get install ser2net</b><br>
правим конфиг <b>/etc/ser2net.conf</b> <a href="https://github.com/RusikOk/board-Raspberry-Pi-2-model-B-v1.1/blob/main/3_config/ser2net.conf">сам конфиг</a> <br>
перезагружаем службу <b>sudo service ser2net restart</b> <br>


почитать https://www.linux.org.ru/forum/development/15402226
<b></b> <br>


<br><br>
ссылки:<br>
<a href="http://security-corp.org/os/linux/892-probros-com-portov-iz-linux-v-windows.html">Проброс COM-портов из Linux в Windows</a>
<br>
<a href="https://networklessons.com/network-management/raspberry-pi-as-cisco-console-server/">Raspberry Pi as Cisco Console Server</a>
<br>
<a href="https://linux.die.net/man/8/ser2net">ser2net(8) - Linux man page</a>
<br>
<a href="https://github.com/qchats/ser2net/blob/master/ser2net.conf">исходники ser2net</a>

<h2>сеть</h2>
посмотреть настройки всех сетевых интерфейсов <b>ip a</b> или только LAN <b>ip addr show eth0</b><br> 
посмотреть открытые порты <b>sudo netstat -tulpn</b><br>

<h2>глянуть по свободе есть ли в этом смысл</h2>
<a href="https://github.com/pi-hole/pi-hole/#one-step-automated-install">Pi-hole</a>

<h1>HARD</h1>

<h2>pinout</h2>
<img src="https://github.com/RusikOk/board-Raspberry-Pi-2-model-B-v1.1/blob/main/1_%D1%81%D1%85%D0%B5%D0%BC%D1%8B/RaspberryPi2_pinout.png">
<br>
<a href="https://pinout.xyz/#">отличная шпора по пинам</a>

<h2>OLED на контроллере SSD1306</h2>
<a href="https://learn.adafruit.com/adafruit-pioled-128x32-mini-oled-for-raspberry-pi/usage">мануал</a>
<br>
<a href="https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples">примеры</a>

<h2>кнопки</h2>
<a href="https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/digital-i-o">примеры</a>
<br>

<h2>RTC на DS3231</h2>
проверка текущего времени: <b>timedatectl</b><br>
установка часового пояса: <b>sudo timedatectl set-timezone Europe/Kiev</b><br>
все доступные часовые пояса в системе можно подсмотреть в дирректории: <b>/usr/share/zoneinfo</b><br>
<img src="https://github.com/RusikOk/board-Raspberry-Pi-2-model-B-v1.1/blob/main/2_datasheet/DS3231/DS3231toRPI.webp" alt="подключение часов к RPi">
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
привести файл <b>/lib/udev/hwclock-set</b> в соответствие этому <a href="https://github.com/RusikOk/board-Raspberry-Pi-2-model-B-v1.1/blob/main/3_config/lib/udev/hwclock-set">ПРИМЕР КОНФИГА</a><br>
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