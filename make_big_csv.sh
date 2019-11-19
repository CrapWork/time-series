#/bin/bash

curl -o data.tar.gz https://ds.codeup.com/fitbit-data.tar.gz
gunzip data.tar.gz
tar -zxvf data.tar
cd fitbit

awk 'NR==36,NR==67' 2018-04-26_through_2018-05-26.csv > ../blob.csv

#LIST=$(ls /Users/fredricklambuth/Projects/fitbit/fitbitCSVs)
LIST="2018-04-26_through_2018-05-26.csv 2018-05-27_through_2018-06-26.csv 2018-06-27_through_2018-07-27.csv 2018-08-27_through_2018-09-26.csv 2018-09-27_through_2018-10-27.csv 2018-10-28_through-2018-11-27.csv"

for ITEM in $LIST
do
	echo "$ITEM"
	awk 'NR==37,NR==67' $ITEM >> ../blob.csv
done

awk 'NR==37,NR==65' 2018-07-28_through_2018-08-26.csv >> ../blob.csv
awk 'NR==37,NR==45' 2018-11-28_through_2018-12-28.csv >> ../blob.csv

rm ../data.tar