def mapper():

    #Also make sure to fill out the reducer code before clicking "Test Run" or "Submit".

    #Each line will be a comma-separated list of values. The
    #header row WILL be included. Tokenize each row using the 
    #commas, and emit (i.e. print) a key-value pair containing the 
    #district (not state) and Aadhaar generated, separated by a tab. 
    #Skip rows without the correct number of tokens and also skip 
    #the header row.

    #You can see a copy of the the input Aadhaar data
    #in the link below:
    #https://www.dropbox.com/s/vn8t4uulbsfmalo/aadhaar_data.csv

    #Since you are printing the output of your program, printing a debug 
    #statement will interfere with the operation of the grader. Instead, 
    #use the logging module, which we've configured to log to a file printed 
    #when you click "Test Run". For example:
    #logging.info("My debugging message")
    #
    #Note that, unlike print, logging.info will take only a single argument.
    #So logging.info("my message") will work, but logging.info("my","message") will not.
    
    for line in sys.stdin:
        data = line.strip().split(',')
        if len(data) == 12 and data[3]!='District':
            print '{0}\t{1}'.format(data[3], data[8])

    return None

mapper()



def reducer():
    
    #Also make sure to fill out the mapper code before clicking "Test Run" or "Submit".

    #Each line will be a key-value pair separated by a tab character.
    #Print out each key once, along with the total number of Aadhaar 
    #generated, separated by a tab. Make sure each key-value pair is 
    #formatted correctly! Here's a sample final key-value pair: 'Gujarat\t5.0'

    #Since you are printing the output of your program, printing a debug 
    #statement will interfere with the operation of the grader. Instead, 
    #use the logging module, which we've configured to log to a file printed 
    #when you click "Test Run". For example:
    #logging.info("My debugging message")
    #Note that, unlike print, logging.info will take only a single argument.
    #So logging.info("my message") will work, but logging.info("my","message") will not.
        
    old_district = None
    for line in sys.stdin:
        data_mapped = line.strip().split('\t')
        if len(data_mapped) != 2:
            # Something has gone wrong. Skip this line.
            continue
        
        # same district
        if old_district and data_mapped[0] == old_district:
            count += float(data_mapped[1])
            
        # new district
        else:
            # not the first district
            if old_district:
                print '{0}\t{1}'.format(old_district,count)
                
            old_district = data_mapped[0]
            count = float(data_mapped[1])
            
    # print the last district
    print '{0}\t{1}'.format(old_district,count)
    
    return None
