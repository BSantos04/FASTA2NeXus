import argparse

def parse_args():
    """
    Before starting retrieving the sequences, first we need to parse the command line arguments to prevent any future misuse from the user.
    
    For that, we use the method argparse.ArgumentParser() to contain the argument specifications. 
    
    After that, we need to specify the arguments we want to attach to the parser.
    
    In that case, we want to attach the FASTA file we want to use as input.
    
    If the file argument is missing, the terminal will display a message with the required missing argument and exit the program.
    
    If there is any extra argument, the terminal will display the unrecognized arguments and close the program.
    
    Returns the FASTA file as argument from the command line using argparse.Namespace.
    """
    parser=argparse.ArgumentParser()  
    parser.add_argument("fasta_file", help="\nYou didn't selected a FASTA file.")
    return parser.parse_args().fasta_file

def fasta_to_dict(file):
    """
    Takes a FASTA file as argument and returns a dictionary with the sequence names/taxa as the keys and the respective sequences as the values.
    
    Write the FASTA file path as the argument for the function.
    """
    fasta={}
    with open(file) as fasta_file:
        for line in fasta_file:
            line=line.strip()
            if not line:
                continue
            if line.startswith(">"):
                seq_names=line[1:]
                if seq_names not in fasta:
                    fasta[seq_names]=""
                continue
            sequence=line
            fasta[seq_names]+=sequence  
    return fasta

def nexus_header(fasta_dict):
    """
    Accepts the dictionary made from the previous function, returning a Nexus file header based on the inputed dictionary.
    """
    return f"#NEXUS\n\nBEGIN DATA;\nDIMENSIONS NTAX={len(fasta_dict)} NCHAR={len(next(iter(fasta_dict.values())))};\nFORMAT DATATYPE=DNA MISSING=N GAP=-;\nMATRIX\n"


def nexus_converter(header, fasta_dict):
    """
    Accepts the header and the dictionary made from the previous functions, create a NeXus file matrix based on the inputed dictionary content, and then concatenate the header and the matrix, creating the NeXus file content of the inputed FASTA file. 
    """
    matrix = "\n".join([f"   {tax} {seq}" for tax, seq in fasta_dict.items()]) + "\n  ;\nEND;"
    return header + matrix 

def main():
    """
    This function is where everything happens.
    """
    fasta_file=parse_args()
    fasta_dict=fasta_to_dict(fasta_file)
    header=nexus_header(fasta_dict)
    print(nexus_converter(header, fasta_dict)) 
    
if __name__=="__main__":
    """
    Just ensuring the code is only executed when the script is run as a standalone program.
    """
    main()
    