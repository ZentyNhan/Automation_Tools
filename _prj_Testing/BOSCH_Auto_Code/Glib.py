import re
import os
import sys

def findfolder(pattern, path):
    result = {'path' : '', 'name': ''}
    for root, dirs, files in os.walk(path):
        for name in dirs:
            if search_f(name, pattern):
                result['path'] = os.path.join(root, name).replace('\\', '/')
                result['name'] = name        
                return result
    return result

def findfile(pattern, path, extension = ''):
    result = {'path' : '', 'name': ''}
    for root, dirs, files in os.walk(path):
        for name in files:            
            if extension != '':
                if name.endswith(extension) == False:
                    continue        
            if search_f(name, pattern):                
                result['path'] = os.path.join(root, name).replace('\\', '/')
                result['name'] = name  
                break
    return result

def replace_f(strInput, Pattern, strRplace):    
    if re.search(Pattern, strInput, re.IGNORECASE) != None : 
        return re.sub(Pattern, strRplace, re.search(Pattern, strInput, re.IGNORECASE).group(), re.IGNORECASE)

def search_f(strInput, Pattern):   
    if re.search(Pattern, strInput, re.IGNORECASE) != None : 
        return re.search(Pattern, strInput, re.IGNORECASE).group()
    else:
        return ""