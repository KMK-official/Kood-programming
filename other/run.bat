@echo off

rmdir /S /Q "dist"
del "compiler.exe"

powershell -Command "Write-Host 'PART 1/4, kide' -ForegroundColor White -BackgroundColor Magenta"
pyarmor gen kide.py
pyinstaller --name kide "dist\kide.py" --add-data "dist\pyarmor_runtime_000000;." --add-data "iss\icon.ico;." --hidden-import=customtkinter --hidden-import=darkdetect --collect-all=customtkinter --onefile --noconfirm --workpath build_temp
rmdir /S /Q "dist\pyarmor_runtime_000000"
del "kide.spec"
del "dist\kide.py"


powershell -Command "Write-Host 'PART 2/4, compiler' -ForegroundColor White -BackgroundColor Magenta"
pyarmor gen compiler.py
pyinstaller --onefile --add-data "dist\pyarmor_runtime_000000;." --add-data "iss\icon.ico;." dist/compiler.py --workpath build_temp
rd /s /q "dist/pyarmor_runtime_000000"
move dist\compiler.exe .
del compiler.spec
del "dist\compiler.py"


powershell -Command "Write-Host 'PART 3/4, kood' -ForegroundColor White -BackgroundColor Magenta"
set "file_name=v2.py"
pyarmor gen %file_name%
pyinstaller --name kood "dist\%file_name%" --add-data "dist\pyarmor_runtime_000000;." --add-data "compiler.exe;." --add-data "error_sound.mp3;." --add-data "iss\icon.ico;." --hidden-import=psutil --hidden-import=platform --hidden-import=screeninfo --hidden-import=just_playback --hidden-import=cffi --hidden-import=simpleeval --onefile --noconfirm --workpath build_temp
rmdir /S /Q "build_temp"
rmdir /S /Q "dist\pyarmor_runtime_000000"
del "kood.spec"
del "dist\%file_name%"


rmdir /S /Q "build_temp"


echo.
echo.
echo files made
echo.
echo.



powershell -Command "Write-Host 'PART 4/4, inno setup' -ForegroundColor White -BackgroundColor Magenta"

"%LocalAppData%\Programs\Kood\unins000.exe" /VERYSILENT /SUPPRESSMSGBOXES
"%LocalAppData%\Programs\Kide\unins000.exe" /VERYSILENT /SUPPRESSMSGBOXES

"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" "iss\inno-setup.iss"
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" "iss\inno-setup-kide.iss"

dist\kood-installer.exe /VERYSILENT /SUPPRESSMSGBOXES /MERGETASKS="desktopicon"
dist\kide-installer.exe /VERYSILENT /SUPPRESSMSGBOXES /MERGETASKS="desktopicon"
