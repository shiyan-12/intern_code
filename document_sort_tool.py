import os

def scan_folder(folder_path: str) -> list:
    """
    Traverse all files inside target folder
    Input: folder directory path
    Output: list of all file full paths
    """
    all_found_files = []
    for item in os.listdir(folder_path):
        full_item_path = os.path.join(folder_path, item)
        if os.path.isfile(full_item_path):
            all_found_files.append(full_item_path)
    return all_found_files


def classify_and_count_files(file_path_list: list) -> dict:
    """
    Classify files by suffix, calculate quantity & total size
    Input: list of file paths
    Output: dictionary storing count and size of each file type
    """
    type_statistics = {}
    target_types = [".py", ".txt", ".docx", ".xlsx"]
    for suffix in target_types:
        type_statistics[suffix] = {"count": 0, "total_size_kb": 0.0}

    for path in file_path_list:
        file_suffix = os.path.splitext(path)[1].lower()
        file_size_kb = os.path.getsize(path) / 1024
        if file_suffix in type_statistics:
            type_statistics[suffix]["count"] += 1
            type_statistics[suffix]["total_size_kb"] += round(file_size_kb, 2)
    return type_statistics


def generate_summary_report(folder_path: str, file_stats: dict):
    """
    Write sorted statistical result into a text report file
    """
    report_path = os.path.join(folder_path, "document_summary_report.txt")
    with open(report_path, "w", encoding="utf-8") as report_file:
        report_file.write("===== Fluid Tech Project Document Summary Report =====\n")
        report_file.write(f"Scanned Folder: {folder_path}\n\n")
        for suffix, data in file_stats.items():
            report_file.write(f"File Type {suffix}: \n")
            report_file.write(f"  Total Files: {data['count']}\n")
            report_file.write(f"  Total Size: {data['total_size_kb']} KB\n\n")
    print(f"Report generated successfully at: {report_path}")


# ---------------------- Test running entry ----------------------
if __name__ == "__main__":
    print("Scanning folder now...")
    test_directory = r"./project_documents"
    all_files = scan_folder(test_directory)
    print(f"Total number of scanned files: {len(all_files)}")
    stats_result = classify_and_count_files(all_files)
    generate_summary_report(test_directory, stats_result)