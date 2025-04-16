import subprocess;
import os;
from pathlib import Path;
from directory_manager import DirectoryManager

class PFAMSearcher:
    def __init__(self, hmm_dir: str, db_dir: str, output_dir: str, dir_manager: DirectoryManager) -> None:
        self.hmm_dir = hmm_dir;
        self.db_dir = db_dir;
        self.output_dir = output_dir;
        self.dir_manager = dir_manager;

    def run_all_searches(self) -> None:
        hmm_path = Path(self.hmm_dir);
        pfam_name = hmm_path.parent.name
        for folder in hmm_path.iterdir():
            pfam_name = str(folder).split("/")[-1];
            for file in folder.iterdir():
                if not self._already_searched(pfam_name):
                    self._run_hmmsearch(file, pfam_name);
                else:
                    self.dir_manager
                    
    def _already_searched(self, pfam_name: str) -> bool:
        # check "../output/pfam_name"
        return self.dir_manager.output_subdir_exists(pfam_name)
        
    
    def _run_hmmsearch(self, file: Path, pfam_name: str):
        # run hmmer search
        # command = f"hmmsearch --tblout ../output/{pfam_name}_hmmsearch -E 0.001 {pfam_hmm} {self.db_dir} "
        # subprocess.run()
        pass

