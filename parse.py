'''
from re import *
with open('new_sam.txt','w') as outfile:
    with open('sam.txt','r') as file:
        for line in file:
            if line.splitlines()[0].split(':')[0][0:4]=='link':
                parsed_line=sub(':[^d ]+','',line)
                print parsed_line
                outfile.write(parsed_line)
'''

# from sets import Set
# import pprint
# import json
# dict={}

# with open('new.txt','r') as file:
#     for line in file:
#         parse_list=line.split(':  ')[-1].rstrip().split(' ')
#         for i in parse_list:
#             try:

#                 dict[i]=Set(dict[i]).union(Set(parse_list)-Set(dict[i])-Set([i]))
#             except KeyError:
#                 dict[i]=Set(parse_list)-Set([i])

# final_dict={}
# for i in dict.keys():
#     final_dict[i]=list(dict[i])

# with open('final.json','w') as outfile:
#     json.dump(final_dict,outfile,indent=4,sort_keys=True)




