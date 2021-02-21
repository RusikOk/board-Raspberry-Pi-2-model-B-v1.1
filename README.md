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

<h1>HARD</h1>

<h2>pinout</h2>
<img src="https://github.com/RusikOk/board-STM32F411RET6-Terraelectronica/blob/main/6_%D1%84%D0%BE%D1%82%D0%BE/terraelectronica%20TE-STM32F103RET6%20KIT%20v100%20top.jpg" alt="">

<h2>OLED на контроллере SSD1306</h2>
<a href="https://learn.adafruit.com/adafruit-pioled-128x32-mini-oled-for-raspberry-pi/usage">мануал</a>
<a href="https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples">примеры</a>
