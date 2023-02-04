from Structure import *
from BlockChain import *

while True:

    print("***************** Functions *********************")
    print("1 : Show Data All Block In Chain")
    print("2 : Show Data In Each Block")
    print("3 : Add Block")
    print("4 : Edit Block")
    print("5 : Validate Block Chain")
    print("6 : Exit Program")
    print("*************************************************")

    Functions = int(input("Please Choose Number Of Functions : "))

    if Functions == 1:
        blockchain.display_all_chain()

    elif Functions == 2:
        block_number = int(input("Please Choose Number Of Block : "))
        blockchain.display_chain(block_number)
        print("")

    elif Functions == 3:
        blockchain.add_datas()

    elif Functions == 4:
        block = int(input("Edit Block : "))
        New_Property_Owner = input("Property Owner : ")
        New_Tel = input("Tel : ")
        New_Address = input("Address : ")
        New_Title_Deed = int(input("Title Deed : "))
        New_Area = float(input("Area (Square Metre) : "))
        New_Unit = int(input("Unit : "))
        New_permis_de_construire = input("permis De Construire : ")
        New_Eia = input("EIA : ")
        print("*************************************************")
        blockchain.edit_datas(block, New_Property_Owner, New_Tel, New_Address,
                              New_Title_Deed, New_Area, New_Unit, New_permis_de_construire, New_Eia)

    elif Functions == 5:
        bools, blockchain = blockchain.is_valid()

        if bools == True:
            print("*************************************************")
            print("")
            print("No Data Change")
            print("")
            print("*************************************************")
        else:
            print("*************************************************")
            print("")
            print("Data Has Changed")
            print("Block : ", blockchain)
            print("")
            print("*************************************************")

    elif Functions == 6:
        break

    else:
        print("Please Choose Number Of Functions : ")
