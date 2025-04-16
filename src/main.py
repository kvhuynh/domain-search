import argparse
from pfam_pipeline import PFAMPipeline
from directory_manager import DirectoryManager;

def main():
    parser = argparse.ArgumentParser(
        description="Run PFAM domain search pipeline on EukProt data"
    );

    parser.add_argument("--hmm-dir", type=str, default="../pfam_models", help="Directory of PFAM HMM models");
    parser.add_argument("--fasta-dir", type=str, default="../db/", help="Directory of input protein FASTA files");
    parser.add_argument("--results-dir", type=str, default="../results", help="Directory to store hmmsearch results")
    parser.add_argument("--output", type=str, default="../output", help="Output CSV path");

    parser.add_argument("--run-searches", action="store_true", help="Run hmmsearch on all HMM x FASTA combos");
    parser.add_argument("--parse", action="store_true", help="Parse all hmmsearch results");

    args = parser.parse_args();

    dir_manager = DirectoryManager("../output", "../results", "../db", "../pfam_models");
    dir_manager.setup();
    
    pipeline = PFAMPipeline(
        hmm_dir=args.hmm_dir,
        fasta_dir=args.fasta_dir,
        results_dir=args.results_dir,
        dir_manager=dir_manager
    );


    if args.run_searches:
        pipeline.run_searches();
        


if __name__ == "__main__":
    main();
