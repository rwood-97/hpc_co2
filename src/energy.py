import pandas as pd

def get_energy_cpu(row, cluster_info):
	"""Calculate CPU energy consumption in kWh."""
	constraints = row["Constraints"]
	if pd.isna(constraints):
		tdp_w = float(cluster_info["partitions"]["baskerville-all"]["CPU_TDP"])
	else:
		tdp_w = float(cluster_info["partitions"][f"baskerville-{constraints}"]["CPU_TDP"])
	energy_kwh = (row["Run Time (sec)"] / 3600) * row["Number of cores"] * (tdp_w / 1000) #kWh 
	return energy_kwh

def get_energy_gpu(row, cluster_info):
	"""Calculate GPU energy consumption in kWh."""
	constraints = row["Constraints"]
	if pd.isna(constraints):
		tdp_w = float(cluster_info["partitions"]["baskerville-all"]["TDP"])
	else:
		tdp_w = float(cluster_info["partitions"][f"baskerville-{constraints}"]["TDP"])
	energy_kwh = (row["Run Time (sec)"] / 3600) * row["Number of GPU"] * (tdp_w / 1000) #kWh
	return energy_kwh

def get_energy_mem(row, cluster_info):
	"""Calculate memory energy consumption in kWh."""
	power_memory_perGB=0.3725 # W/GB (ref: https://github.com/GreenAlgorithms/GreenAlgorithms4HPC/blob/main/data/fixed_parameters.yaml)
	energy_kwh = (row["Run Time (sec)"] / 3600) * row["Memory (GB)"] * (power_memory_perGB / 1000) #kWh
	return energy_kwh