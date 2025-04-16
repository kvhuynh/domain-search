from pfam_searcher import PFAMSearcher

class PFAMPipeline:
    def __init__(self, hmm_dir: str, fasta_dir: str, results_dir: str) -> None:
        self.searcher = PFAMSearcher(hmm_dir, fasta_dir, results_dir);
        self.searcher.run_all_searches();