x = []  # Registers
x.append(0)
for i in range(1, 32):
    x.append(0)
    if (i == 3):
        x[i] = int("0x10000000", 16)  # gp
    elif (i == 2):
        x[i] = int("0x7FFFFFF0", 16)  # sp

memory = {}


# executing functions
def executeMuskan(string, rs1, rs2, rd):
    if (string == "add"):  # executing add
        rs1 = int(rs1, 2)
        rs2 = int(rs2, 2)
        rd = int(rd, 2)
        print("rs1= ", rs1, " rs2= ", rs2, " rd= ", rd)
        s = x[rs1] + x[rs2]
        if (s >= -(pow(2, 31)) and s <= (pow(2, 31)) - 1):  # checking for underflow or overflow
            x[rd] = s


    elif (string == "and"):  # executing and
        rs1 = int(rs1, 2)
        rs2 = int(rs2, 2)
        rd = int(rd, 2)
        print("rs1= ", rs1, " rs2= ", rs2, " rd= ", rd)
        s = x[rs1] & x[rs2]
        if (s >= -(pow(2, 31)) and s <= (pow(2, 31)) - 1):  # checking for underflow or overflow
            x[rd] = s


    elif (string == "or"):  # executing or
        rs1 = int(rs1, 2)
        rs2 = int(rs2, 2)
        rd = int(rd, 2)
        print("rs1= ", rs1, " rs2= ", rs2, " rd= ", rd)
        s = x[rs1] | x[rs2]
        if (s >= -(pow(2, 31)) and s <= (pow(2, 31)) - 1):  # checking for underflow or overflow
            x[rd] = s


    elif (string == "sll"):  # executing sll
        rs1 = int(rs1, 2)
        rs2 = int(rs2, 2)
        rd = int(rd, 2)
        print("rs1= ", rs1, " rs2= ", rs2, " rd= ", rd)
        s = x[rs1] << x[rs2]
        if (s >= -(pow(2, 31)) and s <= (pow(2, 31)) - 1):  # checking for underflow or overflow
            x[rd] = s

    print("Registers :")
    for i in range(0, 32):
        print("x[", i, "]=", x[i])


def executeManan(string, rs1, rs2, rd):
    rd = int(rd, 2)
    rs1 = int(rs1, 2)
    rs2 = int(rs2, 2)
    if string == 'xor':
        output = x[rs1] ^ x[rs2]
        if -(pow(2, 31)) <= output <= (pow(2, 31)) - 1:  # Underflow and overflow
            x[rd] = output
    elif string == 'mul':
        output = x[rs1] * x[rs2]
        if -(pow(2, 31)) <= output <= (pow(2, 31)) - 1:  # Underflow and overflow
            x[rd] = output
    elif string == "div":
        output = x[rs1] // x[rs2]
        if -(pow(2, 31)) <= output <= (pow(2, 31)) - 1:  # Underflow and overflow
            x[rd] = output
    elif string == "rem":
        output = x[rs1] % x[rs2]
        if -(pow(2, 31)) <= output <= (pow(2, 31)) - 1:  # Underflow and overflow
            x[rd] = output
    print(string)
    print("Registers :")
    for i in range(0, 32):
        print("x[", i, "]=", x[i], end=" ", sep='')


def executePratima(string, rd, imm, PC):
    imm = int(imm, 2)
    rd = int(rd, 2)
    print("imm = ", imm, " rd = ", rd)
    if string == "lui":  # executing lui
        if (imm <= pow(2, 19) - 1 and imm >= -pow(2, 19)):  # checking range of imm
            x[rd] = 0 | imm
            temp = x[rd] << 12
            if (temp >= -(pow(2, 31)) and temp <= (pow(2, 31)) - 1):  # checking for underflow or overflow
                x[rd] = temp
    elif string == "auipc":  # executing auipc
        if (imm <= pow(2, 19) - 1 and imm >= -pow(2, 19)):  # checking range of imm
            temp = 0 | imm
            temp = temp << 12
            temp = temp + PC
            if (temp >= -(pow(2, 31)) and temp <= (pow(2, 31)) - 1):  # checking for underflow or overflow
                x[rd] = temp
    else:
        print("Error")
    print("Registers :")
    for i in range(0, 32):
        print("x[", i, "]=", x[i])


def executeRajasekhar(string, rs1, rs2, rd):
    # slt,sra,srl,sub
    rd = int(rd, 2)
    rs1 = int(rs1, 2)
    rs2 = int(rs2, 2)

    if (string == "slt"):
        if (x[rs1] < x[rs2]):
            x[rd] = 1
        else:
            x[rd] = 0
    elif (string == "sra"):
        result = x[rs1] >> x[rs2]
        lowerlimit = -1 * (1 << 31)
        upperlimit = (1 << 31) - 1
        if (lowerlimit <= result and result <= upperlimit):  # checking underflow and overflow condition
            x[rd] = result
    elif (string == "srl"):
        result = x[rs1] >> x[rs2]
        lowerlimit = -1 * (1 << 31)
        upperlimit = (1 << 31) - 1
        if (lowerlimit <= result and result <= upperlimit):
            x[rd] = result
    elif (string == "sub"):
        result = x[rs1] - x[rs2]
        lowerlimit = -1 * (1 << 31)
        upperlimit = (1 << 31) - 1
        if (lowerlimit <= result and result <= upperlimit):
            x[rd] = result

    print("Registers :")
    for i in range(0, 32):
        print("x[", i, "]=", x[i])


def executePraveen(string, rd, rs1, imm):  # PRAVEEN KUMAR 2019CSb1108      #addi,andi,ori
    rs1 = int(rs1, 2)
    rd = int(rd, 2)
    imm = int(imm, 2)

    if (string == "addi"):
        print("Operation is addi")
        if (imm <= pow(2, 11) - 1 and imm >= -pow(2, 11)):  # checking range of imm
            s = x[rs1] + imm
            if (s >= -(pow(2, 31)) and s <= (pow(2, 31)) - 1):  # checking for underflow or overflow
                x[rd] = s

    elif (string == "andi"):
        print("Operation is andi")
        if (imm <= pow(2, 11) - 1 and imm >= -pow(2, 11)):  # checking range of imm
            s = x[rs1] & imm
            if (s >= -(pow(2, 31)) and s <= (pow(2, 31)) - 1):  # checking for underflow or overflow
                x[rd] = s

    elif (string == "ori"):
        print("Operation is ori")
        if (imm <= pow(2, 11) - 1 and imm >= -pow(2, 11)):  # checking range of imm
            s = x[rs1] | imm
            if (s >= -(pow(2, 31)) and s <= (pow(2, 31)) - 1):  # checking for underflow or overflow
                x[rd] = s

    print("rs1= ", rs1, " rd= ", rd, " imm= ", imm)
    print("Registers :")
    for i in range(0, 32):
        print("x[", i, "]=", x[i])


def executeManan1(string, rs1, rs2, imm, pc):
    rs1 = int(rs1, 2)
    rs2 = int(rs2, 2)
    imm = int(imm, 2)
    imm = imm << 1
    if string == "bge":
        if x[rs1] >= x[rs2]:
            pc = pc + imm
        else:
            pc = pc + 4
    elif string == 'blt':
        if x[rs1] < x[rs2]:
            pc = pc + imm
        else:
            pc = pc + 4

    print("Registers :")
    for i in range(0, 32):
        print("x[", i, "]=", x[i], end=" ", sep='')

    return pc


def executeRajasekhar1(string, rs1, rs2, imm, pc):
    rs1 = int(rs1, 2)
    rs2 = int(rs2, 2)
    imm = int(imm, 2)
    imm = imm << 1
    if (string == 'beq'):
        if (x[rs1] == x[rs2]):
            pc = pc + imm
        else:
            pc = pc + 4
    elif (string == 'bne'):
        if (x[rs1] != x[rs2]):
            pc = pc + imm
        else:
            pc = pc + 4

    print("Registers :")
    for i in range(0, 32):
        print("x[", i, "]=", x[i], end=" ", sep='')

    return pc


def executePraveen1(string, rd, imm, pc):  # Praveen Kumar 2019CSB1108    jal  function
    rd = int(rd, 2)
    imm = int(imm, 2)
    imm = imm << 1
    if (string == 'jal'):
        temp = pc
        pc = pc + imm
        x[rd] = temp + 4
    return pc


def executePraveen2(string, rs1, rd, imm, pc):  # Praveen Kumar 2019CSB1108    jalr function
    rs1 = int(rs1, 2)
    rd = int(rd, 2)
    imm = int(imm, 2)
    if (string == 'jalr'):
        temp = pc
        pc = x[rs1] + imm
        if (rd != 0):
            x[rd] = temp + 4

    return pc


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
                executeRajasekhar("slt", rs1, rs2, rd)
                print(x)
                print("slt")
            elif (funct3 == "101"):
                # srl
                executeRajasekhar("srl", rs1, rs2, rd)
                print(x)
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
                executeRajasekhar("sub", rs1, rs2, rd)
                print(x)
                print("sub")
            elif (funct3 == "101"):
                # sra
                executeRajasekhar("sra", rs1, rs2, rd)
                print(x)
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


def I_Format(binaryInstruction, PC):  # Pratima_Singh
    # addi, andi, ori, lb, lh, lw, jalr
    imm = binaryInstruction[0:12]
    rs1 = binaryInstruction[12:17]
    funct3 = binaryInstruction[17:20]
    rd = binaryInstruction[20:25]
    opcode = binaryInstruction[25:32]
    print("opcode: ", opcode, " imm: ", imm, " rs1: ", rs1, " funct3: ", funct3, " rd: ", rd)
    if (opcode == "0000011"):
        if (funct3 == "000"):
            # lb
            print("lb")
            PC += 4
        elif (funct3 == "001"):
            # lh
            print("lh")
            PC += 4
        elif (funct3 == "010"):
            # lw
            print("lw")
            PC += 4
        else:
            print("Error")
            PC += 4
    elif (opcode == "0010011"):
        if (funct3 == "000"):
            # addi
            executePraveen("addi", rd, rs1, imm)
            print("addi")
            PC += 4
        elif (funct3 == "111"):
            # andi
            executePraveen("andi", rd, rs1, imm)
            print("andi")
            PC += 4
        elif (funct3 == "110"):
            # ori
            executePraveen("ori", rd, rs1, imm)
            print("ori")
            PC += 4
        else:
            print("Error")
            PC += 4
    elif (opcode == "1100111"):
        if (funct3 == "000"):
            # jalr
            PC = executePraveen2("jalr", rs1, rd, imm, PC)
            print("jalr")
        else:
            print("Error")
            PC += 4

    return PC


def sb_format(binary, pc):  # MANAN SINGHAL 2019CSB1099
    sb_opcode = binary[25:32]
    funct3 = binary[17:20]
    rs1 = binary[12:17]
    rs2 = binary[7:12]
    imm = binary[0] + binary[24] + binary[1:7] + binary[20:24]
    # print("Opcode:" + sb_opcode, ", funct3:", funct3, ", rs2:", rs2, ", rs1:", rs1, ", imm:", imm)
    if funct3 == '000':
        print("beq")
        pc = executeRajasekhar1("beq", rs1, rs2, imm, pc)
    elif funct3 == '001':
        print("bne")
        pc = executeRajasekhar1("bne", rs1, rs2, imm, pc)
    elif funct3 == '101':
        print("bge")
        pc = executeManan1("bge", rs1, rs2, imm, pc)
    elif funct3 == '100':
        print("blt")
        pc = executeManan1("blt", rs1, rs2, imm, pc)
    else:
        print("Error")

    return pc


def MemoryStore(string, rs1, rs2, imm):
    rs1 = int(rs1, 2)
    rs2 = int(rs2, 2)
    imm = int(imm, 2)
    dataa = hex(x[rs2])[2:].zfill(8)

    if (string == "sw"):
        if (x[rs1] + imm >= 268435456):  # data segment starts with address 268435456 or 0x10000000
            memory[x[rs1] + imm] = int(dataa[6:], 16)
            memory[x[rs1] + imm + 1] = int(dataa[4:6], 16)
            memory[x[rs1] + imm + 2] = int(dataa[2:4], 16)
            memory[x[rs1] + imm + 3] = int(dataa[0:2], 16)
    elif (string == "sh"):
        if (x[rs1] + imm >= 268435456):
            memory[x[rs1] + imm] = int(dataa[6:], 16)
            memory[x[rs1] + imm + 1] = int(dataa[4:6], 16)
    elif (string == "sb"):
        if (x[rs1] + imm >= 268435456):
            memory[x[rs1] + imm] = int(dataa[6:], 16)


def S_Format(m_c):  # PRAVEEN KUMAR 2019CSB1108

    func3 = m_c[17:20]  # funct3
    rs1 = m_c[12:17]  # source register1
    rs2 = m_c[7:12]  # source register2
    imm = m_c[0:7] + m_c[20:25]  # offset added to base adress
    # print("funct3:", func3)
    # print("rs1:",rs1)
    # print("rs2:",rs2)
    # print("immediate:",imm)
    Sr1 = 0  # for decimal value of source register1
    Sr2 = 0  # for decimal value of source register2
    for i in range(0, 5):
        if (rs1[i] == '1'):
            Sr1 = Sr1 + pow(2, 4 - i)
        if (rs2[i] == '1'):
            Sr2 = Sr2 + pow(2, 4 - i)
    # print("Decimal Value of rs1:",Sr1)
    # print("Decimal Value of rs2:",Sr2)
    Offset = 0
    for i in range(0, 12):
        if (imm[i] == '1'):
            Offset = Offset + pow(2, 11 - i)

    # print("Decimal Value of offset:",Offset)

    if (func3 == '000'):

        # Execution of store_byte(sb)
        print("sb")
        MemoryStore("sb", rs1, rs2, imm)


    elif (func3 == '001'):

        # Execution of store_halfword(sh)
        print("sh")
        MemoryStore("sh", rs1, rs2, imm)


    elif (func3 == '010'):
        # Execution of store_word(sw)
        print("sw")
        MemoryStore("sw", rs1, rs2, imm)
    else:
        print("ERROR")


def U_Format(machinecode, PC):  # RAJASEKHAR 2019CSB1105
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


def UJ_Format(machinecode, pc):  # RAJASEKHAR 2019CSB1105
    # jal
    opcode = machinecode[25:32]
    imm = machinecode[0] + machinecode[11:20] + machinecode[20] + machinecode[1:11]
    # imm=machinecode[0]+machinecode[10:20]+machinecode[9]+machinecode[1:9]
    print(int(imm, 2))
    rd = machinecode[20:25]
    if (opcode == "1101111"):
        # jal
        print(pc)
        pc = executePraveen1("jal", rd, imm, pc)
        print("jal", pc)
    else:
        print("Error")

    return pc


# fetching
file = open('machinecd.mc', 'r')
PC = 0
datasegOrnot = 0
for line in file:
    if (line == "\n"):
        datasegOrnot = 1
        continue
    if (datasegOrnot == 1):  # fetching memory from data segment
        dataArray = line.split(' ')
        daata = dataArray[1][2:]
        memory[int(dataArray[0], 16)] = int(daata, 16)
        continue
file.close()

Instruct={}
last_PC=0
file = open('machinecd.mc', 'r')
for line in file:
    if (line == "\n"):
        break
    inputsArray = line.split(' ')
    tempc = int(inputsArray[0][2:], 16)
    binaryno = bin(int(inputsArray[1][2:], 16))[2:].zfill(32)
    Instruct[tempc] = binaryno
    last_PC = tempc
file.close()
    # binaryno = bin(int(line[2:], 16))[2:].zfill(32)
    #print("Instruction in binary: ", binaryno)
while (PC<=last_PC):
    binaryno=Instruct[PC]
    opcode = binaryno[25:32]
    # print("opcode in the instruction ",opcode)
    R_oper = ["0110011"]
    I_oper = ["0010011", "0000011", "1100111"]
    S_oper = ["0100011"]
    SB_oper = ["1100011"]
    U_oper = ["0110111", "0010111"]
    UJ_oper = ["1101111"]

    #address_in_binary = bin(int(inputsArray[0][2:], 16))[2:].zfill(32)
    #address_in_decimal = int(address_in_binary, 2)

    #if PC == address_in_decimal:
    if opcode in R_oper:
        # decode

        R_Format(binaryno)
        PC += 4
    elif opcode in I_oper:
        # decode
        PC = I_Format(binaryno, PC)


    elif opcode in S_oper:
        S_Format(binaryno)
        PC += 4
        # decode

    elif opcode in SB_oper:
        # decode
        PC = sb_format(binaryno, PC)

    elif opcode in U_oper:
        # decode
        U_Format(binaryno, PC)
        PC += 4

    elif opcode in UJ_oper:
        # decode
        PC = UJ_Format(binaryno, PC)


    else:
        print("Error")
        PC += 4

print(memory)  # printing memory key is address and value is data


# function to convert any -ve number into 32 bit twos compliment binary number
def findTwoscomplement(str):  # Rajasekhar 2019CSB1105
    # note: argument for this function is 32bit binary str of positive number
    # to convert any integer into 32bit binary number. use '{:032b}'.format(n) where n is the number
    n = len(str)

    i = n - 1
    while (i >= 0):
        if (str[i] == '1'):
            break

        i -= 1

    if (i == -1):
        return '1' + str

    k = i - 1
    while (k >= 0):

        # Just flip the values
        if (str[k] == '1'):
            str = list(str)
            str[k] = '0'
            str = ''.join(str)
        else:
            str = list(str)
            str[k] = '1'
            str = ''.join(str)

        k -= 1

    return str
