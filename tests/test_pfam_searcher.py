import pytest;
import os;
from pfam_searcher import PFAMSearcher;
from directory_manager import DirectoryManager;
from pathlib import Path;

# @pytest.fixture
# def dummy_hmm_dir(tmp_path):
#     pfam_dir = f"{tmp_path}/pfam_models/TEST_DOMAIN";
#     print(pfam_dir);
    
@pytest.fixture
def test_dm_initialization() -> None:
    dir_manager: DirectoryManager = DirectoryManager(
        output_dir=Path("tests/test_data/output"),
        result_dir=Path("tests/test_data/results"),
        db_dir=Path("tests/test_data/db")
    )

def test_searcher_initialization(dir_manger: DirectoryManager) -> None:
    searcher: PFAMSearcher = PFAMSearcher(
        hmm_dir=Path("tests/test_data/pfam_models"),
        db_dir=Path("tests/test_data/db"),
        output_dir=Path("tests/test_data/output"),
        dir_manager=dir_manager
    );
    assert isinstance(searcher, PFAMSearcher);

def test_run_hmmersearch():
    assert 1 == 1;

def test_skips_if_output_exists() -> None:
    dir_path: str = "";
    assert os.path.isdir(dir_path);