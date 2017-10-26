c_defects=~/work/itc-benchmarks/01.w_Defects/
cpp_defects=~/work/itc-benchmarks/03.w_Defects_Cpp/

all: count-errors gather-errors

count-errors:
	./count-errors-per-file.sh $(c_defects) c_count_errors.csv
	./count-errors-per-file.sh $(cpp_defects) cpp_count_errors.csv

gather-errors:
	./gather-errors-by-line.sh $(c_defects) c_errors_per_line.csv
	./gather-errors-by-line.sh $(c_defects) cpp_error_per_line.csv


clean:
	rm -f *.csv *~ 
