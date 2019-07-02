import pandas as pd
from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

# We import the database
db = pd.read_csv("db.csv", sep=';', header=0)
# And the reference file.
reffile = open("corpus_text.txt","r",encoding="utf-8")
references = reffile.read().splitlines()
reffile.close()

# We split content in two categories :
# even : preference
# odd : transcript
content = db["content"]
transcripts = []
preferences = []
for i in range(len(content)):
    if i%2:
        # A transcript.
        transcripts.append(content[i])
    else:
        # A preference.
        preferences.append(content[i])
			

# List of sample number in each test.
samples_pre = db["sample index"]
samples = []
# Only half of the indexes are useful.
for i in range(len(samples_pre)):
    if i%2 == 1:
        samples.append(int(samples_pre[i]%40))

# System list.
systems = ["GL100","GL75","GL50","None","PhoneGL0","PhoneGL1"]

# List of systems and their position in each test.
sys1 = [] # System A
sys2 = [] # System B
sys3 = [] # System used for transcription.
sys = db["system index"]
for i in range(len(sys)):
	# System A - System B
	if sys[i] == "SysA":
		# GL100 - GL75
		if samples_pre[i] < 40:
			if i%2 == 0:
				sys1.append("GL100")
				sys2.append("GL75")
			else:
				sys3.append("GL100")
		# GL100 - GL50
		elif samples_pre[i] < 80:
			if i%2 == 0:
				sys1.append("GL100")
				sys2.append("GL50")
			else:
				sys3.append("GL100")
		# GL75 - GL50
		elif samples_pre[i] < 120:
			if i%2 == 0:
				sys1.append("GL75")
				sys2.append("GL50")
			else:
				sys3.append("GL75")
		# Phone GL 0 - Phone GL 1
		elif samples_pre[i] <= 160:
			if i%2 == 0:
				sys1.append("PhoneGL0")
				sys2.append("PhoneGL1")
			else:
				sys3.append("PhoneGL0")
	# System B - System A
	elif sys[i] == "SysB":
		# GL100 - GL75
		if samples_pre[i] < 40:
			if i%2 == 0:
				sys1.append("GL75")
				sys2.append("GL100")
			else:
				sys3.append("GL75")
		# GL100 - GL50
		elif samples_pre[i] < 80:
			if i%2 == 0:
				sys1.append("GL50")
				sys2.append("GL100")
			else:
				sys3.append("GL50")
		# GL75 - GL50
		elif samples_pre[i] < 120:
			if i%2 == 0:
				sys1.append("GL50")
				sys2.append("GL75")
			else:
				sys3.append("GL50")
		elif samples_pre[i] <= 160:
			if i%2 == 0:
				sys1.append("PhoneGL1")
				sys2.append("PhoneGL0")
			else:
				sys3.append("PhoneGL1")

# Preference for all six systems plus the "No Preference" option.
pref_all = OrderedDict()
for system in systems:
	pref_all[system] = 0

# WER for all six systems.
wer_all = OrderedDict()
for system in systems:
	wer_all[system] = []

# Counter for each system encountred.
nbSystem = OrderedDict()
for system in systems:
	nbSystem[system] = 0

# Matrix of signal length/preference.
# Extracts goes from 2 words up to 19 words.
length = []
for i in range(4):
	length.append([0]*len(systems))
	i += 1

# Dictionary of extract length to use with the length/preference matrix.
# Extract length was manually verified.
syslen = {}
syslen[0]=	2
syslen[1]=	4
syslen[2]=	4
syslen[3]=	4
syslen[4]=	6
syslen[5]=	6
syslen[6]=	7
syslen[7]=	8
syslen[8]=	9
syslen[9]=	7
syslen[10]=	9
syslen[11]=	10
syslen[12]=	10
syslen[13]=	10
syslen[14]=	11
syslen[15]=	9
syslen[16]=	9
syslen[17]=	12
syslen[18]=	8
syslen[19]=	12
syslen[20]=	13
syslen[21]=	12
syslen[22]=	11
syslen[23]=	13
syslen[24]=	13
syslen[25]=	14
syslen[26]=	14
syslen[27]=	16
syslen[28]=	16
syslen[29]=	14
syslen[30]=	12
syslen[31]=	16
syslen[32]=	17
syslen[33]=	13
syslen[34]=	16
syslen[35]=	19
syslen[36]=	17
syslen[37]=	19
syslen[38]=	17
syslen[39]=	16

lengroup = []
#lengroup.append((0,1,2,3,4,5,6,9,7,18))
#lengroup.append((8,10,15,16,11,12,13,14,22))
#lengroup.append((17,19,21,30,20,23,24,33,25,26,29))
#lengroup.append((27,28,31,34,39,32,36,38,35,37))
lengroup.append(range(2,9))
lengroup.append(range(9,12))
lengroup.append(range(12,15))
lengroup.append(range(16,20))

# Matrix of system preference.
# To navigate in this matrix, you'll need the systonum dictionary :
perception = []
for system in systems:
	perception.append([0]*len(systems))

# Dictionary to navigate in the preference matrix.
systonum = {}
i = 0
for system in systems:
	systonum[system] = i
	i = i + 1

def wercalc(r, h):
    # initialisation
    import numpy
    d = numpy.zeros((len(r)+1)*(len(h)+1), dtype=numpy.uint8)
    d = d.reshape((len(r)+1, len(h)+1))
    for i in range(len(r)+1):
        for j in range(len(h)+1):
            if i == 0:
                d[0][j] = j
            elif j == 0:
                d[i][0] = i

    # computation
    for i in range(1, len(r)+1):
        for j in range(1, len(h)+1):
            if r[i-1] == h[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                substitution = d[i-1][j-1] + 1
                insertion = d[i][j-1] + 1
                deletion = d[i-1][j] + 1
                d[i][j] = min(substitution, insertion, deletion)

    return d[len(r)][len(h)]

# Add a preference to the length/preference matrix.
def addlength(sample, sys):
	for i in range(len(length)):
		if sample in lengroup[i]:
			length[i][sys] += 1

# At each test, we asked if system 1 was preferred in term of quality, or if it was system 2 or none.
def preferred(preferences, sys1, sys2, samples):
    i = 0
    for c in range(len(preferences)):
		# We note that those two systems were encountred.
        nbSystem[sys1[i]] += 1
        nbSystem[sys2[i]] += 1
        nbSystem["None"] += 1
        # System A was preferred.
        if preferences[c] == '1':
            pref_all[sys1[i]] += 1
            # We add this choice to the preference matrix for the tuple (sys1,sys2).
            # The matrix use numerical indexes so you have to pass the system name through systonum to get its index.
            perception[systonum[sys1[i]]][systonum[sys2[i]]] += 1
            # We add this choice to the length/preference matrix for this sample.
            addlength(syslen[samples[c]%40]-2,systonum[sys1[i]])
        # System B was preferred.
        elif preferences[c] == '2':
            pref_all[sys2[i]] += 1
            perception[systonum[sys2[i]]][systonum[sys1[i]]] += 1
            addlength(syslen[samples[c]%40]-2,systonum[sys2[i]])
        # Neither system was preferred.
        else:
            pref_all["None"] += 1
            perception[systonum["None"]][systonum[sys1[i]]] += 1
            perception[systonum["None"]][systonum[sys2[i]]] += 1
            addlength(syslen[samples[c]%40]-2,systonum["None"])
        i = i + 1
    # We normalize preference to make up if system were not equally tested.
    for system in pref_all.keys():
        if nbSystem[system] != 0:
            pref_all[system] = pref_all[system] / nbSystem[system]

# We calculate Word Error Rate (WER) at each test.
def wer(transcripts, samples, references, sys1):
    for i in range(len(transcripts)):
        # We retrieve the sample number.
        sample = samples[i]
        # We tokenize and lowerize all words.
        transcript = transcripts[i].lower().split(" ")
        reference = references[sample].lower().split(" ")
        wer = wercalc(transcript,reference)/len(reference)
        wer_all[sys1[i]].append(wer)

# Calculate WER average.
def wer_avg(values):
    if not values:
        return -1
    avg = sum(values) / len(values)
    return avg

# Define system rank in order of preference.
def order(dico):
	order = {}
	result = 99999
	c = 0
	for rank in sorted(dico, key=dico.get, reverse=True):
		if dico[rank] < result:
			c += 1
			result = dico[rank]
		order[rank] = c
	order_list = []
	for key in dico.keys():
		order_list.append(order[key])
	return order_list

# Function to make pretty stacked bar plots.
def stacked_bar(data, series_labels, category_labels=None,
				show_values=False, value_format="{}", y_label=None,
				x_label=None, grid=False, reverse=True, label=None):
	"""Plots a stacked bar chart with the data and labels provided.

	Keyword arguments:
	data			-- 2-dimensional numpy array or nested list
					   containing data for each series in rows
	series_labels	-- list of series labels (these appear in
					   the legend)
	category_labels	-- list of category labels (these appear
					   on the x-axis)
	show_values		-- if True then numeric value labels will
					   be shown on each bar
	value_format	-- format string for numeric value labels
					   (default is "{}")
	y_label			-- label for y-axis (str)
	x_label			-- label for x-axis (str)
	grid			-- if True display grid
	reverse			-- if True reverse the order that the
					   series are displayed (left-to-right
					   or right-to-left)
	label			-- text to be written on the bar
	"""

	ny = len(data[0])
	ind = np.arange(ny)

	axes = []
	cum_size = np.zeros(ny)

	data = np.array(data)

	if reverse:
		data = np.flip(data, axis=1)
		category_labels = reversed(category_labels)

	for i, row_data in enumerate(data):
		axes.append(plt.bar(ind, row_data, bottom=cum_size,
							label=series_labels[i]))
		cum_size += row_data
	
	if category_labels:
		bar_width = [bar.get_width() for axis in axes for bar in axis]
		plt.xticks(ind, category_labels)

	if y_label:
		plt.ylabel(y_label)

	if x_label:
		plt.xlabel(x_label)

	plt.legend()

	if grid:
		plt.grid()

	if show_values:
		a = 0
		b = 0
		for axis in axes:
			for bar in axis:
				w, h = bar.get_width(), bar.get_height()
				plt.text(bar.get_x() + w/2, bar.get_y() + h/2,
						 label[a][b%4], ha="center",
						 va="center")
				b += 1
			a += 1


# Main
preferred(preferences,sys1,sys2,samples)
wer(transcripts, samples, references, sys3)
order_list = order({k: pref_all[k] for k in list(pref_all)[:4]})
order_list = order_list + order({k: pref_all[k] for k in list(pref_all)[4:]})

# Print WER for each system.
# Note : a WER of -1 means that the system was never evaluated.
print("WER list :")
for element in wer_all:
	wer_all[element] = wer_avg(wer_all[element])
wer_list = pd.DataFrame(wer_all.items(), columns=["System","WER"])
print(tabulate(wer_list,headers="keys",tablefmt="psql",showindex=False))
print("")

# Print preference for each system.
print("Preference list :")
pref_list = pd.DataFrame(pref_all.items(), columns=["System","Preference"])
pref_list["Rank"] = order_list
pref_list["Number of evaluations"] = nbSystem.values()
print(tabulate(pref_list,headers="keys",tablefmt="psql",showindex=False))
print("")

# Print length/preference matrix.
print("Length/Preference matrix :")
len_list = pd.DataFrame(length,("2<=X<9","9<=X<12","12<=X<14","14<=X<19"),systems)
print(tabulate(len_list,headers="keys",tablefmt="psql"))
print("")

# Print preference matrix.
print("Preference matrix :")
per_list = pd.DataFrame(perception,systems,systems)
print(tabulate(per_list,headers="keys",tablefmt="psql"))
print("")

# Print preference graph.
print("Preference graph in rank.png file.")
plt.figure(figsize=(15, 5))

series_labels = ["Système A", "Pas de préférence", "Système B"]

# On va créer un système qui remplit automatiquement la liste data.
# Pour chaque système (à l'exception de None et du dernier de la liste)
# on va placer
# dans data[0] la valeur perception[sys1][sys2]
# dans data[1] la valeur min(perception[none][sys1],perception[none][sys2])
# dans data[2] la valeur perception[sys2][sys1]
# Les valeurs dans bis permetteront l'affichage dans l'histogramme.
data = [[],[],[]]
bis = [[],[],[]]
for i in range(len(perception)-4):
	for j in range(i,len(perception)-3):
		if i != j:
			scorea = perception[i][j]
			scorenone = min(perception[systonum["None"]][i],perception[systonum["None"]][j])
			scoreb = perception[j][i]
			total = scorea + scoreb + scorenone
			if total == 0:
				total = 1
			data[0].append(scorea/total)
			data[1].append(scorenone/total)
			data[2].append(scoreb/total)
			bis[0].append(scorea)
			bis[1].append(scorenone)
			bis[2].append(scoreb)
# And the same for the Phonetic evaluation.
scorea = perception[4][5]
scorenone = min(perception[systonum["None"]][4],perception[systonum["None"]][5])
scoreb = perception[5][4]
total = scorea + scoreb + scorenone
if total == 0:
	total = 1
data[0].append(scorea/total)
data[1].append(scorenone/total)
data[2].append(scoreb/total)
bis[0].append(scorea)
bis[1].append(scorenone)
bis[2].append(scoreb)

category_labels = ["A=GL100-B=GL75","A=GL100-B=GL50","A=GL75-B=GL50","A=PhoneGL0-B=PhoneGL1"]

stacked_bar(
	data,
	series_labels,
	category_labels=category_labels,
	show_values=True,
	value_format="{:.1f}",
	y_label="Taux de préférence",
	x_label="Système",
	reverse=False,
	label=bis
)

plt.savefig("rank.png")
#plt.show()


# Show length/preference bar chart.
print("Length/preference graph in length.png file.")
length = np.array(length)

ind = np.arange(len(length))  # the x locations for the groups
width = 0.10  # the width of the bars

fig, ax = plt.subplots(figsize=(12,4))
ax.bar(ind - 2.5*width, length[:,0], width, label='GL100')
ax.bar(ind - 1.5*width, length[:,1], width, label='GL75')
ax.bar(ind - 0.5*width, length[:,2], width, label='GL50')
ax.bar(ind + 0.5*width, length[:,3], width, label='Pas de préférence')
ax.bar(ind + 1.5*width, length[:,4], width, label='PhoneGL0')
ax.bar(ind + 2.5*width, length[:,5], width, label='PhoneGL1')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Nombre de fois où le système est préféré')
ax.set_xlabel('Nombre de mots')
ax.set_xticks(ind)
ax.set_xticklabels(("2<=X<9","9<=X<12","12<=X<14","14<=X<19"))
ax.legend()


fig.tight_layout()
plt.savefig("length.png")

plt.show()