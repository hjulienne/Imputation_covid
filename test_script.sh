#!/bin/bash

BASE_DIR="/home/hanna_julienne/bucket/"

jass_preprocessing --gwas-info $BASE_DIR/meta_HGI.csv --ref-path $BASE_DIR/ref_panel/annotation_complete.bim --input-folder $BASE_DIR/sumstats/ --diagnostic-folder $BASE_DIR/diag_preprocessing/ --output-folder-1-file $BASE_DIR/z_scores/ --output-folder $BASE_DIR/z_scores_chr/ --minimum-MAF 0

raiss --chrom chr22 --gwas COVID_FINNGEN --ref-folder $BASE_DIR/ref_panel/ --ld-folder $BASE_DIR/ld/ --zscore-folder $BASE_DIR/z_scores_chr/ --output-folder $BASE_DIR/z_scores_imputed --ld-type scipy --ref-panel-suffix .bim


python3 test_performance.py $BASE_DIR COVID_FINNGEN
