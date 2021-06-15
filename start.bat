ECHO OFF
CLS
:MENU
ECHO.
ECHO ...............................................
ECHO PRESS 1, 2, 3, 4 or 5 to select your tests, or 6 to EXIT.
ECHO ...............................................
ECHO.
ECHO 1 - Run All Tests
ECHO 2 - Run First Task Test
ECHO 3 - Run Additional Tests
ECHO 4 - Run Connection Tests 
ECHO 5 - Run Performace Tests
ECHO 6 - EXIT
ECHO.
SET /P M=Type 1, 2, 3, 4, 5 or 6 then press ENTER:
IF %M%==1 GOTO ALLTESTS
IF %M%==2 GOTO FIRSTTASKTEST
IF %M%==3 GOTO ADDITIONALTESTS
IF %M%==4 GOTO CONNECTION
IF %M%==5 GOTO PERFORMANCE
IF %M%==6 GOTO EOF

:ALLTESTS
CLS
python test.py 
pause
CLS
GOTO MENU

:FIRSTTASKTEST
CLS
python -m unittest test.A_FirstTaskTest
pause
CLS
GOTO MENU

:ADDITIONALTESTS
CLS
python -m unittest test.B_AdditionalTests
pause
CLS
GOTO MENU

:CONNECTION
CLS
python -m unittest test.D_ConnectionTests
pause
CLS
GOTO MENU

:PERFORMANCE
CLS
python -m unittest test.C_ServerPerformaceTests
pause
CLS
GOTO MENU