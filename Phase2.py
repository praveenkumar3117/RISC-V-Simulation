x = []  # Registers
x.append(0)
for i in range(1, 32):
    x.append(0)
    if (i == 3):
        x[i] = int("0x10000000", 16)  # gp
    elif (i == 2):
        x[i] = int("0x7FFFFFF0", 16)  # sp

memory = {}


class five_steps:
    def __init__(self):
        self.PC = 0x0
        # self.IR = 0
        self.PC_temp = self.PC
        self.clock = 0
        # self.Cycles = 0
        self.IF = ''
        self.ID = {}
        self.IE = {}
        self.IM = []
        self.data = []

        ############ DECODE   ###########
        self.operation = ''
        self.rs1 = ''
        self.rs2 = ''
        self.rd = ''
        self.imm = ''
        self.jot = 0
        ####### END     #########

        ############ MEMORY   ###########
        self.string = ''
        self.dataa = ''
        self.address = ''
        ####### END     #########

        # self.stall_one = False
        # self.stall_two = False
        self.total_cycles = 0

    def fetch(self, binaryCode):
        self.IF = binaryCode
        self.PC_temp = self.PC
        print("FETCH:Fetch instruction " + hex(int(self.IF, 2))[2:].zfill(8) + " from address " + hex(self.PC)[2:].zfill(8))
        self.PC += 4


    def decode(self, binaryInstruction):
        opcode = binaryInstruction[25:32]

        R_oper = ["0110011"]
        I_oper = ["0010011", "0000011", "1100111"]
        S_oper = ["0100011"]
        SB_oper = ["1100011"]
        U_oper = ["0110111", "0010111"]
        UJ_oper = ["1101111"]

        if opcode in R_oper:
            # decode

            funct7 = binaryInstruction[0:7]
            rs2 = binaryInstruction[7:12]
            rs1 = binaryInstruction[12:17]
            funct3 = binaryInstruction[17:20]
            rd = binaryInstruction[20:25]
            opcode = binaryInstruction[25:32]
            self.rs1 = rs1
            self.rs2 = rs2
            self.rd = rd
            self.imm = ''

            if (opcode == "0110011"):
                if (funct7 == "0000000"):
                    if (funct3 == "000"):

                        self.operation = "add"

                        # add
                        # execute("add", rs1, rs2, rd, " ", PC)  # " " is don't care for imm


                    elif (funct3 == "111"):

                        self.operation = "and"
                        # and
                        # execute("and", rs1, rs2, rd, " ", PC)

                    elif (funct3 == "110"):

                        self.operation = "or"
                        # or
                        # execute("or", rs1, rs2, rd, " ", PC)

                    elif (funct3 == "001"):

                        self.operation = "sll"
                        # sll
                        # execute("sll", rs1, rs2, rd, " ", PC)


                    elif (funct3 == "010"):

                        self.operation = "slt"
                        # slt
                        # execute("slt", rs1, rs2, rd, " ", PC)

                    elif (funct3 == "101"):

                        self.operation = "srl"
                        # srl
                        # execute("srl", rs1, rs2, rd, " ", PC)

                    elif (funct3 == "100"):

                        self.operation = "xor"
                        # xor
                        # execute("xor", rs1, rs2, rd, " ", PC)

                    else:
                        print("Error")
                elif (funct7 == "0100000"):
                    if (funct3 == "000"):

                        self.operation = "sub"
                        # sub
                        # execute("sub", rs1, rs2, rd, " ", PC)

                    elif (funct3 == "101"):

                        self.operation = "sra"
                        # sra
                        # execute("sra", rs1, rs2, rd, " ", PC)

                    else:
                        print("Error")
                elif (funct7 == "0000001"):
                    if (funct3 == "000"):

                        self.operation = "mul"
                        # mul
                        # execute("mul", rs1, rs2, rd, " ", PC)

                    elif (funct3 == "100"):
                        self.operation = "div"
                        # div
                        # execute("div", rs1, rs2, rd, " ", PC)

                    elif (funct3 == "110"):
                        self.operation = "rem"
                        # rem
                        # execute("rem", rs1, rs2, rd, " ", PC)

                    else:
                        print("Error")
                else:
                    print("Error")
            else:
                print("Error")
        elif opcode in I_oper:
            imm = binaryInstruction[0:12]
            rs1 = binaryInstruction[12:17]
            funct3 = binaryInstruction[17:20]
            rd = binaryInstruction[20:25]
            opcode = binaryInstruction[25:32]

            self.rs1 = rs1
            self.rs2 = ''
            self.rd = rd
            self.imm = imm

            # print("opcode: ", opcode, " imm: ", imm, " rs1: ", rs1, " funct3: ", funct3, " rd: ", rd)
            if (opcode == "0000011"):
                if (funct3 == "000"):
                    # lb

                    self.operation = "lb"
                    # execute("lb", rs1, " ", rd, imm, PC)
                    # PC += 4
                elif (funct3 == "001"):

                    self.operation = "lh"
                    # lh

                    # execute("lh", rs1, " ", rd, imm, PC)
                    # PC += 4
                elif (funct3 == "010"):

                    self.operation = "lw"
                    # lw

                    # execute("lw", rs1, " ", rd, imm, PC)
                    # PC += 4
                else:
                    print("Error")
                    # PC += 4
            elif (opcode == "0010011"):
                if (funct3 == "000"):

                    self.operation = "addi"
                    # addi
                    # execute("addi", rs1, " ", rd, imm, PC)

                    # PC += 4
                elif (funct3 == "111"):

                    self.operation = "andi"
                    # andi
                    # execute("andi", rs1, " ", rd, imm, PC)

                    # PC += 4
                elif (funct3 == "110"):
                    # ori
                    self.operation = "ori"
                    # execute("ori", rs1, " ", rd, imm, PC)

                else:
                    print("Error")
            elif (opcode == "1100111"):
                if (funct3 == "000"):

                    self.operation = "jalr"
                    # jalr
                    # PC = execute("jalr", rs1, " ", rd, imm, PC)

                else:
                    print("Error")
        elif opcode in S_oper:

            func3 = binaryInstruction[17:20]  # funct3
            rs1 = binaryInstruction[12:17]  # source register1
            rs2 = binaryInstruction[7:12]  # source register2
            imm = binaryInstruction[0:7] + binaryInstruction[20:25]  # offset added to base adress

            self.rs1 = rs1
            self.rs2 = rs2
            self.rd = ""
            self.imm = imm

            Sr1 = 0  # for decimal value of source register1
            Sr2 = 0  # for decimal value of source register2
            for i in range(0, 5):
                if (rs1[i] == '1'):
                    Sr1 = Sr1 + pow(2, 4 - i)
                if (rs2[i] == '1'):
                    Sr2 = Sr2 + pow(2, 4 - i)

            Offset = 0
            for i in range(0, 12):
                if (imm[i] == '1'):
                    Offset = Offset + pow(2, 11 - i)

            if (func3 == '000'):

                self.operation = "sb"
                # Execution of store_byte(sb)

                # execute("sb", rs1, rs2, " ", imm, PC)

            elif (func3 == '001'):

                self.operation = "sh"
                # Execution of store_halfword(sh)

                # execute("sh", rs1, rs2, " ", imm, PC)

            elif (func3 == '010'):

                self.operation = "sw"
                # Execution of store_word(sw)

                # execute("sw", rs1, rs2, " ", imm, PC)
            else:
                print("ERROR")
        elif opcode in SB_oper:
            funct3 = binaryInstruction[17:20]
            rs1 = binaryInstruction[12:17]
            rs2 = binaryInstruction[7:12]
            imm = binaryInstruction[0] + binaryInstruction[24] + binaryInstruction[1:7] + binaryInstruction[20:24]

            self.rs1 = rs1
            self.rs2 = rs2
            self.rd = ''
            self.imm = imm

            if funct3 == '000':

                self.operation = "beq"
                # pc = execute("beq", rs1, rs2, " ", imm, pc)
            elif funct3 == '001':

                self.operation = "bne"
                # pc = execute("bne", rs1, rs2, " ", imm, pc)
            elif funct3 == '101':

                self.operation = "bge"
                # pc = execute("bge", rs1, rs2, " ", imm, pc)
            elif funct3 == '100':

                self.operation = "blt"
                # pc = execute("blt", rs1, rs2, " ", imm, pc)
            else:
                print("Error")
        elif opcode in U_oper:
            # decode

            imm = binaryInstruction[0:20]
            rd = binaryInstruction[20:25]
            opcode = binaryInstruction[25:32]  # opcode is enough to distinguish u and uj format instructions

            self.rs1 = ''
            self.rs2 = ''
            self.rd = rd
            self.imm = imm

            if (opcode == "0010111"):
                # auipc
                self.operation = "auipc"
                # execute("auipc", " ", " ", rd, imm, PC)

            elif (opcode == "0110111"):
                # lui

                self.operation = "lui"
                # execute("lui", " ", " ", rd, imm, PC)
            else:
                print("Error")
        elif opcode in UJ_oper:
            opcode = binaryInstruction[25:32]
            imm = binaryInstruction[0] + binaryInstruction[12:20] + binaryInstruction[11] + binaryInstruction[1:11]
            rd = binaryInstruction[20:25]

            self.rs1 = ''
            self.rs2 = ''
            self.rd = rd
            self.imm = imm

            if (opcode == "1101111"):
                # jal

                self.operation = "jal"
                # pc = execute("jal", " ", " ", rd, imm, pc)

            else:
                print("Error")
        else:
            print("Error")

    def execute(self):
        # self.operation is referring to the the operation we are going to do

        if (self.operation == "add" or self.operation == "and" or self.operation == "or" or self.operation == "sll"):

            print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2), ",source register 2:",
                  int(self.rs2, 2),
                  ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
            self.executeMuskan(self.operation, self.rs1, self.rs2, self.rd)
        elif (self.operation == "xor" or self.operation == "mul" or self.operation == "div" or self.operation == "rem"):

            print("Decode-> operation:", self.operation, ",source register 1:", int(self.rs1, 2), ",source register 2:", int(self.rs2, 2),
                  ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
            self.executeManan(self.operation, self.rs1, self.rs2, self.rd)


        elif (self.operation == "slt" or self.operation == "srl" or self.operation == "sub" or self.operation == "sra"):

            print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2), ",source register 2:",
                  int(self.rs2, 2),
                  ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
            self.executeRajasekhar(self.operation, self.rs1, self.rs2, self.rd)

        elif (self.operation == "addi" or self.operation == "andi" or self.operation == "ori"):
            temp = self.imm
            if (temp[0:1] == '1'):
                check = str(temp)
                check = check[::-1]
                temp = self.findnegative(check)
            else:
                temp = int(temp, 2)
            print("Decode -> operation :", self.operation, ",source register 1:", int(self.rs1, 2), ",Immediate:", temp,
                  ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
            self.executePraveen(self.operation, self.rd, self.rs1, self.imm)


        elif (self.operation == "lui" or self.operation == "auipc"):

            temp = self.imm
            if (temp[0:1] == '1'):
                check = str(temp)
                check = check[::-1]
                temp = self.findnegative(check)
            else:
                temp = int(temp, 2)
            print("Decode -> operation :", self.operation, ",Immediate:", temp,
                  ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
            self.executePratima(self.operation, self.rd, self.imm, self.PC_temp)

        elif (self.operation == "bge" or self.operation == "blt"):

            temp = self.imm
            if (temp[0:1] == '1'):
                check = str(temp)
                check = check[::-1]
                temp = self.findnegative(check)
            else:
                temp = int(temp, 2)
            print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2), ",Source register 2:",
                  int(self.rs2, 2),
                  ",Immediate: ", temp, end=" \n", sep=" ")
            self.executeManan1(self.operation, self.rs1, self.rs2, self.imm, self.PC_temp)

        elif (self.operation == "beq" or self.operation == "bne"):

            temp = self.imm
            if (temp[0:1] == '1'):
                check = str(temp)
                check = check[::-1]
                temp = self.findnegative(check)
            else:
                temp = int(temp, 2)
            print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2), ",Source register 2:",
                  int(self.rs2, 2),
                  ",Immediate: ", temp, end=" \n", sep=" ")
            self.executeRajasekhar1(self.operation, self.rs1, self.rs2, self.imm, self.PC_temp)


        elif (self.operation == "jal"):

            temp = self.imm
            if (temp[0:1] == '1'):
                check = str(temp)
                check = check[::-1]
                temp = self.findnegative(check)
            else:
                temp = int(temp, 2)
            print("Decode:-> operation: ", self.operation, ",destinaton register:", int(self.rd, 2), ",Immediate: ",
                  temp, end=" \n",sep=" ")
            self.executePraveen1(self.operation, self.rd, self.imm, self.PC_temp)

        elif (self.operation == "jalr"):

            temp = self.imm
            if (temp[0:1] == '1'):
                check = str(temp)
                check = check[::-1]
                temp = self.findnegative(check)
            else:
                temp = int(temp, 2)
            print("Decode-> operation: ", self.operation, ",Source register 1:", int(self.rs1, 2), ",destinaton register:"
                  , int(self.rd, 2), ",Immediate: ", temp, end=" \n", sep=" ")
            self.executePraveen2(self.operation, self.rs1, self.rd, self.imm, self.PC_temp)
        elif (self.operation == "sw" or self.operation == "sh" or self.operation == "sb"):

            temp = self.imm
            if (temp[0:1] == '1'):
                check = str(temp)
                check = check[::-1]
                temp = self.findnegative(check)
            else:
                temp = int(temp, 2)
            print("Decode-> operation: ", self.operation, ",source register 1:", int(self.rs1, 2), ",Source register 2:",
                  int(self.rs2, 2),
                  ",Immediate: ", temp, end=" \n", sep=" ")
            self.executeStore(self.operation, self.rs1, self.rs2, self.imm)
        elif (self.operation == "lw" or self.operation == "lh" or self.operation == "lb"):

            temp = self.imm
            if (temp[0:1] == '1'):
                check = str(temp)
                check = check[::-1]
                temp = self.findnegative(check)
            else:
                temp = int(temp, 2)
            print("Decode-> operation: ", self.operation, ",Source register 1:", int(self.rs1, 2),
                  ",destinaton register:", int(self.rd, 2), ",Immediate: ", temp, end=" \n", sep=" ")
            self.executeRead(self.operation, self.rs1, self.rd, self.imm)

    def executeMuskan(self, string, rs1, rs2, rd):
        if (string == "add"):  # executing add
            rs1 = int(rs1, 2)
            rs2 = int(rs2, 2)
            rd = int(rd, 2)
            s = x[rs1] + x[rs2]
            print("Execute :", string, x[rs1], "and", x[rs2])
            print("MEMORY:No memory  operation")
            if (s >= -(pow(2, 31)) and s <= (pow(2, 31)) - 1):  # checking for underflow or overflow
                self.jot = s
                #WriteBack(rd, s)


        elif (string == "and"):  # executing and
            rs1 = int(rs1, 2)
            rs2 = int(rs2, 2)
            rd = int(rd, 2)
            s = x[rs1] & x[rs2]
            print("Execute :", string, x[rs1], "and", x[rs2])
            print("MEMORY:No memory  operation")
            if (s >= -(pow(2, 31)) and s <= (pow(2, 31)) - 1):  # checking for underflow or overflow
                self.jot = s
                #WriteBack(rd, s)


        elif (string == "or"):  # executing or
            rs1 = int(rs1, 2)
            rs2 = int(rs2, 2)
            rd = int(rd, 2)
            s = x[rs1] | x[rs2]
            print("Execute :", string, x[rs1], "and", x[rs2])
            print("MEMORY:No memory  operation")
            if (s >= -(pow(2, 31)) and s <= (pow(2, 31)) - 1):  # checking for underflow or overflow
                self.jot = s
                #WriteBack(rd, s)


        elif (string == "sll"):  # executing sll
            rs1 = int(rs1, 2)
            rs2 = int(rs2, 2)
            rd = int(rd, 2)
            s = x[rs1] << x[rs2]
            print("Execute :", string, x[rs1], "and", x[rs2])
            print("MEMORY:No memory  operation")
            if (s >= -(pow(2, 31)) and s <= (pow(2, 31)) - 1):  # checking for underflow or overflow
                self.jot = s
                #WriteBack(rd, s)

    def executeManan(self, string, rs1, rs2, rd):
        rd = int(rd, 2)
        rs1 = int(rs1, 2)
        rs2 = int(rs2, 2)
        if string == 'xor':
            output = x[rs1] ^ x[rs2]
            if -(pow(2, 31)) <= output <= (pow(2, 31)) - 1:  # Underflow and overflow
                print("Execute :", string, x[rs1], "and", x[rs2])
                print("MEMORY:No memory  operation")
                self.jot = output
                #WriteBack(rd, output)
        elif string == 'mul':
            output = x[rs1] * x[rs2]
            if -(pow(2, 31)) <= output <= (pow(2, 31)) - 1:  # Underflow and overflow
                print("Execute :", string, x[rs1], "and", x[rs2])
                print("MEMORY:No memory  operation")
                self.jot = output
                #WriteBack(rd, output)
        elif string == "div":
            output = x[rs1] // x[rs2]
            if -(pow(2, 31)) <= output <= (pow(2, 31)) - 1:  # Underflow and overflow
                print("Execute :", string, x[rs1], "and", x[rs2])
                print("MEMORY:No memory  operation")
                self.jot = output
                #WriteBack(rd, output)
        elif string == "rem":
            output = x[rs1] % x[rs2]
            if -(pow(2, 31)) <= output <= (pow(2, 31)) - 1:  # Underflow and overflow
                print("Execute :", string, x[rs1], "and", x[rs2])
                print("MEMORY:No memory  operation")
                self.jot = output
                #WriteBack(rd, output)

    def executePratima(self, string, rd, imm, PC):
        if (imm[0:1] == '1'):
            check = str(imm)
            check = check[::-1]
            imm = self.findnegative(check)
        else:
            imm = int(imm, 2)
        rd = int(rd, 2)

        if string == "lui":  # executing lui
            if (imm <= pow(2, 19) - 1 and imm >= -pow(2, 19)):  # checking range of imm
                temp = 0 | imm
                temp = temp << 12
                if (temp >= -(pow(2, 31)) and temp <= (pow(2, 31)) - 1):  # checking for underflow or overflow
                    print("Execute :", string, x[rd], "and", imm)
                    print("MEMORY:No memory  operation")
                    self.jot = temp
                    #WriteBack(rd, temp)
        elif string == "auipc":  # executing auipc
            if (imm <= pow(2, 19) - 1 and imm >= -pow(2, 19)):  # checking range of imm
                temp = 0 | imm
                temp = temp << 12
                temp = temp + PC
                if (temp >= -(pow(2, 31)) and temp <= (pow(2, 31)) - 1):  # checking for underflow or overflow
                    print("Execute :", string, x[rd], "and", imm)
                    print("MEMORY:No memory  operation")
                    self.jot = temp
                    #WriteBack(rd, temp)
        else:
            print("Error")

    def executeRajasekhar(self, string, rs1, rs2, rd):
        # slt,sra,srl,sub
        rd = int(rd, 2)
        rs1 = int(rs1, 2)
        rs2 = int(rs2, 2)

        if (string == "slt"):
            if (x[rs1] < x[rs2]):
                jot = 1
                print("Execute :", string, x[rs1], "and", x[rs2])
                print("MEMORY:No memory  operation")
                self.jot = jot
                #WriteBack(rd, jot)
            else:
                jot = 0
                print("Execute :", string, x[rs1], "and", x[rs2])
                print("MEMORY:No memory  operation")
                self.jot = jot
                #WriteBack(rd, jot)
        elif (string == "sra"):
            result = x[rs1] >> x[rs2]
            lowerlimit = -1 * (1 << 31)
            upperlimit = (1 << 31) - 1
            if (lowerlimit <= result and result <= upperlimit):  # checking underflow and overflow condition
                print("Execute :", string, x[rs1], "and", x[rs2])
                print("MEMORY:No memory  operation")
                self.jot = result
                #WriteBack(rd, result)
        elif (string == "srl"):
            result = x[rs1] >> x[rs2]
            lowerlimit = -1 * (1 << 31)
            upperlimit = (1 << 31) - 1
            if (lowerlimit <= result and result <= upperlimit):
                print("Execute :", string, x[rs1], "and", x[rs2])
                print("MEMORY:No memory  operation")
                self.jot = result
                #WriteBack(rd, result)
        elif (string == "sub"):
            result = x[rs1] - x[rs2]
            lowerlimit = -1 * (1 << 31)
            upperlimit = (1 << 31) - 1
            if (lowerlimit <= result and result <= upperlimit):
                print("Execute :", string, x[rs1], "and", x[rs2])
                print("MEMORY:No memory  operation")
                self.jot = result
                #WriteBack(rd, result)

    def executePraveen(self, string, rd, rs1, imm):  # PRAVEEN KUMAR 2019CSb1108      #addi,andi,ori
        rs1 = int(rs1, 2)
        rd = int(rd, 2)
        # print(imm)
        if (imm[0:1] == '1'):
            check = str(imm)
            check = check[::-1]
            imm = self.findnegative(check)
        else:
            imm = int(imm, 2)

        if (string == "addi"):
            if (imm <= pow(2, 11) - 1 and imm >= -pow(2, 11)):  # checking range of imm
                s = x[rs1] + imm
                if (s >= -(pow(2, 31)) and s <= (pow(2, 31)) - 1):  # checking for underflow or overflow
                    print("Execute :", string, x[rs1], "and", imm)
                    print("MEMORY:No memory  operation")
                    self.jot = s
                    #WriteBack(rd, s)

        elif (string == "andi"):
            if (imm <= pow(2, 11) - 1 and imm >= -pow(2, 11)):  # checking range of imm
                s = x[rs1] & imm
                if (s >= -(pow(2, 31)) and s <= (pow(2, 31)) - 1):  # checking for underflow or overflow
                    print("Execute :", string, x[rs1], "and", imm)
                    print("MEMORY:No memory  operation")
                    self.jot = s
                    #WriteBack(rd, s)

        elif (string == "ori"):

            if (imm <= pow(2, 11) - 1 and imm >= -pow(2, 11)):  # checking range of imm
                s = x[rs1] | imm
                if (s >= -(pow(2, 31)) and s <= (pow(2, 31)) - 1):  # checking for underflow or overflow
                    print("Execute :", string, x[rs1], "and", imm)
                    print("MEMORY:No memory  operation")
                    self.jot = s
                    #WriteBack(rd, s)

    def executeManan1(self, string, rs1, rs2, imm, pc):
        rs1 = int(rs1, 2)
        rs2 = int(rs2, 2)
        if (imm[0:1] == '1'):
            check = str(imm)
            check = check[::-1]
            imm = self.findnegative(check)
        else:
            imm = int(imm, 2)
        imm = imm << 1
        if string == "bge":
            if x[rs1] >= x[rs2]:
                print("Execute :", string, x[rs1], "and", x[rs2])
                print("MEMORY:No memory  operation")
                print("WRITEBACK: no writeback \n")
                pc = pc + imm
            else:
                print("Execute :No execute")
                print("MEMORY:No memory  operation")
                print("WRITEBACK: no writeback \n")
                pc = pc + 4
        elif string == 'blt':
            if x[rs1] < x[rs2]:
                print("Execute :", string, x[rs1], "and", x[rs2])
                print("MEMORY:No memory  operation")
                print("WRITEBACK: no writeback \n")
                pc = pc + imm
            else:
                print("Execute :No execute")
                print("MEMORY:No memory  operation")
                print("WRITEBACK: no writeback \n")
                pc = pc + 4

        self.PC = pc

    def executeRajasekhar1(self, string, rs1, rs2, imm, pc):
        rs1 = int(rs1, 2)
        rs2 = int(rs2, 2)
        if (imm[0:1] == '1'):
            check = str(imm)
            check = check[::-1]
            imm = self.findnegative(check)
        else:
            imm = int(imm, 2)
        imm = imm << 1
        if (string == 'beq'):
            if (x[rs1] == x[rs2]):
                print("Execute :", string, x[rs1], "and", x[rs2])
                print("MEMORY:No memory  operation")
                print("WRITEBACK: no writeback \n")
                pc = pc + imm
            else:
                print("Execute :No execute")
                print("MEMORY:No memory  operation")
                print("WRITEBACK: no writeback \n")
                pc = pc + 4
        elif (string == 'bne'):
            if (x[rs1] != x[rs2]):
                print("Execute :", string, x[rs1], "and", x[rs2])
                print("MEMORY:No memory  operation")
                print("WRITEBACK: no writeback \n")
                pc = pc + imm
            else:
                print("Execute :No execute")
                print("MEMORY:No memory  operation")
                print("WRITEBACK: no writeback \n")
                pc = pc + 4

        self.PC = pc

    def executePraveen1(self, string, rd, imm, pc):  # Praveen Kumar 2019CSB1108    jal  function
        rd = int(rd, 2)

        if (imm[0:1] == '1'):
            check = str(imm)

            check = check[::-1]
            imm = self.findnegative(check)

        else:
            imm = int(imm, 2)

        imm = imm << 1

        if (string == 'jal'):
            temp = pc
            pc = pc + imm

            jot = temp + 4
            print("Execute :", string, x[rd], "and", imm)
            print("MEMORY:No memory  operation")
            if rd != 0:
                self.jot = jot
                #WriteBack(rd, jot)
            else:
                print("WRITEBACK: no writeback \n")

        self.PC = pc

    def executePraveen2(self, string, rs1, rd, imm, pc):  # Praveen Kumar 2019CSB1108    jalr function
        rs1 = int(rs1, 2)
        rd = int(rd, 2)
        if (imm[0:1] == '1'):
            check = str(imm)
            check = check[::-1]
            imm = self.findnegative(check)
        else:
            imm = int(imm, 2)
        if (string == 'jalr'):
            temp = pc
            pc = x[rs1] + imm
            print("Execute :", string, x[rs1], "and", imm)
            print("MEMORY:No memory  operation")
            if (rd != 0):
                jot = temp + 4
                self.jot = jot
                #WriteBack(rd, jot)
            else:
                print("WRITEBACK: no writeback \n")

        self.PC = pc

    def executeStore(self, string, rs1, rs2, imm):
        rs1 = int(rs1, 2)
        rs2 = int(rs2, 2)
        if (imm[0:1] == '1'):
            check = str(imm)
            check = check[::-1]
            imm = self.findnegative(check)
        else:
            imm = int(imm, 2)
        dataa = hex(x[rs2])[2:].zfill(8)
        self.dataa = dataa
        if (string == "sw"):
            if (x[rs1] + imm >= 268435456):  # data segment starts with address 268435456 or 0x10000000
                address = x[rs1] + imm  # calculating address
                print("Execute : calculating effective address by adding", x[rs1], "and", imm)
                self.string = "sw"
                self.address = address
                #self.MemoryStore("sw", dataa, address)
        elif (string == "sh"):
            if (x[rs1] + imm >= 268435456):
                address = x[rs1] + imm
                print("Execute : calculating effective address by adding", x[rs1], "and", imm)
                self.string = "sh"
                self.address = address
                #self.MemoryStore("sh", dataa, address)
        elif (string == "sb"):
            if (x[rs1] + imm >= 268435456):
                address = x[rs1] + imm
                print("Execute : calculating effective address by adding", x[rs1], "and", imm)
                self.string = "sb"
                self.address = address
                #self.MemoryStore("sb", dataa, address)

    def MemoryStore(self, string, dataa, address):
        print("Memory: accessed memory location at", address)
        if (string == "sw"):
            memory[address] = dataa[6:]
            memory[address + 1] = dataa[4:6]
            memory[address + 2] = dataa[2:4]
            memory[address + 3] = dataa[0:2]
        elif (string == "sh"):
            memory[address] = dataa[6:]
            memory[address + 1] = dataa[4:6]
        elif (string == "sb"):
            memory[address] = dataa[6:]
        print("WRITEBACK: no writeback \n")

    def executeRead(self, string, rs1, rd, imm):
        rs1 = int(rs1, 2)
        rd = int(rd, 2)

        check = imm
        if (imm[0:1] == '1'):  # imm is a negative number, since sign bit is 1
            check = str(check)
            check = check[::-1]  # reversing the string

            t1 = self.findnegative(check)

            imm = t1
        else:
            imm = int(imm, 2)  # sign bit is 0

        temp1 = x[rs1] + imm  # calculating address
        self.address=temp1
        print("Execute : calculating effective address by adding", x[rs1], "and", imm)
        self.imm=imm
        #self.Memoryread(self, string, temp1, rd, imm)

    def Memoryread(self, string, temp1, rd, imm):  # Pratima Singh 2018CEB1021
        #print("imm=",imm)
        if (imm <= pow(2, 11) - 1 and imm >= -pow(2, 11)):  # checking range of imm
            if (string == "lw"):
                if (temp1 >= 268435456):  # data segment starts with address 268435456 or 0x10000000
                    if temp1 in memory:
                        print("Memory: accessed memory location at", temp1)
                        temp2 = memory[temp1 + 3] + memory[temp1 + 2] + memory[temp1 + 1] + memory[temp1]

                        jot = int(temp2, 16)
                        self.jot = jot
                        #WriteBack(rd, jot)
                    else:
                        memory[temp1] = "00"
                        memory[temp1 + 1] = "00"
                        memory[temp1 + 2] = "00"
                        memory[temp1 + 3] = "00"
                        self.Memoryread(string, temp1, rd, imm)
                else:
                    print("\n Invalid offset")
                    print(temp1)
            elif string == "lh":
                if temp1 >= 268435456:  # data segment starts with address 268435456 or 0x10000000
                    if temp1 in memory:
                        print("Memory: accessed memory location at", temp1)
                        temp2 = memory[temp1 + 3] + memory[temp1 + 2]
                        jot = int(temp2, 16)
                        self.jot = jot
                        #WriteBack(rd, jot)
                    else:
                        memory[temp1] = "00"
                        memory[temp1 + 1] = "00"
                        memory[temp1 + 2] = "00"
                        memory[temp1 + 3] = "00"
                        self.Memoryread(string, temp1, rd, imm)
                else:
                    print("\n Invalid offset")
                    print(temp1)
            elif string == "lb":
                if temp1 >= 268435456:  # data segment starts with address 268435456 or 0x10000000
                    if temp1 in memory:
                        print("Memory: accessed memory location at", temp1)
                        temp2 = memory[temp1 + 3]
                        jot = int(temp2, 16)
                        self.jot = jot
                        #WriteBack(rd, jot)
                    else:
                        memory[temp1] = "00"
                        memory[temp1 + 1] = "00"
                        memory[temp1 + 2] = "00"
                        memory[temp1 + 3] = "00"
                        self.Memoryread(string, temp1, rd, imm)
                else:
                    print("\n Invalid offset")
                    print(temp1)
            else:
                print("\nError")
    def Memory(self,string,dataa,rd,imm,address):
        if(string=="lb" or string=="lw" or string=="lh"):
            self.Memoryread(string, address, rd, imm)
        elif(string=="sb" or string=="sw" or string=="sh"):
            self.MemoryStore(string, dataa, address)

    def WriteBack(self, rd, content):
        if(len(rd)==0):
            return
        rd=int(rd,2)
        if rd != 0:
            x[rd] = content
            print("WRITEBACK: write", content, " to x[", rd, "]")
        print("\n")

    def findnegative(self, string):  # Pratima_Singh 2018CEB1021 function to get the sign extended value of a negative imm field
        length = len(string)
        neg = -1  # intialize neg with -1
        sum = 0
        i = 0  # counter
        while i <= length - 1:
            if (string[i] == '0'):
                sum += -pow(2, i)
            i = i + 1
        neg = neg + sum
        return neg


file = open('machinecd.mc', 'r')
datasegOrnot = 0
Instruct = {}
memory = {}
for line in file:
    if (line == "\n"):
        datasegOrnot = 1
        continue
    if (datasegOrnot == 1):  # fetching memory from data segment
        dataArray = line.split(' ')
        daata = dataArray[1][2:4]
        memory[int(dataArray[0], 16)] = daata
        continue
file.close()

last_PC = 0
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


nonp=five_steps()
nonp.PC=0
while (nonp.PC <= last_PC):
    nonp.fetch(Instruct[nonp.PC])
    nonp.decode(nonp.IF)
    nonp.execute()
    nonp.Memory(nonp.operation, nonp.dataa, nonp.rd, nonp.imm, nonp.address)
    nonp.WriteBack(nonp.rd,nonp.jot)
print(x)
print(memory)