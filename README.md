### This template aims to create a boilerplate for Machine Learning tasks
# Machine Learning - project-template
Machine Learning project template

## STEPS -

### STEP 01- Create a repository by using template repository

### STEP 02- Clone the new repository

### STEP 03- Create a conda environment after opening the repository in VSCODE

```bash
conda create --prefix ./env python=3.8 -y
```

```bash
conda activate ./env
```
OR
```bash
source activate ./env
```

### STEP 04- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 05 - Create conda.yaml file
```bash
conda env export > conda.yaml
```

### STEP 06- Commit and push the changes to the remote repository


### STEP 07- Run the command for initializing the repository with all required libraries
```bash
bash init_setup.sh
```

### STEP 08- Run the below command in bash for the first time to have the initial setup done
```bash
mlflow run . --no-conda
```
