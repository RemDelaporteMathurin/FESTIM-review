import subprocess
import timeit
import json


def run_external_script(script_path):
    try:
        subprocess.check_call(['python', script_path])
    except subprocess.CalledProcessError as e:
        print(f"Error running script: {e}")

nb_exec = 1

case_to_path = {
    "ver-1e": 'ver_1e/tmap8_ver1e.py',
    "val-2b": 'val_2b/val_2b.py',
    "ver-1d-diffusion": 'ver_1d/tmap8_diffusion.py'
}

case_to_time = {case: None for case in case_to_path}

for case, path in case_to_path.items():
    time_festim = timeit.timeit(lambda: run_external_script(path), number=nb_exec)
    case_to_time[case] = time_festim/nb_exec

# write results to JSON
with open('comparison_results.json') as f:
    data = json.load(f)

for case, time in case_to_time.items():
    data[case] = {'festim': time, 'tmap': 0}

with open('comparison_results.json', "w") as f:
    json.dump(data, f, indent=4)
