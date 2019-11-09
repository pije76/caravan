import requests
import time

#***********************************************************************************
# @function: Get Xml Data
#-----------------------------------------------------------------------------------
def getXmlData(xml_string, target):
    idx1 = xml_string.find("<" + target + ">")
    idx2 = xml_string.find("</" + target + ">")
    if idx1 == -1 or idx2 == -1:
        return None
    return xml_string[idx1 + len("<" + target + ">"):idx2]


#***********************************************************************************
# @function: Get Status of Sim Cards
#-----------------------------------------------------------------------------------
def getSimStatus(iccid_list):
    return None


# ***********************************************************************************
# @function: Update Status of Sim Card
# -----------------------------------------------------------------------------------
def updateSimStatus(iccid, status):
    return None