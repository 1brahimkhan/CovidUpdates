import os
csv_header = 'Timestamp,Client IP,Web Service,Status,Good,Bad'
csv_out = 'SampleOutputDirectory/20191101.csv'
csv_dir = "SampleInputDirectory/20191101"
csv_header="Timestamp,Last,LastSize,TotalVolume,Bid,Ask,TickId,BasisForLast,TradeMarketCenter,TradeConditions"
temp_csv_updated_header =(csv_header+"Symbol","ExpiryDates","OpionsType","StrikePriority")
csv_updated_header = str(temp_csv_updated_header)


dir_tree = os.walk(csv_dir)
for dirpath, dirnames, filenames in dir_tree:
   pass

csv_list = []
for file in filenames:
   if file.endswith('.csv'):
      csv_list.append(file)

csv_merge = open(csv_out, 'w')
csv_merge.write(csv_updated_header)
csv_merge.write('\n')

for file in csv_list:
   new = str(csv_dir+"/"+file)
   csv_in = open(new)
   for line in csv_in:
      SplitString = file.split(" ")
      Date =  str(SplitString[1]+" "+SplitString[2]+" "+SplitString[3])
      if line.startswith(csv_header):
         continue
      temp = str([SplitString[0],Date,SplitString[4],SplitString[5],line])
      csv_merge.write(temp)
   csv_in.close()
csv_merge.close()
print('CSV file : ' + csv_out)