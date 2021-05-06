RISC-V Simulator

Team Details:
Muskan Gupta	2019CSB1100
Manan Singhal	2019CSB1099
Praveen kumar	2019CSB1108
Pratima singh	2018CEB1021
Rajasekhar		2019CSB1105

Contribution:
Muskan Gupta - Functions for add ,and, or, sll, executeread, memory store, executestore, main decode, R format(decoding), Fetch main, Memory writeback to mc file, Write back, main execute, Debugging, logic thinking
Praveen kumar - Functions for addi, andi, ori, jal, jalr, memory read, s format(decoding),Fetch main, Memory writeback to mc file, main execute, Debugging, logic thinking
Manan Singhal - Functions for xor, mul , div, rem, bge , blt, main decode, sb format (decoding),Fetch main, Memory writeback to mc file, main execute, Debugging, logic thinking
Pratima Singh - functions for lui, auipc, memory read, I format(decoding),Fetch main, Memory writeback to mc file, find negative function, main execute, Debugging, logic thinking
Rajasekhar - Functions for slt, sra, srl, sub, beq, bne, U format (decoding), UJ format (decoding) ,Fetch main, Memory writeback to mc file, main execute, Debugging, logic thinking

How to run the program:
1) First of all, unzip all the files.
2) To run use command $python3 Phase1.py "Your_mc_file.mc"      #Example $python3 Phase1.py fact.mc
3) fact.mc is the machine code file for factorial program.
4) fibo.mc is the machine code file for fibonacci program.
5) bubblesort.mc is the machine code file for bubble sort program.
6) Phase1.py consists of function simulator code for phase1.
NOTE: 0xFFFFFFFF is the termination instruction, after that no further operations.



OUTPUT FORMAT:
1) At every instruction it will show fetched machine code and it's address.
2) Then it will show the operation needed to be performed and it's sources.
3) Then it will show the ALU content.
4) Then it will show whether the memory is accessed or not, if yes then show the address of memory.
5) Then it will show whether writeback is to be performed or not, if yes then it shows Destination register and value to be writebacked.
6) Then it will show the clock cycle at the particular instruction.














