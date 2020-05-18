# Code to work with the Mitutoyo Roundness machine RA2200

This is repository for code to work with and analyse files generated by the Mitutoyo ROUNDPAK software on the RA2200 roundness machine.

There is previous code in `I:\MSL\Private\LENGTH\Roundness and Talyrond\Mitutoyo 2015` which will be pulled across to here and fixed as needed.

Functions working
roundness.processing.read_roundpak 
    read_result, 
    read_result_list

reorganised folder structure so that notebooks, data, docs, results see under a project folder under `ls_RA2200` and alongside the package folder `roundness`. This is a better structure for multiple projects that will use one code base. 
```
C:.
C:.
├───.pytest_cache
│   └───v
│       └───cache
├───.vscode
├───flick_stds_2020-05
│   ├───data
│   │   └───raw
│   │       └───verrification
│   ├───docs
│   ├───notebooks
│   │   └───__pycache__
│   └───results
│       └───figures
├───roundness
│   ├───analysis
│   ├───processing
│   │   └───__pycache__
│   ├───tests
│   ├───visualisation
│   └───__pycache__
└───roundness.egg-info
```
Note the config.py file that sets data and result folders is now under notebooks. There may be reason to have project specific code (for example a `do_all_analyis.py` file) in the `/flick_stds_2020-05` folder that would need to know where the data is. This could either `import notebooks.config` or recreate.