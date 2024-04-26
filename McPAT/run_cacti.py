import os

# List of subdirectories
root = "/home/rashid/rashid_rackham/results/1cores/L2_TLB_v23/"
#root = "/home/rashid/extract_data/McPAT/"
subdirectories = ["cactuBSSN","exchange2", "gcc", "imagick","lbm","leela", "mcf","nab","omnetpp","perlbench","xalancbmk", "crono_cc", "crono_sssp","crono_apsp", "crono_tsp","crono_XSBench","bfs","cc","cc_sv","pr", "pr_spmv","sssp","tc"]  # Add your subdirectories here

#subdirectories = ["cactuBSSN"]  # Add your subdirectories here
# Command to run
command_to_run = "/home/rashid/mcpat/mcpat -infile "

# Function to run command in each subdirectory
def run_command_in_subdirectories(subdirectories, command_to_run):
    for subdir in subdirectories:
        # Change directory to the subdirectory
        os.chdir(root + subdir)
        xml_file = root + subdir + "/"
        command = command_to_run + xml_file + "out.xml > McPat.txt"
        print("command is " + str(command))
        # Run the command
        os.system(command)
        print(str("Prgram :") + str(subdir) + " finished") 
        # Change directory back to the parent directory
        os.chdir("..")

# Call the function
run_command_in_subdirectories(subdirectories, command_to_run)

