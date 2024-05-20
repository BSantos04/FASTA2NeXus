import sys

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
    But fisrt we need to parse the command line arguments.
    We will raise an exception if the command line arguments doesn`t correspond with the asked.
    """
    if len(sys.argv) !=3:
        print("Try this instead: python3 FASTA2NeXus.py {.fasta file/input file} {.nex file/output file}")
    else:
        fasta_dict=fasta_to_dict(sys.argv[1])
        header=nexus_header(fasta_dict)
        print(nexus_converter(header, fasta_dict)) 
        output_file = sys.argv[2]
        with open(output_file, "w") as out:
            out.write(nexus_converter(header, fasta_dict))
        print("\n\n\nNeXus file saved sucessfully!\nGo check the file on your directory.")
    
if __name__=="__main__":
    """
    Just ensuring the code is only executed when the script is run as a standalone program.
    """
    main()
    
