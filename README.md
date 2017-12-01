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

python datamining.py (path/to/datasetfile.scv) min_supp min_conf

where min_supp is the minimum support and min_conf is the minimum confidence, both in decimal form. 

d:
(a) We used only the New York City Leading Causes of Death Data set
(b) We exported the file to CSV, then removed columns that contained only numerical data (years, death numbers, death rate, adjusted death rate) from the CSV file. 
(c) The health and wellbeing of its citizens should be at the top of any government's priorty list, and one way to monitor this is by analyzing the data on the leading causes of deaths. Analysing this dataset for association rules will show which demographic groups are being affected by which causes of death. Rules where certain causes are disproportionately affecting different groups (of which there are many) should be investigated, as they may be signs of areas where the government could further protect the health of its citizens

e:

f:
python datamining.py NYC_Death_Causes.csv .01 .5 
There is all sorts of alarming info that you can glean fromt the results. Ex: while Alzheimer's disease affects twice as many women as men, 96% of Alzheimer's related deaths in NYC are women. Another, not as surprising but still important observation: 85% of homicide victims are men. This gives us a glimps into the potentiall issues being faced in the city.



