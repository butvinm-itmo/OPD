#### «Национальный исследовательский университет ИТМО»
### Основы профессиональной деятельности
## Лабораторная работа 1
## Вариант 3002
### Бутвин Михаил, P3130
###  2022
<div style="page-break-after: always;"></div>

## Задание 1
![Task1](https://sun9-40.userapi.com/impg/awP17VlTfbK-OHVLV8ccctgRiDL7GwG8NPgs0Q/QWBvB95mdvk.jpg?size=1503x700&quality=95&sign=4be42e9e1edfb1d56a3847296783e0fc&type=album)

Введенные команды:

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

Результат:

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
Установить согласно заданию права на файлы и каталоги при помощи команды chmod, используя различные способы указания прав.
- archeops3: r--r--r--
- gurdurr6: владелец должен читать файл; группа-владелец должна не иметь никаких прав; остальные пользователи должны не иметь никаких прав
- piloswine7: владелец должен читать файл; группа-владелец должна читать файл; остальные пользователи должны не иметь никаких прав
- poochyena9: владелец должен читать, записывать директорию и переходить в нее; группа-владелец должна записывать директорию и переходить в нее; остальные пользователи должны записывать директорию и переходить в нее
- ludicolo: владелец должен читать файл; группа-владелец должна читать файл; остальные пользователи должны читать файл
- seel: владелец должен записывать директорию и переходить в нее; группа-владелец должна записывать директорию и переходить в нее; остальные пользователи должны записывать директорию и переходить в нее
- simisage: владелец должен записывать директорию и переходить в нее; группа-владелец должна только переходить в директорию; остальные пользователи должны только переходить в директорию
- sunkern4: права 751
- hydreigon: владелец должен читать директорию и переходить в нее; группа-владелец должна записывать директорию; остальные пользователи должны читать директорию
- honchkrow: права 337
- bronzong: rwxr-x-wx
- mightyena: r--------
- prinplup: r--------
- cottonee: права 644
- tangela5: владелец должен читать, записывать директорию и переходить в нее; группа-владелец должна записывать директорию и переходить в нее; остальные пользователи должны записывать директорию и переходить в нее
- tangrowth: права 330
- treecko: права 664
- rampardos: права 046

Введенные команды:

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

Результат

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


## Задание 3
> !!! Из-за изменения прав на файлы во втором задании некоторые команды могут выдавать ошибки доступа. Выполните **chmod -R 777 lab0**, чтобы избежать этого. Чтобы проверить перенаправление ошибок в 4 задании, снова выполните второй скрипт

> !!! Перейдите в lab0 перед выполнением (чтобы убрать повторяющиеся *lab0*/ в  путях файлов)

Скопировать часть дерева и создать ссылки внутри дерева согласно заданию при помощи команд cp и ln, а также комманды cat и перенаправления ввода-вывода.

- скопировать рекурсивно директорию sunkern4 в директорию lab0/poochyena9/seel
- скопировать содержимое файла piloswine7 в новый файл lab0/poochyena9/ludicolopiloswine
- объеденить содержимое файлов lab0/tangela5/treecko, lab0/tangela5/rampardos, в новый файл lab0/archeops3_69
- создать символическую ссылку c именем Copy_53 на директорию sunkern4 в каталоге lab0
- cоздать символическую ссылку для файла piloswine7 с именем lab0/poochyena9/ludicolopiloswine
- cоздать жесткую ссылку для файла gurdurr6 с именем lab0/sunkern4/prinplupgurdurr
- скопировать файл piloswine7 в директорию lab0/sunkern4/hydreigon

### 1
Команда:

    cp -r sunkern4 poochyena9/seel
Результат:

    [s367945@helios ~/OPD/lab0/poochyena9/seel/sunkern4]$ ls
    bronzong        cottonee        honchkrow       hydreigon       mightyena       prinplup

### 2
Команда:

    cp piloswine7 ./poochyena9/ludicolopiloswine

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
    [s367945@helios ~/OPD/lab0/lab0]$ cd Copy_53
    [s367945@helios ~/OPD/lab0/lab0/Copy_53]$ ls
    bronzong        cottonee        honchkrow       hydreigon       mightyena       prinplup

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
> Inode файлов одинаковы, следовательно создана жесткая ссылка


### 7
Команда:

    cp piloswine7 sunkern4/hydreigon/piloswine7
Результат:

    [s367945@helios ~/OPD/lab0/sunkern4/hydreigon]$ cat piloswine7
    Способности Freezing Point Landslide
    Oblivious Snow Cloak

## Задание 4
> Перейдите в lab0 перед выполнением (чтобы убрать повторяющиеся *lab0*/ в  путях файлов)

Используя команды cat, wc, ls, head, tail, echo, sort, grep выполнить в соответствии с вариантом задания поиск и фильтрацию файлов, каталогов и содержащихся в них данных.

- Подсчитать количество строк содержимого файла archeops3, результат дописать в тот-же файл, ошибки доступа не подавлять и не перенаправлять
- Вывести рекурсивно список имен и атрибутов файлов в директории poochyena9, список отсортировать по возрастанию даты модификации файла, ошибки доступа не подавлять и не перенаправлять
- Вывести содержимое файла archeops3 с номерами строк, оставить только строки, содержащие "te", регистр символов игнорировать, подавить вывод ошибок доступа
- Рекурсивно вывести содержимое файлов из директории lab0, имя которых заканчивается на 'o', строки отсортировать по имени a->z, ошибки доступа перенаправить в файл в директории /tmp
- Вывести рекурсивно список имен и атрибутов файлов в директории lab0, начинающихся на символ 'p', список отсортировать по возрастанию даты изменения записи о файле, ошибки доступа перенаправить в файл в директории /tmp
- Вывести содержимое файлов в директории poochyena9, исключить строки, заканчивающиеся на 'h', регистр символов игнорировать, подавить вывод ошибок доступа

### 1
Команда:

    wc -l archeops3 | head -c 8 | tail -c 1 1>> archeops3
    echo \ 1>> archeops3
Результат:

    [s367945@helios ~/OPD/lab0]$ cat archeops3
    Возможности Overland=12 Surface=1 Sky=6 Jump=6 Power2=0
    Inteliigence=4 Fragile=0
    2

### 2
Команда:

    ls -R1trl | grep "^[d|-]"
Результат:

    -rw-r--r--  1 s367945  studs   95 10 сент. 18:03 archeops3
    drwxr-xr-x  5 s367945  studs    9 10 сент. 17:59 sunkern4
    drwxr-xr-x  4 s367945  studs    6 10 сент. 17:59 poochyena9
    -rw-r--r--  1 s367945  studs   88 10 сент. 17:59 archeops3_69
    drwxr-xr-x  3 s367945  studs    5 10 сент. 17:56 tangela5
    -rw-r--r--  1 s367945  studs   69 10 сент. 17:56 piloswine7
    -rw-r--r--  2 s367945  studs  121 10 сент. 17:56 gurdurr6
    drwxr-xr-x  2 s367945  studs    3 10 сент. 17:59 hydreigon
    drwxr-xr-x  2 s367945  studs    2 10 сент. 17:56 bronzong
    drwxr-xr-x  2 s367945  studs    2 10 сент. 17:56 honchkrow
    -rw-r--r--  1 s367945  studs   20 10 сент. 17:56 cottonee
    -rw-r--r--  1 s367945  studs  106 10 сент. 17:56 prinplup
    -rw-r--r--  1 s367945  studs  141 10 сент. 17:56 mightyena
    -rw-r--r--  2 s367945  studs  121 10 сент. 17:56 prinplupgurdurr
    -rw-r--r--  1 s367945  studs  69 10 сент. 17:59 piloswine7
    drwxr-xr-x  3 s367945  studs   3 10 сент. 17:59 seel
    drwxr-xr-x  2 s367945  studs   2 10 сент. 17:56 simisage
    -rw-r--r--  1 s367945  studs  50 10 сент. 17:56 ludicolo
    drwxr-xr-x  5 s367945  studs  8 10 сент. 17:59 sunkern4
    drwxr-xr-x  2 s367945  studs    2 10 сент. 17:59 hydreigon
    -rw-r--r--  1 s367945  studs   20 10 сент. 17:59 cottonee
    -rw-r--r--  1 s367945  studs  141 10 сент. 17:59 mightyena
    drwxr-xr-x  2 s367945  studs    2 10 сент. 17:59 bronzong
    -rw-r--r--  1 s367945  studs  106 10 сент. 17:59 prinplup
    drwxr-xr-x  2 s367945  studs    2 10 сент. 17:59 honchkrow
    drwxr-xr-x  2 s367945  studs   2 10 сент. 17:56 tangrowth
    -rw-r--r--  1 s367945  studs  60 10 сент. 17:56 rampardos
    -rw-r--r--  1 s367945  studs  28 10 сент. 17:56 treecko

### 3
Команда:

    grep -ni te archeops3 2> /dev/null
Результат:

    2:Inteliigence=4 Fragile=0

### 4
Команда:
> Уберите флаг h для проверки названия файлов

    grep --include=\*o -rh ".*" . | sort 2> /tmp/s3467945_errors
Результат:

    Tempo
    Развитые способности Own
    Тип диеты Herbivore

### 5
Команда:

    ls -R1crl | grep "^[d|-]" | grep -E " p.+$" 2>> /tmp/s3467945_errors
Результат:

    -rwxrwxrwx  1 s367945  studs   69 18 сент. 01:09 piloswine7
    drwxrwxrwx  4 s367945  studs    6 18 сент. 01:09 poochyena9
    -rwxrwxrwx  1 s367945  studs  106 18 сент. 01:09 prinplup

### 6   
Команда:

    grep -rhi ".*[^h]$" ./poochyena9/ 2> /dev/null
Результат:

    Развитые способности Own
    Tempo
    Ходы Covert Dive Icy Wind Mud-Slap Signal Beam Sleep
    Talk Snore Stealth Rock Water Pledge Water Pulse
    Roar Swagger Assurance Scary Face Taunt Embargo Take Down Thief Sucker
    satk=4
    sdef=5 spd=7

## Задание 5
> Перейдите в lab0 перед выполнением (чтобы убрать повторяющиеся *lab0*/ в  путях файлов)

Выполнить удаление файлов и каталогов при помощи команд rm и rmdir согласно варианту задания.

- Удалить файл archeops3
- Удалить файл lab0/sunkern4/cottonee
- удалить символические ссылки Copy_*
- удалить жесткие ссылки lab0/sunkern4/prinplupgurdu*
- Удалить директорию sunkern4
- Удалить директорию lab0/sunkern4/honchkrow

### 1
Команда:

    rm archeops3
Результат:

    [s367945@helios ~/OPD/lab0]$ ls
    archeops3_69    Copy_53         gurdurr6        piloswine7      poochyena9      sunkern4        tangela5        

### 2
Команда:

    rm ./sunkern4/cottonee
Результат:

    [s367945@helios ~/OPD/lab0/sunkern4]$ ls
    bronzong        honchkrow       hydreigon       mightyena       prinplup        prinplupgurdurr

### 3
Команда:

    rm ./Copy_53
Результат:

    [s367945@helios ~/OPD/lab0]$ ls
    archeops3_69    gurdurr6        piloswine7      poochyena9      sunkern4        tangela5        

### 4
Команда:

    rm ./sunkern4/prinplupgurdurr
Результат:

    [s367945@helios ~/OPD/lab0/sunkern4]$ ls
    bronzong        honchkrow       hydreigon       mightyena       prinplup
### 5
Команда:

    rm -fr ./sunkern4
Результат:

    [s367945@helios ~/OPD/lab0]$ ls
    archeops3_69    gurdurr6        piloswine7      poochyena9      tangela5        

### 6
Команда:

    rm -fr ./sunkern4/honchkrow
Результат:

    [s367945@helios ~/OPD/lab0]$ rm -fr ./sunkern4/honchkrow
    [s367945@helios ~/OPD/lab0]$

> Вывода нет, тк мы уже удалили директорию sunkern4 и все файлы в ней ранее


## Вывод
В ходе работы были изучены консольные команды ОС FreeDOS

![Mem](https://sun9-72.userapi.com/impg/I3gP9F8g-CVKDqLkNojPSu70k7LNnCNV1GdAqw/PJkv3DxOx_E.jpg?size=1470x2048&quality=96&sign=07bbbd631fd10526cc30b69122e9e71b&type=album) 