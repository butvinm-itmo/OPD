cd lab0 

:: 1
wc -l archeops3 | head -c 8 | tail -c 1 1>> archeops3
echo \ 1>> archeops3

:: 2
ls -Rt1l poochyena9

:: 3
grep -ni te archeops3 2> /dev/null

:: 4
grep --include=\*o -rh ".*" . | sort 2> /tmp/s3467945_errors

:: 5
grep --include=\p* -rl  ".*" . |xargs ls -lc 2> /tmp/s3467945_errors

:: 6
grep -rhi ".*[^h]$" ./poochyena9/ 2> /dev/null