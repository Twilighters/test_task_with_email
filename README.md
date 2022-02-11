[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Python + Pytest + Selenium + Selenoid. Test email sending
## Selenoid - Selenium grid on docker containers
***
1. Запустить Selenoid командами:
   1. Download the latest release binary from [GitHub releases](https://github.com/aerokube/cm/releases) for your platform (linux/darwin/windows).
   2. In CLI run ```./cm.exe selenoid start --vnc```
   3. In CLI run ```./cm.exe selenoid-ui start```
2. Запустить тесты: ```pytest```
3. Открыть Selenoid UI, который доступен по адресу http://localhost:8080/

***
## Создание отчетов при помощи Allure

***
Чтобы сгенерировать Allure отчет после прогона тестов необходимо выполнить два шага:
1. Скачать (установить) _**Allure commandline application**_  на свою операционную систему.

   **Для пользователей Windows** лучше выбрать один из 2-х нижеперечисленных вариантов:
   1) Установить _**Allure commandline application**_ через _**PowerShell**_ командой:
   <br>```scoop install allure```<br>
      смотри [видеоинструкцию](https://www.youtube.com/watch?v=3WuTSDkfuqQ) (таймкод с 0:38 по 1:10)
   2) Если у вас не установлен scoop, то тогда следует скачать _**Allure commandline application**_ вручную:<br>
      смотри [видеоинструкцию](https://www.youtube.com/watch?v=3WuTSDkfuqQ) (таймкод с 1:39 по 3:07)
   3) Также вне зависимости от способа установки _**Allure commandline application**_ на Windows,
   <br>для работы с **Allure** необходимо будет
   установить Java - [видеоинструкция](https://www.youtube.com/watch?v=6qASwPL86MM&t=1352s) (таймкод с 7:00 по 8:35)

   **Для пользователей Linux и MacOS** смотрите как установить
_**Allure commandline application**_ [тут](https://docs.qameta.io/allure/#_installing_a_commandline).

2. Создать данные о выполнении тестов, на основании которых будут сгенерированы отчеты.
<br>Для этого нужно запускать тесты следующей командой в терминале:<br>```pytest --alluredir=allure_reports```


После прогона тестов останется только сгенерировать отчет командой в терминале:
<br>```allure serve allure_reports```<br>(отчет будет представлен на страничке браузера)
