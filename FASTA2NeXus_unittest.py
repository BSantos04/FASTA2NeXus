import unittest
import FASTA2NeXus

class test_functions(unittest.TestCase):
    """
    Creating a class with all the fuctions we are going to use to test each function form thhe FASTA2NeXus. py script individually
    """
    def test_fasta_to_dict(self):
        """
        Tests if fasta_to_dict function reads the input FASTA file correctly and returns the expected dictionary.
        
        In that case, we are going to use the sequence.fasta file as input for exemple.
        
        Remeber to save the python programs and the file in the same repository and run on it, otherwise the code will ot work.
        """
        self.assertEqual(FASTA2NeXus.fasta_to_dict('sequence.fasta'), {'FJ598681.1 Carcharhinus acronotus isolate 13 12S ribosomal RNA gene, partial sequence; tRNA-Val gene, complete sequence; and 16S ribosomal RNA gene, partial sequence; mitochondrial': 'TACTACAAGCGCTAGCTTAAAACCCAAAGGACTTGGCGGTATCCCATACCCACCTAGAGGAGCCTGTTCTATAACCGATAATCCCCGTTCAACCTCACCACTTCTTGCCATTACCGTCTATATACCGCCGTCGTCAGCCCACCCTGTGAAGGACCAAAAGTAAGCAAAAAGAATTAAACTCCAAAACGTTAGGTCGAGGTGTAGCAAATGAAGTGGGAAGAAATGGGCTACATTTTTTTCCAAAAATATACGAATGGTAAACTGAAAACATACCTAAAGGTGGATTTAGCAGTAAGAAGAGATCAGAATACTCCTCTGAAATCGGCTCTGGGATAAGCACACACCGCCCGTCACTCTCCTCAAAAACAACTCACCACTTTCCATAAATACATTCCTTCAACAAGAGGAGGCAAGTCGTAACATGGTAAGTGTACTGGAAAGTGCACTTGGAATCAAAATGTGGCTAAATTAGTAAAGTACCTCCCTTACACCGAGGAGATATCCGCGCAATTCGGATCATTTTGAACCTTAAAGCTAGCCTATAATATTAATTCAACTAGACCTTATAAATCTAATATATATATTACAATTTTTAATCAAAACATTCTCAACCTTCTAGTATGGGTGACAGAACAATAACCTCAGCGCAATAGCTTATGTACCGCAAGGGAAAGCTGAAAAAGAAATGAAACAAATCATTAAAGTACTAAAAAGCAGAGATTATACCTCGTACCTTTTGCATCATGATTTAGCTAGAAAAACTAGGCAAAAAGACCTTAAGTCTATCTCCCCGAAACTAAACGAGCTACTCCGAAGCAGCATTACAAGAGCCAACCCGTCTCTGTGGCAAAAGAGTGGGAAGACTTCCGAGTAGCGGTGAAAAGCCTACCGAGTTTAGTGATAGCTGGTTACCCAAGAAAAGAACTTCAGTTCTGCATTAATTTTTCACTATCTAAACAAGACTTACTCGTCAAAGAAATCTATAAGAATTAATAGTTATTTAGAAGAGGTACAACCCTTCTAAACCAAGACACAACTTTTTAAGGTGGGAAATGATCATAATTATTAAGGTTACCATCTCAGTGGGCCTAAAAGCAGCCATCTGTCAAGCAAGCGTCGCAGCTCTAATCTAATAATTAAACCTCTAATTCAGATATCCATTCATAACCCCCTTTATCCTATTGGGTTATTTTATATTTATATAAAAGAACTTATGCTAAAATGAGTAATAAAGAGAACAAATCTCTCCCGACACAAGTGTATGTCAGAAAGAATTAAATCACTGATAATTAAACGACCCCAAACTGAGGTCATTATATTACTTAATCATTAACTAGAAAATCCTATTCTCTTACCCGTTA'})
    
    def test_nexus_header(self):
        """
        Tests if nexus_header function create properly the NeXus file header based on the inputed dictionary.
        
        I already inputed a dictionary with one taxa and a sequence of 9 characters and the respctive output, facilitating the interpretation of both arguments.
        """
        self.assertEqual(FASTA2NeXus.nexus_header({'FJ598681': 'ATGCGCAAA'}), "#NEXUS\n\nBEGIN DATA;\nDIMENSIONS NTAX=1 NCHAR=9;\nFORMAT DATATYPE=DNA MISSING=N GAP=-;\nMATRIX\n")
    
    def test_nexus_converter(self):
        """
        Tests if nexus_convertion function create the NeXus file matrix based on the accepted arguments, returning the NeXus file content.
        
        Like the previous function, I already prepared the inputs and the output to facilitate test interpretation.
        """
        self.assertEqual(FASTA2NeXus.nexus_converter("#NEXUS\n\nBEGIN DATA;\nDIMENSIONS NTAX=1 NCHAR=9;\nFORMAT DATATYPE=DNA MISSING=N GAP=-;\nMATRIX\n",{'FJ598681': 'ATGCGCAAA'}), '#NEXUS\n\nBEGIN DATA;\nDIMENSIONS NTAX=1 NCHAR=9;\nFORMAT DATATYPE=DNA MISSING=N GAP=-;\nMATRIX\n   FJ598681 ATGCGCAAA\n  ;\nEND;')
if __name__=="__main__":
    """
    Just ensuring the code is only executed when the script is run as a standalone program.
    """
    unittest.main()