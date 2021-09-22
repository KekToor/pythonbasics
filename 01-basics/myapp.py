import time
import sys
#Nvidia Driver Setup
choice = input('Vitejte v průvodci instalace driverů Nvidia 470! Pro pokračování napište "y": ')
c = choice.strip()
if(c.lower() == 'y'):
    print("Vyberte umístění: (no you can't): ")
    time.sleep(1)
    choice = input('Upozorňujeme, že instalací ovladačů souhlasíte, že společnost Nvidia nenese žádnou odpovědnost za chyby '
          'způsobené instalací ovladačů (pro souhlas vypište ANO): ')
    c = choice.strip()
    if(c.upper() == 'ANO'):
        time.sleep(1)
        sys.stdout.write('\rInstalling, progress: -------------------- 0%')
        time.sleep(0.6)
        sys.stdout.flush()
        sys.stdout.write('\rInstalling, progress: ##------------------ 10%')
        time.sleep(1.2)
        sys.stdout.flush()
        sys.stdout.write('\rInstalling, progress: ###----------------- 15%')
        time.sleep(2.5)
        sys.stdout.flush()
        sys.stdout.write('\rInstalling, progress: ######-------------- 30%')
        time.sleep(2.2)
        sys.stdout.flush()
        sys.stdout.write('\rInstalling, progress: ############-------- 60%')
        time.sleep(5)
        print('\nERROR: You tried to install an NVIDIA driver. Your computer will now crash and never work again.\n')
        time.sleep(3)
        while(1):
            print('haha')
    else:
        print('Bye Bye.')
        sys.exit()
else:
    print('Bye Bye.')
