all: count-errors gather-errors

count-errors:
	./count-errors-per-file.sh ~/work/itc-benchmarks/01.w_Defects/ c_count_errors.csv
	./count-errors-per-file.sh ~/work/itc-benchmarks/03.w_Defects_Cpp/ cpp_count_errors.csv

gather-errors:
	./gather-errors-by-line.sh ~/work/itc-benchmarks/01.w_Defects/ c_errors_per_line.csv
	./gather-errors-by-line.sh ~/work/itc-benchmarks/03.w_Defects_Cpp/ cpp_error_per_line.csv
