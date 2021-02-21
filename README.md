# board-Raspberry-Pi-2-model-B-v1.1
 полезные штуки в одном месте для удобства работы с малиной

<h1>SOFT</h1>

<h2>консоль</h2>

<h3>UART</h3>
config.txt<br>
# rusikok PRI3 enable UART
enable_uart=1

<h3>SSH</h3>

<h4>Включение SSH без экрана</h4>
Перейдите в каталог загрузки SD-карты с помощью файлового менеджера ОС. Пользователи Linux и macOS также могут сделать это из командной строки. Создайте новый пустой файл с именем ssh без расширения внутри загрузочного каталога.

<h4>Включение SSH из терминала</h4>
raspi-config -> Interfacing Options -> SSH -> Yes -> Entertop -> Finish

<h2>аутентификация</h2>
В Raspberry Pi OS (ранее известном как Raspbian), например, имя пользователя по умолчанию — <b>pi</b>, а пароль по умолчанию — <b>raspberry</b>, но для большинства дистрибутивов это далеко не стандарт.
<br>
Чтобы изменить пароль пользователя root в Raspberry Pi, выполните: <b>sudo passwd root</b>

<h2>выключение</h2>
Выполните команду: <b>sudo shutdown -h now</b>

<h2>для удобного переброса файлов через ZMODEM</h2>
Выполните команду: <b>sudo apt-get install lrzsz</b>

<h2>глянуть по свободе есть ли в этом смысл</h2>
<a href="https://github.com/pi-hole/pi-hole/#one-step-automated-install">Pi-hole</a>

<h1>HARD</h1>

<h2>pinout</h2>
<img src="https://github.com/RusikOk/board-Raspberry-Pi-2-model-B-v1.1/blob/main/1_%D1%81%D1%85%D0%B5%D0%BC%D1%8B/RaspberryPi2_pinout.png" alt="">

<h2>OLED на контроллере SSD1306</h2>
<a href="https://learn.adafruit.com/adafruit-pioled-128x32-mini-oled-for-raspberry-pi/usage">мануал</a>
<br>
<a href="https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples">примеры</a>

<h2>кнопки</h2>
<a href="https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/digital-i-o">примеры</a>
<br>