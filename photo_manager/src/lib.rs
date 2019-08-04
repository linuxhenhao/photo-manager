use std::path::Path;
use std::fs;
use mime_guess;

fn build_index(dir_path: &str) {
    
}

fn find_image(dir_path: &Path) -> Vec<Path> {
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
