from .editData import insertChangeOnSupply, insertChangeOnService

def validationForEdit(root, type, id, val1, val2, val3, val4, val5, val6):

    val1String = str(val1)
    val2String = str(val2)
    val3String = str(val3)
    val4String = str(val4)
    val5String = str(val5)
    val6String = str(val6)

    val1Up = val1String.upper()
    val2Up = val2String.upper()
    val3Up = val3String.upper()
    val4Up = val4String.upper()
    val5Up = val5String.upper()
    val6Up = val6String.upper()

    if type == "CLIENT":
        val1UpWhitoutSpace = val1Up.replace(" ", "")
        insertChangeOnService(root, id, val1UpWhitoutSpace, val2Up, val3Up, val4Up, val5Up, val6Up)
    elif type == "SUPPLY":
        insertChangeOnSupply(root, id, val1Up, val2Up, val3Up, val4Up, val5Up, val6Up)
    