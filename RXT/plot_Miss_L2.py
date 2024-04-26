import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import matplotlib.ticker as ticker
# Read the CSV file
#data = pd.read_csv('Pointer_Chasing_Percentage.csv')
data = np.genfromtxt('L2_Miss.csv',delimiter=',',skip_header=0,usecols=(0,1))

program_names = ["cactuBSSN","lbm", "mcf", "exchange2", "nab", "leela", "imagick", "perlbench", "omnetpp", "xalancbmk", "gcc", "bc" ,"bfs",  "sssp" ,"pr" , "pr_spmv","cc_sv" ,"tc", "GMEAN"]


# Extract the necessary columns
#programs = data.iloc[:, 0]
#baseline = data.iloc[:, 1]

programs = data[:, 0]
baseline = data[:, 1]
#l0tlb = data[:,2]
#selfTrans = data[:, 3]

#approach = data.iloc[:, 2]

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Set custom font
font_path = '/home/rashid/fonts/Merriweather-Regular.ttf'  # Replace with the path to your font file
prop = fm.FontProperties(fname=font_path)

# Set the x-axis positions for the bars
x = np.arange(len(programs))

# Plot the data with a thin black line border
#baseline_plot = ax.bar(x - 0.25 , baseline, label='Baseline', width=0.25, color='#000000', edgecolor='black', linewidth=1,hatch ='///')
l0tlb_plot = ax.bar(x  , baseline, label='T-Reg', width=0.25, color='#b3b0b0', edgecolor='black', linewidth=1,hatch ='//')
#self_plot = ax.bar(x + 0.25, selfTrans, label='RXT', width=0.25, color='#33b24c', edgecolor='black', linewidth=1,hatch = 'xxx')
# Add labels and title with custom fonts
#ax.set_xlabel('Programs', fontproperties=prop, fontsize=20)
ax.set_ylabel('TLB MPKI', fontproperties=prop, fontsize=8)
#ax.set_title('Comparison of Baseline and Our Approach', fontproperties=prop, fontsize=20)


#ax.legend(prop=prop, fontsize=8,loc='upper left')
#plt.ticklabel_format(axis='y')
#ax.legend().get_frame().set_linewidth(2.5)
#for text in ax.legend().get_texts():
#    text.set_fontsize(7)

#legend_bbox_to_anchor = (0.76, 0.83)  # Example: move legend to the upper-right corner
#legend_loc = 'lower left'  # Example: additional positioning based on anchor
#ax.legend(bbox_to_anchor=legend_bbox_to_anchor,fontsize=7, loc=legend_loc,ncol=3)


# Add legend with custom fonts
#ax.legend(prop=prop, fontsize=12)

#ax.legend().get_frame().set_linewidth(2.5)
#for text in ax.legend().get_texts():
#    text.set_fontsize(24)

# Rotate x-axis labels for better readability (optional)
plt.xticks(rotation=45)

# Set the size and thickness of X and Y axis labels
#ax.set_xlabel('Programs', fontproperties=prop, fontsize=30, labelpad=10)

# Adjust y-axis limits (optional)
#ax.set_ylim(0, max(max(baseline), max(approach)) * 1.1)

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)

# Customize tick parameters
ax.tick_params(axis='x', labelsize=80, width=2)
ax.tick_params(axis='y', labelsize=22, width=2)




section_positions = [10.5, 17.5]  # Example positions where you want to mark the sections
#section_labels = ['ASCYLIB', 'SPEC17', 'CRONO']  # Example labels for the sections

section_labels = ['', '', '']  # Example labels for the sections

for position, label in zip(section_positions, section_labels):
    ax.axvline(x=position, color='gray', linestyle='--', linewidth=1)  # Mark the section with a vertical line
    ax.text(position, 4, label, transform=ax.transData, ha='right', va='top', fontsize=12, fontweight='bold')  # Add the section label

bars = ax.bar(range(len(program_names)), baseline, width=0.4, alpha=0, color='#01090b', edgecolor='black', linewidth=1.5)

# Annotate each bar with its value
for bar, value in zip(bars, baseline):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{value:.2f}', ha='center', va='bottom', fontsize=8, color='black')

section_positions = [15.5, 31.5]  # Example positions where you want to mark the sections
#section_labels = ['ASCYLIB', 'SPEC17', 'CRONO']  # Example labels for the sections

section_labels = ['', '', '']  # Example labels for the sections

#for position, label in zip(section_positions, section_labels):
#    ax.axvline(x=position, color='black', linestyle='-', linewidth=3)  # Mark the section with a vertical line
#    ax.text(position, 4, label, transform=ax.transData, ha='right', va='top', fontsize=12, fontweight='bold')  # Add the section label



section_positions = [6,15]  # Example positions where you want to mark the sections
section_labels = ['SPEC 2017', 'GAPBS']  # Example labels for the sections


for position, label in zip(section_positions, section_labels):
    ax.axvline(x=position, color='white', linestyle='', linewidth=4)  # Mark the section with a vertical line
    ax.text(position,115, label, transform=ax.transData, ha='right', va='top', fontsize=12)  # Add the section label


fig = plt.gcf()
fig.set_size_inches(12,1.8)

average = baseline.mean()

# Create the bar chart
#approach_plot = ax.bar(x, baseline, width=0.4, alpha=0.7, color='#01090b', edgecolor='black', linewidth=1.5)

# Display the average value
'''
for i, rect in enumerate(approach_plot):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 1, f'{baseline[i]:.2f}', ha='center', va='bottom', fontproperties=prop, fontsize=12)
   # ax.text(rect.get_x() + rect.get_width() / 2, height / 2, f'Avg: {average:.2f}', ha='center', va='center', fontproperties=prop, fontsize=12, fontweight='bold')
'''
# Apply custom font to program names on x-axis
#plt.xticks(x, programs, fontproperties=prop, fontsize=16)
#plt.xticks(range(len(program_names)),program_names, fontproperties=prop, fontsize=10)
#plt.ylabel("Y-axis", fontproperties=prop)


ax.axhline(y=50, color='grey', linestyle='--',alpha=0.5)
ax.axhline(y=100, color='grey', linestyle='--',alpha=0.5)

plt.xlim(-0.5, len(program_names) - 0.5)
# Apply custom font to program names on x-axis
#plt.xticks(x, programs, fontproperties=prop, fontsize=16)
plt.xticks(range(len(program_names)),program_names, fontproperties=prop, fontsize=9)
#plt.ylabel("Y-axis", fontproperties=prop)
plt.ylim(bottom=0,top=102)
plt.yticks([0,20,40, 60, 80,100])
plt.yticks(fontproperties=prop, fontsize=10)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: f'{y*1:.0f}'))
# Save the plot as an image or display it
plt.tight_layout()
plt.savefig('fig_Miss_L2.pdf',format='pdf',bbox_inches='tight', dpi=300)
#plt.show()

