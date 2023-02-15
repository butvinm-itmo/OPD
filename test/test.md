This is Basic Computer assembly
<!-- 

file://c:\Coding\.OPD\test\test.bcomp#3
file://c:\Coding\.OPD\test\test.bcomp:3
file:///c:\Coding\.OPD\test\test.bcomp#3
file:///c:\Coding\.OPD\test\test.bcomp:3 
file:///c:\Coding\.OPD\test\test.bcomp:3
-->
```bcomp
ORG             0x000

result:         WORD	    ?

process_input:	HLT
	            input:	    WORD	?
	            RET

START:	        CLA
	            JUMP	    loop

loop:	        CALL	    process_input
	            LD	        input
	            ROR
```

