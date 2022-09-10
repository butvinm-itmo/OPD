cd lab0 

:: 1
wc -l archeops3 | head -c 8 | tail -c 1 >> archeops3
echo \ >> archeops3

:: 2
ls -Rt1l poochyena9

:: 3
grep -n -i te archeops3 2> /dev/null

:: 4
mkdir tmp
grep --include=\*o -rh ".*" . | sort 2> tmp/errors

:: 5
grep --include=\p* -rl  ".*" . |xargs  ls -lt 2> tmp/errors

:: 6
grep -rhi ".*[^h]$" ./poochyena9/ 2> /dev/null