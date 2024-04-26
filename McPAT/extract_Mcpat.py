import os
import csv
# List of subdirectories
root = "/home/rashid/rashid_rackham/results/1cores/L2_TLB_v23/"
#root = "/home/rashid/extract_data/McPAT/"
benchmarks = ["cactuBSSN","exchange2", "gcc", "imagick","lbm","leela", "mcf","nab","omnetpp","perlbench","xalancbmk", "crono_cc", "crono_sssp","crono_apsp", "crono_tsp","crono_XSBench","bfs","cc","cc_sv","pr", "pr_spmv","sssp","tc"]  # Add your subdirectories here

benchmarks = ["cactuBSSN","exchange2", "gcc", "imagick","lbm","leela", "mcf","nab","omnetpp","perlbench","xalancbmk", "crono_cc", "crono_sssp", "crono_tsp","crono_XSBench","bfs","cc","cc_sv","pr", "pr_spmv","sssp","tc"]  # Add your subdirectories here
#subdirectories = ["cactuBSSN"]  # Add your subdirectories here


file_name = "McPat.txt"
IFU_area =[]
RU_area = []
LSQ_area = []
MMU_area = []
EXE_area = []


IFU_dyn =[]
RU_dyn = []
LSQ_dyn = []
MMU_dyn = []
EXE_dyn = []
area = []
dyn = []
def extract_McPAT (benchmark_name):
    area = []
    dyn = []
    with open(root + benchmark_name + "/" + file_name, "r") as file:
        roi = False
        ifu = False
        ru = False
        lsu = False
        mmu = False
        exe = False
        for line in file:
            # Do something with each line
            if "Core:" in line:
                print("Enter ROI ")
                roi = True
            if roi == True:
                if "Instruction Fetch Unit:" in line:
                    ifu = True
                if "Renaming Unit:" in line:
                    ru = True
                if "Load Store Unit:" in line:
                    lsu = True
                if "Memory Management Unit:" in line:
                    mmu = True
                if "Execution Unit:" in line:
                    exe = True
    
    ####################################################
                if ifu == True:
                    if "Area = " in line:
                        parts = line.split()
                        area.append(float(parts[-2]))
                    if "Runtime Dynamic = " in line:
                        parts = line.split()
                        dyn.append(float(parts[-2]))
                        ifu = False
                elif ru == True:
                    if "Area = " in line:
                        parts = line.split()
                        area.append(float(parts[-2]))
                    if "Runtime Dynamic = " in line:
                        parts = line.split()
                        dyn.append(float(parts[-2]))
                        ru = False
                elif lsu == True:
                    if "Area = " in line:
                        parts = line.split()
                        area.append(float(parts[-2]))
                    if "Runtime Dynamic = " in line:
                        parts = line.split()
                        dyn.append(float(parts[-2]))
                        lsu= False
                elif mmu == True:
                    if "Area = " in line:
                        parts = line.split()
                        area.append(float(parts[-2]))
                    if "Runtime Dynamic = " in line:
                        parts = line.split()
                        dyn.append(float(parts[-2]))
                        mmu = False 
                elif exe == True:
                    if "Area = " in line:
                        parts = line.split()
                        area.append(float(parts[-2]))
                    if "Runtime Dynamic = " in line:
                        parts = line.split()
                        dyn.append(float(parts[-2]))
                        exe = False
                        roi == False
                        print("Exiting ROI")
                        return area,dyn



data_area = {}
data_dyn = {}

for benchmark in benchmarks:
    print("Running " + str(benchmark))
    area, dyn = extract_McPAT(benchmark)
    print("====")
    print("DYN " + str(dyn))
    print("AREA " + str(area))
    data_area[benchmark]= area
    data_dyn[benchmark]= dyn
print("AREA : ")
print(str(data_area))
print("PPWER : ")
print(str(data_dyn))
file_name = "./power_results.csv"

with open (file_name, mode='w', newline='') as file:
    writer =csv.writer(file)
    for key, values in data_dyn.items():
        row = [key] + values
        writer.writerow(row)

print("CSV written was finished")

file_name = "./power_density_results.csv"
power_density = {}
power_density_list =[]

for key_area, values_area in data_area.items():
    dyn_list = data_dyn[key_area]
    #print("DYN " + str(dyn_list))
    #print("values area " + str(values_area))
    results =[x / y for x, y in zip(dyn_list,values_area)]
    print(str(results))
    #print("=========")
    print(str(key_area))
    power_density[key_area]= results


#print(str(power_density))
with open (file_name, mode='w', newline='') as file:
    writer =csv.writer(file)
    for key, value in power_density.items():
        writer.writerow([key] +value)


