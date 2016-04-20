import sqlite3
import json
import numpy as np


class SocialInfluence(object):
    __connection=None
    __cursor=None

    def __init__(self,dataset):
        self.dataset=dataset
        self.__connection=sqlite3.connect('{}.db'.format(self.dataset))
        self.__cursor=self.__connection.cursor()


    def append_tables(self):
        ## populate database by parsing json file.
        
        self.__cursor.execute("CREATE TABLE NODES(NodeId TEXT PRIMARY KEY,Degree INTEGER)")
        p=0
        with open('{}.json'.format(self.dataset)) as file:
            data=json.load(file)
            for i in data.keys():
                p+=1
                # print type(i)
                self.__cursor.execute("CREATE TABLE {}(Neighbours TEXT)".format("N"+i))

                self.__cursor.execute("INSERT INTO Nodes Values(?,?);",("N"+i,len(data[u''+i])))
                query="INSERT INTO {}(Neighbours) VALUES(?);".format("N"+i)
                self.__cursor.executemany(query,[("N" + k,) for k in data[i]])
                if p==1000:
                    print "10k"
                    p=0

            self.__connection.commit()



    def influence(self,**options):
        ## can pass through hop,nodeid as keyword agruments.
        # self.__cursor.execute("INSERT INTO Nodes VALUES('N132',65)")
        # self.__cursor.execute("CREATE TABLE {}(Neighbours TEXT)".format("Q12345"))
        # self.__cursor.execute("SELECT name FROM sqlite_master WHERE Type='table';")
        # for i in self.__cursor.fetchall():

        a=self.__cursor.execute("SELECT name FROM sqlite_master WHERE Type='table';")
        
        print len(a.fetchall())
        for i in a:
            print i
    
        a=self.__cursor.execute("Select * from Nodes Where degree>1000")
    
        print max(a.fetchall())
    
    def frequency_table(self,hop_column):
        maximum=self.__cursor.execute("select max(Degree) from Nodes").fetchone()[0]
        print maximum
        i=1
        self.__cursor.execute("create table {}(Degrees INTEGER PRIMARY KEY,FREQUENCY INTEGER)".format(hop_column))
        while i<=maximum:
            
            a=self.__cursor.execute("Select count(NodeId) from Nodes where degree={}".format(i))
            b=a.fetchone()[0]
            if b!=0:
                self.__cursor.execute("insert into {} values({},{});".format(hop_column,i,b))
                #print "degree {} => {}".format(i,b)
 
            i+=1
        self.__connection.commit()
    

    
    def delete(self,table):
        self.__cursor.execute("Drop table {}".format(table))
        self.__connection.commit()
        
    def try_this(self):
        #self.__cursor.execute("Drop table Nodes")
        #a="[0_hop]"
        #print a
        self.__cursor.execute("Create table Nodes_new(NodeId Text PRIMARY KEY,[0_hop] Integer)")
        self.__cursor.execute("Insert into Nodes_new select NodeId,Degree from Nodes")
        self.__cursor.execute("Alter table Nodes rename to Nodes_back")
        self.__cursor.execute("Alter table Nodes_new rename to Nodes")
        self.__connection.commit()
    

    def hops(self,hop):


        ## calculating hops of each node
        all_nodes=self.__cursor.execute("select * from NODES")
        print all_nodes.description[-1]
        # if hop<len(all_nodes.description)-2:
        #     print "Currently the database contains information upto {} hops".format(str(len(a.description)-2))
        #
        # else:
        #     for i in range(len(all_nodes.description)-1,hop+1):
        #         # a=self.__cursor.execute("select * from nodes")
        #
        #         print "Currently the database contains information upto {} hops, calculating {} hops..".format(str(len(all_nodes.description)-2),str(i))
        #         col="{}_hop".format(str(i))
        #         # print a.fetchall()
        #         self.hop_query(col,all_nodes)
        #         print col


    def hop_query(self,col,all_nodes):
        #create a column with col
        print type(col)
        #all_nodes=self.__cursor.execute("select * from nodes")
        # print all_nodes.description
        self.__cursor.execute("alter table 'nodes' add column {} integer".format(col))
        for i in all_nodes:
            # self.__cursor.execute("alter table 'nodes' add column {} integer ".format(col))
            print i
            break





    def stats(self):
        ## average and standard deviation of each hop.
        self.__cursor.execute("Create table stats(hops TEXT, average INTEGER,standard_deviation INTEGER)")
        
        a=self.__cursor.execute("select * from nodes limit 1").description

        #print a.description

        for i in range(1,len(a)):
            b=self.__cursor.execute("select [{}] from nodes".format(a[i][0])).fetchall()
            c=[k[0] for k in b]
            print type(a[i][0])

            self.__cursor.execute("insert into stats values(?,?,?);",(a[i][0],np.mean(c),np.std(c)))

        self.__connection.commit()


# SocialInfluence("facebook").append_tables()
# SocialInfluence().influence()
SocialInfluence("facebook.db").hops(1)
#SocialInfluence().frequency_table("one_hop")
# SocialInfluence().stats()
