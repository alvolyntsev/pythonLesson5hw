# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import os, shutil
def makedirs():
    for idx in range(1,10):
        try:
            os.mkdir('./dir_'+str(idx))
        except FileExistsError:
            print('./dir_'+str(idx), ': Такая директория существует')
def deldirs():
    for idx in range(1,10):
        try:
            os.removedirs('./dir_'+str(idx))
        except FileNotFoundError:
            print('Такой директории не существует')
def alldirs():
    print(os.listdir(path='./'))

def copyscr():
    shutil.copy(__file__, './'+'copy'+os.path.basename(__file__))
#alldirs()
#print(os.path.basename(__file__), __file__, '\n','./'+'copy'+os.path.basename(__file__))

