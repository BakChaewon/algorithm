def solution(new_id):
    special_char = "~!@#$%^&*()=+[{]}:?,<>/"
    
    new_id = new_id.lower()
    
    for i in special_char:
        new_id = new_id.replace(i,'')

    while('..' in new_id):
        new_id = new_id.replace('..','.')
        
    new_id = new_id.strip('.')
        
    if(new_id == ""):
        new_id+='a'
    
    if(len(new_id)>15):
        new_id = new_id[:15]
    new_id = new_id.rstrip('.')
        
    while(len(new_id)<3):
        new_id += new_id[-1]
        
    return new_id