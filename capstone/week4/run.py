#!/usr/bin/env python3 


def GetListOfFiles(directory):
    import os
    print('Processing files from ' + directory)

    return os.listdir(directory)

def CreateDictionaryFromFile(filepath):
    print('Creating dictionary for file ' + filepath)

    feedback={} # create empty dictionary
    with open(filepath,'r') as f:
        data = f.read().split('\n')
        feedback = { 'name':data[0], 'weight':str(data[1]).replace(' lbs',''), 'description ':data[2], 'image_name':data[3] }
    
    return feedback

 


def UploadFeedback(feedback):

    import requests

    external_ip='34.69.172.207'

 
    url='http://' + external_ip + '/feedback/'
    #url='http://35.224.23.11/feedback'
    

    response = requests.post(url, data=feedback)

    print('response.status_code:' + str(response.status_code))

    #I needed to add '/' after "http://25.192.192.226/feedback" before it worked. I was getting response code 500, and response.text gave me this feedback which pointed me to the solution.
    #"Exception Type: RuntimeError at /feedback
    # Exception Value: You called this URL via POST, but the URL doesn&#39;t end in a slash and you have APPEND _SLASH set. Django can&#39;t redirect to the slash URL while maintaining POST data. Change your form to point to 35.192.192.226/feedback/ (note the trailing slash), or set APPEND_SLASH=False in your Django settings.

    
def main():

    import os, sys
    this_script_path=(os.path.dirname(sys.argv[0]))
    this_script_name=(os.path.basename(sys.argv[0]))
    #datadir=os.path.abspath(os.path.join(this_script_path,"data", "feedback"))
    datadir=os.path.abspath(os.path.join(this_script_path,"supplier-data", "descriptions"))
    #outdir='/opt/icons'

    filelist=GetListOfFiles(datadir)
    print(filelist)

    for file in filelist:
        filepath=os.path.join(datadir,file)
        print('Processing file ' + filepath)
        description = CreateDictionaryFromFile(filepath)
        print(description)
        #UploadFeedback(description)
        



if __name__=='__main__':
    main()