import subprocess;
import os;
from pathlib import Path;

class PFAMSearcher:
    def __init__(self, hmm_dir: str, fasta_dir: str, output_dir: str) -> None:
        self.hmm_dir = hmm_dir;
        self.fasta_dir = fasta_dir;
        self.output_dir = output_dir;

    def run_all_searches(self) -> None:
        paths_to_hmm = [];
        hmm_path = Path(self.hmm_dir)
        for folder in hmm_path.iterdir():
            for file in folder.iterdir():
                if file.suffix == ".hmm":
                    
                    
        
    
    def _run_hmmsearch():
        pass

