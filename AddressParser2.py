# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:29:57 2020

@author: sfarleig
"""

class AddressParser:
    
    def __init__(self):
        pass
    
    
    streetTypesList = [
            "Rd","Rd.","RD","RD.","ROAD",
           "St","St.","ST","ST.","STREET",
           "Ave","Ave.","AVE","AVE.","AVENUE",
           "Hwy","HWY","HIGHWAY",
           "Cir","Cir.","CIR","CIR.","CIRCLE","Circle",
           "Blvd","BLVD","Boulevard","BOULEVARD","Blvd.",
           "Wy","WY","Way","WAY",
           "Dr","Dr.","Drive","DR","DR.","DRIVE",
           "Ct","CT","COURT","COURTS","Ctr",
           "Trl","TRL","TRAIL",
           "Ln","LN","LANE",
           "Ter","TER","TERRACE",
           "Pkwy","PKWY","Parkway","PARKWAY",
           "Bnd","BND",
           "Plaza", "PLAZA","PLZ","Plz","PL",
           "Tpke", "TPKE", "TURNPIKE","PIKE","Pike",
           "Grn",
           "SQ","SQUARE",
           "PARK","Park","Run"
           "ARCH","SQUARE","LOOP","BEND","PLACE","GRADE","CMNS","CMN",
                   ]
    
    rdList = ["Rd","Rd.","RD","RD.","ROAD"]
    stList = ["St","St.","ST","ST.","STREET"]
    aveList = ["Ave","Ave.","AVE","AVE.","AVENUE"]
    hwyList = ["Hwy","HWY","HIGHWAY"]
    cirList = ["Cir","Cir.","CIR","CIR.","CIRCLE","Circle"]
    blvdList = ["Blvd","BLVD","Boulevard","BOULEVARD","Blvd."]
    wayList = ["Wy","WY","Way","WAY"]
    drList = ["Dr","Dr.","Drive","DR","DR.","DRIVE"]
    ctList = ["Ct","CT","COURT","COURTS"]
    trlList = ["Trl","TRL","TRAIL"]
    lnList = ["Ln","LN","LANE"]
    terList = ["Ter","TER","TERRACE"]
    pkwyList = ["Pkwy","PKWY","Parkway","PARKWAY"]
    bndList = ["Bnd","BND"]
    plazaList = ["Plaza", "PLAZA","PLZ","Plz","PL"]
    tnpkList = ["Tpke", "TPKE", "TURNPIKE","PIKE","Pike"]
    
    miscList = ["Grn","ARCH","Arch","SQUARE","Square","LOOP","Loop","BEND","Bend","PLACE","Place","GRADE","Grade","HOLLOW","Hollow","CMNS","CMN","Park"]
        

    
    suiteTypesList = [
            "Suite","Ste","Apartment","Apt","Trlr","Lot","Room","Rm","Unit","Bldg","Fl",
            "SUITE","STE","APARTMENT","APT","TRLR","LOT","ROOM","RM","UNIT","BLDG","FL",
            "#","BOX"
            ]
        

    directionList = [
            'N','S','E','W','NE','NW','SE','SW',
             'NORTH','North','north',
             'SOUTH','South','south',
             'EAST','East','east',
             'WEST','West','west',
             'NORTHEAST', 'Northeast','northeast',
             'NORTH EAST','North East','north east',
             'NORTHWEST','Northwest','northwest',
             'NORTH WEST','North West','north west'
             'SOUTHEAST','Southeast','southeast',
             'SOUTH EAST','South East','south east',
             'SOUTHWEST','Southwest','southwest'
             'SOUTH WEST','South West','south west'            
             ]
    
    poBoxList = [
            "P.O.","PO","p.o.","P O","po","p o","P.o.","POBOX","PoBox"
            ]


    addressDict = {
            "orgName" : "",
            "streetNumber" : "",
            "streetDirection1": "",
            "streetName" : "",
            "streetType" : "",
            "streetDirection2" : "",
            "suiteType" : "",
            "suiteNumber" : "",
            "city" : "",
            "state" : "",
            "zipFirst5" : "",
            "zipLast4" : ""
            }
    
    indexDict = {
            "IDX_orgName" : -1,
            "IDX_streetNumber" : -1,
            "IDX_streetDirection1": -1 ,
            "IDX_streetName" : -1,
            "IDX_streetType" : -1,
            "IDX_streetDirection2" : -1,
            "IDX_suiteType" : -1,
            "IDX_suiteNumber" : -1,
            "IDX_city" : -1,
            "IDX_state" : -1,
            "IDX_zip" : -1  
            }
    
    streetTypeDict = {
            1 : rdList,
            2 : stList,
            3 : aveList,
            4 : hwyList,
            5 : cirList,
            6 : blvdList,
            7 : wayList,
            8 : drList,
            9 : ctList,
            10 : trlList,
            11 : lnList,
            12 : terList,
            13 : pkwyList,
            14 : bndList,
            15 : plazaList,
            16 : tnpkList,
            20 : miscList
        }
   
    
###############################################################################
#                               FUNCTIONS
###############################################################################    
    

    def ParseAddress(self,address):
                
        # simple logic for parsing out a postal code - determine if it's 5 or 9 
        # digits and get rid of any special characters.
        def GetZip(zipCode):
            # zip
            if len(zipCode) == 5:
                
                return zipCode
                           
            elif len(zipCode) == 9:
                zipFirst5 = zipCode[0:5]
                zipLast4 = zipCode[5:9]
                
                z = [zipFirst5, zipLast4]
                return z
                
            elif len(zipCode) == 10:
                c = zipCode.split('-')
                return c
        
        
        # logic for parsing out the street name in the address string. uses positional indexes to 
        # determine how many words are in the street name and returns it
        def GetStreetName(addressSplit, indexDictionary):
            if indexDictionary["IDX_streetDirection1"] < 0:
                delta = indexDictionary["IDX_streetType"] - indexDictionary["IDX_streetNumber"]
                
                if delta == 2:
                    streetName = addressSplit[indexDictionary["IDX_streetType"] - 1]
                    return streetName
                
                elif delta > 2:
                    streetName = ""
                    for i in range(indexDictionary["IDX_streetNumber"] + 1, indexDictionary["IDX_streetType"]):
                        streetName = streetName + addressSplit[i] + " "
                        
                    streetName = streetName.rstrip()
                    return streetName
                
                
            elif indexDictionary["IDX_streetDirection1"] > 0:
                delta = indexDictionary["IDX_streetType"] - indexDictionary["IDX_streetDirection1"]
                
                if delta == 2:
                    streetName = addressSplit[indexDictionary["IDX_streetType"] - 1]
                    return streetName
                
                elif delta > 2:
                    streetName = ""
                    for i in range(indexDictionary["IDX_streetDirection1"] + 1, indexDictionary["IDX_streetType"]):
                        streetName = streetName + addressSplit[i] + " "
                        
                    streetName = streetName.rstrip()
                    return streetName
                
                
            
        # logic for parsing out the city name in the address string. uses positional indexes to 
        # determine how many words are in the city name and returns it    
        def GetCityName(addressSplit, indexDictionary):
            suiteNum = indexDictionary["IDX_suiteNumber"]
            streetDirection = indexDictionary["IDX_streetDirection2"]
            streetType = indexDictionary["IDX_streetType"]
            
            lst = [suiteNum, streetDirection, streetType]
            idx = max(lst)
            
            state = indexDictionary["IDX_state"]
            
            delta = state - idx
            
            if delta == 2:
                cityName = addressSplit[indexDictionary["IDX_state"] - 1]
                return cityName
            
            elif delta > 2:
                cityName = ""
                for i in range(idx + 1, state):              
                    cityName = cityName + addressSplit[i] + " "
           
                cityName.rstrip()
                return cityName
        
        # Utility function for parseAddress function
        def parsePOBoxAddress(address):
    
            
            addressSplit = address.split()
            splitFactor = len(addressSplit)
            
            addrDict = self.addressDict
            
            # po box
            streetNumber = addressSplit[0] + " " + addressSplit[1] + " " + addressSplit[2]
            addrDict["streetNumber"] = streetNumber
            streetNumberIndex = 2
            
            
            #state
            state = addressSplit[splitFactor - 2]
            addrDict["state"] = state
            stateIndex = splitFactor - 2
            
            #city
            if stateIndex - streetNumberIndex > 2:
                for i in range(streetNumberIndex + 1, stateIndex):
                    addrDict["city"] = addrDict["city"] + addressSplit[i] + " "
                
            elif stateIndex - streetNumberIndex == 2:
                cityIndex = stateIndex - 1
                addrDict["city"] = addressSplit[cityIndex]
            
            addrDict["city"] = addrDict["city"].rstrip()
            
            #zip
            zipcode = addressSplit[splitFactor - 1]
            if len(zipcode) == 5:
                addrDict["zipFirst5"] == zipcode
                    
            
            elif len(zipcode) == 9:
                addrDict["zipFirst5"] = zipcode[0:5]
                addrDict["zipLast4"] = zipcode[5:9]
                
            elif len(zipcode) == 10:
                zipcode = addressSplit[splitFactor - 1].split('-')
                addrDict["zipFirst5"] = zipcode[0]
                addrDict["zipLast4"] = zipcode[1]
                
            return addrDict
        
       
        ################################
        #     LOGIC STARTS HERE
        
        
        # get our lists and bring in copies of the dictionaries to hold
        # index values and address values
        addrDict = self.addressDict.copy()
        streetTypes = self.streetTypesList
        suiteTypes = self.suiteTypesList
        directions = self.directionList
        poBox = self.poBoxList
        idx = self.indexDict.copy()
        
        # split the address and get our count
        addressUpper = address.upper()
        addressSplit = addressUpper.split()
        splitFactor = len(addressSplit)
        
        # if the address is a PO box, then stop here and call the function specifically 
        # for PO Boxes
        if addressSplit[0] in poBox:
            return parsePOBoxAddress(address)
        
        
        # find the street number index
        for x in addressSplit:
            if x.isdigit() or x[0:len(x)-1].isdigit():
                idx["IDX_streetNumber"] = addressSplit.index(x)
                break
            
                            
           
        # find the street type index
        streetTypeCount = 0
        for x in addressSplit:
            if x in streetTypes:
                streetTypeCount += 1
                idx["IDX_streetType"] = addressSplit.index(x)
                if streetTypeCount > 1 and addressSplit.index(x) < (len(addressSplit)-3):
                    idx["IDX_streetType"] = addressSplit.index(x)
                    
                    # print statement for debugging
                    #print("this is working")
                    
                else:
                    break
                    
                
                        
        # find the street direction index if exists
        for x in addressSplit:
            if x in directions:
                x1 = addressSplit.index(x)
                
                if x1 < idx["IDX_streetType"]:
                    idx["IDX_streetDirection1"] = addressSplit.index(x)
                    break
                    
                elif x1 > idx["IDX_streetType"]:
                    idx["IDX_streetDirection2"] = addressSplit.index(x)
                    break
                    
            else:
                pass
        
        
        # find the suite type index if exists
        for x in addressSplit:
            if x in suiteTypes:
                idx["IDX_suiteType"] = addressSplit.index(x)
                
                # Grab the suite number index since it'll always be right after the suite type.
                idx["IDX_suiteNumber"] = addressSplit.index(x) + 1
                
            elif x.startswith("#"):
                idx["IDX_suiteNumber"] = addressSplit.index(x)
                
                
        
        # find the zip code
        zipcode = addressSplit[splitFactor - 1]
        idx["IDX_zip"] = splitFactor - 1
        zipCode = GetZip(zipcode)
        
        if len(zipCode) == 5:
            addrDict["zipFirst5"] = zipCode
            
        elif len(zipCode) == 2:
            addrDict["zipFirst5"] = zipCode[0]
            addrDict["zipLast4"] = zipCode[1]
            
            
        # find state index
        idx["IDX_state"] = idx["IDX_zip"] - 1
        
        
        # Determine if there is an orgName in the address, and if so then add it
        # to the address dictionary
        if idx["IDX_streetNumber"] > 0:
            for i in range(0, idx["IDX_streetNumber"] - 1):
                addrDict["orgName"] = addrDict["orgName"] + addressSplit[i] + " "
        
        

        # get index values out of index and load them into our addrDict where index is 
        # greater or equal to 0
            
        if idx["IDX_streetNumber"] >= 0:
            addrDict["streetNumber"] = addressSplit[idx["IDX_streetNumber"]]
            
        if idx["IDX_streetDirection1"] >= 0:
            addrDict["streetDirection1"] = addressSplit[idx["IDX_streetDirection1"]]
            
        if idx["IDX_streetType"] >= 0:
            addrDict["streetType"] = addressSplit[idx["IDX_streetType"]]
            
        if idx["IDX_streetDirection2"] >= 0:
            addrDict["streetDirection2"] = addressSplit[idx["IDX_streetDirection2"]]
                       
        if idx["IDX_suiteType"] >= 0:
            addrDict["suiteType"] = addressSplit[idx["IDX_suiteType"]]
            
        if idx["IDX_suiteNumber"] >= 0:
            addrDict["suiteNumber"] = addressSplit[idx["IDX_suiteNumber"]]
            
        if idx["IDX_state"] >= 0:
            addrDict["state"] = addressSplit[idx["IDX_state"]]
            
            
        # Determine if the street name is one word or multiple words, and add them to 
        # the dictionary
        streetName = GetStreetName(addressSplit, idx)        
        addrDict["streetName"] = streetName
        
        # Determine if the city name is one word or multiple words, and add them to the dictionary
        cityName = GetCityName(addressSplit, idx)
        addrDict["city"] = cityName
        
        # make sure the dictionary being returned is usable
        # i.e. if there is no street type or city or state, throw an error
#        try:
#            if addrDict["city"] == None or addrDict["streetName"] == None:
#                raise Exception("Address did not parse correctly")
#                
#        except Exception as e:
#            print("A city name or street name was unable to be indexed\nError: {}".format(e))
#            return 0
#        
#        finally:
#            pass
        
        #return the address dictionary
        return addrDict
    
    
    
    
    def CompareAddress(self, address1, address2, outputStyle):
        
        def checkAddressItem(addressItem, add1, add2):
            idx = addressItem
            errCount = 0
            
            if add1[idx] == add2[idx]:
                confidence = 100
                return confidence
            
            else:
               a = len(add1[idx])
               b = len(add2[idx])
               c = a - b
               
               if c == 0:
                  a_lst = list(add1[idx])
                  b_lst = list(add2[idx])
                  
                  for i in range(max(a,b)):
                      if a_lst[i] == b_lst[i]:
                          pass
                      else:
                          errCount += 1
                          
                    
                  confidence = errCount / a
                  return confidence
              
               else:
                   confidence = 0
                   return confidence
               
                
        def checkStreetType(add1, add2):
            streetDict = self.streetTypeDict
            
            t1 = add1.get("streetType")
            for x in streetDict:
                for y in streetDict[x]:
                    if t1 in y:
                        t1_idx = x
                        
            t2 = add2.get("streetType")
            for x in streetDict:
                for y in streetDict[x]:
                    if t2 in y:
                        t2_idx = y
                        
            
            if t1_idx == t2_idx:
                confidence = 100
                return confidence
            
            else:
                confidence = 0
                return confidence
            
        
        ###############################
        #  Logic Starts Here
                
        CONF_streetNumber = 0
        CONF_streetName = 0
        CONF_streetType = 0
        CONF_city = 0
        CONF_state = 0
        CONF_zip = 0
        
        CONF_total = 0

        

        
        addr1 = self.ParseAddress(address1.upper()).copy()
        addr2 = self.ParseAddress(address2.upper()).copy()

        
        # If they are the exact same values, 100% match, then stop here.
        if addr1 == addr2:
            if outputStyle == 1:
                results = "Exact Match"
                return results
        
            elif outputStyle == 2:
                return 1
        
        else:
            
            # check street number
            CONF_streetNumber = checkAddressItem("streetNumber", addr1, addr2)
             
            # check street name
            CONF_streetName = checkAddressItem("streetName", addr1, addr2)
            
            # check street type*
            CONF_streetType = checkStreetType(addr1, addr2)
            
            # check city
            CONF_city = checkAddressItem("city", addr1, addr2)
            
            # check state
            CONF_state = checkAddressItem("state", addr1, addr2)
            
            # check zip
            CONF_zip = checkAddressItem("zipFirst5", addr1, addr2)
            
            
            # total confidence
            CONF_total = (CONF_streetNumber + CONF_streetName + CONF_streetType + CONF_city + CONF_state + CONF_zip) / 6
            
            if outputStyle == 1:
                if CONF_total > 80:
                    return "MATCH. Confidence: {:.2f}%".format(CONF_total)
                
                else:
                    return "NO MATCH. Confidence: {:.2f}%".format(CONF_total)
                
            elif outputStyle == 2:
                if CONF_total > 80:
                    return 1
                
                else:
                    return 0
            
#%%
    
