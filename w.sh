v_list=$(ls -l ./ |grep ^d | awk '{print $9}')
for j in $v_list
do
#cp INCAR  vasp.sh POTCAR ./${j}
cd ${j}
cp CONTCAR ./POSCAR
(echo 102; echo 2; echo 0.03;echo "") | vaspkit
rm POT* INCAR 
cd ../
cp  INCAR  vasp.sh POTCAR  ./${j}
cd ${j}
#cp CONTCAR ./POSCAR
#vaspkit -task 103
#bsub < vasp.sh
cd ../
done
