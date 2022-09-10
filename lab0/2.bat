:: Character	Effect on files	                Effect on directories
:: -	        The file cannot be read.        The directory's contents cannot be shown.
:: r	        The file can be read.           The directory's contents can be shown.

:: -	        The file cannot be modified.    The directory's contents cannot be modified.
:: w	        The file can be modified.       The directory's contents can be modified (create new files or directories; rename or delete existing files or directories); requires the execute permission to be also set, otherwise this permission has no effect.

:: -	        The file cannot be executed.    The directory cannot be accessed with cd.
:: x	        The file can be executed.       The directory can be accessed with cd; this is the only permission bit that in practice can be considered to be "inherited" from the ancestor directories, in fact if any directory in the path does not have the x bit set, the final file or directory cannot be accessed either, regardless of its permissions; see path_resolution(7) for more information.


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

chmod u=rx,g=w,o=r hydregion
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