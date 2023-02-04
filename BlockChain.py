from inspect import BlockFinder
from Structure import *
import datetime


class Blockchain:

    def create_genesis_block(self):
        return Structure(["Bob", "0957423478", "222/78", "45236578545878", 999.00, 80, "8/2566", "8/2566"], "0")

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def display_all_chain(self):
        for i, block in enumerate(self.chain):
            print("{")
            print(f"    Block : {i},")
            print(f"    Hash : {block.hash},")
            print(f"    Previous Hash : {block.previous_hash},")
            print(f"    TimeStamp : {block.TimeStamp},")
            print(f"    Property Owner : {block.datas[0]},")
            print(f"    Tel : {block.datas[1]},")
            print(f"    Address : {block.datas[2]},")
            print(f"    Title Deed : {block.datas[3]},")
            print(f"    Area : {block.datas[4]},")
            print(f"    Unit : {block.datas[5]},")
            print(f"    Permis de construire : {block.datas[6]},")
            print(f"    EIA : {block.datas[7]}")
            print("}")

    def display_chain(self, block_number):
        block = self.chain[block_number]
        print("{")
        print(f"    Block : {block_number},")
        print(f"    Hash : {block.hash},")
        print(f"    Previous Hash : {block.previous_hash},")
        print(f"    TimeStamp : {block.TimeStamp},")
        print(f"    Property Owner : {block.datas[0]},")
        print(f"    Tel : {block.datas[1]},")
        print(f"    Address : {block.datas[2]},")
        print(f"    Title Deed : {block.datas[3]},")
        print(f"    Area : {block.datas[4]},")
        print(f"    Unit : {block.datas[5]},")
        print(f"    Permis de construire : {block.datas[6]},")
        print(f"    EIA : {block.datas[7]}")
        print("}")

    def add_block(self, datas):
        previous_hash = self.chain[-1].hash
        new_block = Structure(datas, previous_hash)
        self.chain.append(new_block)

    def add_datas(self):
        datas = []
        print("*************************************************")

        Property_Owner = input("Property Owner : ")
        datas.append(Property_Owner)

        Tel = input("Tel : ")
        datas.append(Tel)

        Address = input("Address : ")
        datas.append(Address)

        Title_Deed = int(input("Title Deed : "))
        datas.append(Title_Deed)

        Area = float(input("Area (Square Metre) : "))
        datas.append(Area)

        Unit = int(input("Unit : "))
        datas.append(Unit)

        permis_de_construire = input("permis De Construire : ")
        datas.append(permis_de_construire)

        Eia = input("EIA : ")
        datas.append(Eia)

        print("*************************************************")
        self.add_block(datas)

    def edit_datas(self, block, New_Property_Owner, New_Tel, New_Address, New_Title_Deed, New_Area, New_Unit, New_permis_de_construire, New_Eia):
        block = self.chain[block]
        block.Time = datetime.datetime.now()
        block.datas[0] = New_Property_Owner
        block.datas[1] = New_Tel
        block.datas[2] = New_Address
        block.datas[3] = New_Title_Deed
        block.datas[4] = New_Area
        block.datas[5] = New_Unit
        block.datas[6] = New_permis_de_construire
        block.datas[7] = New_Eia
        block.hash = block.calculate_hash()

    def is_valid(self):
        for i in range(1, len(self.chain)):
            Current_block = self.chain[i]
            Previous_block = self.chain[i - 1]
            if Current_block.hash != Current_block.calculate_hash():
                blockchain = i-1
                bools = False
                return bools, blockchain
            if Current_block.previous_hash != Previous_block.hash:
                blockchain = i-1
                bools = False
                return bools, blockchain
        return True


blockchain = Blockchain()
