import raiss
import pandas as pd


Zscore = pd.read_csv("/home/hjulienn/Project/COVID-19/Imputation_HGI/z_score_chr/z_COVID_FINNGEN_chr22.txt", sep="\t", index_col=0)

Zscore.head()
Z_masked = raiss.imputation_R2.generated_test_data(Zscore,20000)
len(Z_masked[1])

Z_masked[0].to_csv("/home/hjulienn/Project/COVID-19/Imputation_HGI/z_score_masked/z_COVID_FINNGEN_chr22.txt", sep="\t")


perf_results = raiss.imputation_R2.grid_search("/home/hjulienn/Project/COVID-19/Imputation_HGI/z_score_chr/",
                                "/home/hjulienn/Project/COVID-19/Imputation_HGI/z_score_masked/",
                                "/home/hjulienn/Project/COVID-19/Imputation_HGI/z_score_imputed/",
                                "/home/hjulienn/Project/COVID-19/Imputation_HGI/ref_panel/",
                                "/home/hjulienn/Project/COVID-19/Imputation_HGI/ld/",
                                "COVID_FINNGEN", eigen_ratio_grid =[0.1, 0.01, 0.005, 0.001], N_to_mask=20000,
                                ref_panel_suffix = ".bim",
                                ld_type="scipy")

perf_results.to_csv("/home/hjulienn/Project/COVID-19/Imputation_HGI/imputation_test/performance_COVID_FINNGEN.csv")
