[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Python + Pytest + Selenium + Selenoid. Test email sending
## Selenoid - Selenium grid on docker containers
***
1. Run Selenoid with commands:
   1. Download the latest release binary from [GitHub releases](https://github.com/aerokube/cm/releases) for your platform (linux/darwin/windows).
   2. In CLI run ```./cm.exe selenoid start --vnc```
   3. In CLI run ```./cm.exe selenoid-ui start```
2. Run tests: ```pytest```
3. Open the Selenoid UI ```http://localhost:8080/```

***
## Creating reports with using Allure

***
To generate an Allure report after running the tests, you need to perform two steps:
1. Download and install _**Allure commandline application**_ on your OS.

   **For Windows users, it is better to choose one of the following 2 options:
   1) Install _**Allure commandline application**_ via _**PowerShell**_ with the command:
   <br>scoop install allure<br>
      see [video](https://www.youtube.com/watch?v=3WuTSDkfuqQ) (timecode с 0:38 по 1:10)
   2) If you do not have scoop installed, then you should download _**Allure commandline application**_ вручную:<br>
      see [video](https://www.youtube.com/watch?v=3WuTSDkfuqQ) (timecode с 1:39 по 3:07)
   3)  Also, regardless of the installation method _**Allure commandline application**_ на Windows,
   <br>for work with **Allure**  you will need to
   install Java - [video](https://www.youtube.com/watch?v=6qASwPL86MM&t=1352s) (timecode с 7:00 по 8:35)

   **For Linux and macOS users** see how to install
_**Allure commandline application**_ [here](https://docs.qameta.io/allure/#_installing_a_commandline).

2. Create data on the execution of tests, on the basis of which reports will be generated.
<br>To do this, run the tests with the following command in the terminal:<br>```pytest --alluredir=allure_reports```


After running the tests, you will only need to generate a report using the command in the terminal:
<br>```allure serve allure_reports```<br>(the report will be presented on the browser page)
