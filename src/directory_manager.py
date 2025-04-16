from pathlib import Path;
class DirectoryManager:
    def __init__(self, output_dir: str, result_dir: str, db_dir: str, pfam_dir) -> None:
        self.dirs = { 
            "output": Path(output_dir),
            "result": Path(result_dir),
            "db": Path(db_dir),
            "pfam_models": Path(pfam_dir)
        };

    def setup(self) -> None:
        for name, path in self.dirs.items():
            path.mkdir(parents=True, exist_ok=True);
    
    def output_subdir_exists(self, pfam_name: str) -> bool:
        return os.path(f"../output/{pfam_name}");
    
        
        