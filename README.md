# Install Cplex for Python 3.11

# How to install cplex for python 3.11

<b>Step 1. install cplex using pip</b>

Once you have CPLEX for old version python, 

&nbsp;&nbsp;&nbsp;&nbsp;Uninstall it first. Run this code in your command prompt `pip uninstall cplex`. 

&nbsp;&nbsp;&nbsp;&nbsp;Then run this code in your command prompt `pip install cplex`.

If you don't have CPLEX package in your python, run this code in your command prompt `pip install cplex`.  
<br/><br/>
<b>Step 2. install docplex using pip</b>

The procedures are the same as step 1. use this code `pip install docplex`.

<b>Note: these libraries provided by pip are community edition.</b>

# Once you have cplex product with unlimited use after installation
Connect your cplex on your PC into python cplex as the following:
<br/>
<b>Step 1. Download this python file provided by IBM</b>  
https://www.ibm.com/support/pages/system/files/inline-files/make_full.py_.zip
<br/><br/>
<b>Step 2. Unzip it and then run python file in your command prompt.</b>  
Move to the directory where the python file exists.  
Then run this code `python make_full.py 'C:\Program Files\IBM\ILOG\CPLEX_Studio2211'`.
Note that the path is your cplex location.
<br/><br/>
<b>Once you fail to do step 2, copy these two files into python libraries path by hand.</b>
<br/><br/>
File 1: cplex2211.dll, copy and paste it into two locations  
&nbsp;&nbsp;&nbsp;&nbsp;path for copy: C:\\Program Files\\IBM\\ILOG\\CPLEX_Studio2211\\cplex\\bin\\x64_win64\\cplex2211.dll  
&nbsp;&nbsp;&nbsp;&nbsp;path for paste 1 : "your python path"\\Python\\envs\\arcgispro-py3\\Lib\\site-packages\\cplex\\_internal\\cplex2211.dll  
&nbsp;&nbsp;&nbsp;&nbsp;path for paste 2 : "your python path"\\Python\\envs\\arcgispro-py3\\Scripts\\cplex2211.dll  
<br/>
File 2: cpoptimizer.exe, copy and paste it into two locations  
&nbsp;&nbsp;&nbsp;&nbsp;path for paste : "your python path"\\Python\\envs\\arcgispro-py3\\Scripts\\cpoptimizer.exe



# Official support page regarding cplex for python 3.11
https://www.ibm.com/support/pages/node/7160884

