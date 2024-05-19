set /A clientAmount=%1%

for /l %%x in (1,1, %clientAmount%) do call ".\ProjectZomboid64 - nosteam-debug.bat"