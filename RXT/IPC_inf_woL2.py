import os
import re
import csv
import math

folder_path_vanilla = '/home/rashid/rackham_results/1cores/L2_TLB_v23/'
folder_path_rxt = '/home/rashid/rackham_results/1cores/RXT_v23/'
directory_names = ["cactuBSSN", "lbm", "mcf", "exchange2", "nab","leela", "deepsjeng", "exchange" ,"imagick", "perlbench","omnetpp", "xalancbmk", "gcc" ,"bc" ,"bfs", "sssp" ,"pr", "pr_spmv","cc_sv" ,"tc"]
csv_file_path = './IPC_inf_woL2.csv'

numbers = []
numbers_gmean_vanilla = []
numbers_gmean_rxt = []
#numbers_gmean_rxt_50e = []
#numbers_gmean_rxt_100e = []
#numbers_gmean_rxt_pop = []

def calculate_gmean(numbers):
    log_sum = 0
    for num in numbers:
        log_sum += math.log(num)
    gmean = math.exp(log_sum / len(numbers))
    return gmean


for directory_name in directory_names:
    dir_path_vanilla = os.path.join(folder_path_vanilla, directory_name + "_raw_woL2" )
    dir_path_rxt = os.path.join(folder_path_rxt, directory_name + "_inf_woL2" )

    txt_file_path_vanilla = os.path.join(dir_path_vanilla, 'stats.txt')
    txt_file_path_rxt = os.path.join(dir_path_rxt, 'stats.txt')
    if os.path.exists(txt_file_path_vanilla) and  os.path.exists(txt_file_path_rxt):
        with open(txt_file_path_vanilla, 'r') as file_vanilla,  open (txt_file_path_rxt,'r') as file_rxt:
            numbers = []
            for line_vanilla in file_vanilla:
                match_vanilla = re.search(r"system\.cpu\.commitStats0\.ipc\s+(\d+\.\d+)\s*#", line_vanilla)
                if match_vanilla:
                    number_vanilla = float(match_vanilla.group(1))
                    numbers.append((directory_name, number_vanilla))
                    #numbers_gmean_self.append(number_self)
            
            for line_rxt in file_rxt:
                match_rxt = re.search(r"system\.cpu\.commitStats0\.ipc\s+(\d+\.\d+)\s*#", line_rxt)
                if match_rxt:
                            number_rxt = float(match_rxt.group(1))
                            result = []
                            
                            result.append(float(number_vanilla/number_vanilla)*100)
                            result.append(float(number_rxt/number_vanilla)*100)
                            numbers_gmean_vanilla.append(float(number_vanilla/number_vanilla)*100)
                            numbers_gmean_rxt.append(float(number_rxt/number_vanilla)*100)
                            break

            with open(csv_file_path, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                combined_data = [directory_name] + result
                #writer = csv.writer(csv_file)
                #writer.writerow([directory_name])
                writer.writerow(combined_data)

result = []
gmean_result_vanilla = 0
gmean_result_rxt = 0
gmean_result_vanilla = calculate_gmean(numbers_gmean_vanilla)
gmean_result_rxt = calculate_gmean(numbers_gmean_rxt)
result.append("GMEAN")
result.append(gmean_result_vanilla)
result.append(gmean_result_rxt)
with open(csv_file_path, 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["GMEAN", gmean_result_vanilla,gmean_result_rxt])

