## Location of ITC workbench: this should be modified by need
W_C_DEFECTS_DIR=~/work/itc-benchmarks/01.w_Defects/
W_CPP_DEFECTS_DIR=~/work/itc-benchmarks/03.w_Defects_Cpp/

WO_C_DEFECTS_DIR=~/work/itc-benchmarks/02.wo_Defects/
WO_CPP_DEFECTS_DIR=~/work/itc-benchmarks/04.wo_Defects_Cpp/



## MAIN SCRIPTS to run
COUNT_ERRORS=./count-errors-per-file.sh
GATHER_ERRORS=./gather-errors-by-line.sh
MERGE_EXE=./merge-csv.sh

## Output files
# COUNT ALL ERRORS
C_COUNT_ERROR_FILE=c_count_errors.csv
CPP_COUNT_ERROR_FILE=cpp_count_errors.csv

# GATHER ERRORS FORM ITC BENCHMARK  PER LINE
C_ERRORS_PER_LINE_FILE=c_errors_per_line.csv
CPP_ERRORS_PER_LINE_FILE=cpp_errors_per_line.csv
C_WO_ERRORS_PER_LINE_FILE=c_wo_errors_per_line.csv
CPP_WO_ERRORS_PER_LINE_FILE=cpp_wo_errors_per_line.csv

# MERGE FILES 
C_MERGE_FILE=c_merge_file.csv
CPP_MERGE_FILE=cpp_merge_file.csv





## Tools configurations

## CLANG
# CLANG=./clang.sh
# CLANG_EXE=/usr/bin/clang
# CLANG_OUTPUT=clang_c_errors_per_line.csv
# CLANG_OPTS="-cc1 -analyze -analyzer-checker=core"

## CPPCHECK
CPPCHECK=./cppcheck.sh
CPPCHECK_EXE=/usr/local/bin/cppcheck
CPPCHECK_OUTPUT_C_W=cppcheck_c_w_errors_per_line.csv
CPPCHECK_OUTPUT_C_WO=cppcheck_c_wo_errors_per_line.csv
CPPCHECK_OUTPUT_CPP_W=cppcheck_cpp_w_errors_per_line.csv
CPPCHECK_OUTPUT_CPP_WO=cppcheck_cpp_wo_errors_per_line.csv
CPPCHECK_OPTS="--xml --xml-version=2"
CPPCHECK_OUT_SUBDEFECTS=cppcheck_out_subdefects.csv
CPPCHECK_OUT_DEFECTS=cppcheck_out_defects.csv
CPPCHECK_OUT_TOTAL=cppcheck_out_total.csv


## FLAWFINDER
FLAWFINDER=./flawfinder.sh
FLAWFINDER_EXE=/usr/local/bin/flawfinder
FLAWFINDER_OUTPUT_C_W=flawfinder_c_w_errors_per_line.csv
FLAWFINDER_OUTPUT_C_WO=flawfinder_c_wo_errors_per_line.csv
FLAWFINDER_OUTPUT_CPP_W=flawfinder_cpp_w_errors_per_line.csv
FLAWFINDER_OUTPUT_CPP_WO=flawfinder_cpp_wo_errors_per_line.csv
FLAWFINDER_OPTS=
FLAWFINDER_OUT_SUBDEFECTS=flawfinder_out_subdefects.csv
FLAWFINDER_OUT_DEFECTS=flawfinder_out_defects.csv
FLAWFINDER_OUT_TOTAL=flawfinder_out_total.csv




# GENERAL

all: count-errors gather-errors merge-files

base: gather-errors merge-files

count-errors:
	$(COUNT_ERRORS) $(W_C_DEFECTS_DIR) $(WO_C_DEFECTS_DIR) $(C_COUNT_ERROR_FILE)
	$(COUNT_ERRORS) $(W_CPP_DEFECTS_DIR) $(WO_CPP_DEFECTS_DIR) $(CPP_COUNT_ERROR_FILE)

gather-errors:
	$(GATHER_ERRORS) $(W_C_DEFECTS_DIR) $(C_ERRORS_PER_LINE_FILE) 0
	$(GATHER_ERRORS) $(WO_C_DEFECTS_DIR) $(C_WO_ERRORS_PER_LINE_FILE) 1
	$(GATHER_ERRORS) $(W_CPP_DEFECTS_DIR) $(CPP_ERRORS_PER_LINE_FILE) 0
	$(GATHER_ERRORS) $(WO_CPP_DEFECTS_DIR) $(CPP_WO_ERRORS_PER_LINE_FILE) 1

merge-files: gather-errors
	$(MERGE_EXE) $(C_ERRORS_PER_LINE_FILE) $(C_WO_ERRORS_PER_LINE_FILE) $(C_MERGE_FILE)
	$(MERGE_EXE) $(CPP_ERRORS_PER_LINE_FILE) $(CPP_WO_ERRORS_PER_LINE_FILE) $(CPP_MERGE_FILE)

statistics: merge-files cppcheck flawfinder




# TOOLS TARGETS
cppcheck: 
	$(CPPCHECK) $(W_C_DEFECTS_DIR) $(CPPCHECK_OUTPUT_C_W) $(CPPCHECK_EXE) $(CPPCHECK_OPTS) 
	$(CPPCHECK) $(WO_C_DEFECTS_DIR) $(CPPCHECK_OUTPUT_C_WO) $(CPPCHECK_EXE) $(CPPCHECK_OPTS) 
	python3 ./statistics.py $(C_MERGE_FILE) $(CPPCHECK_OUTPUT_C_W) $(CPPCHECK_OUTPUT_C_WO) $(CPPCHECK_OUT_SUBDEFECTS) $(CPPCHECK_OUT_DEFECTS) $(CPPCHECK_OUT_TOTAL)


flawfinder:
	$(FLAWFINDER) $(W_C_DEFECTS_DIR) $(FLAWFINDER_OUTPUT_C_W) $(FLAWFINDER_EXE) $(FLAWFINDER_OPTS) 
	$(FLAWFINDER) $(WO_C_DEFECTS_DIR) $(FLAWFINDER_OUTPUT_C_WO) $(FLAWFINDER_EXE) $(FLAWFINDER_OPTS) 
	python3 ./statistics.py $(C_MERGE_FILE) $(FLAWFINDER_OUTPUT_C_W) $(FLAWFINDER_OUTPUT_C_WO) $(FLAWFINDER_OUT_SUBDEFECTS) $(FLAWFINDER_OUT_DEFECTS) $(FLAWFINDER_OUT_TOTAL)

clang:
	$(CLANG) $(W_C_DEFECTS_DIR) $(CLANG_OUTPUT) $(CLANG_EXE) $(CLANG_OPTS) 






# UTILS

clean:
	rm -f *.csv 


time: count-errors-with-time gather-errors-with-time

count-errors-with-time:
	time $(COUNT_ERRORS) $(W_C_DEFECTS_DIR) $(C_COUNT_ERROR_FILE)
	time $(COUNT_ERRORS) $(W_CPP_DEFECTS_DIR) $(CPP_COUNT_ERROR_FILE)

gather-errors-with-time:
	time $(GATHER_ERRORS) $(W_C_DEFECTS_DIR) $(C_ERRORS_PER_LINE_FILE)
	time $(GATHER_ERRORS) $(W_CPP_DEFECTS_DIR) $(CPP_ERRORS_PER_LINE_FILE)
