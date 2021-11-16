# Solar-cell-Material-discovery
Setting up a machine-learning model that circumvents performing computaionally expensive dft calculations and accelerates the discovery for the optimal candidates for solar cell applications. The model enables us to predict property of interest bandgap for a perovskite oxide structures, by taking elements and their respective position in the lattices as input. The chemical space of the structures are of the form ABO3.
# 1. Library Generation
The file **Perovskite_doping_Structure_Library.ipynb** creates random library of structures and genrates their respective cif and xyz files and aslo numbers every structure uniquely based on their differences in lattice arrangement. 
The file **folder_sorter.py** rearranges the structures base on their classes(BO3) and structure similarity. For eg BaCaTiO3 will have multiple structures where the positions of Ba and Ca will vary in the unit cell, but their substructures will be grouped under TiO3 folder and every subtructures will have their own folder with cif and xyz files.
The **xyz_modifier_module.py** further rearranges the xyz files based on a set frame of reference decided by the user. This ensures that the information of interatomic positions is correctly captured.

# 2. DFT Calculations
The file **cp2k_input_file.inp** is used to perform the bandgap calculations on CP2K.

# 3. Post DFT
Once the structures are converged we use the **Featurelist.ipynb** notebook for fingerprinting the features, the dataset then generated is further send to the Ml notebook for model development.

# 4. For further reference please refer my thesis

