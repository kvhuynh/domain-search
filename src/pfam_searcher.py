import subprocess;
import os;
from pathlib import Path;

class PFAMSearcher:
    def __init__(self, hmm_dir: str, fasta_dir: str, output_dir: str) -> None:
        self.hmm_dir = hmm_dir;
        self.fasta_dir = fasta_dir;
        self.output_dir = output_dir;

    def run_all_searches(self) -> None:
        hmm_path = Path(self.hmm_dir);
        pfam_name = hmm_path.parent.name
        for folder in hmm_path.iterdir():
            # output_path = self.raw_dir/pfam_name;
            print(folder);
            
            for file in folder.iterdir():
                # check if the output file for the hmmsearch is already there
                # otherwise make it
                # if it exists then continue
                # if ()
                # _run_hmmsearch();
                pass;
                    
        
    
    def _run_hmmsearch():
        
        pass

