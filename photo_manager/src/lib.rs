use std::path::Path;
use std::fs;
use std::iter::Iterator;

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

struct FileIter {
    root_path: &Path,
    genera_iter: Iterator,
}

impl FileIter {
    pub fn new(root_path: &Path) -> FileIter {
        Filter {root_path, root_path.iter()}
    }
}

impl Iterator for FileIter {
    type Item = Path;

    fn next(&mut self) -> Option(Path) {
        if let Some(item_path) = self.genera_iter.next() {
            if item_path.is_dir() {
                find_images
            } else if item_path.is_file() {
                // ignore symlink file
                fs::metadata(item_path.to
            }
        }
    }
}


impl Indexer {
    fn build(&self) -> vec<OneIndex> {
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

    fn file_path_iter(&self) -> Iterator<Path> {
        let root_path = Path::new(self.root_dir);
        let mut results = Vec::new();
        
    }
}
    
fn find_image(dir_path: &Path) -> Vec<Path> {
}



