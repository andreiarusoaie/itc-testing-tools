## Modify the location of these folders according to your needs
W_C_DEFECTS_DIR=~/work/itc-benchmarks/01.w_Defects/
W_CPP_DEFECTS_DIR=~/work/itc-benchmarks/03.w_Defects_Cpp/
WO_C_DEFECTS_DIR=~/work/itc-benchmarks/02.wo_Defects/
WO_CPP_DEFECTS_DIR=~/work/itc-benchmarks/04.wo_Defects_Cpp/

## Tools locations & output files

## CLANG
CLANG=./clang.sh
CLANG_EXE=/usr/bin/clang
CLANG_OUTPUT=clang_c_errors_per_line.csv
CLANG_OPTS="-cc1 -analyze -analyzer-checker=core"

## CPPCHECK
CPPCHECK=./cppcheck.sh
CPPCHECK_EXE=/usr/local/bin/cppcheck
CPPCHECK_OUTPUT=cppcheck_c_errors_per_line.csv
CPPCHECK_OPTS="--xml --xml-version=2"



## Do not modify these
COUNT_ERRORS=./count-errors-per-file.sh
GATHER_ERRORS=./gather-errors-by-line.sh

## Output files
C_COUNT_ERROR_FILE=c_count_errors.csv
CPP_COUNT_ERROR_FILE=cpp_count_errors.csv
C_ERRORS_PER_LINE_FILE=c_errors_per_line.csv
CPP_ERRORS_PER_LINE_FILE=cpp_errors_per_line.csv


all: count-errors gather-errors

count-errors:
	$(COUNT_ERRORS) $(W_C_DEFECTS_DIR) $(WO_C_DEFECTS_DIR) $(C_COUNT_ERROR_FILE)
	$(COUNT_ERRORS) $(W_CPP_DEFECTS_DIR) $(WO_CPP_DEFECTS_DIR) $(CPP_COUNT_ERROR_FILE)

gather-errors:
	$(GATHER_ERRORS) $(W_C_DEFECTS_DIR) $(C_ERRORS_PER_LINE_FILE)
	$(GATHER_ERRORS) $(W_CPP_DEFECTS_DIR) $(CPP_ERRORS_PER_LINE_FILE)

clang:
	$(CLANG) $(W_C_DEFECTS_DIR) $(CLANG_OUTPUT) $(CLANG_EXE) $(CLANG_OPTS) 

cppcheck:
	$(CPPCHECK) $(W_C_DEFECTS_DIR) $(CPPCHECK_OUTPUT) $(CPPCHECK_EXE) $(CPPCHECK_OPTS) 


clean:
	rm -f $(C_COUNT_ERROR_FILE) $(CPP_COUNT_ERROR_FILE) $(C_ERRORS_PER_LINE_FILE) $(CPP_ERRORS_PER_LINE_FILE)


time: count-errors-with-time gather-errors-with-time

count-errors-with-time:
	time $(COUNT_ERRORS) $(W_C_DEFECTS_DIR) $(C_COUNT_ERROR_FILE)
	time $(COUNT_ERRORS) $(W_CPP_DEFECTS_DIR) $(CPP_COUNT_ERROR_FILE)

gather-errors-with-time:
	time $(GATHER_ERRORS) $(W_C_DEFECTS_DIR) $(C_ERRORS_PER_LINE_FILE)
	time $(GATHER_ERRORS) $(W_CPP_DEFECTS_DIR) $(CPP_ERRORS_PER_LINE_FILE)
