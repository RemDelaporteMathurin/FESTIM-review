source activate festim
number_exec=10
start_festim=`date +%s%3N`
for ((i = 1; i <= number_exec; i++))
do
    echo "iteration $i"
    python tmap8_diffusion.py
done
end_festim=`date +%s%3N`
elapsed_time_festim=$(( ($end_festim - $start_festim) / $number_exec ))

conda deactivate
source activate moose

start_tmap8=`date +%s%3N`
for ((i = 1; i <= number_exec; i++))
do
    echo "iteration $i"
    ./tmap8-opt -i ./ver-1d-diffusion.i
done
end_tmap8=`date +%s%3N`
elapsed_time_tmap8=$(( ($end_tmap8 - $start_tmap8) / $number_exec ))

echo FESTIM execution time was $elapsed_time_festim miliseconds.
echo TMAP8 execution time was $elapsed_time_tmap8 miliseconds.