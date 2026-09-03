
class ErrorLog:
    def log(e,classname="",methodname="",otherinfo=""):
        message = "----------------------------------------------------\n"
        message += "Error Line: "+ str(e.__traceback__.tb_lineno)+"\n"
        message += "Error Message: "+ str(e)+"\n"
        message += "Error Type: "+type(e).__name__+"\n"
        message += "Class Name: "+classname+"\n"
        message += "Method Name: "+methodname+"\n"
        message += "Other Info: "+otherinfo+"\n"
        message += "------------------------------------------------------\n"
        with open("error.txt","a") as file:
            file.write(message)