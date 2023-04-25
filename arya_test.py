import os
import re
import statistics
import sys

import json

print("Loading Tests: ",sys.argv[1])

with open(sys.argv[1], 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)
tests = json_object
print(tests)

arg_vals = tests["SamplingCounts"]

depth = 1

def gen_args(depth):
    if(depth == 0):
        return [[]]
    
    output = []
    for i in gen_args(depth-1):
        for j in arg_vals:
            new_item = i[:]
            new_item.append(j)
            output.append(new_item)
    
    return output

threads = tests["Threads"]
def run_tests(testname, program, graph_name, pattern, base = False):
    results = {}
    for i in gen_args(depth):
        print(f"mpirun -n 4 ./{program} {graph_name} {pattern} {i[0]} {threads[0]} 4")
        var = os.popen(f"mpirun -n 4 {program} {graph_name} {pattern} {i[0]} {threads[0]} 4").read() 
        m = re.findall('([0-9e\+.]+) ([0-9e\+.]+) ([0-9e\+.]+) ([0-9e\+.]+)', var)

        if (base):
            results[" ".join(i)] = [[float(time) / 1000000 for count,time,i,j in m], [abs(base - float(count)) / base for count,time,i,j in m]]
        else:
            results[" ".join(i)] = [[float(time) / 1000000 for count,time,i,j in m], [float(count) for count,time,i,j in m]]
        
    
    output = []
    for k in results:
        if(base):
            output.append({"args": k, "error": statistics.mean(results[k][1]), "time": statistics.mean(results[k][0])})
        else:
            output.append({"args": k, "avg_count": statistics.mean(results[k][1]), "time": statistics.mean(results[k][0])})

    output = sorted(output, key=lambda d: float(d['args'])) 

    with open(f"{testname}.json", "w") as outfile:
        outfile.write(json.dumps(output))


for t in tests["Tests"]:
    run_tests(t["TestName"], t["AlgPath"],t["GraphPath"], t["PatternPath"])





