ldm 4
xch r14
ldm 7
xch r15
ldm 3
xch r12
ldm 10
xch r13

main:
jms $3f0
xch r2
jcn az finish
xch r1
jms process_char
xch r0
xch r2
xch r1
xch r3
xch r1
jms $3e0
jms process_char
xch r0
xch r2
xch r1
xch r3
jms $3e0
jun main


process_char:
ld r1
sub r13
jcn c1 letters
jcn c0 numbers

letters:
clb
ld r14
xch r0
ld r1
add r15
xch r1
bbl

numbers:
clb
ld r12
xch r0
bbl

finish:
jms $3ff
nop