from pathlib import Path

def analyze_log(filename):
    current_dir=Path(__file__).parent
    config_path=current_dir/filename
    dic = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    try:
        with open(config_path, "r", encoding="utf-8") as file:
                for line in file:
                    clean_line = line.strip()
        
                    if not clean_line:
                        continue
        
                    parts = clean_line.split()
                    log_type = parts[0]
        
                    if log_type in dic:
                        dic[log_type] += 1
    except FileNotFoundError:
         print('文件名无法找到 请传入正确文件名')
         return None
    
    return dic