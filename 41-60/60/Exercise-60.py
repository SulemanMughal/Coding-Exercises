def return_end_of_number(num):
    str_num = str(num)
    if(str_num[-1] == '1'):
        return(str_num + "-ST")
    elif(str_num[-1] == '2'):
        return(str_num + "-ND")
    elif(str_num[-1] == '3'):
        return(str_num + "-RD")
    else:
        return(str_num + "-TH")