import os
import re
import csv
import math

folder_path_vanilla = '/home/rashid/rashid_rackham/results/1cores/L2_TLB_v23/'
folder_path_rxt = '/home/rashid/rashid_rackham/results/1cores/RXT_v23/'
directory_names = ["cactuBSSN", "exchange2", "gcc", "imagick", "lbm" ,"leela", "mcf", "nab", "omnetpp","perlbench","xalancbmk", "crono_apsp", "crono_cc", "crono_sssp","crono_tc", "crono_tsp", "crono_XSBench", "bfs","cc" ,"cc_sv","pr", "pr_spmv", "sssp", "tc"]

csv_file_path = './TLB_L1_miss_ratio.csv'

numbers = []
numbers_gmean_vanilla = []
numbers_gmean_treg = []
numbers_gmean_rxt = []
result = []
def calculate_gmean(numbers):
    log_sum = 0
    for num in numbers:
        log_sum += math.log(num)
    gmean = math.exp(log_sum / len(numbers))
    return gmean


for directory_name in directory_names:
    dir_path_vanilla = os.path.join(folder_path_vanilla, directory_name  )
    #dir_path_treg = os.path.join(folder_path_treg, directory_name)
    #dir_path_rxt = os.path.join(folder_path_rxt, directory_name )

    txt_file_path_vanilla = os.path.join(dir_path_vanilla, 'stats.txt')
    #txt_file_path_treg = os.path.join(dir_path_treg, 'stats.txt')
    #txt_file_path_rxt = os.path.join(dir_path_rxt, 'stats.txt')
    if os.path.exists(txt_file_path_vanilla):
        with open(txt_file_path_vanilla, 'r') as file_vanilla:
            numbers = []
            number_vanilla = 0
            number_vanilla_access = 0
            for line_vanilla in file_vanilla:
                match_vanilla = re.search(r"system\.cpu\.mmu\.dtb\.rdMisses\s+(\d+)\s*#", line_vanilla)
                match_vanilla_access = re.search(r"system\.cpu\.mmu\.dtb\.rdAccesses\s+(\d+)\s*#", line_vanilla)
                if match_vanilla_access:
                    number_vanilla_access = float(match_vanilla_access.group(1))
                    print(str(number_vanilla_access))
                    numbers.append((directory_name, number_vanilla))
                if match_vanilla:
                    number_vanilla = float(match_vanilla.group(1))
                    print(str(number_vanilla))
                    tlb_miss_ratio = float(number_vanilla/number_vanilla_access)* 100
                    result.append((directory_name,tlb_miss_ratio))
                    numbers_gmean_vanilla.append(float((number_vanilla / number_vanilla_access)* 100))
                    print(str(result))
                    break

            with open(csv_file_path, 'w', newline='') as csv_file:
                #writer = csv.writer(csv_file)
                #combined_data = [directory_name] + result
                #writer = csv.writer(csv_file)
                #writer.writerow([directory_name])
                #writer.writerow(combined_data)
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(result)
'''
gmean_result_vanilla = 0
#gmean_result_treg = 0
gmean_result_rxt = 0
gmean_result_vanilla = calculate_gmean(numbers_gmean_vanilla)
#gmean_result_treg = calculate_gmean(numbers_gmean_treg)
#gmean_result_rxt = calculate_gmean(numbers_gmean_rxt)
result.append("GMEAN")
result.append(gmean_result_vanilla)
#result.append(gmean_result_treg)
#result.append(gmean_result_rxt)
with open(csv_file_path, 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["GMEAN", gmean_result_vanilla])
'''
