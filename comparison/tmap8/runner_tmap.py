import subprocess
import timeit
import json


def run_external_script(script_path):
    try:
        subprocess.run(['./tmap8-opt', '-i', script_path])
    except subprocess.CalledProcessError as e:
        print(f"Error running the executable: {e}")

nb_exec = 1

case_to_path = {
    "ver-1e": 'ver_1e/ver-1e.i',
    "val-2b": 'val_2b/val-2b.i',
    "ver-1d-diffusion": 'ver_1d/ver-1d-diffusion.i'
}

case_to_time = {case: None for case in case_to_path}

for case, path in case_to_path.items():
    time_festim = timeit.timeit(lambda: run_external_script(path), number=nb_exec)
    case_to_time[case] = time_festim/nb_exec

# write results to JSON
with open('comparison_results.json') as f:
    data = json.load(f)

for case, time in case_to_time.items():
    data[case]['tmap'] = time

with open('comparison_results.json', "w") as f:
    json.dump(data, f, indent=4)
