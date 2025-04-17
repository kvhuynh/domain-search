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
    
    test_PFAM_CARD = Path("tests/test_data/pfam_models/CARD");
    for hmm_file in test_PFAM_CARD.glob("*.hmm"):
        shutil.copy(hmm_file, pfam_dir / hmm_file.name)

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
    pfam_name = "PF00619";
    pfam_dir: Path = searcher.output_dir / pfam_name;

    # Manually create the directory to simulate a previous search
    pfam_dir.mkdir(parents=True, exist_ok=True)

    assert searcher._already_searched(pfam_name) is True
    assert pfam_dir.exists()
    assert pfam_dir.is_dir()

# def test_run_searches() -> None:
#     searcher.run_searches();
        