ECHO OFF
CLS
:MENU
ECHO.
ECHO ...............................................
ECHO PRESS 1, 2 OR 3 to select your tests, or 4 to EXIT.
ECHO ...............................................
ECHO.
ECHO 1 - Run All Tests
ECHO 2 - Run First Class Tasks
ECHO 3 - Run Second Class Tasks
ECHO 4 - EXIT
ECHO.
SET /P M=Type 1, 2, 3, or 4 then press ENTER:
IF %M%==1 GOTO 1TASK
IF %M%==2 GOTO 2TASK
IF %M%==3 GOTO 3TASK
IF %M%==4 GOTO EOF

:1TASK
CLS
python test.py 
pause
CLS
GOTO MENU

:2TASK
CLS
python -m unittest test.ServerTestCase
pause
CLS
GOTO MENU

:3TASK
CLS
python -m unittest test.ServerTestCase2
pause
CLS
GOTO MENU