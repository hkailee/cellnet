# CellNet

## What is CellNet?

CellNet integrates the CellPhoneDB - a publicly available repository of curated receptors, ligands and its interactions and re-architects the formula by considering normal and tumor groups simultaneously when analysing the interactions between both ligands and receptors. 

Please refer to [existing cellphonedb repository](https://www.cellphonedb.org/)/ 


## Starting to use CellNet 

### Installing CellNet
NOTE: Works with Python v3.5 or superior. If your default Python interpreter is for v2.x (you can check it with `python --version`), calls to `python`/`pip` should be substituted by `python3`/`pip3`.

We highly recommend to use a virtual env (steps 1 and 2) but you can omit.
1. Create python > 3.5 virtual-env
```shell
python -m venv cpdb-venv
```

2. Activate virtual-env
```shell
source cpdb-venv/bin/activate
```

3. Install cellnet
```shell
pip install cellnet
```


## Running CellNet Methods

Please, run step 0 if you didn't activate the virtual-env previously

0. Activate virtual-env
```shell
source cpdb-venv/bin/activate
```


###  Example with running the statistical method
```shell
cellnet method statistical_analysis test_meta.txt test_counts.txt 
```


### Example without using the statistical method
```shell
cellnet method analysis test_meta.txt test_counts.txt 
```


### Method optional parameters

~ **Optional Method parameters**:
- `--project-name`: Name of the project. It creates a subfolder in output folder
- `--iterations`: Number of pvalues analysis iterations [1000]
- `--threshold`: % of cells expressing a gene
- `--result-precision`: Number of decimal digits in results [3]
- `--output-path`: Directory where the results will be allocated (the directory must exist) [out]
- `--means-result-name`: Means result namefile [means.txt]
- `--significant-mean-result-name`: Significant result namefile [significant_means.txt]
- `--deconvoluted-result-name`: Deconvoluted result namefile [deconvoluted.txt]
- `--verbose/--quiet`: Print or hide cellphonedb logs [verbose]

~ **Optional Method Statistical parameters**
- `--pvalues-result-name`: Pvalues result namefile [pvalues.txt]
- `--means-pvalues-result-name`: Pvalues-means result namefile [pvalues_means.txt]
- `--debug-seed`: Debug random seed -1 for disable it. >=0 [-1]
- `--threads`: Number of threads to use. >=1 [-1]

**Usage Examples**:

Set number of iterations and threads
```shell
cellnet method statistical_analysis yourmetafile.txt yourcountsfile.txt --iterations=10 --threads=2
```
Set project subfolder
```shell
cellnet method analysis yourmetafile.txt yourcountsfile.txt --project-name=new_project
```

Set output path
```shell
mkdir custom_folder
cellnet method statistical_analysis yourmetafile.txt yourcountsfile.txt --output-path=custom_folder
```

