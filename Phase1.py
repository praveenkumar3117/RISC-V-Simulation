x = []  # Registers
x.append(0)
for i in range(1, 32):
    x.append(i)
    if (i == 3):
        x[i] = int("0x10000000", 16)  # gp
    elif (i == 2):
        x[i] = int("0x7FFFFFF0", 16)  # sp


# executing functions
def executeMuskan(string, rs1, rs2, rd):
    if (string == "add"):  # executing add
        rs1 = int(rs1, 2)
        rs2 = int(rs2, 2)
        rd = int(rd, 2)
        print("rs1= ", rs1, " rs2= ", rs2, " rd= ", rd)
        x[rd] = x[rs1] + x[rs2]
        print("Registers :")
        for i in range(0, 32):
            print("x[", i, "]=", x[i])
    elif (string == "and"):  # executing and
        rs1 = int(rs1, 2)
        rs2 = int(rs2, 2)
        rd = int(rd, 2)
        print("rs1= ", rs1, " rs2= ", rs2, " rd= ", rd)
        x[rd] = x[rs1] & x[rs2]
        print("Registers :")
        for i in range(0, 32):
            print("x[", i, "]=", x[i])
    elif (string == "or"):  # executing or
        rs1 = int(rs1, 2)
        rs2 = int(rs2, 2)
        rd = int(rd, 2)
        print("rs1= ", rs1, " rs2= ", rs2, " rd= ", rd)
        x[rd] = x[rs1] | x[rs2]
        print("Registers :")
        for i in range(0, 32):
            print("x[", i, "]=", x[i])
    elif (string == "sll"):  # executing sll
        rs1 = int(rs1, 2)
        rs2 = int(rs2, 2)
        rd = int(rd, 2)
        print("rs1= ", rs1, " rs2= ", rs2, " rd= ", rd)
        x[rd] = x[rs1] << x[rs2]
        print("Registers :")
        for i in range(0, 32):
            print("x[", i, "]=", x[i])


def executeManan(string, rs1, rs2, rd):
    rd = int(rd, 2)
    rs1 = int(rs1, 2)
    rs2 = int(rs2, 2)
    if string == 'xor':
        x[rd] = x[rs1] ^ x[rs2]
    elif string == 'mul':
        x[rd] = x[rs1] * x[rs2]
    elif string == "div":
        x[rd] = x[rs1] // x[rs2]
    elif string == "rem":
        x[rd] = x[rs1] % x[rs2]
    print("Registers :")
    for i in range(0, 32):
        print("x[", i, "]=", x[i])


def executePratima(string,rd,imm,PC):
    imm = int(imm, 2)
    rd = int(rd, 2)
    print("imm = ", imm, " rd = ", rd)
    if string == "lui":  # executing lui
        x[rd] = 0 | imm
        x[rd] = x[rd] << 12
    elif string == "auipc": # executing lui
	    temp = 0 | imm
	    temp = temp << 12
	    x[rd] = PC + temp
    else:
            print("Error")
    print("Registers :")
    for i in range(0, 32):
        print("x[", i, "]=", x[i])


# decoding functions
def R_Format(binaryInstruction):  # MUSKAN GUPTA 2019CSB1100
    # add, and, or, sll, slt, sra, srl, sub, xor, mul, div, rem
    funct7 = binaryInstruction[0:7]
    rs2 = binaryInstruction[7:12]
    rs1 = binaryInstruction[12:17]
    funct3 = binaryInstruction[17:20]
    rd = binaryInstruction[20:25]
    opcode = binaryInstruction[25:32]
    # print("opcode: ",opcode," funct7:",funct7," rs2 ",rs2," rs1",rs1," funct3",funct3," rd ",rd)
    if (opcode == "0110011"):
        if (funct7 == "0000000"):
            if (funct3 == "000"):
                # add
                executeMuskan("add", rs1, rs2, rd)
                print("add")
            elif (funct3 == "111"):
                # and
                executeMuskan("and", rs1, rs2, rd)
                print(x)
                print("and")
            elif (funct3 == "110"):
                # or
                executeMuskan("or", rs1, rs2, rd)
                print(x)
                # add, and, or, sll,
                print("or")
            elif (funct3 == "001"):
                # sll
                executeMuskan("sll", rs1, rs2, rd)
                print(x)
                print("sll")
            elif (funct3 == "010"):
                # slt
                print("slt")
            elif (funct3 == "101"):
                # srl
                print("srl")
            elif (funct3 == "100"):
                # xor
                executeManan("xor", rs1, rs2, rd)
                print("xor")
            else:
                print("Error")
        elif (funct7 == "0100000"):
            if (funct3 == "000"):
                # sub
                print("sub")
            elif (funct3 == "101"):
                # sra
                print("sra")
            else:
                print("Error")
        elif (funct7 == "0000001"):
            if (funct3 == "000"):
                # mul
                executeManan("mul", rs1, rs2, rd)
                print("mul")
            elif (funct3 == "100"):
                # div
                executeManan("div", rs1, rs2, rd)
                print("div")
            elif (funct3 == "110"):
                # rem
                executeManan("rem", rs1, rs2, rd)
                print("rem")
            else:
                print("Error")
        else:
            print("Error")
    else:
        print("Error")
    return


def I_Format(binaryInstruction):  # Pratima_Singh
    # addi, andi, ori, lb, lh, lw, jalr
    imm = binaryInstruction[0:12]
    rs1 = binaryInstruction[12:17]
    funct3 = binaryInstruction[17:20]
    rd = binaryInstruction[20:25]
    opcode = binaryInstruction[25:32]
    print("opcode: ", opcode, " imm: ", imm, " rs1", rs1, " funct3", funct3, " rd ", rd)
    if (opcode == "0000011"):
        if (funct3 == "000"):
            # lb
            print("lb")
        elif (funct3 == "001"):
            # lh
            print("lh")
        elif (funct3 == "010"):
            # lw
            print("lw")
        else:
            print("Error")
    elif (opcode == "0010011"):
        if (funct3 == "000"):
            # addi
            print("addi")
        elif (funct3 == "111"):
            # andi
            print("andi")
        elif (funct3 == "110"):
            # ori
            print("ori")
        else:
            print("Error")
    elif (opcode == "1100111"):
        if (funct3 == "000"):
            # jalr
            print("jalr")
        else:
            print("Error")

    return


def sb_format(binary):  # MANAN SINGHAL 2019CSB1099
    opcode = binary[25:32]
    funct3 = binary[17:20]
    rs1 = binary[12:17]
    rs2 = binary[7:12]
    imm = binary[20:25] + binary[0:7]
    if funct3 == '000':
        print("beq")
    elif funct3 == '001':
        print("bne")
    elif funct3 == '101':
        print("bge")
    elif funct3 == '100':
        print("blt")
    else:
        print("Error")
    print("Opcode:" + opcode, funct3, rs2, rs1, imm)


def S_Format(m_c):  # PRAVEEN KUMAR 2019CSB1108

    func3 = m_c[17:20]  # funct3
    rs1 = m_c[12:17]  # source register1
    rs2 = m_c[7:12]  # source register2
    imm = m_c[0:7] + m_c[20:25]  # offset added to base adress
    # print("funct3:", func3)
    # print("rs1:",rs1)
    # print("rs2:",rs2)
    # print("immediate:",imm)
    Sr1 = 0;  # for decimal value of source register1
    Sr2 = 0;  # for decimal value of source register2
    for i in range(0, 5):
        if (rs1[i] == '1'):
            Sr1 = Sr1 + pow(2, 4 - i)
        if (rs2[i] == '1'):
            Sr2 = Sr2 + pow(2, 4 - i)
    # print("Decimal Value of rs1:",Sr1)
    # print("Decimal Value of rs2:",Sr2)
    Offset = 0;
    for i in range(0, 12):
        if (imm[i] == '1'):
            Offset = Offset + pow(2, 11 - i)

    # print("Decimal Value of offset:",Offset)

    if (func3 == '000'):

        # Execution of store_byte(sb)
        print("S_B")


    elif (func3 == '001'):

        # Execution of store_halfword(sh)
        print("S_H")


    elif (func3 == '010'):

        # Execution of store_word(sw)
        print("S_W")
    else:
        print("ERROR")


def U_Format(machinecode,PC):  # RAJASEKHAR 2019CSB1105
    # auipc,lui
    imm = machinecode[0:20]
    rd = machinecode[20:25]
    opcode = machinecode[25:32]  # opcode is enough to distinguish u and uj format instructions
    if (opcode == "0010111"):
        # auipc
        print("auipc")
        executePratima("auipc", rd, imm, PC)
    elif (opcode == "0110111"):
        # lui
        print("lui")
        executePratima("lui", rd, imm, PC)
    else:
        print("Error")

    return


def UJ_Format(machinecode):  # RAJASEKHAR 2019CSB1105
    # jal
    opcode = machinecode[25:32]

    if (opcode == "1101111"):
        # jal
        print("jal")
    else:
        print("Error")

    return


# fetching
file = open('machinecd.mc', 'r')
PC = 0
for line in file:
    PC += 4
    binaryno = bin(int(line[2:], 16))[2:].zfill(32)
    print("Instruction in binary: ", binaryno)
    opcode = binaryno[25:32]
    # print("opcode in the instruction ",opcode)
    R_oper = ["0110011"]
    I_oper = ["0010011", "0000011", "1100111"]
    S_oper = ["0100011"]
    SB_oper = ["1100011"]
    U_oper = ["0110111", "0010111"]
    UJ_oper = ["1101111"]
    if opcode in R_oper:
        # decode
        R_Format(binaryno)
    elif opcode in I_oper:
        # decode
        I_Format(binaryno)

    elif opcode in S_oper:
        S_Format(binaryno)
        # decode

    elif opcode in SB_oper:
        # decode
        sb_format(binaryno)

    elif opcode in U_oper:
        # decode
        U_Format(binaryno,PC)

    elif opcode in UJ_oper:
        # decode
        UJ_Format(binaryno)

    else:
        print("Error")






