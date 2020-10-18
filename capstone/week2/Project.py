#!/usr/bin/env python3 

#Project Problem Statement
#To complete this module, you'll write a script that interacts with a running web service.  The web service is part of your company's website and is in charge of storing and displaying the customer reviews of the company.
#The reviews are stored in text files in the local disk. Your script should open those files, process the information to turn it into the format expected by the web service, then send it to the web service to get stored.
#For this lab, the service is running on the same machine, and you can actually look at how all of it is implemented, if you want.  But you don't need to change the service implementation to complete the exercise.
#Remember that you can take your time to prepare the code that you’ll write. You can start the lab later on, once you have a good idea of what you'll do and how you'll do it.
#Also, feel free to check out the resources that we pointed to as many times as you need.
#Good luck, you've got this!



#Introduction
#You're working at a company that sells second-hand cars. 
# Your company constantly collects feedback in the form of customer reviews. 
# Your manager asks you to take those reviews (saved as .txt files) and display them on your company's website. 
# To do this, you'll need to write a script to 
#   * convert those .txt files and 
#   * process them into Python dictionaries, 
#   * then upload the data onto your company's website (currently using Django).

# What you'll do
# Use the Python OS module to process a directory of text files
# Manage information stored in Python dictionaries
# Use the Python requests module to upload content to a running Web service
# Understand basic operations for Python requests like GET and POST methods
# You'll have 90 minutes to complete this lab.





def GetListOfFiles(directory):
    import os
    print('Processing files from ' + directory)

    return os.listdir(directory)

def CreateDictionaryFromFile(filepath):
    print('Creating dictionary for file ' + filepath)

    feedback={} # create empty dictionary
    with open(filepath,'r') as f:
        data = f.read().split('\n')
        feedback = { 'title':data[0], 'name':data[1], 'date':data[2], 'feedback':data[3] }
    
    return feedback

def CreateDictionaryFromFile_OLDVersion(filepath):
    print('Creating dictionary for file ' + filepath)

    feedback={} # create empty dictionary
    with open(filepath,'r') as f:
        i=1
        for line in f:
            if i == 1:
                feedback['title'] = line
            elif i == 2:
                feedback['name'] = line
            elif i == 3:
                feedback['date'] = line
            elif i == 4:
                feedback['feedback'] = line
            
            i += 1
    
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
    datadir=os.path.abspath(os.path.join("/","data", "feedback"))
    #outdir='/opt/icons'

    filelist=GetListOfFiles(datadir)
    print(filelist)

    for file in filelist:
        filepath=os.path.join(datadir,file)
        print('Processing file ' + filepath)
        feedback = CreateDictionaryFromFile(filepath)
        print(feedback)
        UploadFeedback(feedback)
        



if __name__=='__main__':
    main()