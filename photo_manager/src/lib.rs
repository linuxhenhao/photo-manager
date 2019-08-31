use std::path::{Path, PathBuf};
use std::fs;
use std::iter::Iterator;
use std::io;

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

struct FileIter<'a> {
    root_path: &'a Path,
    dir_iters: Vec<fs::ReadDir>,
}

impl<'a> FileIter<'a> {
    pub fn new(root_path: &'a Path) -> FileIter {
        FileIter {
            root_path: root_path,
            dir_iters: vec![root_path.read_dir().expect("error while read dir")]
        }
    }

    fn get_file_from_dirs(dir_iters: &mut Vec<fs::ReadDir>) -> Option<PathBuf> {
        if let Some(dir_iter) = dir_iters.pop() {
            // has dir_iter
            while let Some(dir_entry_result) = dir_iter.next() {
                // dir_iter has more entries
                if let Ok(dir_entry) = dir_entry_result {
                    if let Ok(file_t) = dir_entry.file_type() {
                        if file_t.is_dir() {
                            // this is a directory, push to dir_iters
                            dir_iters.push(dir_entry.path().read_dir().expect("read_dir failed"));
                            // goto next dir entry in this dir iter
                            continue;
                        } else if file_t.is_file() {
                            // is file, push dir_iter back into dir_iters for next run
                            dir_iters.push(dir_iter);
                            return Some(dir_entry.path());
                        } else {
                            // not file, not dir
                            continue;
                        }
                    } else {
                        // cannot get file type from this dir entry, error
                        return None;
                    }
                } else {
                    // bad dir entry result, error, return None
                    return None;
                }
            }
            // run out of this dir_iter, and no file was found
            // goto next dir_iter
            return Self::get_file_from_dirs(dir_iters);
        } else {
            // no more dir_iters, over, return None
            None
        }
    }
}


impl<'a> Iterator for FileIter<'a> {
    type Item = Path;

    fn next(&mut self) -> Option<PathBuf> {
        Self::get_file_from_dirs(&mut self.dir_iters)
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



