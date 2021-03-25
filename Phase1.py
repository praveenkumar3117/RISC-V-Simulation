x=[] #Registers
x.append(0)
for i in range(1,32):
    x.append(i)
    if(i==3):
        x[i]=int("0x10000000",16)  #gp
    elif(i==2):
        x[i]=int("0x7FFFFFF0",16)  #sp




#executing functions
def execute(string,rs1,rs2,rd):
    if(string=="add"):   #executing add
        rs1=int(rs1,2)
        rs2 = int(rs2, 2)
        rd = int(rd, 2)
        print("rs1= ",rs1," rs2= ",rs2," rd= ",rd)
        x[rd]=x[rs1]+x[rs2]
        print("Registers :")
        for i in range(0,32):
            print("x[",i,"]=",x[i])
    elif(string=="and"):   #executing and
        rs1 = int(rs1, 2)
        rs2 = int(rs2, 2)
        rd = int(rd, 2)
        print("rs1= ", rs1, " rs2= ", rs2, " rd= ", rd)
        x[rd] = x[rs1] & x[rs2]
        print("Registers :")
        for i in range(0, 32):
            print("x[", i, "]=", x[i])
    elif(string=="or"):   #executing or
        rs1 = int(rs1, 2)
        rs2 = int(rs2, 2)
        rd = int(rd, 2)
        print("rs1= ", rs1, " rs2= ", rs2, " rd= ", rd)
        x[rd] = x[rs1] | x[rs2]
        print("Registers :")
        for i in range(0, 32):
            print("x[", i, "]=", x[i])
    elif(string=="sll"):   #executing sll
        rs1 = int(rs1, 2)
        rs2 = int(rs2, 2)
        rd = int(rd, 2)
        print("rs1= ", rs1, " rs2= ", rs2, " rd= ", rd)
        x[rd] = x[rs1] << x[rs2]
        print("Registers :")
        for i in range(0, 32):
            print("x[", i, "]=", x[i])







# decoding functions
def R_Format(binaryInstruction):
    #add, and, or, sll, slt, sra, srl, sub, xor, mul, div, rem
    funct7=binaryInstruction[0:7]
    rs2=binaryInstruction[7:12]
    rs1=binaryInstruction[12:17]
    funct3=binaryInstruction[17:20]
    rd=binaryInstruction[20:25]
    opcode=binaryInstruction[25:32]
    #print("opcode: ",opcode," funct7:",funct7," rs2 ",rs2," rs1",rs1," funct3",funct3," rd ",rd)
    if(opcode=="0110011"):
        if(funct7=="0000000"):
            if(funct3=="000"):
                #add
                execute("add",rs1,rs2,rd)
                print("add")
            elif(funct3=="111"):
                #and
                execute("and", rs1, rs2, rd)
                print(x)
                print("and")
            elif(funct3=="110"):
                #or
                execute("or", rs1, rs2, rd)
                print(x)
                #add, and, or, sll,
                print("or")
            elif(funct3=="001"):
                #sll
                execute("sll", rs1, rs2, rd)
                print(x)
                print("sll")
            elif(funct3=="010"):
                #slt
                print("slt")
            elif(funct3=="101"):
                #srl
                print("srl")
            elif(funct3=="100"):
                #xor
                print("xor")
            else:
                print("Error")
        elif(funct7=="0100000"):
            if(funct3=="000"):
                #sub
                print("sub")
            elif(funct3=="101"):
                #sra
                print("sra")
            else:
                print("Error")
        elif(funct7=="0000001"):
            if (funct3 == "000"):
                # mul
                print("mul")
            elif (funct3 == "100"):
                # div
                print("div")
            elif (funct3 == "110"):
                # rem
                print("rem")
            else:
                print("Error")
        else:
            print("Error")
    else:
        print("Error")
    return


#fetching
file = open('machinecd.mc', 'r')
PC=0
for line in file:
    PC+=4
    binaryno=bin(int(line[2:], 16))[2:].zfill(32)
    print("Instruction in binary: ",binaryno)
    opcode=binaryno[25:32]
    #print("opcode in the instruction ",opcode)
    R_oper=["0110011"]
    I_oper=["0010011","0000011","1100111"]
    S_oper=["0100011"]
    SB_oper=["1100111"]
    U_oper=["0110111","0010111"]
    UJ_oper=["1101111"]
    if opcode in R_oper:
        #decode
        R_Format(binaryno)
    elif opcode in I_oper:
        # decode
        pass
    elif opcode in S_oper:
        # decode
        pass
    elif opcode in SB_oper:
        # decode
        pass
    elif opcode in U_oper:
        # decode
        pass
    elif opcode in UJ_oper:
        # decode
        pass
    else:
        print("Error")

