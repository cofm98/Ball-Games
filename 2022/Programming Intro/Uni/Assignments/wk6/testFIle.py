def openFile (file : str):
    fileData = open(file,"r")
    for lineOfText in fileData:
        array1 = ",".split(lineOfText)
        students.append(array1[0])
        try:
            payment.append(int(array1[1]))
        except:
            print("Payment not an integer for ")
    fileData.close()

try:
    openFile(15)
except:
    print(45)
