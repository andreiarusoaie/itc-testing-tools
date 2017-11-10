import sys
import os.path
import os
import python.system
import python.clanalyze

# ## Location of ITC workbench: this should be modified by need
W_C_DEFECTS_DIR = "../itc-benchmarks/01.w_Defects/"
W_CPP_DEFECTS_DIR = "../itc-benchmarks/03.w_Defects_Cpp/"

WO_C_DEFECTS_DIR = "../itc-benchmarks/02.wo_Defects/"
WO_CPP_DEFECTS_DIR = "../itc-benchmarks/04.wo_Defects_Cpp/"

STATISTICS="./bash/statistics.py"

# ## Output files
# # COUNT ALL ERRORS
C_COUNT_ERROR_FILE = "./csv/setup/temp/c_count_errors.csv"
CPP_COUNT_ERROR_FILE = "./csv/setup/temp/cpp_count_errors.csv"

# # MERGE FILES 
C_MERGE_FILE = "./csv/setup/c_merge_file.csv"
CPP_MERGE_FILE = "./csv/setup/cpp_merge_file.csv"

# ## Tools configurations

# ## CLANG CORE
CLANG_CORE = "./python/clang.py"
CLANG_CORE_PP = "./python/clang++.py"
CLANG_CORE_EXE = "clang"
CLANG_CORE_EXE_CPP = "clang++"
CLANG_CORE_OUTPUT_C_W = "./csv/clangcore/temp/clang_core_c_w_errors_per_line.csv"
CLANG_CORE_OUTPUT_C_WO = "./csv/clangcore/temp/clang_core_c_wo_errors_per_line.csv"
CLANG_CORE_OUTPUT_CPP_W = "./csv/clangcore/temp/clang_core_cpp_w_errors_per_line.csv"
CLANG_CORE_OUTPUT_CPP_WO = "./csv/clangcore/temp/clang_core_cpp_wo_errors_per_line.csv"
CLANG_CORE_OPTS = "'-cc1 -analyze -analyzer-checker=core'"
CLANG_CORE_OUT_SUBDEFECTS = "./csv/clangcore/clang_core_out_subdefects.csv"
CLANG_CORE_OUT_DEFECTS = "./csv/clangcore/clang_core_out_defects.csv"
CLANG_CORE_OUT_TOTAL = "./csv/clangcore/clang_core_out_total.csv"
CLANG_CORE_OUT_CPP_SUBDEFECTS = "./csv/clangcore/clang_core_out_cpp_subdefects.csv"
CLANG_CORE_OUT_CPP_DEFECTS = "./csv/clangcore/clang_core_out_cpp_defects.csv"
CLANG_CORE_OUT_CPP_TOTAL = "./csv/clangcore/clang_core_out_cpp_total.csv"


# ## CLANG ALPHA
CLANG_ALPHA = "./python/clang.py"
CLANG_ALPHA_PP = "./python/clang++.py"
CLANG_ALPHA_EXE = "clang"
CLANG_ALPHA_EXE_CPP = "clang++"
CLANG_ALPHA_OUTPUT_C_W = "./csv/clangalpha/temp/clang_alpha_c_w_errors_per_line.csv"
CLANG_ALPHA_OUTPUT_C_WO = "./csv/clangalpha/temp/clang_alpha_c_wo_errors_per_line.csv"
CLANG_ALPHA_OUTPUT_CPP_W = "./csv/clangalpha/temp/clang_alpha_cpp_w_errors_per_line.csv"
CLANG_ALPHA_OUTPUT_CPP_WO = "./csv/clangalpha/temp/clang_alpha_cpp_wo_errors_per_line.csv"
CLANG_ALPHA_OPTS = "'-cc1 -analyze -analyzer-checker=alpha'"
CLANG_ALPHA_OUT_SUBDEFECTS = "./csv/clangalpha/clang_alpha_out_subdefects.csv"
CLANG_ALPHA_OUT_DEFECTS = "./csv/clangalpha/clang_alpha_out_defects.csv"
CLANG_ALPHA_OUT_TOTAL = "./csv/clangalpha/clang_alpha_out_total.csv"
CLANG_ALPHA_OUT_CPP_SUBDEFECTS = "./csv/clangalpha/clang_alpha_out_cpp_subdefects.csv"
CLANG_ALPHA_OUT_CPP_DEFECTS = "./csv/clangalpha/clang_alpha_out_cpp_defects.csv"
CLANG_ALPHA_OUT_CPP_TOTAL = "./csv/clangalpha/clang_alpha_out_cpp_total.csv"

# ## CPPCHECK
CPPCHECK = "./python/cppcheck.py"
CPPCHECK_EXE = "cppcheck"
CPPCHECK_EXE_CPP = "cppcheck"
CPPCHECK_OUTPUT_C_W = "./csv/cppcheck/temp/cppcheck_c_w_errors_per_line.csv"
CPPCHECK_OUTPUT_C_WO = "./csv/cppcheck/temp/cppcheck_c_wo_errors_per_line.csv"
CPPCHECK_OUTPUT_CPP_W = "./csv/cppcheck/temp/cppcheck_cpp_w_errors_per_line.csv"
CPPCHECK_OUTPUT_CPP_WO = "./csv/cppcheck/temp/cppcheck_cpp_wo_errors_per_line.csv"
CPPCHECK_OPTS = "\"--xml --xml-version=2\""
CPPCHECK_OUT_SUBDEFECTS = "./csv/cppcheck/cppcheck_out_subdefects.csv"
CPPCHECK_OUT_DEFECTS = "./csv/cppcheck/cppcheck_out_defects.csv"
CPPCHECK_OUT_TOTAL = "./csv/cppcheck/cppcheck_out_total.csv"
CPPCHECK_OUT_CPP_SUBDEFECTS = "./csv/cppcheck/cppcheck_out_cpp_subdefects.csv"
CPPCHECK_OUT_CPP_DEFECTS = "./csv/cppcheck/cppcheck_out_cpp_defects.csv"
CPPCHECK_OUT_CPP_TOTAL = "./csv/cppcheck/cppcheck_out_cpp_total.csv"

# ## CPPLINT
CPPLINT = "./python/cpplint.py"
CPPLINT_EXE = "cpplint"
CPPLINT_EXE_CPP = "cpplint"
CPPLINT_OUTPUT_C_W = "./csv/cpplint/temp/cpplint_c_w_errors_per_line.csv"
CPPLINT_OUTPUT_C_WO = "./csv/cpplint/temp/cpplint_c_wo_errors_per_line.csv"
CPPLINT_OUTPUT_CPP_W = "./csv/cpplint/temp/cpplint_cpp_w_errors_per_line.csv"
CPPLINT_OUTPUT_CPP_WO = "./csv/cpplint/temp/cpplint_cpp_wo_errors_per_line.csv"
CPPLINT_OPTS = ""
CPPLINT_OUT_SUBDEFECTS = "./csv/cpplint/cpplint_out_subdefects.csv"
CPPLINT_OUT_DEFECTS = "./csv/cpplint/cpplint_out_defects.csv"
CPPLINT_OUT_TOTAL = "./csv/cpplint/cpplint_out_total.csv"
CPPLINT_OUT_CPP_SUBDEFECTS = "./csv/cpplint/cpplint_out_cpp_subdefects.csv"
CPPLINT_OUT_CPP_DEFECTS = "./csv/cpplint/cpplint_out_cpp_defects.csv"
CPPLINT_OUT_CPP_TOTAL = "./csv/cpplint/cpplint_out_cpp_total.csv"

# ## OCLINT
OCLINT = "./python/oclint.py"
OCLINT_EXE = "oclint"
OCLINT_EXE_CPP = "oclint"
OCLINT_OUTPUT_C_W = "./csv/oclint/temp/oclint_c_w_errors_per_line.csv"
OCLINT_OUTPUT_C_WO = "./csv/oclint/temp/oclint_c_wo_errors_per_line.csv"
OCLINT_OUTPUT_CPP_W = "./csv/oclint/temp/oclint_cpp_w_errors_per_line.csv"
OCLINT_OUTPUT_CPP_WO = "./csv/oclint/temp/oclint_cpp_wo_errors_per_line.csv"
OCLINT_OPTS = ""
OCLINT_OUT_SUBDEFECTS = "./csv/oclint/oclint_out_subdefects.csv"
OCLINT_OUT_DEFECTS = "./csv/oclint/oclint_out_defects.csv"
OCLINT_OUT_TOTAL = "./csv/oclint/oclint_out_total.csv"
OCLINT_OUT_CPP_SUBDEFECTS = "./csv/oclint/oclint_out_cpp_subdefects.csv"
OCLINT_OUT_CPP_DEFECTS = "./csv/oclint/oclint_out_cpp_defects.csv"
OCLINT_OUT_CPP_TOTAL = "./csv/oclint/oclint_out_cpp_total.csv"

# ## SPARSE
SPARSE = "./python/sparse.py"
SPARSE_EXE = "sparse"
SPARSE_EXE_CPP = "sparse"
SPARSE_OUTPUT_C_W = "./csv/sparse/temp/sparse_c_w_errors_per_line.csv"
SPARSE_OUTPUT_C_WO = "./csv/sparse/temp/sparse_c_wo_errors_per_line.csv"
SPARSE_OUTPUT_CPP_W = "./csv/sparse/temp/sparse_cpp_w_errors_per_line.csv"
SPARSE_OUTPUT_CPP_WO = "./csv/sparse/temp/sparse_cpp_wo_errors_per_line.csv"
SPARSE_OPTS = ""
SPARSE_OUT_SUBDEFECTS = "./csv/sparse/sparse_out_subdefects.csv"
SPARSE_OUT_DEFECTS = "./csv/sparse/sparse_out_defects.csv"
SPARSE_OUT_TOTAL = "./csv/sparse/sparse_out_total.csv"
SPARSE_OUT_CPP_SUBDEFECTS = "./csv/sparse/sparse_out_cpp_subdefects.csv"
SPARSE_OUT_CPP_DEFECTS = "./csv/sparse/sparse_out_cpp_defects.csv"
SPARSE_OUT_CPP_TOTAL = "./csv/sparse/sparse_out_cpp_total.csv"


# ## UNO
UNO = "./bash/uno.sh"
UNO_EXE = "uno"
UNO_EXE_CPP = "uno"
UNO_OUTPUT_C_W = "./csv/uno/temp/uno_c_w_errors_per_line.csv"
UNO_OUTPUT_C_WO = "./csv/uno/temp/uno_c_wo_errors_per_line.csv"
UNO_OUTPUT_CPP_W = "./csv/uno/temp/uno_cpp_w_errors_per_line.csv"
UNO_OUTPUT_CPP_WO = "./csv/uno/temp/uno_cpp_wo_errors_per_line.csv"
UNO_OPTS = ""
UNO_OUT_SUBDEFECTS = "./csv/uno/uno_out_subdefects.csv"
UNO_OUT_DEFECTS = "./csv/uno/uno_out_defects.csv"
UNO_OUT_TOTAL = "./csv/uno/uno_out_total.csv"
UNO_OUT_CPP_SUBDEFECTS = "./csv/uno/uno_out_cpp_subdefects.csv"
UNO_OUT_CPP_DEFECTS = "./csv/uno/uno_out_cpp_defects.csv"
UNO_OUT_CPP_TOTAL = "./csv/uno/uno_out_cpp_total.csv"


# ## FLAWFINDER
FLAWFINDER = "./python/flawfinder.py"
FLAWFINDER_EXE = "flawfinder"
FLAWFINDER_OUTPUT_C_W = "./csv/flawfinder/temp/flawfinder_c_w_errors_per_line.csv"
FLAWFINDER_OUTPUT_C_WO = "./csv/flawfinder/temp/flawfinder_c_wo_errors_per_line.csv"
FLAWFINDER_OUTPUT_CPP_W = "./csv/flawfinder/temp/flawfinder_cpp_w_errors_per_line.csv"
FLAWFINDER_OUTPUT_CPP_WO = "./csv/flawfinder/temp/flawfinder_cpp_wo_errors_per_line.csv"
FLAWFINDER_OPTS = ""
FLAWFINDER_OUT_SUBDEFECTS = "./csv/flawfinder/flawfinder_out_subdefects.csv"
FLAWFINDER_OUT_DEFECTS = "./csv/flawfinder/flawfinder_out_defects.csv"
FLAWFINDER_OUT_TOTAL = "./csv/flawfinder/flawfinder_out_total.csv"
FLAWFINDER_OUT_CPP_SUBDEFECTS = "./csv/flawfinder/flawfinder_out_cpp_subdefects.csv"
FLAWFINDER_OUT_CPP_DEFECTS = "./csv/flawfinder/flawfinder_out_cpp_defects.csv"
FLAWFINDER_OUT_CPP_TOTAL = "./csv/flawfinder/flawfinder_out_cpp_total.csv"


# ## INFER
INFER = "./python/infer.py"
INFER_EXE = "infer"
INFER_OUTPUT_C_W = "./csv/infer/temp/infer_c_w_errors_per_line.csv"
INFER_OUTPUT_C_WO = "./csv/infer/temp/infer_c_wo_errors_per_line.csv"
INFER_OUTPUT_CPP_W = "./csv/infer/temp/infer_cpp_w_errors_per_line.csv"
INFER_OUTPUT_CPP_WO = "./csv/infer/temp/infer_cpp_wo_errors_per_line.csv"
INFER_OPTS = ""
INFER_OUT_SUBDEFECTS = "./csv/infer/infer_out_subdefects.csv"
INFER_OUT_DEFECTS = "./csv/infer/infer_out_defects.csv"
INFER_OUT_TOTAL = "./csv/infer/infer_out_total.csv"
INFER_OUT_CPP_SUBDEFECTS = "./csv/infer/infer_out_cpp_subdefects.csv"
INFER_OUT_CPP_DEFECTS = "./csv/infer/infer_out_cpp_defects.csv"
INFER_OUT_CPP_TOTAL = "./csv/infer/infer_out_cpp_total.csv"


# ## CLANALYZE
CLANALYZE = "./python/clanalyze.py"
CLANALYZE_EXE = "cl /analyze"
CLANALYZE_OUTPUT_C_W = "./csv/clanalyze/temp/clanalyze_c_w_errors_per_line.csv"
CLANALYZE_OUTPUT_C_WO = "./csv/clanalyze/temp/clanalyze_c_wo_errors_per_line.csv"
CLANALYZE_OUTPUT_CPP_W = "./csv/clanalyze/temp/clanalyze_cpp_w_errors_per_line.csv"
CLANALYZE_OUTPUT_CPP_WO = "./csv/clanalyze/temp/clanalyze_cpp_wo_errors_per_line.csv"
CLANALYZE_OPTS = ""
CLANALYZE_OUT_SUBDEFECTS = "./csv/clanalyze/clanalyze_out_subdefects.csv"
CLANALYZE_OUT_DEFECTS = "./csv/clanalyze/clanalyze_out_defects.csv"
CLANALYZE_OUT_TOTAL = "./csv/clanalyze/clanalyze_out_total.csv"
CLANALYZE_OUT_CPP_SUBDEFECTS = "./csv/clanalyze/clanalyze_out_cpp_subdefects.csv"
CLANALYZE_OUT_CPP_DEFECTS = "./csv/clanalyze/clanalyze_out_cpp_defects.csv"
CLANALYZE_OUT_CPP_TOTAL = "./csv/clanalyze/clanalyze_out_cpp_total.csv"

# ## SPLINT
SPLINT = "./python/splint.py"
SPLINT_EXE = "splint"
SPLINT_OUTPUT_C_W = "./csv/splint/temp/splint_c_w_errors_per_line.csv"
SPLINT_OUTPUT_C_WO = "./csv/splint/temp/splint_c_wo_errors_per_line.csv"
SPLINT_OUTPUT_CPP_W = "./csv/splint/temp/splint_cpp_w_errors_per_line.csv"
SPLINT_OUTPUT_CPP_WO = "./csv/splint/temp/splint_cpp_wo_errors_per_line.csv"
SPLINT_OPTS = ""
SPLINT_OUT_SUBDEFECTS = "./csv/splint/splint_out_subdefects.csv"
SPLINT_OUT_DEFECTS = "./csv/splint/splint_out_defects.csv"
SPLINT_OUT_TOTAL = "./csv/splint/splint_out_total.csv"
SPLINT_OUT_CPP_SUBDEFECTS = "./csv/splint/splint_out_cpp_subdefects.csv"
SPLINT_OUT_CPP_DEFECTS = "./csv/splint/splint_out_cpp_defects.csv"
SPLINT_OUT_CPP_TOTAL = "./csv/splint/splint_out_cpp_total.csv"

# ## FRAMAC
FRAMAC = "./python/framac.py"
FRAMAC_EXE = "frama-c"
FRAMAC_EXE_CPP = "frama-c"
FRAMAC_OUTPUT_C_W = "./csv/framac/temp/framac_c_w_errors_per_line.csv"
FRAMAC_OUTPUT_C_WO = "./csv/framac/temp/framac_c_wo_errors_per_line.csv"
FRAMAC_OUTPUT_CPP_W = "./csv/framac/temp/framac_cpp_w_errors_per_line.csv"
FRAMAC_OUTPUT_CPP_WO = "./csv/framac/temp/framac_cpp_wo_errors_per_line.csv"
FRAMAC_OPTS = ""
FRAMAC_OUT_SUBDEFECTS = "./csv/framac/framac_out_subdefects.csv"
FRAMAC_OUT_DEFECTS = "./csv/framac/framac_out_defects.csv"
FRAMAC_OUT_TOTAL = "./csv/framac/framac_out_total.csv"
FRAMAC_OUT_CPP_SUBDEFECTS = "./csv/framac/framac_out_cpp_subdefects.csv"
FRAMAC_OUT_CPP_DEFECTS = "./csv/framac/framac_out_cpp_defects.csv"
FRAMAC_OUT_CPP_TOTAL = "./csv/framac/framac_out_cpp_total.csv"


def make_dirs_forgive(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        print("Already exists: " + path)

def prepare_dirs():
    print("Preparing folders\n")
    make_dirs_forgive(os.path.join(".", "csv", "setup", "temp"))
    make_dirs_forgive(os.path.join(".", "csv", "cppcheck", "temp"))
    make_dirs_forgive(os.path.join(".", "csv", "clanalyze", "temp"))
    make_dirs_forgive(os.path.join(".", "csv", "sparse", "temp"))
    make_dirs_forgive(os.path.join(".", "csv", "uno", "temp"))
    make_dirs_forgive(os.path.join(".", "csv", "clangalpha", "temp"))
    make_dirs_forgive(os.path.join(".", "csv", "clangcore", "temp"))
    make_dirs_forgive(os.path.join(".", "csv", "flawfinder", "temp"))
    make_dirs_forgive(os.path.join(".", "csv", "infer", "temp"))
    make_dirs_forgive(os.path.join(".", "csv", "splint", "temp"))
    make_dirs_forgive(os.path.join(".", "csv", "framac", "temp"))
    make_dirs_forgive(os.path.join(".", "csv", "cpplint", "temp"))
    make_dirs_forgive(os.path.join(".", "csv", "oclint", "temp"))

def call_python(args):
    python.system.system_call("python3 " + " ".join(args))

def run_cppcheck():
    print("Running cppcheck")
    call_python([CPPCHECK, W_C_DEFECTS_DIR, CPPCHECK_OUTPUT_C_W, CPPCHECK_EXE, CPPCHECK_OPTS])
    call_python([CPPCHECK, WO_C_DEFECTS_DIR, CPPCHECK_OUTPUT_C_WO, CPPCHECK_EXE, CPPCHECK_OPTS])
    call_python([STATISTICS, C_MERGE_FILE, CPPCHECK_OUTPUT_C_W, CPPCHECK_OUTPUT_C_WO, CPPCHECK_OUT_SUBDEFECTS, CPPCHECK_OUT_DEFECTS, CPPCHECK_OUT_TOTAL])
    call_python([CPPCHECK, W_CPP_DEFECTS_DIR, CPPCHECK_OUTPUT_CPP_W, CPPCHECK_EXE_CPP, CPPCHECK_OPTS])
    call_python([CPPCHECK, WO_CPP_DEFECTS_DIR, CPPCHECK_OUTPUT_CPP_WO, CPPCHECK_EXE_CPP, CPPCHECK_OPTS])
    call_python([STATISTICS, CPP_MERGE_FILE, CPPCHECK_OUTPUT_CPP_W, CPPCHECK_OUTPUT_CPP_WO, CPPCHECK_OUT_CPP_SUBDEFECTS, CPPCHECK_OUT_CPP_DEFECTS, CPPCHECK_OUT_CPP_TOTAL])

def run_cpplint():
    print("Running cpplint")
    call_python([CPPLINT, W_C_DEFECTS_DIR, CPPLINT_OUTPUT_C_W, CPPLINT_EXE, CPPLINT_OPTS])
    call_python([CPPLINT, WO_C_DEFECTS_DIR, CPPLINT_OUTPUT_C_WO, CPPLINT_EXE, CPPLINT_OPTS])
    call_python([STATISTICS, C_MERGE_FILE, CPPLINT_OUTPUT_C_W, CPPLINT_OUTPUT_C_WO, CPPLINT_OUT_SUBDEFECTS, CPPLINT_OUT_DEFECTS, CPPLINT_OUT_TOTAL])
    call_python([CPPLINT, W_CPP_DEFECTS_DIR, CPPLINT_OUTPUT_CPP_W, CPPLINT_EXE_CPP, CPPLINT_OPTS])
    call_python([CPPLINT, WO_CPP_DEFECTS_DIR, CPPLINT_OUTPUT_CPP_WO, CPPLINT_EXE_CPP, CPPLINT_OPTS])
    call_python([STATISTICS, CPP_MERGE_FILE, CPPLINT_OUTPUT_CPP_W, CPPLINT_OUTPUT_CPP_WO, CPPLINT_OUT_CPP_SUBDEFECTS, CPPLINT_OUT_CPP_DEFECTS, CPPLINT_OUT_CPP_TOTAL])

def run_oclint():
    print("Running oclint")
    call_python([OCLINT, W_C_DEFECTS_DIR, OCLINT_OUTPUT_C_W, OCLINT_EXE, OCLINT_OPTS])
    call_python([OCLINT, WO_C_DEFECTS_DIR, OCLINT_OUTPUT_C_WO, OCLINT_EXE, OCLINT_OPTS])
    call_python([STATISTICS, C_MERGE_FILE, OCLINT_OUTPUT_C_W, OCLINT_OUTPUT_C_WO, OCLINT_OUT_SUBDEFECTS, OCLINT_OUT_DEFECTS, OCLINT_OUT_TOTAL])
    call_python([OCLINT, W_CPP_DEFECTS_DIR, OCLINT_OUTPUT_CPP_W, OCLINT_EXE_CPP, OCLINT_OPTS])
    call_python([OCLINT, WO_CPP_DEFECTS_DIR, OCLINT_OUTPUT_CPP_WO, OCLINT_EXE_CPP, OCLINT_OPTS])
    call_python([STATISTICS, CPP_MERGE_FILE, OCLINT_OUTPUT_CPP_W, OCLINT_OUTPUT_CPP_WO, OCLINT_OUT_CPP_SUBDEFECTS, OCLINT_OUT_CPP_DEFECTS, OCLINT_OUT_CPP_TOTAL])
    
def run_framac():
    print("Running framac")
    call_python([FRAMAC, W_C_DEFECTS_DIR, FRAMAC_OUTPUT_C_W, FRAMAC_EXE, FRAMAC_OPTS])
    call_python([FRAMAC, WO_C_DEFECTS_DIR, FRAMAC_OUTPUT_C_WO, FRAMAC_EXE, FRAMAC_OPTS])
    call_python([STATISTICS, C_MERGE_FILE, FRAMAC_OUTPUT_C_W, FRAMAC_OUTPUT_C_WO, FRAMAC_OUT_SUBDEFECTS, FRAMAC_OUT_DEFECTS, FRAMAC_OUT_TOTAL])
    call_python([FRAMAC, W_CPP_DEFECTS_DIR, FRAMAC_OUTPUT_CPP_W, FRAMAC_EXE_CPP, FRAMAC_OPTS])
    call_python([FRAMAC, WO_CPP_DEFECTS_DIR, FRAMAC_OUTPUT_CPP_WO, FRAMAC_EXE_CPP, FRAMAC_OPTS])
    call_python([STATISTICS, CPP_MERGE_FILE, FRAMAC_OUTPUT_CPP_W, FRAMAC_OUTPUT_CPP_WO, FRAMAC_OUT_CPP_SUBDEFECTS, FRAMAC_OUT_CPP_DEFECTS, FRAMAC_OUT_CPP_TOTAL])
    
def run_sparse():
    print("Running sparse")
    call_python([SPARSE, W_C_DEFECTS_DIR, SPARSE_OUTPUT_C_W, SPARSE_EXE, SPARSE_OPTS]) 
    call_python([SPARSE, WO_C_DEFECTS_DIR, SPARSE_OUTPUT_C_WO, SPARSE_EXE, SPARSE_OPTS]) 
    call_python([STATISTICS, C_MERGE_FILE, SPARSE_OUTPUT_C_W, SPARSE_OUTPUT_C_WO, SPARSE_OUT_SUBDEFECTS, SPARSE_OUT_DEFECTS, SPARSE_OUT_TOTAL])
    call_python([SPARSE, W_CPP_DEFECTS_DIR, SPARSE_OUTPUT_CPP_W, SPARSE_EXE_CPP, SPARSE_OPTS]) 
    call_python([SPARSE, WO_CPP_DEFECTS_DIR, SPARSE_OUTPUT_CPP_WO, SPARSE_EXE_CPP, SPARSE_OPTS])
    call_python([STATISTICS, CPP_MERGE_FILE, SPARSE_OUTPUT_CPP_W, SPARSE_OUTPUT_CPP_WO, SPARSE_OUT_CPP_SUBDEFECTS, SPARSE_OUT_CPP_DEFECTS, SPARSE_OUT_CPP_TOTAL])

def run_uno():
    print("Running uno")
    call_python([UNO, W_C_DEFECTS_DIR, UNO_OUTPUT_C_W, UNO_EXE, UNO_OPTS]) 
    call_python([UNO, WO_C_DEFECTS_DIR, UNO_OUTPUT_C_WO, UNO_EXE, UNO_OPTS]) 
    call_python([STATISTICS, C_MERGE_FILE, UNO_OUTPUT_C_W, UNO_OUTPUT_C_WO, UNO_OUT_SUBDEFECTS, UNO_OUT_DEFECTS, UNO_OUT_TOTAL])
    call_python([UNO, W_CPP_DEFECTS_DIR, UNO_OUTPUT_CPP_W, UNO_EXE_CPP, UNO_OPTS]) 
    call_python([UNO, WO_CPP_DEFECTS_DIR, UNO_OUTPUT_CPP_WO, UNO_EXE_CPP, UNO_OPTS])
    call_python([STATISTICS, CPP_MERGE_FILE, UNO_OUTPUT_CPP_W, UNO_OUTPUT_CPP_WO, UNO_OUT_CPP_SUBDEFECTS, UNO_OUT_CPP_DEFECTS, UNO_OUT_CPP_TOTAL])

def run_flawfinder():
    print("Running flawfinder")
    call_python([FLAWFINDER, W_C_DEFECTS_DIR, FLAWFINDER_OUTPUT_C_W, FLAWFINDER_EXE, FLAWFINDER_OPTS]) 
    call_python([FLAWFINDER, WO_C_DEFECTS_DIR, FLAWFINDER_OUTPUT_C_WO, FLAWFINDER_EXE, FLAWFINDER_OPTS]) 
    call_python([STATISTICS, C_MERGE_FILE, FLAWFINDER_OUTPUT_C_W, FLAWFINDER_OUTPUT_C_WO, FLAWFINDER_OUT_SUBDEFECTS, FLAWFINDER_OUT_DEFECTS, FLAWFINDER_OUT_TOTAL])
    call_python([FLAWFINDER, W_CPP_DEFECTS_DIR, FLAWFINDER_OUTPUT_CPP_W, FLAWFINDER_EXE, FLAWFINDER_OPTS]) 
    call_python([FLAWFINDER, WO_CPP_DEFECTS_DIR, FLAWFINDER_OUTPUT_CPP_WO, FLAWFINDER_EXE, FLAWFINDER_OPTS])
    call_python([STATISTICS, CPP_MERGE_FILE, FLAWFINDER_OUTPUT_CPP_W, FLAWFINDER_OUTPUT_CPP_WO, FLAWFINDER_OUT_CPP_SUBDEFECTS, FLAWFINDER_OUT_CPP_DEFECTS, FLAWFINDER_OUT_CPP_TOTAL])

def run_splint():
    print("Running splint")
    call_python([SPLINT, W_C_DEFECTS_DIR, SPLINT_OUTPUT_C_W, SPLINT_EXE, SPLINT_OPTS]) 
    call_python([SPLINT, WO_C_DEFECTS_DIR, SPLINT_OUTPUT_C_WO, SPLINT_EXE, SPLINT_OPTS]) 
    call_python([STATISTICS, C_MERGE_FILE, SPLINT_OUTPUT_C_W, SPLINT_OUTPUT_C_WO, SPLINT_OUT_SUBDEFECTS, SPLINT_OUT_DEFECTS, SPLINT_OUT_TOTAL])
    call_python([SPLINT, W_CPP_DEFECTS_DIR, SPLINT_OUTPUT_CPP_W, SPLINT_EXE, SPLINT_OPTS]) 
    call_python([SPLINT, WO_CPP_DEFECTS_DIR, SPLINT_OUTPUT_CPP_WO, SPLINT_EXE, SPLINT_OPTS])
    call_python([STATISTICS, CPP_MERGE_FILE, SPLINT_OUTPUT_CPP_W, SPLINT_OUTPUT_CPP_WO, SPLINT_OUT_CPP_SUBDEFECTS, SPLINT_OUT_CPP_DEFECTS, SPLINT_OUT_CPP_TOTAL])

def run_clang_core():
    print("Running clang-core")
    call_python([CLANG_CORE, W_C_DEFECTS_DIR, CLANG_CORE_OUTPUT_C_W, CLANG_CORE_EXE, CLANG_CORE_OPTS]) 
    call_python([CLANG_CORE, WO_C_DEFECTS_DIR, CLANG_CORE_OUTPUT_C_WO, CLANG_CORE_EXE, CLANG_CORE_OPTS]) 
    call_python([STATISTICS, C_MERGE_FILE, CLANG_CORE_OUTPUT_C_W, CLANG_CORE_OUTPUT_C_WO, CLANG_CORE_OUT_SUBDEFECTS, CLANG_CORE_OUT_DEFECTS, CLANG_CORE_OUT_TOTAL])
    call_python([CLANG_CORE_PP, W_CPP_DEFECTS_DIR, CLANG_CORE_OUTPUT_CPP_W, CLANG_CORE_EXE_CPP, CLANG_CORE_OPTS]) 
    call_python([CLANG_CORE_PP, WO_CPP_DEFECTS_DIR, CLANG_CORE_OUTPUT_CPP_WO, CLANG_CORE_EXE_CPP, CLANG_CORE_OPTS])
    call_python([STATISTICS, CPP_MERGE_FILE, CLANG_CORE_OUTPUT_CPP_W, CLANG_CORE_OUTPUT_CPP_WO, CLANG_CORE_OUT_CPP_SUBDEFECTS, CLANG_CORE_OUT_CPP_DEFECTS, CLANG_CORE_OUT_CPP_TOTAL])

def run_clang_alpha():
    print("Running clang-alpha")
    call_python([CLANG_ALPHA, W_C_DEFECTS_DIR, CLANG_ALPHA_OUTPUT_C_W, CLANG_ALPHA_EXE, CLANG_ALPHA_OPTS]) 
    call_python([CLANG_ALPHA, WO_C_DEFECTS_DIR, CLANG_ALPHA_OUTPUT_C_WO, CLANG_ALPHA_EXE, CLANG_ALPHA_OPTS]) 
    call_python([STATISTICS, C_MERGE_FILE, CLANG_ALPHA_OUTPUT_C_W, CLANG_ALPHA_OUTPUT_C_WO, CLANG_ALPHA_OUT_SUBDEFECTS, CLANG_ALPHA_OUT_DEFECTS, CLANG_ALPHA_OUT_TOTAL])
    call_python([CLANG_ALPHA_PP, W_CPP_DEFECTS_DIR, CLANG_ALPHA_OUTPUT_CPP_W, CLANG_ALPHA_EXE_CPP, CLANG_ALPHA_OPTS])
    call_python([CLANG_ALPHA_PP, WO_CPP_DEFECTS_DIR, CLANG_ALPHA_OUTPUT_CPP_WO, CLANG_ALPHA_EXE_CPP, CLANG_ALPHA_OPTS])
    call_python([STATISTICS, CPP_MERGE_FILE, CLANG_ALPHA_OUTPUT_CPP_W, CLANG_ALPHA_OUTPUT_CPP_WO, CLANG_ALPHA_OUT_CPP_SUBDEFECTS, CLANG_ALPHA_OUT_CPP_DEFECTS, CLANG_ALPHA_OUT_CPP_TOTAL])

def run_infer():
    print("Running infer")
    call_python([INFER, W_C_DEFECTS_DIR, INFER_OUTPUT_C_W, INFER_EXE]) 
    call_python([INFER, WO_C_DEFECTS_DIR, INFER_OUTPUT_C_WO, INFER_EXE]) 
    call_python([STATISTICS, C_MERGE_FILE, INFER_OUTPUT_C_W, INFER_OUTPUT_C_WO, INFER_OUT_SUBDEFECTS, INFER_OUT_DEFECTS, INFER_OUT_TOTAL])
    call_python([INFER, W_CPP_DEFECTS_DIR, INFER_OUTPUT_CPP_W, INFER_EXE]) 
    call_python([INFER, WO_CPP_DEFECTS_DIR, INFER_OUTPUT_CPP_WO, INFER_EXE])
    call_python([STATISTICS, CPP_MERGE_FILE, INFER_OUTPUT_CPP_W, INFER_OUTPUT_CPP_WO, INFER_OUT_CPP_SUBDEFECTS, INFER_OUT_CPP_DEFECTS, INFER_OUT_CPP_TOTAL])

def run_clanalyze():
    print("Running cl /analyze")
    python.clanalyze.clanalyze(W_C_DEFECTS_DIR, CLANALYZE_OUTPUT_C_W, CLANALYZE_EXE, CLANALYZE_OPTS)
    python.clanalyze.clanalyze(WO_C_DEFECTS_DIR, CLANALYZE_OUTPUT_C_WO, CLANALYZE_EXE, CLANALYZE_OPTS) 
#    call_python([CLANALYZE, W_C_DEFECTS_DIR, CLANALYZE_OUTPUT_C_W, CLANALYZE_EXE, CLANALYZE_OPTS]) 
#    call_python([CLANALYZE, WO_C_DEFECTS_DIR, CLANALYZE_OUTPUT_C_WO, CLANALYZE_EXE, CLANALYZE_OPTS]) 
    call_python([STATISTICS, C_MERGE_FILE, CLANALYZE_OUTPUT_C_W, CLANALYZE_OUTPUT_C_WO, CLANALYZE_OUT_SUBDEFECTS, CLANALYZE_OUT_DEFECTS, CLANALYZE_OUT_TOTAL])
    python.clanalyze.clanalyze(W_CPP_DEFECTS_DIR, CLANALYZE_OUTPUT_CPP_W, CLANALYZE_EXE, CLANALYZE_OPTS) 
    python.clanalyze.clanalyze(WO_CPP_DEFECTS_DIR, CLANALYZE_OUTPUT_CPP_WO, CLANALYZE_EXE, CLANALYZE_OPTS)
#    call_python([CLANALYZE, W_CPP_DEFECTS_DIR, CLANALYZE_OUTPUT_CPP_W, CLANALYZE_EXE, CLANALYZE_OPTS]) 
#    call_python([CLANALYZE, WO_CPP_DEFECTS_DIR, CLANALYZE_OUTPUT_CPP_WO, CLANALYZE_EXE, CLANALYZE_OPTS])
    call_python([STATISTICS, CPP_MERGE_FILE, CLANALYZE_OUTPUT_CPP_W, CLANALYZE_OUTPUT_CPP_WO, CLANALYZE_OUT_CPP_SUBDEFECTS, CLANALYZE_OUT_CPP_DEFECTS, CLANALYZE_OUT_CPP_TOTAL])

def clean_temp():
    python.system.system_call("rm -rf ./csv/temp/")
    python.system.system_call("rm -f ./csv/clanalyze/*.csv")
    python.system.system_call("rm -f ./csv/clanalyze/temp/*.csv")
    python.system.system_call("rm -f ./csv/cppcheck/*.csv")
    python.system.system_call("rm -f ./csv/cppcheck/temp/*.csv")
    python.system.system_call("rm -f ./csv/clangcore/*.csv")
    python.system.system_call("rm -f ./csv/clangcore/temp/*.csv")
    python.system.system_call("rm -f ./csv/clangalpha/*.csv")
    python.system.system_call("rm -f ./csv/clangalpha/temp/*.csv")
    python.system.system_call("rm -f ./csv/infer/*.csv")
    python.system.system_call("rm -f ./csv/infer/temp/*.csv")
    python.system.system_call("rm -f ./csv/flawfinder/*.csv")
    python.system.system_call("rm -f ./csv/flawfinder/temp/*.csv")

action = sys.argv[1]
if action == 'prepare_dirs':
    prepare_dirs()
elif action == "clean":
    clean_temp()
elif action == 'statistics':
    print("Running all statistics")
    run_cppcheck()
    run_sparse()
    run_uno()
    run_infer()
    run_splint()
    run_flawfinder()
    run_clang_core()
    run_clang_alpha()
    run_clanalyze()
elif action == 'cppcheck':
    run_cppcheck()
elif action == 'clanalyze':
    run_clanalyze()
elif action == 'sparse':
    run_sparse()
elif action == "uno":
    run_uno()
elif action == 'infer':
    run_infer()
elif action == 'splint':
    run_splint()
elif action == "flawfinder":
    run_flawfinder()
elif action == 'clang-core':
    run_clang_core()
elif action == "clang-alpha":
    run_clang_alpha()
elif action == 'framac':
    run_framac()
elif action == 'cpplint':
    run_cpplint()
elif action == 'oclint':
    run_oclint()
else:
    print("Action ", action, " not supported.\n")
