#!/bin/bash

BASE_DIR="/home/hanna_julienne/bucket/"

jass_preprocessing --gwas-info $BASE_DIR/meta_HGI.csv --ref-path $BASE_DIR/ref_panel/chr22.bim --input-folder $BASE_DIR/sumstat/ --diagnostic-folder $BASE_DIR/diag/ --output-folder-1-file $BASE_DIR/z_score/ --output-folder $BASE_DIR/z_score_chr/ --minimum-MAF 0

raiss --chrom chr22 --gwas COVID_FINNGEN --ref-folder $BASE_DIR/ref_panel/ --ld-folder $BASE_DIR/ld/ --zscore-folder $BASE_DIR/z_score_chr/ --output-folder $BASE_DIR/z_score_imputed --ld-type scipy --ref-panel-suffix .bim


python3 test_performance.py $BASE_DIR COVID_FINNGEN
