## Location of ITC workbench: this should be modified by need
W_C_DEFECTS_DIR=../itc-benchmarks/01.w_Defects/
W_CPP_DEFECTS_DIR=../itc-benchmarks/03.w_Defects_Cpp/

WO_C_DEFECTS_DIR=../itc-benchmarks/02.wo_Defects/
WO_CPP_DEFECTS_DIR=../itc-benchmarks/04.wo_Defects_Cpp/


## MAIN SCRIPTS to run
COUNT_ERRORS=./bash/count-errors-per-file.sh
GATHER_ERRORS=./bash/gather-errors-by-line.sh
MERGE_EXE=./bash/merge-csv.sh
STATISTICS=./bash/statistics.py

## Output files
# COUNT ALL ERRORS
C_COUNT_ERROR_FILE=./csv/setup/temp/c_count_errors.csv
CPP_COUNT_ERROR_FILE=./csv/setup/temp/cpp_count_errors.csv

# GATHER ERRORS FORM ITC BENCHMARK  PER LINE
C_ERRORS_PER_LINE_FILE=./csv/setup/temp/c_errors_per_line.csv
CPP_ERRORS_PER_LINE_FILE=./csv/setup/temp/cpp_errors_per_line.csv
C_WO_ERRORS_PER_LINE_FILE=./csv/setup/temp/c_wo_errors_per_line.csv
CPP_WO_ERRORS_PER_LINE_FILE=./csv/setup/temp/cpp_wo_errors_per_line.csv

# MERGE FILES 
C_MERGE_FILE=./csv/setup/c_merge_file.csv
CPP_MERGE_FILE=./csv/setup/cpp_merge_file.csv





## Tools configurations

## CLANG CORE
CLANG_CORE=./python/clang.py
CLANG_CORE_PP=./python/clang++.py
CLANG_CORE_EXE=clang
CLANG_CORE_EXE_CPP=clang++
CLANG_CORE_OUTPUT_C_W=./csv/clangcore/temp/clang_core_c_w_errors_per_line.csv
CLANG_CORE_OUTPUT_C_WO=./csv/clangcore/temp/clang_core_c_wo_errors_per_line.csv
CLANG_CORE_OUTPUT_CPP_W=./csv/clangcore/temp/clang_core_cpp_w_errors_per_line.csv
CLANG_CORE_OUTPUT_CPP_WO=./csv/clangcore/temp/clang_core_cpp_wo_errors_per_line.csv
CLANG_CORE_OPTS='-cc1 -analyze -analyzer-checker=core'
CLANG_CORE_OUT_SUBDEFECTS=./csv/clangcore/clang_core_out_subdefects.csv
CLANG_CORE_OUT_DEFECTS=./csv/clangcore/clang_core_out_defects.csv
CLANG_CORE_OUT_TOTAL=./csv/clangcore/clang_core_out_total.csv
CLANG_CORE_OUT_CPP_SUBDEFECTS=./csv/clangcore/clang_core_out_cpp_subdefects.csv
CLANG_CORE_OUT_CPP_DEFECTS=./csv/clangcore/clang_core_out_cpp_defects.csv
CLANG_CORE_OUT_CPP_TOTAL=./csv/clangcore/clang_core_out_cpp_total.csv


## CLANG ALPHA
CLANG_ALPHA=./python/clang.py
CLANG_ALPHA_PP=./python/clang++.py
CLANG_ALPHA_EXE=clang
CLANG_ALPHA_EXE_CPP=clang++
CLANG_ALPHA_OUTPUT_C_W=./csv/clangalpha/temp/clang_alpha_c_w_errors_per_line.csv
CLANG_ALPHA_OUTPUT_C_WO=./csv/clangalpha/temp/clang_alpha_c_wo_errors_per_line.csv
CLANG_ALPHA_OUTPUT_CPP_W=./csv/clangalpha/temp/clang_alpha_cpp_w_errors_per_line.csv
CLANG_ALPHA_OUTPUT_CPP_WO=./csv/clangalpha/temp/clang_alpha_cpp_wo_errors_per_line.csv
CLANG_ALPHA_OPTS='-cc1 -analyze -analyzer-checker=alpha'
CLANG_ALPHA_OUT_SUBDEFECTS=./csv/clangalpha/clang_alpha_out_subdefects.csv
CLANG_ALPHA_OUT_DEFECTS=./csv/clangalpha/clang_alpha_out_defects.csv
CLANG_ALPHA_OUT_TOTAL=./csv/clangalpha/clang_alpha_out_total.csv
CLANG_ALPHA_OUT_CPP_SUBDEFECTS=./csv/clangalpha/clang_alpha_out_cpp_subdefects.csv
CLANG_ALPHA_OUT_CPP_DEFECTS=./csv/clangalpha/clang_alpha_out_cpp_defects.csv
CLANG_ALPHA_OUT_CPP_TOTAL=./csv/clangalpha/clang_alpha_out_cpp_total.csv

## CPPCHECK
CPPCHECK=./python/cppcheck.py
CPPCHECK_EXE=cppcheck
CPPCHECK_EXE_CPP=cppcheck
CPPCHECK_OUTPUT_C_W=./csv/cppcheck/temp/cppcheck_c_w_errors_per_line.csv
CPPCHECK_OUTPUT_C_WO=./csv/cppcheck/temp/cppcheck_c_wo_errors_per_line.csv
CPPCHECK_OUTPUT_CPP_W=./csv/cppcheck/temp/cppcheck_cpp_w_errors_per_line.csv
CPPCHECK_OUTPUT_CPP_WO=./csv/cppcheck/temp/cppcheck_cpp_wo_errors_per_line.csv
CPPCHECK_OPTS="--xml --xml-version=2"
CPPCHECK_OUT_SUBDEFECTS=./csv/cppcheck/cppcheck_out_subdefects.csv
CPPCHECK_OUT_DEFECTS=./csv/cppcheck/cppcheck_out_defects.csv
CPPCHECK_OUT_TOTAL=./csv/cppcheck/cppcheck_out_total.csv
CPPCHECK_OUT_CPP_SUBDEFECTS=./csv/cppcheck/cppcheck_out_cpp_subdefects.csv
CPPCHECK_OUT_CPP_DEFECTS=./csv/cppcheck/cppcheck_out_cpp_defects.csv
CPPCHECK_OUT_CPP_TOTAL=./csv/cppcheck/cppcheck_out_cpp_total.csv


## SPARSE
SPARSE=./python/sparse.py
SPARSE_EXE=sparse
SPARSE_EXE_CPP=sparse
SPARSE_OUTPUT_C_W=./csv/sparse/temp/sparse_c_w_errors_per_line.csv
SPARSE_OUTPUT_C_WO=./csv/sparse/temp/sparse_c_wo_errors_per_line.csv
SPARSE_OUTPUT_CPP_W=./csv/sparse/temp/sparse_cpp_w_errors_per_line.csv
SPARSE_OUTPUT_CPP_WO=./csv/sparse/temp/sparse_cpp_wo_errors_per_line.csv
SPARSE_OPTS=
SPARSE_OUT_SUBDEFECTS=./csv/sparse/sparse_out_subdefects.csv
SPARSE_OUT_DEFECTS=./csv/sparse/sparse_out_defects.csv
SPARSE_OUT_TOTAL=./csv/sparse/sparse_out_total.csv
SPARSE_OUT_CPP_SUBDEFECTS=./csv/sparse/sparse_out_cpp_subdefects.csv
SPARSE_OUT_CPP_DEFECTS=./csv/sparse/sparse_out_cpp_defects.csv
SPARSE_OUT_CPP_TOTAL=./csv/sparse/sparse_out_cpp_total.csv


## UNO
UNO=./bash/uno.sh
UNO_EXE=uno
UNO_EXE_CPP=uno
UNO_OUTPUT_C_W=./csv/uno/temp/uno_c_w_errors_per_line.csv
UNO_OUTPUT_C_WO=./csv/uno/temp/uno_c_wo_errors_per_line.csv
UNO_OUTPUT_CPP_W=./csv/uno/temp/uno_cpp_w_errors_per_line.csv
UNO_OUTPUT_CPP_WO=./csv/uno/temp/uno_cpp_wo_errors_per_line.csv
UNO_OPTS=
UNO_OUT_SUBDEFECTS=./csv/uno/uno_out_subdefects.csv
UNO_OUT_DEFECTS=./csv/uno/uno_out_defects.csv
UNO_OUT_TOTAL=./csv/uno/uno_out_total.csv
UNO_OUT_CPP_SUBDEFECTS=./csv/uno/uno_out_cpp_subdefects.csv
UNO_OUT_CPP_DEFECTS=./csv/uno/uno_out_cpp_defects.csv
UNO_OUT_CPP_TOTAL=./csv/uno/uno_out_cpp_total.csv


## FLAWFINDER
FLAWFINDER=./python/flawfinder.py
FLAWFINDER_EXE=flawfinder
FLAWFINDER_OUTPUT_C_W=./csv/flawfinder/temp/flawfinder_c_w_errors_per_line.csv
FLAWFINDER_OUTPUT_C_WO=./csv/flawfinder/temp/flawfinder_c_wo_errors_per_line.csv
FLAWFINDER_OUTPUT_CPP_W=./csv/flawfinder/temp/flawfinder_cpp_w_errors_per_line.csv
FLAWFINDER_OUTPUT_CPP_WO=./csv/flawfinder/temp/flawfinder_cpp_wo_errors_per_line.csv
FLAWFINDER_OPTS=
FLAWFINDER_OUT_SUBDEFECTS=./csv/flawfinder/flawfinder_out_subdefects.csv
FLAWFINDER_OUT_DEFECTS=./csv/flawfinder/flawfinder_out_defects.csv
FLAWFINDER_OUT_TOTAL=./csv/flawfinder/flawfinder_out_total.csv
FLAWFINDER_OUT_CPP_SUBDEFECTS=./csv/flawfinder/flawfinder_out_cpp_subdefects.csv
FLAWFINDER_OUT_CPP_DEFECTS=./csv/flawfinder/flawfinder_out_cpp_defects.csv
FLAWFINDER_OUT_CPP_TOTAL=./csv/flawfinder/flawfinder_out_cpp_total.csv


## INFER
INFER=./python/infer.py
INFER_EXE=infer
INFER_OUTPUT_C_W=./csv/infer/temp/infer_c_w_errors_per_line.csv
INFER_OUTPUT_C_WO=./csv/infer/temp/infer_c_wo_errors_per_line.csv
INFER_OUTPUT_CPP_W=./csv/infer/temp/infer_cpp_w_errors_per_line.csv
INFER_OUTPUT_CPP_WO=./csv/infer/temp/infer_cpp_wo_errors_per_line.csv
INFER_OPTS=""
INFER_OUT_SUBDEFECTS=./csv/infer/infer_out_subdefects.csv
INFER_OUT_DEFECTS=./csv/infer/infer_out_defects.csv
INFER_OUT_TOTAL=./csv/infer/infer_out_total.csv
INFER_OUT_CPP_SUBDEFECTS=./csv/infer/infer_out_cpp_subdefects.csv
INFER_OUT_CPP_DEFECTS=./csv/infer/infer_out_cpp_defects.csv
INFER_OUT_CPP_TOTAL=./csv/infer/infer_out_cpp_total.csv


## SPLINT
SPLINT=./python/splint.py
SPLINT_EXE=splint
SPLINT_OUTPUT_C_W=./csv/splint/temp/splint_c_w_errors_per_line.csv
SPLINT_OUTPUT_C_WO=./csv/splint/temp/splint_c_wo_errors_per_line.csv
SPLINT_OUTPUT_CPP_W=./csv/splint/temp/splint_cpp_w_errors_per_line.csv
SPLINT_OUTPUT_CPP_WO=./csv/splint/temp/splint_cpp_wo_errors_per_line.csv
SPLINT_OPTS=
SPLINT_OUT_SUBDEFECTS=./csv/splint/splint_out_subdefects.csv
SPLINT_OUT_DEFECTS=./csv/splint/splint_out_defects.csv
SPLINT_OUT_TOTAL=./csv/splint/splint_out_total.csv
SPLINT_OUT_CPP_SUBDEFECTS=./csv/splint/splint_out_cpp_subdefects.csv
SPLINT_OUT_CPP_DEFECTS=./csv/splint/splint_out_cpp_defects.csv
SPLINT_OUT_CPP_TOTAL=./csv/splint/splint_out_cpp_total.csv



# GENERAL

all: count-errors gather-errors merge-files

prepare-dirs:
	mkdir -p ./csv/setup/temp/
	mkdir -p ./csv/cppcheck/temp/
	mkdir -p ./csv/sparse/temp/
	mkdir -p ./csv/uno/temp/
	mkdir -p ./csv/clangalpha/temp/
	mkdir -p ./csv/clangcore/temp/
	mkdir -p ./csv/flawfinder/temp/
	mkdir -p ./csv/infer/temp/
	mkdir -p ./csv/splint/temp/

base: prepare-dirs gather-errors merge-files

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

statistics: merge-files cppcheck flawfinder clang-core clang-alpha infer




# TOOLS TARGETS
cppcheck:
	python3 $(CPPCHECK) $(W_C_DEFECTS_DIR) $(CPPCHECK_OUTPUT_C_W) $(CPPCHECK_EXE) $(CPPCHECK_OPTS) 
	python3 $(CPPCHECK) $(WO_C_DEFECTS_DIR) $(CPPCHECK_OUTPUT_C_WO) $(CPPCHECK_EXE) $(CPPCHECK_OPTS) 
	python3 ${STATISTICS} $(C_MERGE_FILE) $(CPPCHECK_OUTPUT_C_W) $(CPPCHECK_OUTPUT_C_WO) $(CPPCHECK_OUT_SUBDEFECTS) $(CPPCHECK_OUT_DEFECTS) $(CPPCHECK_OUT_TOTAL)
	python3 $(CPPCHECK) $(W_CPP_DEFECTS_DIR) $(CPPCHECK_OUTPUT_CPP_W) $(CPPCHECK_EXE_CPP) $(CPPCHECK_OPTS) 
	python3 $(CPPCHECK) $(WO_CPP_DEFECTS_DIR) $(CPPCHECK_OUTPUT_CPP_WO) $(CPPCHECK_EXE_CPP) $(CPPCHECK_OPTS)
	python3 ${STATISTICS} $(CPP_MERGE_FILE) $(CPPCHECK_OUTPUT_CPP_W) $(CPPCHECK_OUTPUT_CPP_WO) $(CPPCHECK_OUT_CPP_SUBDEFECTS) $(CPPCHECK_OUT_CPP_DEFECTS) $(CPPCHECK_OUT_CPP_TOTAL)

sparse:
	python3 $(SPARSE) $(W_C_DEFECTS_DIR) $(SPARSE_OUTPUT_C_W) $(SPARSE_EXE) $(SPARSE_OPTS) 
	python3 $(SPARSE) $(WO_C_DEFECTS_DIR) $(SPARSE_OUTPUT_C_WO) $(SPARSE_EXE) $(SPARSE_OPTS) 
	python3 ${STATISTICS} $(C_MERGE_FILE) $(SPARSE_OUTPUT_C_W) $(SPARSE_OUTPUT_C_WO) $(SPARSE_OUT_SUBDEFECTS) $(SPARSE_OUT_DEFECTS) $(SPARSE_OUT_TOTAL)
	python3 $(SPARSE) $(W_CPP_DEFECTS_DIR) $(SPARSE_OUTPUT_CPP_W) $(SPARSE_EXE_CPP) $(SPARSE_OPTS) 
	python3 $(SPARSE) $(WO_CPP_DEFECTS_DIR) $(SPARSE_OUTPUT_CPP_WO) $(SPARSE_EXE_CPP) $(SPARSE_OPTS)
	python3 ${STATISTICS} $(CPP_MERGE_FILE) $(SPARSE_OUTPUT_CPP_W) $(SPARSE_OUTPUT_CPP_WO) $(SPARSE_OUT_CPP_SUBDEFECTS) $(SPARSE_OUT_CPP_DEFECTS) $(SPARSE_OUT_CPP_TOTAL)

uno:
	$(UNO) $(W_C_DEFECTS_DIR) $(UNO_OUTPUT_C_W) $(UNO_EXE) $(UNO_OPTS) 
	$(UNO) $(WO_C_DEFECTS_DIR) $(UNO_OUTPUT_C_WO) $(UNO_EXE) $(UNO_OPTS) 
	python3 ${STATISTICS} $(C_MERGE_FILE) $(UNO_OUTPUT_C_W) $(UNO_OUTPUT_C_WO) $(UNO_OUT_SUBDEFECTS) $(UNO_OUT_DEFECTS) $(UNO_OUT_TOTAL)
	$(UNO) $(W_CPP_DEFECTS_DIR) $(UNO_OUTPUT_CPP_W) $(UNO_EXE_CPP) $(UNO_OPTS) 
	$(UNO) $(WO_CPP_DEFECTS_DIR) $(UNO_OUTPUT_CPP_WO) $(UNO_EXE_CPP) $(UNO_OPTS)
	python3 ${STATISTICS} $(CPP_MERGE_FILE) $(UNO_OUTPUT_CPP_W) $(UNO_OUTPUT_CPP_WO) $(UNO_OUT_CPP_SUBDEFECTS) $(UNO_OUT_CPP_DEFECTS) $(UNO_OUT_CPP_TOTAL)


flawfinder:
	python3 $(FLAWFINDER) $(W_C_DEFECTS_DIR) $(FLAWFINDER_OUTPUT_C_W) $(FLAWFINDER_EXE) $(FLAWFINDER_OPTS) 
	python3 $(FLAWFINDER) $(WO_C_DEFECTS_DIR) $(FLAWFINDER_OUTPUT_C_WO) $(FLAWFINDER_EXE) $(FLAWFINDER_OPTS) 
	python3 ${STATISTICS} $(C_MERGE_FILE) $(FLAWFINDER_OUTPUT_C_W) $(FLAWFINDER_OUTPUT_C_WO) $(FLAWFINDER_OUT_SUBDEFECTS) $(FLAWFINDER_OUT_DEFECTS) $(FLAWFINDER_OUT_TOTAL)
	python3 $(FLAWFINDER) $(W_CPP_DEFECTS_DIR) $(FLAWFINDER_OUTPUT_CPP_W) $(FLAWFINDER_EXE) $(FLAWFINDER_OPTS) 
	python3 $(FLAWFINDER) $(WO_CPP_DEFECTS_DIR) $(FLAWFINDER_OUTPUT_CPP_WO) $(FLAWFINDER_EXE) $(FLAWFINDER_OPTS)
	python3 ${STATISTICS} $(CPP_MERGE_FILE) $(FLAWFINDER_OUTPUT_CPP_W) $(FLAWFINDER_OUTPUT_CPP_WO) $(FLAWFINDER_OUT_CPP_SUBDEFECTS) $(FLAWFINDER_OUT_CPP_DEFECTS) $(FLAWFINDER_OUT_CPP_TOTAL)


splint:
	python3 $(SPLINT) $(W_C_DEFECTS_DIR) $(SPLINT_OUTPUT_C_W) $(SPLINT_EXE) $(SPLINT_OPTS) 
	python3 $(SPLINT) $(WO_C_DEFECTS_DIR) $(SPLINT_OUTPUT_C_WO) $(SPLINT_EXE) $(SPLINT_OPTS) 
	python3 ${STATISTICS} $(C_MERGE_FILE) $(SPLINT_OUTPUT_C_W) $(SPLINT_OUTPUT_C_WO) $(SPLINT_OUT_SUBDEFECTS) $(SPLINT_OUT_DEFECTS) $(SPLINT_OUT_TOTAL)
	python3 $(SPLINT) $(W_CPP_DEFECTS_DIR) $(SPLINT_OUTPUT_CPP_W) $(SPLINT_EXE) $(SPLINT_OPTS) 
	python3 $(SPLINT) $(WO_CPP_DEFECTS_DIR) $(SPLINT_OUTPUT_CPP_WO) $(SPLINT_EXE) $(SPLINT_OPTS)
	python3 ${STATISTICS} $(CPP_MERGE_FILE) $(SPLINT_OUTPUT_CPP_W) $(SPLINT_OUTPUT_CPP_WO) $(SPLINT_OUT_CPP_SUBDEFECTS) $(SPLINT_OUT_CPP_DEFECTS) $(SPLINT_OUT_CPP_TOTAL)


clang-core: 
	python3 $(CLANG_CORE) $(W_C_DEFECTS_DIR) $(CLANG_CORE_OUTPUT_C_W) $(CLANG_CORE_EXE) $(CLANG_CORE_OPTS) 
	python3 $(CLANG_CORE) $(WO_C_DEFECTS_DIR) $(CLANG_CORE_OUTPUT_C_WO) $(CLANG_CORE_EXE) $(CLANG_CORE_OPTS) 
	python3 ${STATISTICS} $(C_MERGE_FILE) $(CLANG_CORE_OUTPUT_C_W) $(CLANG_CORE_OUTPUT_C_WO) $(CLANG_CORE_OUT_SUBDEFECTS) $(CLANG_CORE_OUT_DEFECTS) $(CLANG_CORE_OUT_TOTAL)
	python3 $(CLANG_CORE_PP) $(W_CPP_DEFECTS_DIR) $(CLANG_CORE_OUTPUT_CPP_W) $(CLANG_CORE_EXE_CPP) $(CLANG_CORE_OPTS) 
	python3 $(CLANG_CORE_PP) $(WO_CPP_DEFECTS_DIR) $(CLANG_CORE_OUTPUT_CPP_WO) $(CLANG_CORE_EXE_CPP) $(CLANG_CORE_OPTS)
	python3 ${STATISTICS} $(CPP_MERGE_FILE) $(CLANG_CORE_OUTPUT_CPP_W) $(CLANG_CORE_OUTPUT_CPP_WO) $(CLANG_CORE_OUT_CPP_SUBDEFECTS) $(CLANG_CORE_OUT_CPP_DEFECTS) $(CLANG_CORE_OUT_CPP_TOTAL)

clang-alpha:
	python3 $(CLANG_ALPHA) $(W_C_DEFECTS_DIR) $(CLANG_ALPHA_OUTPUT_C_W) $(CLANG_ALPHA_EXE) $(CLANG_ALPHA_OPTS) 
	python3 $(CLANG_ALPHA) $(WO_C_DEFECTS_DIR) $(CLANG_ALPHA_OUTPUT_C_WO) $(CLANG_ALPHA_EXE) $(CLANG_ALPHA_OPTS) 
	python3 ${STATISTICS} $(C_MERGE_FILE) $(CLANG_ALPHA_OUTPUT_C_W) $(CLANG_ALPHA_OUTPUT_C_WO) $(CLANG_ALPHA_OUT_SUBDEFECTS) $(CLANG_ALPHA_OUT_DEFECTS) $(CLANG_ALPHA_OUT_TOTAL)
	python3 $(CLANG_ALPHA_PP) $(W_CPP_DEFECTS_DIR) $(CLANG_ALPHA_OUTPUT_CPP_W) $(CLANG_ALPHA_EXE_CPP) $(CLANG_ALPHA_OPTS)
	python3 $(CLANG_ALPHA_PP) $(WO_CPP_DEFECTS_DIR) $(CLANG_ALPHA_OUTPUT_CPP_WO) $(CLANG_ALPHA_EXE_CPP) $(CLANG_ALPHA_OPTS)
	python3 ${STATISTICS} $(CPP_MERGE_FILE) $(CLANG_ALPHA_OUTPUT_CPP_W) $(CLANG_ALPHA_OUTPUT_CPP_WO) $(CLANG_ALPHA_OUT_CPP_SUBDEFECTS) $(CLANG_ALPHA_OUT_CPP_DEFECTS) $(CLANG_ALPHA_OUT_CPP_TOTAL)

infer: 
	python3 $(INFER) $(W_C_DEFECTS_DIR) $(INFER_OUTPUT_C_W) $(INFER_EXE) $(INFER_OPTS) 
	python3 $(INFER) $(WO_C_DEFECTS_DIR) $(INFER_OUTPUT_C_WO) $(INFER_EXE) $(INFER_OPTS) 
	python3 ${STATISTICS} $(C_MERGE_FILE) $(INFER_OUTPUT_C_W) $(INFER_OUTPUT_C_WO) $(INFER_OUT_SUBDEFECTS) $(INFER_OUT_DEFECTS) $(INFER_OUT_TOTAL)
	python3 $(INFER) $(W_CPP_DEFECTS_DIR) $(INFER_OUTPUT_CPP_W) $(INFER_EXE) $(INFER_OPTS) 
	python3 $(INFER) $(WO_CPP_DEFECTS_DIR) $(INFER_OUTPUT_CPP_WO) $(INFER_EXE) $(INFER_OPTS)
	python3 ${STATISTICS} $(CPP_MERGE_FILE) $(INFER_OUTPUT_CPP_W) $(INFER_OUTPUT_CPP_WO) $(INFER_OUT_CPP_SUBDEFECTS) $(INFER_OUT_CPP_DEFECTS) $(INFER_OUT_CPP_TOTAL)



# UTILS

clean:
	rm -rf ./csv/temp/
	rm -f ./csv/cppcheck/*.csv 
	rm -f ./csv/cppcheck/temp/*.csv 
	rm -f ./csv/clangcore/*.csv 
	rm -f ./csv/clangcore/temp/*.csv 
	rm -f ./csv/clangalpha/*.csv 
	rm -f ./csv/clangalpha/temp/*.csv
	rm -f ./csv/infer/*.csv 
	rm -f ./csv/infer/temp/*.csv
	rm -f ./csv/flawfinder/*.csv 
	rm -f ./csv/flawfinder/temp/*.csv


time: count-errors-with-time gather-errors-with-time

count-errors-with-time:
	time $(COUNT_ERRORS) $(W_C_DEFECTS_DIR) $(C_COUNT_ERROR_FILE)
	time $(COUNT_ERRORS) $(W_CPP_DEFECTS_DIR) $(CPP_COUNT_ERROR_FILE)

gather-errors-with-time:
	time $(GATHER_ERRORS) $(W_C_DEFECTS_DIR) $(C_ERRORS_PER_LINE_FILE)
	time $(GATHER_ERRORS) $(W_CPP_DEFECTS_DIR) $(CPP_ERRORS_PER_LINE_FILE)
