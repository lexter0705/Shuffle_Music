import os
import random



def func_mix(road_path):
    try:
        if road_path !=  None:
            list_file = []
            numbers = []
            for root, dirs, files in os.walk(road_path):  
                for filename in files:
                    list_file.append(filename)
                break
            
            for i in list_file:
                file_r  = i.split(".")[len(i.split(".")) - 1]
                file_name = i[:len(i) - len(file_r) - 1]
                
                new_file_name = delete_prefix(file_name)
                
                number = random.randint(1, len(list_file)+1)
                
                while number in numbers:
                    number = random.randint(1, len(list_file)+1)     
                else:
                    numbers.append(number) 
                    os.rename(road_path+"/"+file_name+"."+file_r, road_path+"/"+str(number)+"_"+new_file_name+"."+file_r)
                    
            return [True, None]
    except Exception as e:
        return [False, str(e)]
                
                
def delete_prefix(name):
    try:
        if len(name.split("_")) != 1:
            is_number = int(name.split("_")[0])
            return name[len(str(is_number))+1:]
        else:
            return name
    except  Exception as e:
        print(e)
        return name
                

        
    
    
    
    
    


    
                
        

    