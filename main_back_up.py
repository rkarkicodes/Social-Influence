# import sqlite3
# import json
 
# class SocialInfluence(object):
#     __connection=None
#     __cursor=None
 
#     def __init__(self):
#         self.__connection=sqlite3.connect('Social_Influence.db')
#         self.__cursor=self.__connection.cursor()
 
 
#     def append_tables(self):
#         with open('final_mini.json') as file:
#             data=json.load(file)
#             for i in data.keys():
 
#                 self.__cursor.execute("CREATE TABLE {}(Neighbours TEXT)".format(i))
#                 self.__cursor.execute("INSERT INTO Nodes Values(?,?);",(i,len(data[i])))
#                 query="INSERT INTO {}(Neighbours) VALUES(?);".format(i)
#                 self.__cursor.executemany(query,[(i,) for i in data[i]])
#                 print i
#         self.__connection.commit()
 
 
#     def influence(self,nodeId=None,hop=None,random=None):
#         ## can pass through hop to specify hops,nodeid to get info on specific node, random to get info
#         #  on random no. of nodes.
 
#         a=self.__cursor.execute('SELECT * from Nodes WHERE NodeId in ("N30080","N26571")')
#         b=self.__cursor.execute('SELECT * from {}'.format("N30080"))
 
#         neigh=tuple([str(i[0]) for i in b.fetchall()])
 
#         print neigh
#         p='SELECT * from Nodes WHERE NodeId in {}'.format(neigh)
#         #print p
#         c=self.__cursor.execute(p)
#         print c.fetchall()
#         # for i in b:
#         #     print i
 
#     def frequency_table(self,hop_column):
#         self.__cursor.execute("create table {}(Degree INTEGER PRIMARY KEY,Frequency INTEGER)".format(hop_column))
#         dict={}
#         degree=self.__cursor.execute("select Degree from Nodes")
#         for i in degree.fetchall():
#             try:
#                 dict[i[0]]=dict[i[0]]+1
#             except KeyError:
#                 dict[i[0]]=1
 
#         a=[(k,dict[k]) for k in dict.keys()]
 
#         self.__cursor.executemany("Insert into {} values(?,?);".format(hop_column),a)
#         self.__connection.commit()
 
#     def delete(self,table):
#         self.__cursor.execute("Drop table {}".format(table))
 
#         self.__connection.commit()
 
    # def one_hop(self):
    #     #self.__cursor.execute("ALTER TABLE Nodes Add COLUMN one_hop INTEGER")
    #     nodes= self.__cursor.execute("Select NodeId from Nodes")
    #     for node in nodes:
    #         neighbour=self.__cursor.execute("Select Neighbours from {}".format(node))
 
 
 
 
    #     self.__connection.commit()
 
#     def try_this(self):
#         self.__cursor.execute("CREATE TABLE {}(Neighbours TEXT)".format("Rohit"))
#         self.__connection.commit()
 
 
# #SocialInfluence().add_col()
# #SocialInfluence().append_tables()
# #SocialInfluence().influence()
# #SocialInfluence().frequency_table("zero_hop")
# #SocialInfluence().delete("zero_hop")
# #SocialInfluence().one_hop()
# SocialInfluence().try_this()









