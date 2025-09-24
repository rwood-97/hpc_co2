# Turing use of Baskerville HPC CO2 data

## Methodology

The methodology comes from the [Green Algorithms paper](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202100707) and [the GRACE-HPC docs](https://grace-hpc.readthedocs.io/en/latest/methodology.html#usage-based-energy-estimates).

## Requirements

Data you will need:
- `Baskerville_total_commas.csv` (ask me)
- `cluster_info.yaml` (ask me or create your own, the `cluster_info.yaml` format comes from https://github.com/GreenAlgorithms/GreenAlgorithms4HPC/blob/main/data/cluster_info.yaml)

Python dependencies:
- pandas
- matplotlib
- numpy
- pyyaml
- IPython (Jupyter)