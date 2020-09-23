@echo off
REM Se instalará: streamlit, pandas y numpy

:start
cls
start "" https://github.com/RicardoPineda2301/Data-Product/tree/master/Tarea_Streamlit

REM 
set python_ver=3.8

conda create --name Tarea_Streamlit
conda activate Tarea_Streamlit
pip3 install streamlit pandas numpy --user --no-warn-script-location

pause

streamlit run first_app.py

pause 

streamlit run uber_pickups.py

pause
exit