document = open("Sample-Input-2.txt").read()
document = document.split()

worker_count = int(document[0])

job_list = document[1:worker_count+1]

worker_list = []

options_dictionary = {}

for x in range(worker_count+1,(3*worker_count)+1,2):
    worker_list.append(document[x])
    templist = document[x+1].split(",")
    options_dictionary[document[x]] = templist
    


class Worker():
    def __init__(self):
	    self.name = ""
	    self.job = None
	    self.options_list = []
	    
        
    def update_options_count(self):
        self.options_count = len(self.options_list)
        
WorkerClassList = []
for x in range(worker_count):
    WorkerClassList.append(Worker())
    WorkerClassList[x].name = worker_list[x]
    WorkerClassList[x].options_list = options_dictionary[WorkerClassList[x].name]
    WorkerClassList[x].update_options_count()
    

    


def done_assigning():
    for x in range(len(WorkerClassList)):
        if WorkerClassList[x].job == None:
            return False
    return True



TempClassList = WorkerClassList


#print(TempClassList[2].name)
#print(TempClassList[2].options_list)

while not done_assigning():
    TempClassList.sort(key = lambda x: x.options_count)
    #print(TempClassList[0].name)
    #print(TempClassList[0].options_list)
    #print(TempClassList[0].options_count)
    if len(TempClassList[0].options_list) != 0:
    	picked_job = TempClassList[0].options_list[0]
    	
    TempClassList[0].job = picked_job
    
    for x in range(len(WorkerClassList)):
        if WorkerClassList[x].name == TempClassList[0].name:
            WorkerClassList[x].job = picked_job
            print(WorkerClassList[x].name,"=",WorkerClassList[x].job)
    
    #print(WorkerClassList[2].name,WorkerClassList[2].job)
    for x in range(len(TempClassList)):
        if picked_job in TempClassList[x].options_list:
        	TempClassList[x].options_list.remove(picked_job)
        TempClassList[x].update_options_count()
    del TempClassList[0]
    
    
    
    
    


    

