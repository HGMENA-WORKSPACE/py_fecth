import sys
import os
import psutil
import time
import platform

argv = sys.argv

''' Obtiene informacion del cpu '''
def cpu_info():
    cpu = psutil.cpu_percent()  # tasa de uso de CPU en un segundo, unidad
    cpu_per = '% .2f %%' % cpu  # se convierte en un porcentaje, mantenga dos decimales
    return cpu_per


''' Obtiene informacion de la memoria '''
def mem_info():
    mem = psutil.virtual_memory()
    mem_per = '%.2f%%' % mem[2]
    mem_total = str(int(mem[0] / 1024 / 1024)) + 'M'
    mem_used = str(int(mem[3] / 1024 / 1024)) + 'M'
    mem_dict = {
        'mem_per': mem_per,
        'mem_total': mem_total,
        'mem_used': mem_used,
    }
    return mem_dict

''' Obtiene informacion del disco '''
def disk_info():
    c_info = psutil.disk_usage("C:")
    c_per = '%.2f%%' % c_info[3]
    return c_per

''' Obtiene informacion del trafico de red '''
def network_info():
    net = psutil.net_io_counters()
    net_sent = str(int(net[0]/1024/1024)) + 'MB'
    net_rece = str(int(net[1]/1024/1024)) + 'MB'
    net_dict = {
        'net_cent': net_sent,
        'net_rece': net_rece
    }
    return net_dict

def fetch():
    system = platform.system()
    cpu = cpu_info()
    mem = mem_info()
    disk = disk_info()
    net = network_info()
    if(len(argv) > 1):
        mes = simple_draw()
    else:
        mes = complex_draw()
    os.system("cls")
    print(mes % (system, cpu, mem.get('mem_per'), mem.get('mem_total'), mem.get('mem_used'), disk, net.get('net_cent'), net.get('net_rece')))
    time.sleep(1)

def simple_draw():
    return '''
==================================================
    system:                             \033[92m% s \033[0m
==================================================
    Uso de CPU:                         \033[93m% s \033[0m
    Uso de memoria:                     \033[93m% s \033[0m
==================================================
    Memoria total:                      \033[93m% s \033[0m
    Memoria usada:                      \033[93m% s \033[0m
==================================================
    Uso de la unidad C:                 \033[34m% s \033[0m
==================================================
    Tráfico de envío de tarjeta de red: \033[94m% s \033[0m
    NIC recibe tráfico:                 \033[95m% s \033[0m
==================================================
    '''

def complex_draw():
    return '''
\033[0m============================================================================================================
\033[91m ⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠢ \033[0m
\033[91m ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⠋⡆⢹ \033[0m                  system:                                       \033[92m% s \033[0m
\033[91m ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡆⢀⣤⢛⠛⣠⣿⠀⡏ \033[0m
\033[91m ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⠟⣡⠊⣠⣾⣿⠃⣠ \033[0m                   ==========================================================
\033[91m ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣯⣿⠀⠊⣤⣿⣿⣿⠃⣴⣧⣄⣀ \033[0m
\033[91m ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⡟⣠⣶⣿⣿⣿⢋⣤⠿⠛⠉⢁⣭⣽⠋ \033[0m               Uso de CPU:                                   \033[93m% s \033[0m
\033[91m   ⠀⠀⠀⠀⠀⠀ ⠀⣠⠖⡭⢉⣿⣯⣿⣯⣿⣿⣿⣟⣧⠛⢉⣤⣶⣾⣿⣿⠋ \033[0m
\033[91m ⠀⠀⠀⠀⠀⠀⠀⠀⣴⣫⠓⢱⣯⣿⢿⠋⠛⢛⠟⠯⠶⢟⣿⣯⣿⣿⣿⣿⣿⣿⣦⣄ \033[0m               Uso de memoria:                               \033[93m% s \033[0m
\033[91m ⠀⠀⠀⠀⠀⠀⢀⡮⢁⣴⣿⣿⣿⠖⣠⠐⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠛⠛⠛⢿⣶⣄ \033[0m
\033[91m ⠀⠀⠀⠀⢀⣤⣷⣿⣿⠿⢛⣭⠒⠉⠀⠀⠀⣀⣀⣄⣤⣤⣴⣶⣶⣶⣿⣿⣿⣿⣿⠿⠋⠁ \033[0m             Memoria total:                                \033[93m% s \033[0m
\033[91m ⠀⢀⣶⠏⠟⠝⠉⢀⣤⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧ \033[0m
\033[91m ⢴⣯⣤⣶⣿⣿⣿⣿⣿⡿⣿⣯⠉⠉⠉⠉⠀⠀⠀⠈⣿⡀⣟⣿⣿⢿⣿⣿⣿⣿⣿⣦ \033[0m               Memoria usada:                                \033[93m% s \033[0m
\033[91m ⠀⠀⠀⠉⠛⣿⣧⠀⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠃⣿⣿⣯⣿⣦⡀⠀⠉⠻⣿⣦ \033[0m
\033[91m ⠀⠀⠀⠀⠀⠀⠉⢿⣮⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠀⣯⠉⠉⠛⢿⣿⣷⣄⠀⠈⢻⣆ \033[0m             Uso de la unidad C:                           \033[34m% s \033[0m
\033[91m ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠢⠀⠀⠀⠀⠀⠀⠀⢀⢡⠃⣾⣿⣿⣦⠀⠀⠀⠙⢿⣿⣤⠀⠙⣄ \033[0m
\033[91m ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢋⡟⢠⣿⣿⣿⠋⢿⣄⠀⠀⠀⠈⡄⠙⣶⣈⡄ \033[0m           ==========================================================
\033[91m ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠚⢲⣿⠀⣾⣿⣿⠁⠀⠀⠉⢷⡀⠀⠀⣇⠀⠀⠈⠻⡀ \033[0m
\033[91m ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⣀⣿⡏⠀⣿⡿⠀⠀⠀⠀⠀⠀⠙⣦⠀⢧ \033[0m               Tráfico de envío de tarjeta de red:           \033[94m% s \033[0m
\033[91m ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠿⣧⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣮ \033[0m
\033[91m ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  \033[0m              NIC recibe tráfico:                           \033[95m% s \033[0m
\033[91m
\033[0m============================================================================================================
    '''


# Reset = '\033[0m'
# Grey = '\033[90m'
# Black = '\033[90m'
# Red = '\033[91m'
# Green = '\033[92m'
# Yellow = '\033[93m'
# Blue = '\033[94m'
# Magenta = '\033[95m'
# Cyan = '\033[96m'
# White = '\033[97m'

# Default      = "\033[39m"
# Black        = "\033[30m"
# Red          = "\033[31m"
# Green        = "\033[32m"
# Yellow       = "\033[33m"
# Blue         = "\033[34m"
# Magenta      = "\033[35m"
# Cyan         = "\033[36m"
# LightGray    = "\033[37m"

# Bold       = "\033[1m"
# Dim        = "\033[2m"
# Underlined = "\033[4m"
# Blink      = "\033[5m"
# Reverse    = "\033[7m"
# Hidden     = "\033[8m"

# ResetBold       = "\033[21m"
# ResetDim        = "\033[22m"
# ResetUnderlined = "\033[24m"
# ResetBlink      = "\033[25m"
# ResetReverse    = "\033[27m"
# ResetHidden     = "\033[28m"

# BackgroundDefault      = "\033[49m"
# BackgroundBlack        = "\033[40m"
# BackgroundRed          = "\033[41m"
# BackgroundGreen        = "\033[42m"
# BackgroundYellow       = "\033[43m"
# BackgroundBlue         = "\033[44m"
# BackgroundMagenta      = "\033[45m"
# BackgroundCyan         = "\033[46m"
# BackgroundLightGray    = "\033[47m"
# BackgroundDarkGray     = "\033[100m"
# BackgroundLightRed     = "\033[101m"
# BackgroundLightGreen   = "\033[102m"
# BackgroundLightYellow  = "\033[103m"
# BackgroundLightBlue    = "\033[104m"
# BackgroundLightMagenta = "\033[105m"
# BackgroundLightCyan    = "\033[106m"
# BackgroundWhite        = "\033[107m"