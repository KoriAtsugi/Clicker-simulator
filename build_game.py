import PyInstaller.__main__

PyInstaller.__main__.run([
    'grandma_game.py',  # Твой основной файл с игрой
    '--onefile',        # Один файл вместо папки
    '--windowed',       # Без консольного окна!
    '--icon=grandma_icon.ico',  # Иконка (нужно конвертировать PNG в ICO)
    '--name=FiveNightsAtGrandmas',  # Название .exe файла
    '--add-data=grandma_icon.png;.',  # Добавляем ресурсы
])