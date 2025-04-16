from pfam_searcher import PFAMSearcher
from directory_manager import DirectoryManager
class PFAMPipeline:
    def __init__(self, hmm_dir: str, fasta_dir: str, results_dir: str, dir_manager: DirectoryManager) -> None:
        self.searcher = PFAMSearcher(hmm_dir, fasta_dir, results_dir, dir_manager);
        self.searcher.run_all_searches();