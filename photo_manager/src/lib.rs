use std::path::Path;
use std::fs;
use mime_guess;

struct Indexer {
    root_dir: String,
}

enum ChecksumType {
    MD5
}

struct OneIndex {
    // relative path
    path: String,
    checksum: String,
    checksum_type: ChecksumType,
}

impl Indexer {
    fn build(&self, ) -> vec<OneIndex> {
        let mut indexes = Vec::new();
        self.root_dir;
        let one_index = OneIndex {
            "test",
            "flkajfklajkler",
            ChecksumType::MD5
        };
        indexes.push(one_index);
        indexes
    }

    fn get_all_file_paths(dir_path: &Path) -> Vec<Path> {
        let mut results = Vec::new();
        for item_path in dir_path.iter() {
            if item_path.is_dir() {
                find_images
            } else if item_path.is_file() {
                // ignore symlink file
                fs::metadata(item_path.to
            }
        }
    }
}
    
fn find_image(dir_path: &Path) -> Vec<Path> {
}



