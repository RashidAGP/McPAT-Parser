import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import matplotlib.ticker as ticker
data = np.genfromtxt('power_density_results.csv',delimiter=',',skip_header=0,usecols=(0,1,2,3,4,5))

program_names = ["cactuBSSN", "exchange2", "gcc", "imagick", "lbm" ,"leela", "mcf", "nab", "omnetpp","perlbench","xalancbmk", "crono_cc", "crono_sssp", "crono_tsp", "XSB", "bfs","cc" ,"cc_sv","pr", "pr_spmv", "sssp", "tc"]

programs = data[:, 0]
IFU = data[:, 1]
RU = data[:,2]
LSU = data[:,3]
MMU = data[:,4]
EXE = data[:,5]
fig, ax = plt.subplots(figsize=(10, 6))
font_path = '/home/rashid/fonts/Merriweather-Regular.ttf'  # Replace with the path to your font file
prop = fm.FontProperties(fname=font_path)

x = np.arange(len(programs))
width = 0.15 
ifu_plot = ax.bar(x - 2 * width , IFU, label='IFU', width=width, color='#c6c6e1', edgecolor='black', linewidth=1,hatch ='///')
ru_plot = ax.bar(x - width , RU, label='RU', width=width, color='#b0b8ce', edgecolor='black', linewidth=1,hatch ='o')
lsu_plot = ax.bar(x  , LSU, label='LSU', width=width, color='#505a74', edgecolor='black', linewidth=1,hatch ='x')
mmu_plot = ax.bar(x + width , MMU, label='MMU', width=width, color='#022954', edgecolor='black', linewidth=1,hatch ='\\')
exe_plot = ax.bar(x + 2 * width , EXE, label='EXE', width=width, color='#354c7c', edgecolor='black', linewidth=1,hatch ='*')
ax.set_ylabel('Power density', fontproperties=prop, fontsize=12)
plt.xticks(rotation=45)


ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)

# Customize tick parameters
ax.tick_params(axis='x', labelsize=80, width=2)
ax.tick_params(axis='y', labelsize=42, width=2)




section_positions = [10.5, 13.5, 14.5,21.5]  # Example positions where you want to mark the sections

section_labels = ['', '', '', '']  # Example labels for the sections

for position, label in zip(section_positions, section_labels):
    ax.axvline(x=position, color='gray', linestyle='--', linewidth=1)  # Mark the section with a vertical line
    ax.text(position, 4, label, transform=ax.transData, ha='right', va='top', fontsize=12, fontweight='bold')  # Add the section label

#bars = ax.bar(range(len(program_names)), l0tlb, width=0.4, alpha=0, color='#01090b', edgecolor='black', linewidth=1.5)

# Annotate each bar with its value

section_positions = [5.5,12.5,14.25,18.5]  # Example positions where you want to mark the sections
section_labels = ['SPEC 2017','CRONO', 'XSB','GAPBS']  # Example labels for the sections

for position, label in zip(section_positions, section_labels):
    if label == 'XSB':
        ax.axvline(x=position, color='white', linestyle='', linewidth=4)  # Mark the section with a vertical line
        #ax.text(position, 103, label, transform=ax.transData, ha='right', va='top', fontsize=11, rotation=90)  # Display vertically
        ax.text(position, 2, label, transform=ax.transData, ha='right', va='top', fontsize=11)  # Display vertically
    else:
        ax.axvline(x=position, color='white', linestyle='', linewidth=4)  # Mark the section with a vertical line
        ax.text(position, 2, label, transform=ax.transData, ha='right', va='top', fontsize=11)  # Display horizontally



fig = plt.gcf()
fig.set_size_inches(12,2.5)

#average = baseline.mean()


ax.axhline(y=1, color='grey', linestyle='--',alpha=0.5)
ax.axhline(y=0.1, color='grey', linestyle='--',alpha=0.5)
ax.axhline(y=0.01, color='grey', linestyle='--',alpha=0.5)
ax.legend(loc='lower left',ncol =5)
plt.xlim(-0.5, len(program_names) - 0.5)
plt.xticks(range(len(program_names)),program_names, fontproperties=prop, fontsize=9)
plt.ylim(bottom=0,top=10)
ax.set_yscale('log')
ax.set_ylim(0.001, 2)
plt.yticks(fontproperties=prop, fontsize=10)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: f'{y*1:.3f}'))
plt.tight_layout()
plt.savefig('power_density.pdf',format='pdf', dpi=300)
plt.show()

