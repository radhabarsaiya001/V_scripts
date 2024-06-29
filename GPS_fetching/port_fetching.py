import serial.tools.list_ports
lst_obj = serial.tools.list_ports.comports()
pattern = r"PL2303GC"
# print(lst_obj)
def port():
    try:
        if len(lst_obj) != 0 or lst_obj != [] :
            for i in lst_obj:
                new = str(i)
                if pattern in new:
                    port_fetching = new.split(' ')
                    port = port_fetching[0]
                    # print(port)
                    return port
                else:
                    # print("No GPS Device found.")
                    return "No GPS Device found."

        # if lst_obj == [] :
        #     print("No any GPS found.")
        else:
            # print("******************")
            # print("Not any com port available, please attach the communication port.")
            return "Not any com port available, please attach the communication port."
    except Exception as e:
        # print("Some Challanges with GPS Connection.")
        return f"{e}" 
    
# port()
