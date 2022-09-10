cd lab0 

:: 1
echo Task 1
wc -l archeops3 | head -c 9 >> archeops3

:: 2
echo Task 2
ls -Rc1l poochyena9

:: 3
echo Task 3
grep -n -i te archeops3 2> /dev/null

:: 4
echo Task 4
mkdir tmp
grep --include=\*o -rh ".*" . | sort 2> tmp/errors

:: 5
echo Task 5
grep --include=\p* -rl  ".*" . |xargs  ls -lc 2> tmp/errors

:: 6
echo Task 6
grep -rhi ".*[^h]$" ./poochyena9/ 2> /dev/null