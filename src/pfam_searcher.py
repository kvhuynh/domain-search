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

    def run_searches(self) -> None:
        hmm_path = Path(self.hmm_dir);
        pfam_name = hmm_path.parent.name
        for folder in hmm_path.iterdir():
            pfam_name = str(folder).split("/")[-1];
            if not self._already_searched(folder, pfam_name):
                self._run_hmmsearch(folder, pfam_name);
            # for file in folder.iterdir():
            #     print(file)
            #     if not self._already_searched(pfam_name):
            #         self._run_hmmsearch(file, pfam_name);
            
                    
    def _already_searched(self, path: Path, pfam_name: str) -> bool:
        # check "../output/pfam_name"
        # print(pfam_name)
        return self.dir_manager.output_subdir_exists(path, pfam_name)
        
    
    def _run_hmmsearch(self, path: Path, pfam_name: str):
        print("hello am i getting used wtf")
        print(path)
        # run hmmer search
        # command = f"hmmsearch --tblout ../output/{pfam_name}_hmmsearch -E 0.001 {pfam_hmm} {self.db_dir} "
        # subprocess.run()

