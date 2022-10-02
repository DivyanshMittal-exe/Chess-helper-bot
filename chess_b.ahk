#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

>^b::
run, python.exe cv_black.py
WinWait, C:\Users\Divyansh Mittal\AppData\Local\Programs\Python\Python39\python.exe
WinMinimize ;

