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
        self.cycle = 0
        self.IF = ''
        # self.ID = {}
        # self.IE = {}
        # self.IM = []
        # self.data = []

        ############ DECODE   ###########
        self.operation = ''
        self.rs1 = ''
        self.rs2 = ''
        # self.rs1a = []
        # self.rs2a = []
        # self.rs1b = []
        # self.rs2b = ''
        self.rd = ''
        self.rd_array1 = []
        self.rd_array2 = []
        self.imm = ''
        self.jot = 0
        ####### END     #########
        # self.jot1=0
        # self.jot2=0
        # self.rd1=0
        # self.rd2=0
        # self.jt=[]
        # self.rdd=[]
        ############ MEMORY   ###########   pipelining.operation1, pipelining.dataa1, pipelining.rd1, pipelining.imm1, pipelining.address1
        self.string = ''
        self.dataa = ''
        self.address = -1

        self.operation1 = ''
        self.dataa1 = ''
        self.rd1 = ''
        self.imm1 = ''
        self.address1 = -1
        ####### END     #########writeback  pipelining.rd1, pipelining.jot1
        self.rd2 = ''
        self.jot2 = 0
        # self.stall_one = False
        # self.stall_two = False
        self.total_cycles = 0

        #####  Previous called memory   #####
        self.previous_memory_operation = ''
        self.previous_memory_dataa = ''
        self.previous_memory_rd = ''
        self.previous_memory_imm = ''
        self.previous_memory_address = -1

        #####  Previous called writeback   #####
        self.previous_writeback_rd = ''
        self.previous_writeback_content = 0

    def fetch(self, binaryCode):
        self.IF = binaryCode
        self.PC_temp = self.PC
        print(
            "FETCH:Fetch instruction " + hex(int(self.IF, 2))[2:].zfill(8) + " from address " + hex(self.PC)[2:].zfill(
                8))
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
                        print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                              ",source register 2:", int(self.rs2, 2), ",destination register:", int(self.rd, 2),
                              end=" \n", sep=" ")
                        # add
                        # execute("add", rs1, rs2, rd, " ", PC)  # " " is don't care for imm


                    elif (funct3 == "111"):

                        self.operation = "and"
                        print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                              ",source register 2:",
                              int(self.rs2, 2),
                              ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
                        # and
                        # execute("and", rs1, rs2, rd, " ", PC)

                    elif (funct3 == "110"):

                        self.operation = "or"
                        print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                              ",source register 2:",
                              int(self.rs2, 2),
                              ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
                        # or
                        # execute("or", rs1, rs2, rd, " ", PC)

                    elif (funct3 == "001"):

                        self.operation = "sll"
                        print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                              ",source register 2:",
                              int(self.rs2, 2),
                              ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
                        # sll
                        # execute("sll", rs1, rs2, rd, " ", PC)


                    elif (funct3 == "010"):

                        self.operation = "slt"
                        print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                              ",source register 2:",
                              int(self.rs2, 2),
                              ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
                        # slt
                        # execute("slt", rs1, rs2, rd, " ", PC)

                    elif (funct3 == "101"):

                        self.operation = "srl"
                        print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                              ",source register 2:",
                              int(self.rs2, 2),
                              ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
                        # srl
                        # execute("srl", rs1, rs2, rd, " ", PC)

                    elif (funct3 == "100"):

                        self.operation = "xor"
                        print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                              ",source register 2:",
                              int(self.rs2, 2),
                              ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
                        # xor
                        # execute("xor", rs1, rs2, rd, " ", PC)

                    else:
                        print("Error")
                elif (funct7 == "0100000"):
                    if (funct3 == "000"):

                        self.operation = "sub"
                        print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                              ",source register 2:",
                              int(self.rs2, 2),
                              ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
                        # sub
                        # execute("sub", rs1, rs2, rd, " ", PC)

                    elif (funct3 == "101"):

                        self.operation = "sra"
                        print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                              ",source register 2:",
                              int(self.rs2, 2),
                              ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
                        # sra
                        # execute("sra", rs1, rs2, rd, " ", PC)

                    else:
                        print("Error")
                elif (funct7 == "0000001"):
                    if (funct3 == "000"):

                        self.operation = "mul"
                        print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                              ",source register 2:",
                              int(self.rs2, 2),
                              ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
                        # mul
                        # execute("mul", rs1, rs2, rd, " ", PC)

                    elif (funct3 == "100"):
                        self.operation = "div"
                        print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                              ",source register 2:",
                              int(self.rs2, 2),
                              ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
                        # div
                        # execute("div", rs1, rs2, rd, " ", PC)

                    elif (funct3 == "110"):
                        self.operation = "rem"
                        print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                              ",source register 2:",
                              int(self.rs2, 2),
                              ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
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
                    print("Decode -> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                          ",Immediate:", imm,
                          ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
                    # execute("lb", rs1, " ", rd, imm, PC)
                    # PC += 4
                elif (funct3 == "001"):

                    self.operation = "lh"
                    print("Decode -> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                          ",Immediate:", imm,
                          ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
                    # lh

                    # execute("lh", rs1, " ", rd, imm, PC)
                    # PC += 4
                elif (funct3 == "010"):

                    self.operation = "lw"
                    print("Decode -> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                          ",Immediate:", imm,
                          ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
                    # lw

                    # execute("lw", rs1, " ", rd, imm, PC)
                    # PC += 4
                else:
                    print("Error")
                    # PC += 4
            elif (opcode == "0010011"):
                if (funct3 == "000"):

                    self.operation = "addi"
                    print("Decode -> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                          ",Immediate:", imm,
                          ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
                    # addi
                    # execute("addi", rs1, " ", rd, imm, PC)

                    # PC += 4
                elif (funct3 == "111"):

                    self.operation = "andi"
                    print("Decode -> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                          ",Immediate:", imm,
                          ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
                    # andi
                    # execute("andi", rs1, " ", rd, imm, PC)

                    # PC += 4
                elif (funct3 == "110"):
                    # ori
                    self.operation = "ori"
                    print("Decode -> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                          ",Immediate:", imm,
                          ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
                    # execute("ori", rs1, " ", rd, imm, PC)

                else:
                    print("Error")
            elif (opcode == "1100111"):
                if (funct3 == "000"):

                    self.operation = "jalr"
                    print("Decode -> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                          ",Immediate:", imm,
                          ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
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
                print("Decode-> operation: ", self.operation, ",source register 1:", int(self.rs1, 2),
                      ",Source register 2:",
                      int(self.rs2, 2),
                      ",Immediate: ", imm, end=" \n", sep=" ")
                # Execution of store_byte(sb)

                # execute("sb", rs1, rs2, " ", imm, PC)

            elif (func3 == '001'):

                self.operation = "sh"
                print("Decode-> operation: ", self.operation, ",source register 1:", int(self.rs1, 2),
                      ",Source register 2:",
                      int(self.rs2, 2),
                      ",Immediate: ", imm, end=" \n", sep=" ")
                # Execution of store_halfword(sh)

                # execute("sh", rs1, rs2, " ", imm, PC)

            elif (func3 == '010'):

                self.operation = "sw"
                print("Decode-> operation: ", self.operation, ",source register 1:", int(self.rs1, 2),
                      ",Source register 2:",
                      int(self.rs2, 2),
                      ",Immediate: ", imm, end=" \n", sep=" ")
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
                print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                      ",Source register 2:",
                      int(self.rs2, 2),
                      ",Immediate: ", imm, end=" \n", sep=" ")
                # pc = execute("beq", rs1, rs2, " ", imm, pc)
            elif funct3 == '001':

                self.operation = "bne"
                print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                      ",Source register 2:",
                      int(self.rs2, 2),
                      ",Immediate: ", imm, end=" \n", sep=" ")
                # pc = execute("bne", rs1, rs2, " ", imm, pc)
            elif funct3 == '101':

                self.operation = "bge"
                print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                      ",Source register 2:",
                      int(self.rs2, 2),
                      ",Immediate: ", imm, end=" \n", sep=" ")
                # pc = execute("bge", rs1, rs2, " ", imm, pc)
            elif funct3 == '100':

                self.operation = "blt"
                print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                      ",Source register 2:",
                      int(self.rs2, 2),
                      ",Immediate: ", imm, end=" \n", sep=" ")
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
                print("Decode -> operation :", self.operation, ",Immediate:", imm,
                      ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
                # execute("auipc", " ", " ", rd, imm, PC)

            elif (opcode == "0110111"):
                # lui

                self.operation = "lui"
                print("Decode -> operation :", self.operation, ",Immediate:", imm,
                      ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
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
                print("Decode:-> operation: ", self.operation, ",destinaton register:", int(self.rd, 2), ",Immediate: ",
                      imm, end=" \n", sep=" ")
                # pc = execute("jal", " ", " ", rd, imm, pc)

            else:
                print("Error")
        else:
            print("Error")

    def execute(self):
        # self.operation is referring to the the operation we are going to do

        if (self.operation == "add" or self.operation == "and" or self.operation == "or" or self.operation == "sll"):

            # print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
            # ",source register 2:",
            # int(self.rs2, 2),
            # ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")
            self.executeMuskan(self.operation, self.rs1, self.rs2, self.rd)
        elif (self.operation == "xor" or self.operation == "mul" or self.operation == "div" or self.operation == "rem"):

            self.executeManan(self.operation, self.rs1, self.rs2, self.rd)


        elif (self.operation == "slt" or self.operation == "srl" or self.operation == "sub" or self.operation == "sra"):

            '''print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                  ",source register 2:",
                  int(self.rs2, 2),
                  ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")'''
            self.executeRajasekhar(self.operation, self.rs1, self.rs2, self.rd)

        elif (self.operation == "addi" or self.operation == "andi" or self.operation == "ori"):
            temp = self.imm
            if (temp[0:1] == '1'):
                check = str(temp)
                check = check[::-1]
                temp = self.findnegative(check)
            else:
                temp = int(temp, 2)
            '''print("Decode -> operation :", self.operation, ",source register 1:", int(self.rs1, 2), ",Immediate:", temp,
                  ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")'''
            self.executePraveen(self.operation, self.rd, self.rs1, self.imm)


        elif (self.operation == "lui" or self.operation == "auipc"):

            temp = self.imm
            if (temp[0:1] == '1'):
                check = str(temp)
                check = check[::-1]
                temp = self.findnegative(check)
            else:
                temp = int(temp, 2)
            '''print("Decode -> operation :", self.operation, ",Immediate:", temp,
                  ",destination register : ", int(self.rd, 2), end=" \n", sep=" ")'''
            self.executePratima(self.operation, self.rd, self.imm, self.PC_temp)

        elif (self.operation == "bge" or self.operation == "blt"):

            temp = self.imm
            if (temp[0:1] == '1'):
                check = str(temp)
                check = check[::-1]
                temp = self.findnegative(check)
            else:
                temp = int(temp, 2)
            '''print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                  ",Source register 2:",
                  int(self.rs2, 2),
                  ",Immediate: ", temp, end=" \n", sep=" ")'''
            self.executeManan1(self.operation, self.rs1, self.rs2, self.imm, self.PC_temp)

        elif (self.operation == "beq" or self.operation == "bne"):

            temp = self.imm
            if (temp[0:1] == '1'):
                check = str(temp)
                check = check[::-1]
                temp = self.findnegative(check)
            else:
                temp = int(temp, 2)
            '''print("Decode-> operation :", self.operation, ",source register 1:", int(self.rs1, 2),
                  ",Source register 2:",
                  int(self.rs2, 2),
                  ",Immediate: ", temp, end=" \n", sep=" ")'''
            self.executeRajasekhar1(self.operation, self.rs1, self.rs2, self.imm, self.PC_temp)


        elif (self.operation == "jal"):

            temp = self.imm
            if (temp[0:1] == '1'):
                check = str(temp)
                check = check[::-1]
                temp = self.findnegative(check)
            else:
                temp = int(temp, 2)
            '''print("Decode:-> operation: ", self.operation, ",destinaton register:", int(self.rd, 2), ",Immediate: ",
                  temp, end=" \n", sep=" ")'''
            self.executePraveen1(self.operation, self.rd, self.imm, self.PC_temp)

        elif (self.operation == "jalr"):

            temp = self.imm
            if (temp[0:1] == '1'):
                check = str(temp)
                check = check[::-1]
                temp = self.findnegative(check)
            else:
                temp = int(temp, 2)
            '''print("Decode-> operation: ", self.operation, ",Source register 1:", int(self.rs1, 2),
                  ",destinaton register:"
                  , int(self.rd, 2), ",Immediate: ", temp, end=" \n", sep=" ")'''
            self.executePraveen2(self.operation, self.rs1, self.rd, self.imm, self.PC_temp)
        elif (self.operation == "sw" or self.operation == "sh" or self.operation == "sb"):

            temp = self.imm
            if (temp[0:1] == '1'):
                check = str(temp)
                check = check[::-1]
                temp = self.findnegative(check)
            else:
                temp = int(temp, 2)
            '''print("Decode-> operation: ", self.operation, ",source register 1:", int(self.rs1, 2),
                  ",Source register 2:",
                  int(self.rs2, 2),
                  ",Immediate: ", temp, end=" \n", sep=" ")'''
            # print("executed store\n")
            self.executeStore(self.operation, self.rs1, self.rs2, self.imm)
        elif (self.operation == "lw" or self.operation == "lh" or self.operation == "lb"):

            temp = self.imm
            if (temp[0:1] == '1'):
                check = str(temp)
                check = check[::-1]
                temp = self.findnegative(check)
            else:
                temp = int(temp, 2)
            '''print("Decode-> operation: ", self.operation, ",Source register 1:", int(self.rs1, 2),
                  ",destinaton register:", int(self.rd, 2), ",Immediate: ", temp, end=" \n", sep=" ")'''
            self.executeRead(self.operation, self.rs1, self.rd, self.imm)
        # pipelining.operation1, pipelining.dataa1, pipelining.rd1, pipelining.imm1, pipelining.address1
        self.operation1 = self.operation
        self.dataa1 = self.dataa
        self.rd1 = self.rd
        self.imm1 = self.imm
        self.address1 = self.address

    def executeMuskan(self, string, rs1, rs2, rd):
        if (string == "add"):  # executing add
            rs1 = int(rs1, 2)
            rs2 = int(rs2, 2)
            rd = int(rd, 2)
            s = x[rs1] + x[rs2]
            print("Execute :", string, x[rs1], "and", x[rs2])
            # print("MEMORY:No memory  operation")
            if (s >= -(pow(2, 31)) and s <= (pow(2, 31)) - 1):  # checking for underflow or overflow
                self.jot = s
                # WriteBack(rd, s)


        elif (string == "and"):  # executing and
            rs1 = int(rs1, 2)
            rs2 = int(rs2, 2)
            rd = int(rd, 2)
            s = x[rs1] & x[rs2]
            print("Execute :", string, x[rs1], "and", x[rs2])
            # print("MEMORY:No memory  operation")
            if (s >= -(pow(2, 31)) and s <= (pow(2, 31)) - 1):  # checking for underflow or overflow
                self.jot = s
                # WriteBack(rd, s)


        elif (string == "or"):  # executing or
            rs1 = int(rs1, 2)
            rs2 = int(rs2, 2)
            rd = int(rd, 2)
            s = x[rs1] | x[rs2]
            print("Execute :", string, x[rs1], "and", x[rs2])
            # print("MEMORY:No memory  operation")
            if (s >= -(pow(2, 31)) and s <= (pow(2, 31)) - 1):  # checking for underflow or overflow
                self.jot = s
                # WriteBack(rd, s)


        elif (string == "sll"):  # executing sll
            rs1 = int(rs1, 2)
            rs2 = int(rs2, 2)
            rd = int(rd, 2)
            s = x[rs1] << x[rs2]
            print("Execute :", string, x[rs1], "and", x[rs2])
            # print("MEMORY:No memory  operation")
            if (s >= -(pow(2, 31)) and s <= (pow(2, 31)) - 1):  # checking for underflow or overflow
                self.jot = s
                # WriteBack(rd, s)

    def executeManan(self, string, rs1, rs2, rd):
        rd = int(rd, 2)
        rs1 = int(rs1, 2)
        rs2 = int(rs2, 2)
        if string == 'xor':
            output = x[rs1] ^ x[rs2]
            if -(pow(2, 31)) <= output <= (pow(2, 31)) - 1:  # Underflow and overflow
                print("Execute :", string, x[rs1], "and", x[rs2])
                # print("MEMORY:No memory  operation")
                self.jot = output
                # WriteBack(rd, output)
        elif string == 'mul':
            output = x[rs1] * x[rs2]
            if -(pow(2, 31)) <= output <= (pow(2, 31)) - 1:  # Underflow and overflow
                print("Execute :", string, x[rs1], "and", x[rs2])
                # print("MEMORY:No memory  operation")
                self.jot = output
                # WriteBack(rd, output)
        elif string == "div":
            output = x[rs1] // x[rs2]
            if -(pow(2, 31)) <= output <= (pow(2, 31)) - 1:  # Underflow and overflow
                print("Execute :", string, x[rs1], "and", x[rs2])
                # print("MEMORY:No memory  operation")
                self.jot = output
                # WriteBack(rd, output)
        elif string == "rem":
            output = x[rs1] % x[rs2]
            if -(pow(2, 31)) <= output <= (pow(2, 31)) - 1:  # Underflow and overflow
                print("Execute :", string, x[rs1], "and", x[rs2])
                # print("MEMORY:No memory  operation")
                self.jot = output
                # WriteBack(rd, output)

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
                    # print("MEMORY:No memory  operation")
                    self.jot = temp
                    # WriteBack(rd, temp)
        elif string == "auipc":  # executing auipc
            if (imm <= pow(2, 19) - 1 and imm >= -pow(2, 19)):  # checking range of imm
                temp = 0 | imm
                temp = temp << 12
                temp = temp + PC
                if (temp >= -(pow(2, 31)) and temp <= (pow(2, 31)) - 1):  # checking for underflow or overflow
                    print("Execute :", string, x[rd], "and", imm)
                    # print("MEMORY:No memory  operation")
                    self.jot = temp
                    # WriteBack(rd, temp)
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
                # print("MEMORY:No memory  operation")
                self.jot = jot
                # WriteBack(rd, jot)
            else:
                jot = 0
                print("Execute :", string, x[rs1], "and", x[rs2])
                # print("MEMORY:No memory  operation")
                self.jot = jot
                # WriteBack(rd, jot)
        elif (string == "sra"):
            result = x[rs1] >> x[rs2]
            lowerlimit = -1 * (1 << 31)
            upperlimit = (1 << 31) - 1
            if (lowerlimit <= result and result <= upperlimit):  # checking underflow and overflow condition
                print("Execute :", string, x[rs1], "and", x[rs2])
                # print("MEMORY:No memory  operation")
                self.jot = result
                # WriteBack(rd, result)
        elif (string == "srl"):
            result = x[rs1] >> x[rs2]
            lowerlimit = -1 * (1 << 31)
            upperlimit = (1 << 31) - 1
            if (lowerlimit <= result and result <= upperlimit):
                print("Execute :", string, x[rs1], "and", x[rs2])
                # print("MEMORY:No memory  operation")
                self.jot = result
                # WriteBack(rd, result)
        elif (string == "sub"):
            result = x[rs1] - x[rs2]
            lowerlimit = -1 * (1 << 31)
            upperlimit = (1 << 31) - 1
            if (lowerlimit <= result and result <= upperlimit):
                print("Execute :", string, x[rs1], "and", x[rs2])
                # print("MEMORY:No memory  operation")
                self.jot = result
                # WriteBack(rd, result)

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
                    # print("MEMORY:No memory  operation")

                    self.jot = s
                    # WriteBack(rd, s)

        elif (string == "andi"):
            if (imm <= pow(2, 11) - 1 and imm >= -pow(2, 11)):  # checking range of imm
                s = x[rs1] & imm
                if (s >= -(pow(2, 31)) and s <= (pow(2, 31)) - 1):  # checking for underflow or overflow
                    print("Execute :", string, x[rs1], "and", imm)
                    # print("MEMORY:No memory  operation")
                    self.jot = s
                    # WriteBack(rd, s)

        elif (string == "ori"):

            if (imm <= pow(2, 11) - 1 and imm >= -pow(2, 11)):  # checking range of imm
                s = x[rs1] | imm
                if (s >= -(pow(2, 31)) and s <= (pow(2, 31)) - 1):  # checking for underflow or overflow
                    print("Execute :", string, x[rs1], "and", imm)
                    # print("MEMORY:No memory  operation")
                    self.jot = s
                    # WriteBack(rd, s)

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
                # print("MEMORY:No memory  operation")
                # print("WRITEBACK: no writeback \n")
                pc = pc + imm
            else:
                print("Execute :No execute")
                # print("MEMORY:No memory  operation")
                # print("WRITEBACK: no writeback \n")
                pc = pc + 4
        elif string == 'blt':
            if x[rs1] < x[rs2]:
                print("Execute :", string, x[rs1], "and", x[rs2])
                # print("MEMORY:No memory  operation")
                # print("WRITEBACK: no writeback \n")
                pc = pc + imm
            else:
                print("Execute :No execute")
                # print("MEMORY:No memory  operation")
                # print("WRITEBACK: no writeback \n")
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
                # print("MEMORY:No memory  operation")
                # print("WRITEBACK: no writeback \n")
                pc = pc + imm
            else:
                print("Execute :No execute")
                # print("MEMORY:No memory  operation")
                # print("WRITEBACK: no writeback \n")
                pc = pc + 4
        elif (string == 'bne'):
            if (x[rs1] != x[rs2]):
                print("Execute :", string, x[rs1], "and", x[rs2])
                # print("MEMORY:No memory  operation")
                # print("WRITEBACK: no writeback \n")
                pc = pc + imm
            else:
                print("Execute :No execute")
                # print("MEMORY:No memory  operation")
                # print("WRITEBACK: no writeback \n")
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
            # print("MEMORY:No memory  operation")
            if rd != 0:
                self.jot = jot
                # WriteBack(rd, jot)
            # else:
            # print("WRITEBACK: no writeback \n")

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
            # print("MEMORY:No memory  operation")
            if (rd != 0):
                jot = temp + 4
                self.jot = jot
                # WriteBack(rd, jot)
            # else:
            # print("WRITEBACK: no writeback \n")

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
        print("dataa: ", dataa)
        print("rs1 ", rs1)
        print("imm ", imm)

        self.dataa = dataa
        if (string == "sw"):
            if (x[rs1] + imm >= 268435456):  # data segment starts with address 268435456 or 0x10000000
                adds = x[rs1] + imm  # calculating address
                print("Execute : calculating effective address by adding", x[rs1], "and", imm)
                self.string = "sw"
                self.address = adds
                # self.MemoryStore("sw", dataa, address)
        elif (string == "sh"):
            if (x[rs1] + imm >= 268435456):
                adds = x[rs1] + imm
                print("Execute : calculating effective address by adding", x[rs1], "and", imm)
                self.string = "sh"
                self.address = adds
                # self.MemoryStore("sh", dataa, address)
        elif (string == "sb"):
            if (x[rs1] + imm >= 268435456):
                adds = x[rs1] + imm
                print("Execute : calculating effective address by adding", x[rs1], "and", imm)
                self.string = "sb"
                self.address = adds
                # self.MemoryStore("sb", dataa, address)

    def MemoryStore(self, string, dataa, address):
        print("Memory: accessed memory location at", address)
        if (string == "sw"):
            print("datak: ", dataa)
            memory[address] = dataa[6:]
            memory[address + 1] = dataa[4:6]
            memory[address + 2] = dataa[2:4]
            memory[address + 3] = dataa[0:2]
        elif (string == "sh"):
            memory[address] = dataa[6:]
            memory[address + 1] = dataa[4:6]
        elif (string == "sb"):
            memory[address] = dataa[6:]
        #print("WRITEBACK: no writeback \n")

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
        self.address = temp1
        print("Execute : calculating effective address by adding", x[rs1], "and", imm)
        self.imm = imm
        # self.Memoryread(self, string, temp1, rd, imm)

    def Memoryread(self, string, temp1, rd, imm):  # Pratima Singh 2018CEB1021
        # print("imm=",imm)
        if (imm <= pow(2, 11) - 1 and imm >= -pow(2, 11)):  # checking range of imm
            if (string == "lw"):
                if (temp1 >= 268435456):  # data segment starts with address 268435456 or 0x10000000
                    if temp1 in memory:
                        print("Memory: accessed memory location at", temp1)
                        temp2 = memory[temp1 + 3] + memory[temp1 + 2] + memory[temp1 + 1] + memory[temp1]

                        jot = int(temp2, 16)
                        self.jot = jot
                        # WriteBack(rd, jot)
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
                        # WriteBack(rd, jot)
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
                        # WriteBack(rd, jot)
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

    def Memory(self, string, dataa, rd, imm, address):
        if (string == "lb" or string == "lw" or string == "lh"):
            self.Memoryread(string, address, rd, imm)
        elif (string == "sb" or string == "sw" or string == "sh"):
            self.MemoryStore(string, dataa, address)
        # writeback  pipelining.rd1, pipelining.jot1
        else:
            print("NO memory operation")
        self.rd2 = rd
        self.jot2 = self.jot

    def WriteBack(self, rd, content):
        print(content, rd)
        if (len(rd) == 0):
            print("WRITEBACK: no writeback \n")
            return
        rd = int(rd, 2)
        if rd != 0:
            x[rd] = content
            print("WRITEBACK: write", content, " to x[", rd, "]")
        print("\n")

    def findnegative(self,
                     string):  # Pratima_Singh 2018CEB1021 function to get the sign extended value of a negative imm field
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

    def save_last_called_memory(self):
        self.previous_memory_operation = self.operation1
        self.previous_memory_rd = self.rd1
        self.previous_memory_imm = self.imm1
        self.previous_memory_dataa = self.dataa1
        self.previous_memory_address = self.address1

    def check_already_called_memory(self):
        if (self.previous_memory_operation == self.operation1 and self.previous_memory_rd == self.rd1 and
                self.previous_memory_imm == self.imm1 and self.previous_memory_dataa == self.dataa1 and
                self.previous_memory_address == self.address1):
            return 1
        else:
            return 0

    def save_last_called_writeback(self):
        self.previous_writeback_rd = self.rd2
        self.previous_writeback_content = self.jot2

    def check_already_called_writeback(self):
        if (self.previous_writeback_rd == self.rd2 and self.previous_writeback_content == self.jot2):
            return 1
        else:
            return 0

    def clear_already_called_writeback(self):
        self.previous_writeback_rd = ''
        self.previous_writeback_content = 0


file = open('machinecd_stalling_case4.mc', 'r')
datasegOrnot = 0
Instruct = {}
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
file = open('machinecd_stalling_case4.mc', 'r')
for line in file:
    if (line == "\n"):
        break
    inputsArray = line.split(' ')
    tempc = int(inputsArray[0][2:], 16)
    binaryno = bin(int(inputsArray[1][2:], 16))[2:].zfill(32)
    Instruct[tempc] = binaryno
    last_PC = tempc
file.close()

knob1 = int(input("Enter the value of Knob1(0/1): 0 for choosing non-pipelining and 1 for choosing pipelining\n"))
if (knob1 == 1):
    knob2 = int(
        input("Enter the value of Knob2(0/1):0 if pipeline is expected to work with stalling and 1 for vice-versa\n"))
knob3 = int(input(
    "Enter the value of Knob3(0/1): 0 for not printing and 1 for printing values in register file at the end of each cycle \n"))
knob4 = int(input(
    "Enter the value of Knob4(0/1): 0 for not printing and 1 for printing the information in the pipeline registers at the end of each cycle (similar to tracing), along with cycle number.\n"))
knob5 = int(input(""))
'''
This knob is like enabling Knob4 for a specific instruction. With this feature we will
be able to see the pipeline registers information for a particular instruction of our
interest. Here, the instruction can be specified as number (example, if the instruction
we are interestd in is the 10th instruction in the input program, 10 will be taken as
input).

'''

nDataTransfer = 0
nALU = 0
nCtrlInstr = 0
clock = 0

if (knob1 == 0):
    non_pipelining = five_steps()
    non_pipelining.PC = 0
    while (non_pipelining.PC <= last_PC):
        non_pipelining.fetch(Instruct[non_pipelining.PC])
        non_pipelining.decode(non_pipelining.IF)
        if (non_pipelining.operation == "lb" or non_pipelining.operation == "lh" or non_pipelining.operation == "lw" or non_pipelining.operation == "sb" or non_pipelining.operation == "sh" or non_pipelining.operation == "sw"):
            nDataTransfer += 1
        elif (non_pipelining.operation == "beq" or non_pipelining.operation == "bge" or non_pipelining.operation == "bne" or non_pipelining.operation == "blt" or non_pipelining.operation == "jal" or non_pipelining.operation == "jalr"):
            nCtrlInstr += 1
        else:
            nALU += 1
        non_pipelining.execute()
        non_pipelining.Memory(non_pipelining.operation, non_pipelining.dataa, non_pipelining.rd, non_pipelining.imm,
                              non_pipelining.address)
        non_pipelining.WriteBack(non_pipelining.rd, non_pipelining.jot)
        if (knob3 == 1):
            for i in range(32):
                print("x[", i, "]=", x[i], end=" ,")
        clock += 1

    print("\n")
    print(x)
    print(memory)
elif (knob1 == 1):
    if (knob2 == 0):
        pipelining = five_steps()
        pipelining.PC = 0
        while (pipelining.PC <= last_PC + 16):
            if (pipelining.cycle == 0):
                pipelining.fetch(Instruct[pipelining.PC])
                pipelining.cycle += 1
            elif (pipelining.cycle == 1):
                pipelining.decode(pipelining.IF)
                pipelining.rd_array1.append(pipelining.rd)
                pipelining.fetch(Instruct[pipelining.PC])
                pipelining.cycle += 1
            elif (pipelining.cycle == 2):
                pipelining.execute()
                pipelining.decode(pipelining.IF)
                pipelining.rd_array1.append(pipelining.rd)
                pipelining.fetch(Instruct[pipelining.PC])
                pipelining.cycle += 1
            elif (pipelining.cycle == 3):
                pipelining.save_last_called_memory()
                pipelining.Memory(pipelining.operation1, pipelining.dataa1, pipelining.rd1, pipelining.imm1,
                                  pipelining.address1)
                if (pipelining.rd_array1[0] == pipelining.rs1 or pipelining.rd_array1[0] == pipelining.rs2):
                    print("Stalling at cycle:", pipelining.cycle)
                    pipelining.rd_array2.append(
                        pipelining.rd_array1[0])  # contains rd of instruction2 and array_2 with instruction1
                    pipelining.rd_array1.pop(0)  # No use of rd of instruction1
                    pipelining.cycle += 1
                else:
                    pipelining.execute()
                    pipelining.decode(pipelining.IF)
                    pipelining.rd_array1.append(pipelining.rd)  # contains rd of instruction2 and instruction3
                    pipelining.rd_array1.pop(0)  # No use of rd of instruction1
                    pipelining.fetch(Instruct[pipelining.PC])
                    pipelining.cycle += 1
            elif (pipelining.cycle >= 4):

                if (len(pipelining.rd_array2) == 2):
                    pipelining.rd_array2.pop(0)
                if (len(pipelining.rd_array1) == 3):
                    pipelining.rd_array2.append(pipelining.rd_array1[0])
                    pipelining.rd_array1.pop(0)
                if (len(pipelining.rd_array2) == 2):
                    pipelining.rd_array2.pop(0)

                if (pipelining.PC == last_PC + 16):
                    pipelining.PC += 4
                if (pipelining.check_already_called_writeback() == 0):
                    pipelining.save_last_called_writeback()
                    pipelining.WriteBack(pipelining.rd2, pipelining.jot2)
                else:
                    print("Writeback Already Called")
                if (pipelining.PC <= last_PC + 12):
                    if (pipelining.check_already_called_memory() == 0):
                        pipelining.save_last_called_memory()
                        pipelining.clear_already_called_writeback()

                        pipelining.Memory(pipelining.operation1, pipelining.dataa1, pipelining.rd1, pipelining.imm1,
                                          pipelining.address1)
                    if (pipelining.PC == last_PC + 12):
                        pipelining.PC += 4

                if (len(pipelining.rd_array2) == 0):
                    if (len(pipelining.rd_array1) == 1 or len(pipelining.rd_array1) == 0):
                        if (len(pipelining.rd_array1) == 2):
                            pipelining.rd_array2.append(pipelining.rd_array1[0])
                            if (len(pipelining.rd_array2) == 2):
                                pipelining.rd_array2.pop(0)
                            pipelining.rd_array1.pop(0)
                        if (len(pipelining.rd_array2) == 2):
                            pipelining.rd_array2.pop(0)

                        if (pipelining.PC <= last_PC + 8):
                            pipelining.execute()
                            if (pipelining.PC == last_PC + 8):
                                pipelining.PC += 4

                        if (pipelining.PC <= last_PC + 4):
                            pipelining.decode(pipelining.IF)
                            pipelining.rd_array1.append(pipelining.rd)
                            if (pipelining.PC == last_PC + 4):
                                pipelining.PC += 4

                        if (pipelining.PC <= last_PC):
                            pipelining.fetch(Instruct[pipelining.PC])

                        pipelining.cycle += 1
                        '''if (pipelining.rd_array1[0] == pipelining.rs1 or pipelining.rd_array1[0] == pipelining.rs2):
                            print("Stalling>4 1.0.0000000 at cycle:", pipelining.cycle, pipelining.rd_array1, pipelining.rd_array2)
                            pipelining.rd_array2.append(pipelining.rd_array1[0])
                            if (len(pipelining.rd_array2) == 2):
                                pipelining.rd_array2.pop(0)
                            pipelining.rd_array1.pop(0)
                            pipelining.cycle += 1
                        else:
                            if (len(pipelining.rd_array1) == 2):
                                pipelining.rd_array2.append(pipelining.rd_array1[0])
                                if (len(pipelining.rd_array2) == 2):
                                    pipelining.rd_array2.pop(0)
                                pipelining.rd_array1.pop(0)
                            if (len(pipelining.rd_array2) == 2):
                                pipelining.rd_array2.pop(0)

                            if (pipelining.PC <= last_PC + 8):
                                pipelining.execute()
                                if (pipelining.PC == last_PC + 8):
                                    pipelining.PC += 4

                            if (pipelining.PC <= last_PC + 4):
                                pipelining.decode(pipelining.IF)
                                pipelining.rd_array1.append(pipelining.rd)
                                if (pipelining.PC == last_PC + 4):
                                    pipelining.PC += 4

                            if (pipelining.PC <= last_PC):
                                pipelining.fetch(Instruct[pipelining.PC])

                            pipelining.cycle += 1'''
                    else:
                        if (pipelining.rd_array1[0] == pipelining.rs1 or pipelining.rd_array1[0] == pipelining.rs2):
                            print("Stalling>4 1.0.0000000 at cycle:", pipelining.cycle, pipelining.rd_array1, pipelining.rd_array2)
                            pipelining.rd_array2.append(pipelining.rd_array1[0])
                            if (len(pipelining.rd_array2) == 2):
                                pipelining.rd_array2.pop(0)
                            pipelining.rd_array1.pop(0)
                            pipelining.cycle += 1
                        else:
                            if (len(pipelining.rd_array1) == 2):
                                pipelining.rd_array2.append(pipelining.rd_array1[0])
                                if (len(pipelining.rd_array2) == 2):
                                    pipelining.rd_array2.pop(0)
                                pipelining.rd_array1.pop(0)
                            if (len(pipelining.rd_array2) == 2):
                                pipelining.rd_array2.pop(0)

                            if (pipelining.PC <= last_PC + 8):
                                pipelining.execute()
                                if (pipelining.PC == last_PC + 8):
                                    pipelining.PC += 4

                            if (pipelining.PC <= last_PC + 4):
                                pipelining.decode(pipelining.IF)
                                pipelining.rd_array1.append(pipelining.rd)
                                if (pipelining.PC == last_PC + 4):
                                    pipelining.PC += 4

                            if (pipelining.PC <= last_PC):
                                pipelining.fetch(Instruct[pipelining.PC])

                            pipelining.cycle += 1
                    '''else:
                        if (len(pipelining.rd_array1) == 2):
                            pipelining.rd_array2.append(pipelining.rd_array1[0])
                            if (len(pipelining.rd_array2) == 2):
                                pipelining.rd_array2.pop(0)
                            pipelining.rd_array1.pop(0)
                        if (len(pipelining.rd_array2) == 2):
                            pipelining.rd_array2.pop(0)

                        if (pipelining.PC <= last_PC + 8):
                            pipelining.execute()
                            if (pipelining.PC == last_PC + 8):
                                pipelining.PC += 4

                        if (pipelining.PC <= last_PC + 4):
                            pipelining.decode(pipelining.IF)
                            pipelining.rd_array1.append(pipelining.rd)
                            if (pipelining.PC == last_PC + 4):
                                pipelining.PC += 4

                        if (pipelining.PC <= last_PC):
                            pipelining.fetch(Instruct[pipelining.PC])

                        pipelining.cycle += 1'''
                elif (len(pipelining.rd_array2) == 1):
                    if (len(pipelining.rd_array1) == 3 or len(pipelining.rd_array1) == 2):
                        if (pipelining.rd_array1[0] == pipelining.rs1 or pipelining.rd_array1[0] == pipelining.rs2):
                            print("Stalling>4 1.0 at cycle:", pipelining.cycle, pipelining.rs1, pipelining.rs2, pipelining.rd_array1, pipelining.rd_array2)
                            pipelining.rd_array2.append(pipelining.rd_array1[0])
                            if (len(pipelining.rd_array2) == 2):
                                pipelining.rd_array2.pop(0)
                            pipelining.rd_array1.pop(0)
                            pipelining.cycle += 1
                        elif (pipelining.rd_array2[0] == pipelining.rs1 or pipelining.rd_array2[0] == pipelining.rs2):
                            print("Stalling>4 2.0.1.1.0", pipelining.rs1, pipelining.rs2, pipelining.rd_array2, pipelining.rd_array1)
                            pipelining.rd_array2.pop(0)
                            pipelining.cycle += 1
                        else:
                            if (len(pipelining.rd_array1) == 2):
                                pipelining.rd_array2.append(pipelining.rd_array1[0])
                                if (len(pipelining.rd_array2) == 2):
                                    pipelining.rd_array2.pop(0)
                                pipelining.rd_array1.pop(0)
                            if (len(pipelining.rd_array2) == 2):
                                pipelining.rd_array2.pop(0)

                            if (pipelining.PC <= last_PC + 8):
                                pipelining.execute()
                                if (pipelining.PC == last_PC + 8):
                                    pipelining.PC += 4

                            if (pipelining.PC <= last_PC + 4):
                                pipelining.decode(pipelining.IF)
                                pipelining.rd_array1.append(pipelining.rd)
                                if (pipelining.PC == last_PC + 4):
                                    pipelining.PC += 4

                            if (pipelining.PC <= last_PC):
                                pipelining.fetch(Instruct[pipelining.PC])

                            pipelining.cycle += 1
                    else:
                        if (pipelining.rd_array2[0] == pipelining.rs1 or pipelining.rd_array2[0] == pipelining.rs2):
                            print("Stalling>4 2.0.1.2", pipelining.rs1, pipelining.rs2, pipelining.rd_array1[0], pipelining.rd_array2[0])
                            pipelining.rd_array2.pop(0)
                            pipelining.cycle += 1
                        else:
                            if (len(pipelining.rd_array1) == 2):
                                pipelining.rd_array2.append(pipelining.rd_array1[0])
                                if (len(pipelining.rd_array2) == 2):
                                    pipelining.rd_array2.pop(0)
                                pipelining.rd_array1.pop(0)

                            if (len(pipelining.rd_array2) == 2):
                                pipelining.rd_array2.pop(0)

                            if (pipelining.PC <= last_PC + 8):
                                pipelining.execute()
                                if (pipelining.PC == last_PC + 8):
                                    pipelining.PC += 4

                            if (pipelining.PC <= last_PC + 4):
                                pipelining.decode(pipelining.IF)
                                pipelining.rd_array1.append(pipelining.rd)
                                if (pipelining.PC == last_PC + 4):
                                    pipelining.PC += 4

                            if (pipelining.PC <= last_PC):
                                pipelining.fetch(Instruct[pipelining.PC])

                            pipelining.cycle += 1
                    '''else:
                        if (len(pipelining.rd_array1) == 2):
                            pipelining.rd_array2.append(pipelining.rd_array1[0])
                            if (len(pipelining.rd_array2) == 2):
                                pipelining.rd_array2.pop(0)
                            pipelining.rd_array1.pop(0)
                        if (len(pipelining.rd_array2) == 2):
                            pipelining.rd_array2.pop(0)

                        if (pipelining.PC <= last_PC + 8):
                            pipelining.execute()
                            if (pipelining.PC == last_PC + 8):
                                pipelining.PC += 4

                        if (pipelining.PC <= last_PC + 4):
                            pipelining.decode(pipelining.IF)
                            pipelining.rd_array1.append(pipelining.rd)
                            if (pipelining.PC == last_PC + 4):
                                pipelining.PC += 4

                        if (pipelining.PC <= last_PC):
                            pipelining.fetch(Instruct[pipelining.PC])

                        pipelining.cycle += 1'''
                '''else:
                    if (len(pipelining.rd_array1) == 1 or len(pipelining.rd_array1) == 2):
                        if (pipelining.rd_array1[0] == pipelining.rs1 or pipelining.rd_array1[0] == pipelining.rs2):
                            print("Stalling>4 1.0.1")
                            pipelining.rd_array2.append(pipelining.rd_array1[0])
                            if (len(pipelining.rd_array2) == 2):
                                pipelining.rd_array2.pop(0)
                            pipelining.rd_array1.pop(0)
                            pipelining.cycle += 2
                        elif (pipelining.rd_array2[0] == pipelining.rs1 or pipelining.rd_array2[0] == pipelining.rs2):
                            print("Stalling>4 2.0.1.1.1:", pipelining.rd_array2, pipelining.rd_array1)
                            pipelining.rd_array2.pop(0)
                            pipelining.cycle += 1
                        else:
                            if (len(pipelining.rd_array1) == 2):
                                pipelining.rd_array2.append(pipelining.rd_array1[0])
                                if (len(pipelining.rd_array2) == 2):
                                    pipelining.rd_array2.pop(0)
                                pipelining.rd_array1.pop(0)

                            if (len(pipelining.rd_array2) == 2):
                                pipelining.rd_array2.pop(0)

                            if (pipelining.PC <= last_PC + 8):
                                pipelining.execute()
                                if (pipelining.PC == last_PC + 8):
                                    pipelining.PC += 4

                            if (pipelining.PC <= last_PC + 4):
                                pipelining.decode(pipelining.IF)
                                pipelining.rd_array1.append(pipelining.rd)
                                if (pipelining.PC == last_PC + 4):
                                    pipelining.PC += 4

                            if (pipelining.PC <= last_PC):
                                pipelining.fetch(Instruct[pipelining.PC])

                            pipelining.cycle += 1
                    else:
                        if (pipelining.rd_array2[0] == pipelining.rs1 or pipelining.rd_array2[0] == pipelining.rs2):
                            print("Stalling>4 2.0.1.2")
                            pipelining.rd_array2.pop(0)
                            pipelining.cycle += 1
                        else:
                            if (len(pipelining.rd_array1) == 2):
                                pipelining.rd_array2.append(pipelining.rd_array1[0])
                                if (len(pipelining.rd_array2) == 2):
                                    pipelining.rd_array2.pop(0)
                                pipelining.rd_array1.pop(0)

                            if (len(pipelining.rd_array2) == 2):
                                pipelining.rd_array2.pop(0)

                            if (pipelining.PC <= last_PC + 8):
                                pipelining.execute()
                                if (pipelining.PC == last_PC + 8):
                                    pipelining.PC += 4

                            if (pipelining.PC <= last_PC + 4):
                                pipelining.decode(pipelining.IF)
                                pipelining.rd_array1.append(pipelining.rd)
                                if (pipelining.PC == last_PC + 4):
                                    pipelining.PC += 4

                            if (pipelining.PC <= last_PC):
                                pipelining.fetch(Instruct[pipelining.PC])

                            pipelining.cycle += 1'''

                '''pipelining.execute()
                pipelining.decode(pipelining.IF)
                pipelining.fetch(Instruct[pipelining.PC])
                pipelining.cycle += 1'''
            print("cycle no. ", pipelining.cycle)
            # for i in range(0, 32):
            #    print("x[", i, "]=", x[i])

    '''pipelining.WriteBack(pipelining.rd2, pipelining.jot2)
    pipelining.Memory(pipelining.operation1, pipelining.dataa1, pipelining.rd1, pipelining.imm1, pipelining.address1)
    if (pipelining.rd_array1[0] == pipelining.rs1 or pipelining.rd_array1[0] == pipelining.rs2):

        #print("Stalling1.0")

        pipelining.cycle += 2

        pipelining.WriteBack(pipelining.rd2, pipelining.jot2)
        pipelining.execute()
        pipelining.decode(pipelining.IF)
        pipelining.rs1a.append(pipelining.rs1)
        pipelining.rs2a.append(pipelining.rs2)
        pipelining.Memory(pipelining.operation1, pipelining.dataa1, pipelining.rd1, pipelining.imm1, pipelining.address1)
        if (pipelining.rd1 == pipelining.rs1a[1] or pipelining.rd1 == pipelining.rs2a[1] or pipelining.rd1 == pipelining.rs1a[2]
                or pipelining.rd1 == pipelining.rs2a[2]):
            print("Stalling1.0.1")
            pipelining.cycle += 2
            pipelining.execute()
            pipelining.WriteBack(pipelining.rd2, pipelining.jot2)
            pipelining.Memory(pipelining.operation1, pipelining.dataa1, pipelining.rd1, pipelining.imm1, pipelining.address1)
            pipelining.WriteBack(pipelining.rd2, pipelining.jot2)
        else:
            pipelining.execute()
            pipelining.WriteBack(pipelining.rd2, pipelining.jot2)
            pipelining.Memory(pipelining.operation1, pipelining.dataa1, pipelining.rd1, pipelining.imm1, pipelining.address1)
            pipelining.WriteBack(pipelining.rd2, pipelining.jot2)
            pipelining.cycle += 1

        pipelining.cycle += 1
    else:
        pipelining.execute()
        pipelining.decode(pipelining.IF)
        pipelining.rs1a.append(pipelining.rs1)
        pipelining.rs2a.append(pipelining.rs2)
        pipelining.cycle += 1
        pipelining.WriteBack(pipelining.rd2, pipelining.jot2)
        pipelining.Memory(pipelining.operation1, pipelining.dataa1, pipelining.rd1, pipelining.imm1, pipelining.address1)
        if (pipelining.rd1 == pipelining.rs1a[1] or pipelining.rd1 == pipelining.rs2a[1] or pipelining.rd1 == pipelining.rs1a[2]
                or pipelining.rd1 == pipelining.rs2a[2]):
            print("Stalling1.2.1")
            pipelining.cycle += 2
            pipelining.execute()
            pipelining.WriteBack(pipelining.rd2, pipelining.jot2)
            pipelining.Memory(pipelining.operation1, pipelining.dataa1, pipelining.rd1, pipelining.imm1, pipelining.address1)
            pipelining.WriteBack(pipelining.rd2, pipelining.jot2)
        else:
            pipelining.execute()
            pipelining.WriteBack(pipelining.rd2, pipelining.jot2)
            pipelining.Memory(pipelining.operation1, pipelining.dataa1, pipelining.rd1, pipelining.imm1, pipelining.address1)
            pipelining.WriteBack(pipelining.rd2, pipelining.jot2)
            pipelining.cycle += 1'''

    for i in range(0, 32):
        print("x[", i, "]=", x[i])
    print("cycle no. ", pipelining.cycle)

    print(memory)

