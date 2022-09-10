# Лабораторная работа 1
Вариант 3002

Бутвин Михаил, P3130


## Задание 1
>Введенные команды:

    mkdir lab0
    cd lab0
    
    :: archeops3
    (
        echo Возможности  Overland=12 Surface=1 Sky=6 Jump=6 Power2=0
        echo Inteliigence=4 Fragile=0
    ) > archeops3

    :: gurdurr6
    (
        echo Ходы  Block Drain Punch Fire Punch
        echo Helping Hand Ice Punch Knock Off Low Kick Sleep Talk Snore Superpower
        echo Thunderpunch
    ) > gurdurr6

    :: piloswine7
    (
        echo Способности  Freezing Point Landslide
        echo Oblivious Snow Cloak
    ) > piloswine7

    :: lab0/poochyena9/
    mkdir poochyena9
    cd poochyena9

    :: ludicolo
    (
        echo Развитые способности  Own
        echo Tempo
    ) > ludicolo

    mkdir seel
    mkdir simisage
    cd ..

    :: lab0/sunkern4
    mkdir sunkern4
    cd sunkern4

    :: mightyena
    (
        echo Способности  Tackle Howl Sand-Attack Bite Odor Sleuth
        echo Roar Swagger Assurance Scary Face Taunt Embargo Take Down Thief Sucker
        echo Punch
    ) > mightyena

    :: prinplup
    (
        echo Ходы  Covert Dive Icy Wind Mud-Slap Signal Beam Sleep
        echo Talk Snore Stealth Rock Water Pledge Water Pulse
    ) > prinplup

    :: cottonee
    (
        echo satk=4
        echo sdef=5 spd=7
    ) > cottonee

    mkdir hydreigon
    mkdir honchkrow
    mkdir bronzong
    cd ..

    :: lab0/tangela5
    mkdir tangela5
    cd tangela5

    :: treecko
    (
        echo Тип диеты  Herbivore
    ) > treecko

    :: rampardos
    (
        echo Способности
        echo Mountain Peak Mold Breaker Rock Head
    ) > rampardos

    mkdir tangrowth
    cd ..
    cd ..

>Результат:

    [s367945@helios ~/OPD]$ cd lab0
    [s367945@helios ~/OPD/lab0]$ ls
    archeops3       gurdurr6        piloswine7      poochyena9      sunkern4        tangela5
    [s367945@helios ~/OPD/lab0]$ cd poochyena9
    [s367945@helios ~/OPD/lab0/poochyena9]$ ls
    ludicolo        seel            simisage
    [s367945@helios ~/OPD/lab0/poochyena9]$ cd ..
    [s367945@helios ~/OPD/lab0]$ cd sunkern4
    [s367945@helios ~/OPD/lab0/sunkern4]$ ls
    bronzong        cottonee        honchkrow       hydreigon       mightyena       prinplup
    [s367945@helios ~/OPD/lab0/sunkern4]$ cd ..
    [s367945@helios ~/OPD/lab0]$ cd tangela5
    [s367945@helios ~/OPD/lab0/tangela5]$ ls
    rampardos       tangrowth       treecko
    [s367945@helios ~/OPD/lab0/tangela5]$


## Задание 2
>Введенные команды:

    cd lab0

    chmod u=r,g=r,o=r archeops3 
    chmod u=r,g=,o= gurdurr6
    chmod u=r,g=r,o= piloswine7

    chmod u=rwx,g=wx,o=wx poochyena9
    cd poochyena9

    chmod u=r,g=r,o=r ludicolo
    chmod u=wx,g=wx,o=wx seel
    chmod u=wx,g=x,o=x simisage
    cd ..

    chmod 751 sunkern4
    cd sunkern4

    chmod u=rx,g=w,o=r hydreigon
    chmod 337 honchkrow
    chmod u=rwx,g=rx,o=wx bronzong
    chmod u=r,g=,o= mightyena
    chmod u=r,g=,o= prinplup
    chmod 664 cottonee
    cd ..

    chmod u=rwx,g=wx,o=wx tangela5
    cd tangela5

    chmod 330 tangrowth
    chmod 664 treecko
    chmod 046 rampardos
    cd ..

>Результат

    [s367945@helios ~/OPD]$ cd lab0
    [s367945@helios ~/OPD/lab0]$ ls -l
    total 15
    -r--r--r--  1 s367945  studs   92 10 сент. 14:45 archeops3
    -r--------  1 s367945  studs  121 10 сент. 14:45 gurdurr6
    -r--r-----  1 s367945  studs   69 10 сент. 14:45 piloswine7
    drwxr-xr-x  4 s367945  studs    5 10 сент. 14:45 poochyena9
    drwxr-x--x  5 s367945  studs    8 10 сент. 14:45 sunkern4
    drwx-wx-wx  3 s367945  studs    5 10 сент. 14:45 tangela5
    [s367945@helios ~/OPD/lab0]$ cd poochyena9
    [s367945@helios ~/OPD/lab0/poochyena9]$ ls -l
    total 2
    -r--r--r--  1 s367945  studs  50 10 сент. 14:45 ludicolo
    drwxrwxrwx  2 s367945  studs   2 10 сент. 14:45 seel
    drwxr-xr-x  2 s367945  studs   2 10 сент. 14:45 simisage
    [s367945@helios ~/OPD/lab0/poochyena9]$ cd ..
    [s367945@helios ~/OPD/lab0]$ cd sunkern4
    [s367945@helios ~/OPD/lab0/sunkern4]$ ls -l
    total 11
    drwxr-----  2 s367945  studs    2 10 сент. 14:45 bronzong
    -rw-r--r--  1 s367945  studs   20 10 сент. 14:45 cottonee
    d-wx-wxrwx  2 s367945  studs    2 10 сент. 14:45 honchkrow
    dr-xrw-r--  2 s367945  studs    2 10 сент. 14:45 hydreigon
    -r--------  1 s367945  studs  141 10 сент. 14:45 mightyena
    -r--------  1 s367945  studs  106 10 сент. 14:45 prinplup
    [s367945@helios ~/OPD/lab0/sunkern4]$ cd ..
    [s367945@helios ~/OPD/lab0]$ cd tangela5
    [s367945@helios ~/OPD/lab0/tangela5]$ ls -l
    total 2
    ----r--rw-  1 s367945  studs  60 10 сент. 14:45 rampardos
    d-wx-wx---  2 s367945  studs   2 10 сент. 14:45 tangrowth
    -rw-rw-r--  1 s367945  studs  28 10 сент. 14:45 treecko

>!!! Из-за изменения прав на файлы во втором задании некоторые команды в следующих заданиях могут выдавать ошибки доступа. Выполните **chmod -R 777 lab0**, чтобы избежать этого

## Задние 3
Перейдите в lab0 перед выполнением (чтобы убрать повторяющиеся *lab0*/ в  путях файлов)
### 1
Команда:

    cp -r sunkern4 poochyena9/seel
Результат:

    [s367945@helios ~/OPD/lab0/poochyena9/seel/sunkern4]$ ls
    bronzong        cottonee        honchkrow       hydreigon       mightyena       prinplup

### 2
Команда:

    cat piloswine7 > poochyena9/ludicolopiloswine

Результат: 

    [s367945@helios ~/OPD/lab0/poochyena9]$ cat ludicolopiloswine
    Способности Freezing Point Landslide
    Oblivious Snow Cloak

### 3
Команда: 

    cat tangela5/treecko tangela5/rampardos > archeops3_69
Результат:

    [s367945@helios ~/OPD/lab0]$ cat archeops3_69
    Тип диеты Herbivore
    Способности
    Mountain Peak Mold Breaker Rock Head

### 4
Команда:

    ln -s sunkern4 Copy_53
Результат:

    [s367945@helios ~/OPD/lab0]$ ls -l
    total 24
    -rwxrwxrwx  1 s367945  studs   92 10 сент. 14:45 archeops3
    -rw-r--r--  1 s367945  studs   88 10 сент. 17:16 archeops3_69
    lrwxr-xr-x  1 s367945  studs    8 10 сент. 17:23 Copy_53 -> sunkern4
    ...

### 5
Команды:

    rm poochyena9/ludicolopiloswine
    ln -s piloswine7 poochyena9/ludicolopiloswine
Результат:

    [s367945@helios ~/OPD/lab0/poochyena9]$ ls -l
    total 2
    -rwxrwxrwx  1 s367945  studs  50 10 сент. 14:45 ludicolo
    lrwxr-xr-x  1 s367945  studs  10 10 сент. 17:26 ludicolopiloswine -> piloswine7
    ...

### 6
Команда:

    ln gurdurr6 sunkern4/prinplupgurdurr
Результат:

    [s367945@helios ~/OPD/lab0]$ ls -l
    total 24
    5478020 -rwxrwxrwx  2 s367945  studs  121 10 сент. 14:45 gurdurr6
    ...
    [s367945@helios ~/OPD/lab0/sunkern4]$ ls -li
    total 16
    5478020 -rwxrwxrwx  2 s367945  studs  121 10 сент. 14:45 prinplupgurdurr
    ...
>Inode файлов одинаковы, следовательно создана жесткая ссылка


### 7
Команда:
Результат: