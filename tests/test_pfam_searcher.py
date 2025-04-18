import pytest;
import os;
import shutil
from pfam_searcher import PFAMSearcher;
from directory_manager import DirectoryManager;
from pathlib import Path;
    
# @pytest.fixture
# def directory_manager() -> DirectoryManager:
#     dir_manager: DirectoryManager = DirectoryManager(
#         output_dir=Path("tests/test_data/output"),
#         result_dir=Path("tests/test_data/results"),
#         db_dir=Path("tests/test_data/db"),
#         pfam_dir=Path("tests/test_data/pfam_models")
#     );
#     return dir_manager;

@pytest.fixture
def searcher(tmp_path: Path) -> None:
    # Test paths
    output_dir: Path = tmp_path / "output";
    results_dir: Path = tmp_path / "results";
    db_dir: Path = tmp_path / "db";
    pfam_dir: Path = tmp_path / "pfam_models";

    # Make test directories
    output_dir.mkdir();
    results_dir.mkdir();
    db_dir.mkdir();
    pfam_dir.mkdir();
    
    # !!! REFACTOR BLOCK 
    test_path = Path("tests/test_data")
    pfam_sources = ["CARD", "NACHT"]

    for pfam_name in pfam_sources:
        pfam_source_dir = test_path / "pfam_models" / pfam_name
        for hmm_file in pfam_source_dir.glob("*.hmm"):
            shutil.copy(hmm_file, pfam_dir / hmm_file.name)

    db_source = test_path / "db" / "EP00074_Homo_sapiens.fasta"
    shutil.copy(db_source, db_dir)
        
    # !!!
    
    dir_manager:DirectoryManager = DirectoryManager(
        output_dir=output_dir,
        results_dir=results_dir,
        db_dir=db_dir,
        pfam_dir = pfam_dir
    );
    dir_manager.setup();
    searcher: PFAMSearcher = PFAMSearcher(
        hmm_dir=pfam_dir,
        db_dir=db_dir,
        output_dir=output_dir,
        dir_manager=dir_manager
    );
    return searcher;

def test_fixture_creates_output_dir(searcher: PFAMSearcher) -> None:
    assert searcher.output_dir.exists();
    assert searcher.output_dir.is_dir();

def test_already_searched(searcher: PFAMSearcher, tmp_path: Path) -> None:

    pfam_dir: Path = searcher.output_dir / "CARD" / "PF00619";
    # print(searcher.output_dir)
    # Manually create the directory to simulate a previous search
    pfam_dir.mkdir(parents=True, exist_ok=True)
    # print(pfam_dir)
    assert searcher._already_searched(pfam_dir, "PF00619") is True
    assert pfam_dir.exists()
    assert pfam_dir.is_dir()

# Assume that hmmersearch works since it's a third party package
# Only testing to see if the file is written out to the right place
def test_run_searches(searcher: PFAMSearcher) -> None:
    searcher.run_searches();
    result_dir: Path = searcher.output_dir;
    
    # test_directories = ["P"]
    result_dir: Path = searcher.output_dir / "NACHT" / "PF05729";
    print(result_dir);
    # result_dir: Path = searcher.output_dir / "CARD" / "PF00619";
    
    # run_searches() should be creating the directory
    # result_dir.mkdir(parents=True, exist_ok=True);
    assert result_dir.exists();
    assert result_dir.is_dir();

        