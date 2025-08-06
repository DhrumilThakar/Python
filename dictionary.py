# Dictionary is key value pair means that it has some value and that value has the key
# e.g
dictionary = {
               "Dhrumil":777
              ,"Dhruv":888
              ,"Thakar":999
              ,0:"God father"
             }
# here Dhrumil , dhruv , thakar are key and 777 ,888,999 arer value
print(dictionary)
print(dictionary["Dhrumil"]) #It will print value of Dhrumil
# properties of dictionary 
"""# 1. It is unordered. 
# 2. It is mutable. 
# 3. It is indexed. 
# 4. Cannot contain duplicate keys."""


# METHODES OF DICTIONARY
"""
• a.items(): Returns a list of (key,value tuples. 
• a.keys(): Returns a list containing dictionary's keys. 
• a.update({"friends":}): Updates the dictionary with supplied key-value pairs. 
• a.get("name"): Returns the value of the specified keys (and value is returned 
eg."harry" is returned here).
"""
print(dictionary.items())
print(dictionary.values())
print(dictionary.keys())
print(dictionary.get("Dhrumil1")) # Print none if the name is not found  
print(dictionary["Dhrumil1"]) # Generate error