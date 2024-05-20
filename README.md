# FASTA2NeXus
Converts FASTA file into NeXus files.
This repository also contains the unit tests for each one of the functions written in the script.
## Motivation
This script was proposed in the curricular unit of Biological Sequences Analysis of the Bioinformatics course. 
## Requisities
-Python3
## Usage
### FASTA2NeXus.py
`python3 FATSA2NeXus.py {FASTA file/input file} {NeXus file/output file}(optional)` 
#### FASTA file
The input file in the FASTA format. Doesn`t matter if the file does not finish with a ".fasta", the program only have the content in consideration.
#### NeXus file
This one is optional.

If you input another file as an output file, the program will print the NeXus content displayed in the terminal, and print a mesage that warns you that the file was sucessfully created.

If there is no file with the same name the program create the file, otherwise it will overwrite the content into that file.

The same happens with the NeXus file/output file as with the FASTA file/input file, it doesn´t matter if you write .nex at the end of the file or not, the content will be at the NeXus format.
### FASTA2NeXus_unittest.py
`python3 FASTA2NeXus_unittest.py` 
## License
GNU v3 License
