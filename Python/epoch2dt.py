import sys
import re
import datetime

# Check filename from argv
if len(sys.argv) >= 2 :
    # argv[0] = progran execute, argv[1] = filename parameter
    file = open(sys.argv[1])
    # read file to data variable
    data = file.read()
    # close file after read
    file.close()
    # check data from file
    if (data != ""):
        print('\nLoading ['+sys.argv[1]+']')
        # using regex finding with pattern 
        # after that get word match convert to Datetime formated 
        # and replace in found place. 
        data = re.sub('([0-9]{10})', lambda r:datetime.datetime.fromtimestamp(int(r.group(1))).strftime('%Y-%m-%d %H:%M:%S'), data)
        # add "modified_" for output file
        fname = 'modified_' + sys.argv[1] 
        print('\nCreating ['+(fname)+']')
        # open new file with 'w' param
        file = open(fname, "w")
        # write data to file
        file.write(data)
        # close file after write
        file.close()
        print('\nComplete.')
else:
    # if not found filename in argv[1]
    print('\nex. epoch2dt.py [filename]')
    
### Test Data ###
#data = "[1620729029.593:hcap-mw]009038.794836:hcap-mw >hcap-mw ] [tid:2233|W|hms_json_util.cpp|77|get_data] no key \"errorCode\""
#data = data + "\n[1620729029.605:tvservice]009038.806558:tvservic>n0000060] handler_cd_hcap_getNetworkInformation_payload"
### Test Data ###

