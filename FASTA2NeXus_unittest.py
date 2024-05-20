import unittest
import FASTA2NeXus 

class test_functions(unittest.TestCase):
    """
    Creating a class with all the fuctions we are going to use to test each function form thhe FASTA2NeXus. py script individually.
    
    In order to test the first funvtion (fasta_to_dict()), we are going to create a FASTA file and save it into the same directory we are running the code. 
    
    To make it simple, the file will only contain 1 taxa and a sequence with 9 nucleotides.
    """
    f = open("sequence.fasta", "w")
    f.write("""
>FJ598681
ATGCGCAAA
            """)
    f.close()
        
    def test_fasta_to_dict(self):
        """
        Tests if fasta_to_dict function reads the input FASTA file correctly and returns the expected dictionary.
        
        In that case, we are going to use the sequence.fasta file created in the code above as an input exemple.
        
        """
        self.assertEqual(FASTA2NeXus.fasta_to_dict('sequence.fasta'), {'FJ598681': 'ATGCGCAAA'})
    
    def test_nexus_header(self):
        """
        Tests if nexus_header function create properly the NeXus file header based on the inputed dictionary.
        """
        self.assertEqual(FASTA2NeXus.nexus_header({'FJ598681': 'ATGCGCAAA'}), "#NEXUS\n\nBEGIN DATA;\nDIMENSIONS NTAX=1 NCHAR=9;\nFORMAT DATATYPE=DNA MISSING=N GAP=-;\nMATRIX\n")
    
    def test_nexus_converter(self):
        """
        Tests if nexus_convertion function create the NeXus file matrix based on the accepted arguments, returning the NeXus file content.
        """
        self.assertEqual(FASTA2NeXus.nexus_converter("#NEXUS\n\nBEGIN DATA;\nDIMENSIONS NTAX=1 NCHAR=9;\nFORMAT DATATYPE=DNA MISSING=N GAP=-;\nMATRIX\n",{'FJ598681': 'ATGCGCAAA'}), '#NEXUS\n\nBEGIN DATA;\nDIMENSIONS NTAX=1 NCHAR=9;\nFORMAT DATATYPE=DNA MISSING=N GAP=-;\nMATRIX\n   FJ598681 ATGCGCAAA\n  ;\nEND;')
if __name__=="__main__":
    """
    Just ensuring the code is only executed when the script is run as a standalone program.
    """
    unittest.main()
