from datetime import datetime

def headinglab(lab):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S") # dd/mm/YY H:M:S
    print("Exrcuted time: {}\n{} Name: Setthapong Kiankhao Student ID: 64114069".format(dt_string, lab))
    return dt_string