import os
import re
import csv
import math

folder_path_vanilla = '/home/rashid/rackham_results/1cores/L2_TLB_v23/'
#folder_path_treg = '/crex/proj/snic2022-22-557/rashid/results/1cores/TREG_v23/'
#folder_path_rxt = '/home/rashid/rackham_results/1cores/RXT_v23/'
#directory_names = ["cactuBSSN", "lbm", "exchange2", "mcf", "nab", "deepsjeng", "leela","exchange" ,"imagick", "perlbench", "omnetpp", "xalancbmk" , "gcc","bc" ,"bfs", "sssp" ,"pr", "pr_spmv","cc_sv" ,"tc"]
directory_names = ["bc" ,"bfs", "sssp" ,"pr", "pr_spmv","cc","cc_sv" ,"tc"]
csv_file_path = './BP_Motiv.csv'
'''
header = ["Program", "TLB_L1_Cache_L1_miss", "TLB_L1_Cache_L1_hit", "TLB_L1_Cache_L2_miss", "TLB_L1_Cache_L2_hit",
           "TLB_L2_Cache_L1_miss", "TLB_L2_Cache_L1_hit", "TLB_L2_Cache_L2_miss", "TLB_L2_Cache_L2_hit"]
'''
numbers_gmean_vanilla = []
result_1 = []
result_2 = []
result_3 = []
result_4 = []
def calculate_gmean(numbers):
    log_sum = 0
    for num in numbers:
        log_sum += math.log(num)
    gmean = math.exp(log_sum / len(numbers))
    return gmean
'''
with open(csv_file_path, 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header)
'''
for directory_name in directory_names:
    dir_path_vanilla = os.path.join(folder_path_vanilla, directory_name )
    #dir_path_treg = os.path.join(folder_path_treg, directory_name)
    #dir_path_rxt = os.path.join(folder_path_rxt, directory_name )

    txt_file_path_vanilla = os.path.join(dir_path_vanilla, 'stats.txt')
    #txt_file_path_treg = os.path.join(dir_path_treg, 'stats.txt')
    #txt_file_path_rxt = os.path.join(dir_path_rxt, 'stats.txt')
    if os.path.exists(txt_file_path_vanilla):
        with open(txt_file_path_vanilla, 'r') as file_vanilla:
            numbers = []
            ## Access
            total_access_tlb_l1 = 0
            total_access_tlb_l2 = 0
            ## Miss
            tlb_l1_cache_l1_miss = 0
            tlb_l1_cache_l2_miss = 0
            tlb_l2_cache_l1_miss = 0
            tlb_l2_cache_l2_miss = 0
            ## hit
            tlb_l1_cache_l1_hit = 0
            tlb_l1_cache_l2_hit = 0
            tlb_l2_cache_l1_hit = 0
            tlb_l2_cache_l2_hit = 0
            for line_vanilla in file_vanilla:
                ## Miss
                match_tlb_l2_cache_l1_miss = re.search(r"system\.cpu\.mmu\.dtb\.L2TLB_l1_miss\s+(\d+)\s*#", line_vanilla)
                match_tlb_l2_cache_l2_miss = re.search(r"system\.cpu\.mmu\.dtb\.L2TLB_l2_miss\s+(\d+)\s*#", line_vanilla)
                match_tlb_l1_cache_l1_miss = re.search(r"system\.cpu\.mmu\.dtb\.L1TLB_l1_miss\s+(\d+)\s*#", line_vanilla)
                match_tlb_l1_cache_l2_miss = re.search(r"system\.cpu\.mmu\.dtb\.L1TLB_l2_miss\s+(\d+)\s*#", line_vanilla)
                ## Hit
                match_tlb_l2_cache_l1_hit = re.search(r"system\.cpu\.mmu\.dtb\.L2TLB_l1_hit\s+(\d+)\s*#", line_vanilla)
                match_tlb_l2_cache_l2_hit = re.search(r"system\.cpu\.mmu\.dtb\.L2TLB_l2_hit\s+(\d+)\s*#", line_vanilla)
                match_tlb_l1_cache_l1_hit = re.search(r"system\.cpu\.mmu\.dtb\.L1TLB_l1_hit\s+(\d+)\s*#", line_vanilla)
                match_tlb_l1_cache_l2_hit = re.search(r"system\.cpu\.mmu\.dtb\.L1TLB_l2_hit\s+(\d+)\s*#", line_vanilla)

                if match_tlb_l2_cache_l1_miss:
                    tlb_l2_cache_l1_miss = float(match_tlb_l2_cache_l1_miss.group(1))
                    print(str(tlb_l2_cache_l1_miss))
                    #xxxxxx.append((directory_name, tlb_l2_cache_l1_miss))
                if match_tlb_l2_cache_l1_hit:
                    tlb_l2_cache_l1_hit = float(match_tlb_l2_cache_l1_hit.group(1))
                    print(str(tlb_l2_cache_l1_hit))
                    #xxxxxx.append((directory_name, tlb_l2_cache_l1_hit))
                if match_tlb_l2_cache_l2_miss:
                    tlb_l2_cache_l2_miss = float(match_tlb_l2_cache_l2_miss.group(1))
                    print(str(tlb_l2_cache_l2_miss))
                    #xxxxxx.append((directory_name, tlb_l2_cache_l2_miss))
                if match_tlb_l2_cache_l2_hit:
                    tlb_l2_cache_l2_hit = float(match_tlb_l2_cache_l2_hit.group(1))
                    print(str(tlb_l2_cache_l2_hit))
                    #xxxxxx.append((directory_name, tlb_l2_cache_l2_hit))
                if match_tlb_l1_cache_l1_miss:
                    tlb_l1_cache_l1_miss = float(match_tlb_l1_cache_l1_miss.group(1))
                    print(str(tlb_l1_cache_l1_miss))
                    #xxxxxx.append((directory_name, tlb_l1_cache_l1_miss))
                if match_tlb_l1_cache_l1_hit:
                    tlb_l1_cache_l1_hit = float(match_tlb_l1_cache_l1_hit.group(1))
                    print(str(tlb_l1_cache_l1_hit))
                    #xxxxxx.append((directory_name, tlb_l1_cache_l1_hit))
                if match_tlb_l1_cache_l2_miss:
                    tlb_l1_cache_l2_miss = float(match_tlb_l1_cache_l2_miss.group(1))
                    print(str(tlb_l1_cache_l2_miss))
                    #xxxxxx.append((directory_name, tlb_l1_cache_l2_miss))
                if match_tlb_l1_cache_l2_hit:
                    tlb_l1_cache_l2_hit = float(match_tlb_l1_cache_l2_hit.group(1))
                    print(str(tlb_l1_cache_l2_hit))
                    total_access_tlb_l1 = tlb_l1_cache_l1_miss + tlb_l1_cache_l1_hit
                    total_access_tlb_l2 = tlb_l2_cache_l1_miss + tlb_l2_cache_l1_hit
                    
                    result_1.append((directory_name))
                    result_2.append((directory_name))
                    result_3.append((directory_name))
                    result_4.append((directory_name))
                    result_1.append(("L1 TLB Miss/L1 cache"))
                    result_2.append(("L1 TLB Miss/L2 cache"))
                    result_3.append(("L2 TLB Miss/L1 cache"))
                    result_4.append(("L2 TLB Miss/L2 cache"))
                    #L1 TLB L1 Cache
                    result_1.append(float(tlb_l1_cache_l1_miss / total_access_tlb_l1))
                    result_1.append(float(tlb_l1_cache_l1_hit / total_access_tlb_l1))
                    #L1 TLB L2 Cache
                    result_2.append(float(tlb_l1_cache_l2_miss / total_access_tlb_l1))
                    result_2.append(float(tlb_l1_cache_l2_hit / total_access_tlb_l1))
                    #L2 TLB L1 Cache
                    result_3.append(float(tlb_l2_cache_l1_miss / total_access_tlb_l2))
                    result_3.append(float(tlb_l2_cache_l1_hit / total_access_tlb_l2))
                    #L2 TLB L2 Cache
                    result_4.append(float(tlb_l2_cache_l2_miss / total_access_tlb_l2))
                    result_4.append(float(tlb_l2_cache_l2_hit / total_access_tlb_l2))
                    break

            with open(csv_file_path, 'a', newline='') as csv_file:
                #writer = csv.writer(csv_file)
                #combined_data = [directory_name] + result
                #writer = csv.writer(csv_file)
                #writer.writerow([directory_name])
                #writer.writerow(combined_data)
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(result_1)
                csv_writer.writerow(result_2)
                csv_writer.writerow(result_3)
                csv_writer.writerow(result_4)
            result_1=[]
            result_2=[]
            result_3=[]
            result_4=[]

#gmean_result_vanilla = 0
#gmean_result_treg = 0
#gmean_result_rxt = 0
#gmean_result_vanilla = calculate_gmean(numbers_gmean_vanilla)
#gmean_result_treg = calculate_gmean(numbers_gmean_treg)
#gmean_result_rxt = calculate_gmean(numbers_gmean_rxt)
#result.append("GMEAN")
#result.append(gmean_result_vanilla)
#result.append(gmean_result_treg)
#result.append(gmean_result_rxt)
#with open(csv_file_path, 'a', newline='') as csv_file:
#    writer = csv.writer(csv_file)
#    writer.writerow(["GMEAN", gmean_result_vanilla])

