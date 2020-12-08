import raiss
import pandas as pd
import sys

base_dir = sys.argv[1]
code_GWAS = sys.argv[2]
print(sys.argv)
# fi_"{0}/z_score_chr/z_{1}_chr22.txt".format(base_dir, code_GWAS)
# Zscore = pd.read_csv(, sep="\t", index_col=0)
#
# Zscore.head()
# Z_masked = raiss.imputation_R2.generated_test_data(Zscore,20000)
# len(Z_masked[1])
#
# f_out_masked = "{0}/z_score_masked/z_{1}_chr22.txt".format(base_dir, code_GWAS)
# Z_masked[0].to_csv(f_out_masked, sep="\t")


perf_results = raiss.imputation_R2.grid_search("{0}/z_score_chr/".format(base_dir),
                                "{0}/z_score_masked/".format(base_dir),
                                "{0}/z_score_imputed/".format(base_dir),
                                "{0}/ref_panel/".format(base_dir),
                                "{0}/ld/".format(base_dir),
                                code_GWAS, eigen_ratio_grid =[0.1, 0.01, 0.005, 0.001], N_to_mask=10000,
                                ref_panel_suffix = ".bim",
                                ld_type="scipy")

perf_results.to_csv("{0}/imputation_performance/performance_{1}.csv".format(base_dir, code_GWAS))
