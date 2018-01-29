@echo off
REM requires you to set the environment variable %picotoolpath%
if exist %appdata%\pico-8\carts\picopods.p8.png (
    xcopy /y %appdata%\pico-8\carts\picopods.p8.png picopods.p8.png
)
if not defined picotoolpath (
    echo please define picotoolpath
    goto end
)

echo Compressing.
py -3 scripts\compress.py main.lua picopods.lua
echo Building.
py -3 %picotoolpath%\p8tool build picopods.p8.png --lua picopods.lua
IF %ERRORLEVEL% EQU 0 (
    echo Success. Copying cartridge.
    xcopy /y picopods.p8.png %appdata%\pico-8\carts\picopods.p8.png
)
:end
