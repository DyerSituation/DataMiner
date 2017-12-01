a:
Project 3 group 13

Erik Dyer, ead2174
Sarina Xie, sx2166

b:
datamining.py
NYC_Death_Causes.csv
README.md
example-run.txt

c: Run:

python datamining.py (path/to/datasetfile.scv) min_supp min_conf > output.txt

where min_supp is the minimum support and min_conf is the minimum confidence, both in decimal form. 

d:
(a) We used only the New York City Leading Causes of Death Data set
(b) We exported the file to CSV, then removed columns that contained only numerical data (years, death numbers, death rate, adjusted death rate) from the CSV file. 
(c) The health and wellbeing of its citizens should be at the top of any government's priorty list, and one way to monitor this is by analyzing the data on the leading causes of deaths. Analysing this dataset for association rules will show which demographic groups are being affected by which causes of death. Rules where certain causes are disproportionately affecting different groups (of which there are many) should be investigated, as they may be signs of areas where the government could further protect the health of its citizens

e:
The csv file is read into a list of lists. Each row corresponds to a sublist and is in the form ['column#-cell value', 'column#-cellvalue', ...]

Then the apriori algorithm described in section 2.1.1 of the Agrawal and Srikant paper is implemented.

First the itemset where k=1 is created outside of the main generative while loop*. It is created by adding every unique string in the list of lists into a list, and then removing the items that have less than the minimum support.
*It was put outside the loop because the end result is a list of strings as opposed to a list of lists.

Then, in the while loop:
1. A list of k+1 itemsets are generated from a list of frequent k itemsets.
2. The frequency of each k+1 itemset is found.
3. The k+1 itemsets that have less than the minimum support are removed.
   The k+1 itemsets that have more than the minimum support are recorded in frequentsets and their frequences are recorded in freqfreqs.
When there are no more frequent k+1 itemsets we break out of the while loop.

The association rules are created by going through each itemset [a, b, c] and creating every combination [a, b] -> c | [a, c] -> b | [b, c] -> a by popping one element off of [a, b, c], recording the rule, and adding the popped element back.

f:
python datamining.py NYC_Death_Causes.csv .01 .5 > output.txt
There is all sorts of alarming info that you can glean fromt the results. Ex: while Alzheimer's disease affects twice as many women as men, 96% of Alzheimer's related deaths in NYC are women. Another, not as surprising but still important observation: 85% of homicide victims are men. This gives us a glimps into the potentiall issues being faced in the city.

g:
We chose to write our output from the commandline instead of from within the python script. We thought this was more useful, as it is more flexible in allowing the user to choose how they see the data and where it gets stored. 



