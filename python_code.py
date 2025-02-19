import mysql.connector as sql

conn = sql.connect(
    host="localhost", user="root", passwd="root", database="shoe_billing"
)

#if conn.is_connected():
#    print("connected sucessfully")

conn.autocommit = True
c1 = conn.cursor()
sql = """CREATE TABLE IF NOT EXISTS shoe_details(
   shoe_code CHAR(5) PRIMARY KEY ,
   brand_name CHAR(20),
   customer_name VARCHAR(25),
   customer_number CHAR(10),
   customer_address VARCHAR(50),
   amount INT)"""
c1.execute(sql)
user = input("enter user: ")
passwd = input("enter password: ")
if user == "SUBU" and passwd == "mou":
    print(
        """
░██████╗██╗░░██╗░█████╗░███████╗  ██████╗░██╗██╗░░░░░██╗░░░░░██╗███╗░░██╗░██████╗░
██╔════╝██║░░██║██╔══██╗██╔════╝  ██╔══██╗██║██║░░░░░██║░░░░░██║████╗░██║██╔════╝░
╚█████╗░███████║██║░░██║█████╗░░  ██████╦╝██║██║░░░░░██║░░░░░██║██╔██╗██║██║░░██╗░
░╚═══██╗██╔══██║██║░░██║██╔══╝░░  ██╔══██╗██║██║░░░░░██║░░░░░██║██║╚████║██║░░╚██╗
██████╔╝██║░░██║╚█████╔╝███████╗  ██████╦╝██║███████╗███████╗██║██║░╚███║╚██████╔╝
╚═════╝░╚═╝░░╚═╝░╚════╝░╚══════╝  ╚═════╝░╚═╝╚══════╝╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░"""
    )
    print(
        "\n\n}------------------------------[+] ᴄᴏᴅᴇ ʙʏ sᴜʙʜᴀᴍ [+]------------------------------{"
    )
    print(
        "}----------------------[+] ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ sʜᴏᴇ ʙɪʟʟɪɴᴅ sʏsᴛᴇᴍ [+]----------------------{"
    )
    print("\nSelect operation.")
    print(" [1] ENTER CUSTOMER DETAILS")
    print(" [2] SHOW CUSTOMERS DETAILS")
    print(" [3] SHOW BILL OF CUSTOMER")
    print("                            ")

    while True:
        choice = input("Enter choice(1/2/3): ")
        print(
            "===================================================================================="
        )
        if choice in ("1", "2", "3", "4", "5", "6"):

            if choice == "1":
                print("\nENTER CUSTOMER DETAILS")
                code = input(" ᴇɴᴛᴇʀ ᴄᴏᴅᴇ: ")
                brand = input(" ᴇɴᴛᴇʀ sʜᴏᴇs ʙʀᴀɴᴅ: ")
                name = input(" ᴇɴᴛᴇʀ ᴄᴜsᴛᴏᴍᴇʀ ɴᴀᴍᴇ: ")
                number = input(" ᴇɴᴛᴇʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ: ")
                details = input(" ᴇɴᴛᴇʀ ᴀᴅʀᴇss: ")
                amount = input(" ᴀᴍᴏᴜɴᴛ: ")

                st = "insert into shoe_details values('{}','{}','{}','{}','{}','{}')".format(
                    code, brand, name, number, details, amount
                )
                c1.execute(st)
                print("\n**CUSTOMER DETAILS INPUTED SUCCESSFULLY**\n")

                # choice=int(input("Enter choice(1/2): "))
                conn.commit()

            elif choice == "2":
                print("SHOW CUSTOMERS DETAILS")
                print("<1> SEARCH BY CUSTOMERS CODE: ")
                print("<2> SEARCH BY CUSTOMERS NAME: ")

                v_choice0 = input("Enter choice(1/2): ")
                if choice in ("1", "2"):

                    if v_choice0 == "1":
                        v_cn = input("Enter Customer Code: ")
                        c1.execute(
                            "select * from shoe_details where shoe_code =" + v_cn
                        )
                        data = c1.fetchall()

                    if v_choice0 == "2":
                        v_cn = str(input("Enter Customer Name: "))
                        print(v_cn)
                        c1.execute(
                            "select * from shoe_details where customer_name ="
                            + '"'
                            + v_cn
                            + '"'
                        )
                        data = c1.fetchall()

                print("\nDETAILS OF CUSTOMER", v_cn)
                print(" sʜᴏᴇs ᴄᴏᴅᴇ............:", data[0][0])
                print(" ʙʀᴀɴᴅ ɴᴀᴍᴇ............:", data[0][1])
                print(" ᴄᴜsᴛᴏᴍᴇʀ ɴᴀᴍᴇ.........:", data[0][2])
                print(" ᴄᴜsᴛᴏᴍᴇʀ ɴᴜᴍʙᴇʀ.......:", data[0][3])
                print(" ᴄᴜsᴛᴏᴍᴇʀ ᴅᴇᴛᴀɪʟ.......:", data[0][4])
                print(" ᴀᴍᴏᴜᴍᴛ................:", data[0][5])
                print("\n")

            elif choice == "3":
                print("\nBILLING PROCESS...")
                v_cn = input("Enter Customer Code: ")
                c1.execute("select * from shoe_details where shoe_code =" + v_cn)
                data = c1.fetchall()

                # for date :
                c1.execute("select now()")

                dt = c1.fetchall()
                a = str(dt)
                l1 = a.split()

                print("dt")

                code = data[0][0]
                number = data[0][3]
                name = data[0][1]

                # cost :
                discount = int(input("Discount on that SHOES: "))
                Total_Bill = ((data[0][5]) / 12) + (data[0][5])
                discountAmount = ((Total_Bill) * discount) / 100
                Total = Total_Bill - discountAmount
                total = round(Total, 2)
                totalstr = str(total)

                discount = str(discount)
                PRISE = str(data[0][5])
                GST_12 = (data[0][5]) / 12
                gst = round(GST_12, 2)
                gstr = str(gst)

                # lenth of data :
                len1 = len(data[0][1])
                len2 = 16 - len(data[0][1])
                len3 = 17 - len(PRISE)
                gap = 44 - (len1 + len2 + len3 + len(PRISE) + 1)

                print("+-------------------------------------------------+")
                print("|          +--------------------------+           |")
                print("|          | WELCOME TO SHOES BILLING |           |")
                print("|          +--------------------------+           |")
                print("|          		   		          |")                      
                print("| "+l1[0][20:24]+'-'+ l1[1][0:2]+'-'+ l1[2][0:2]+"                                      |")
                print("| "+l1[3][0:2]+':'+ l1[4][0:2]+':'+ l1[5][0:2]+"                                        |")
                print("| BHUBANESWAR-751021                              |")
                print("|                                                 |")
                print("| Bill Number : ",code," "*((48-(len(code)))-16)+"|")
                print("| Cutomer Name : ",name," "*((48-(len(name)))-17)+"|")
                print("| Phone No : ",number," "*((48-(len(number)))-13)+"|")
                print("+=================================================+")
                print("| SHOES	            PRICE             QUANTATY    |")
                print("+=================================================+")
                print("| "+data[0][1]," "*(16-len(data[0][1])),PRISE," "*(16-len(PRISE)),1, " "*gap+"|")
                print("|          		   		          |")
                print("|          		   		          |")
                print("|          		   		          |")
                print("+-------------------------------+-----------------+")
                print("| Sub Total 			|  Rs.",data[0][5]," "*((31-(len(PRISE)))-22),"|")
                print("| GST(12%)			|  Rs.",gst," "*((30-(len(gstr)))-21),"|")
                print("| Discount    			| ",discount+"%"," "*(((33-(len(discount)))-22)+1),"|")
                print("| Total Bill :			|  Rs.",total," "*((30-(len(totalstr)))-21),"|")
                print("+-------------------------------+-----------------+\n")

        else:
            break

else:
    print("Sorry, your user/password was incorrect. Please double-check your password.")
