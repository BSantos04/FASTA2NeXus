# FASTA2NeXus
Converts FASTA file into NeXus files.
This repository also contains the unit tests for each one of the functions written in the script.
## Motivation
This script was proposed in the curricular unit of Biological Sequences Analysis of the Bioinformatics course. 
## Requisities
-Python3
## Usage
### FASTA2NeXus.py
`python3 FATSA2NeXus.py {FASTA file/input file} {NeXus file/output file}` 
#### FASTA file
The input file in the FASTA format. Doesn`t matter if the file does not finish with a ".fasta", the program only have the content in consideration.
#### NeXus file
After displaying the content in the NeXus format, the program will save the content in the output file.
The program create the file if there is no file with the same same, otherwise it will overwrite the content into that file.
The same happens with the NeXus file/output file as with the FASTA file/input file, it doesn´t matter if you write .nex at the end of the file or not, the content will be at the NeXus format.
### FASTA2NeXus_unittest.py
`python3 FASTA2NeXus_unittest.py` 
## License
GNU v3 License
