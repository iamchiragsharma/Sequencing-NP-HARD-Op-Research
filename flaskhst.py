from flask import Flask,render_template
import pandas as pd
import copy
from operator import itemgetter
import csv

app = Flask(__name__)

@app.route("/")
def hello():
    p_d = pd.read_csv('dummydata.csv')
    data_raw = p_d.values.tolist()
    data = list(map(list,zip(*data_raw)))
    data.pop(0)
    i = 0
    for d in data:
        d.insert(0,i)
        i=i+1

    print(data)

    df = pd.DataFrame(data,columns=['Unsorted Job','Units per Job','MachineA','MachineB','MachineC'])
    df.set_index('Unsorted Job')
    df_trace = df[['MachineA','MachineB','MachineC']]
    df_final = df_trace.transpose()
    df_final.columns  = ['Job: '+ str(i) for i in range(len(data))]
    cols = ['Job: '+ str(i) for i in range(len(data))]
    df_final

    def finding_lowest_by_job(jobData):
        data_min = [[j[0],min(j[2],j[3],j[4])] for j in jobData]
        return data_min

    order = []
    dataCopy = copy.deepcopy(data)
    i=0
    while dataCopy:
        machineA = [[d[0],d[2]] for d in dataCopy]
        machineB = [[d[0],d[3]] for d in dataCopy]
        machineC = [[d[0],d[4]] for d in dataCopy]
        minA_value = min(machineA,key=itemgetter(1))
        minB_value = min(machineB,key=itemgetter(1))
        minC_value = min(machineC,key=itemgetter(1))
        min_job_values = finding_lowest_by_job(dataCopy)
        min_job = min(min_job_values,key=itemgetter(1))
        if min_job == minA_value:
            x = [d for d in dataCopy if d[0] == minA_value[0] and d[2] == minA_value[1]]
        elif min_job == minB_value:
            x = [d for d in dataCopy if d[0] == minB_value[0] and d[3] == minB_value[1]]
        elif min_job == minC_value:
            x= [d for d in dataCopy if d[0] == minC_value[0] and d[4] == minC_value[1]]
        else:
            pass
        order.append(x[0])
        dataCopy.remove(x[0])
    print(order)

    #final_seq = sorted(data1, key=itemgetter(1))
    #final_seq = [[3, 1, 8, 10], [2, 1, 16, 15], [1, 1, 13, 9], [4, 1, 10, 9], [5, 1, 15, 9]]
    final_seq = order
    dict_time = {'time_A': [], 'time_B': [], 'time_C': []}
    idle_time = {'idle_timeB' : [], 'idle_timeC' : []}
    flag = 0
    for i in range(len(final_seq)):
        for j in range(int(final_seq[i][1])):
            if flag == 0:
                idle_time['idle_timeB'].append(final_seq[0][2])
                idle_time['idle_timeC'].append(final_seq[0][2] + final_seq[0][3])
                dict_time['time_A'].append(final_seq[0][2])
                dict_time['time_B'].append(final_seq[0][2] + final_seq[0][3])
                dict_time['time_C'].append(final_seq[0][2]+ final_seq[0][3]+ final_seq[0][4])
                flag = 1
            else:
                dict_time['time_A'].append(dict_time['time_A'][-1] + final_seq[i][2])
                if dict_time['time_A'][-1] > dict_time['time_B'][-1]:
                    idle_time['idle_timeB'].append(dict_time['time_A'][-1] - dict_time['time_B'][-1])
                    dict_time['time_B'].append(dict_time['time_A'][-1] + final_seq[i][3])
                else:
                    dict_time['time_B'].append(dict_time['time_B'][-1] + final_seq[i][3])
                    idle_time['idle_timeB'].append('_')
                
                if dict_time['time_B'][-1] > dict_time['time_C'][-1]:
                    idle_time['idle_timeC'].append(dict_time['time_B'][-1] - dict_time['time_C'][-1])
                    dict_time['time_C'].append(dict_time['time_B'][-1] + final_seq[i][4])
                else:
                    dict_time['time_C'].append(dict_time['time_C'][-1] + final_seq[i][4])
                    idle_time['idle_timeC'].append('_')
                    
    print("Time For Machine A:", end=" ")
    print(dict_time['time_A'])
    print("Time for Machine B(Dependency on A):", end=" ")
    print(dict_time['time_B'])
    print("Time for Machine C(Dependency on B):", end=" ")
    print(dict_time['time_C'])
    print(idle_time['idle_timeB'])
    print(idle_time['idle_timeC'])
    final_vals = [[dict_time['time_A'][i],dict_time['time_B'][i],dict_time['time_C'][i]] for i in range(len(dict_time['time_A']))]
    return render_template(
    'test.html',vals = final_vals,mystring = "Sorted Data")

if __name__ == "__main__":
    app.run()