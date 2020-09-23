#!/bin/bash
x-www-browser https://github.com/RicardoPineda2301/Data-Product/tree/master/Tarea_Streamlit

echo "Tiene Anaconda instalado?"
select yn in "Si" "No"; do
    case $yn in
        Si ) break;;
        No ) x-www-browser https://phoenixnap.com/kb/how-to-install-anaconda-ubuntu-18-04-or-20-04; exit;;
    esac
done

echo "Se instalará: streamlit, pandas y numpy"


conda create --name Tarea_Streamlit
conda activate Tarea_Streamlit
sudo apt-get install python3-pip -y
pip install streamlit pandas numpy

read -p "Presione cualquier tecla para correr 'first_app' "

streamlit run first_app.py

read -p "Presione cualquier tecla para correr 'uber_pickups' "

streamlit run uber_pickups.py

read -p "Presione cualquier tecla para cerrar esta terminal"
