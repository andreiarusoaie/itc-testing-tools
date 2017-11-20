./count_warnings.sh | grep total | cut -c 1-9 | paste -sd+ - | bc
