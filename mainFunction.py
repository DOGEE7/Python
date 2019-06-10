from concurrent.futures import thread
from py2neo import Graph, Node, Relationship,NodeMatcher
import csv
import time
import threading

relationshipDic = [n for n in range(20)]
holeNum = 0
succeedNum = 0
failureNum = 0
flag = True
def coountTime():
    count = 0
    while flag == True:
        count =count +1
        print("time now is " + str(count) + 's  A'+str(holeNum) +"  S" + str(succeedNum) + "  F" + str(failureNum))
        time.sleep(1)

def create(sth):
    transaction.create(sth)
"""开始计时"""
t = threading.Thread(target = coountTime)
t.start()
"""建立连接"""
graph = Graph(url = "bolt://localhost:7687",
                 username="neo4j",
                 password="neo4j")
transaction = graph.begin()
matcher = NodeMatcher(graph)
"""处理数据"""
with open(r'D:\STUDY\项目\医检易小程序\neo4j\work2.csv', encoding='UTF-8') as f:
            reader = csv.reader(f)
            data = list(reader)
for i in data:
    if i[0] =='1':
        relationshipDic[int(i[2])] = str(i[1])
        succeedNum = succeedNum + 1
    elif i[0] == '2':
        newNode = Node(str(i[1]),name = str(i[2]).strip())
        if i[1] == 'test':
            newNode['normal_value_lower'] = i[3]
            newNode['normal_value_upper'] = i[4]
            newNode['unit'] = i[5]
            newNode['define'] = i[7]
            newNode['specimen'] = i[8]
        graph.create(newNode)
        succeedNum = succeedNum + 1

    elif i[0] == '3':
        node1 = matcher.match(name = str(i[1]).strip()).first()
        node2 = matcher.match(name = str(i[3]).strip()).first()
        if node1 == None or node2 == None:
            failureNum = failureNum + 1
        else:
            newRelationship = Relationship(node1,relationshipDic[int(i[2])],node2)
            graph.create(newRelationship)
            succeedNum = succeedNum +1
    holeNum =holeNum + 1




"""提交"""
transaction.commit()
flag = False
print('END:  A'+str(holeNum) +"  S" + str(succeedNum) + "  F" + str(failureNum))
