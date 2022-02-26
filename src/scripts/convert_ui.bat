@echo off

cd src\gui

for %%f in (*.ui) do (
  pyside6-uic %%~nf.ui -o %%~nf_ui.py
)


cd Dlg

for %%f in (*.ui) do (
  pyside6-uic %%~nf.ui -o %%~nf_ui.py
)