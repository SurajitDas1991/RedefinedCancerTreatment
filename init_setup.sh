echo [$(date)]: "START"
echo [$(date)]: "creating environment"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activate environment"
source activate ./env
echo [$(date)]: "install requirements"
pip install -r requirements.txt
echo [$(date)]: "install ML libraries"
pip install tensorflow
echo [$(date)]: "Create conda yaml file"
conda env export > conda.yaml
echo [$(date)]: "END"