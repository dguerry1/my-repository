
# Dictionarys are "key" : "value"
statuses = {"Alice": "online",
            "Bob": "offline",
            "Eve": "online",      
}

# function that takes dictionary "statuses" as parameter
def online_count(statuses):
    # set x = online
    x = "online"
    
    # initialize counter to 0
    res = 0
    
    # looking into the dictionary statuses at all the values
    for value in statuses:
        
        # if the value in statuses = "online"
        if statuses[value] == x:
            
            # increment counter by 1 when "online"
            # is detected in the dictionary
            res = res + 1
    # print the string res 
    print("Frequency of x is : " +str(res))

# call the function    
online_count(statuses)