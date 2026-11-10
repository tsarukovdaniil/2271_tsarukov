# Ввод: hello   ,   world ,   and ,   goodbye   ->   5, 5, 3, 7
# Только input, print, len, map, split, strip; без циклов и присваиваний.
print(*map(len, map(str.strip, input().split(','))), sep=', ')
