import os
import re
import csv
import math

folder_path_vanilla = '/home/rashid/UAC/'
folder_path_rxt = '/home/rashid/rackham_results/1cores/RXT_v23/'
directory_names = ["bc" ,"bfs","cc" ,"pr", "sssp" ,"tc"]
csv_file_path = './cache_miss.csv'

numbers_hit = []
numbers_miss = []
numbers_access = []
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
    dir_path_vanilla = os.path.join(folder_path_vanilla, directory_name + "_raw/" )

    txt_file_path_vanilla = os.path.join(dir_path_vanilla, 'stats.txt')
    if os.path.exists(txt_file_path_vanilla):
        with open(txt_file_path_vanilla, 'r') as file_vanilla:
            numbers = []
            for line_vanilla in file_vanilla:
                match_hit = re.search(r"system\.ruby\.l2_cntrl0\.L2cache\.m_demand_hits\s+(\d+)\s*#", line_vanilla)
                match_miss = re.search(r"system\.ruby\.l2_cntrl0\.L2cache\.m_demand_misses\s+(\d+)\s*#", line_vanilla)
                match_accesses = re.search(r"system\.ruby\.l2_cntrl0\.L2cache\.m_demand_accesses\s+(\d+)\s*#", line_vanilla)
                if match_hit:
                    number_hit = float(match_hit.group(1))
                    numbers_hit.append((directory_name, number_hit))
                    print(str(number_hit))
                    #numbers_gmean_self.append(number_self)
                if match_miss:
                    number_miss = float(match_miss.group(1))
                    numbers_miss.append((directory_name, number_miss))
                    #numbers_gmean_self.append(number_self)
                if match_accesses:
                    number_access = float(match_accesses.group(1))
                    numbers_access.append((directory_name, number_access))
            with open(csv_file_path, 'a', newline='') as csv_file:
                combined_data = []
                combined_data.append(directory_name)
                combined_data.append(float(number_miss/number_access)* 100)
                combined_data.append(float(number_miss/100000))
                writer = csv.writer(csv_file)
                writer.writerow(combined_data)
'''
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
'''
