#!/usr/bin/env python3
"""
Jarvis v5.1 Cache Manager
文件缓存 + 输出缓存 + Token预算控制
"""

import json
import hashlib
import os
from pathlib import Path

CACHE_DIR = Path("/home/node/.openclaw/workspace/cache")
FILE_HASH_INDEX = CACHE_DIR / "file_hash_index.json"
OUTPUT_CACHE_DIR = CACHE_DIR / "output_cache"
CACHE_CONFIG = CACHE_DIR / "cache_manager.json"

def load_json(path):
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return {}

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def compute_hash(content):
    return hashlib.sha256(content.encode()).hexdigest()[:16]

def should_write_file(file_path, content):
    """文件缓存：检查是否需要写入"""
    file_path = str(file_path)
    hash_index = load_json(FILE_HASH_INDEX)
    
    content_hash = compute_hash(content)
    
    if file_path in hash_index and hash_index[file_path] == content_hash:
        return False  # 相同，不写入
    
    # 更新hash
    hash_index[file_path] = content_hash
    save_json(FILE_HASH_INDEX, hash_index)
    return True  # 不同，写入

def get_output_cache(task_input):
    """输出缓存：检查是否命中"""
    task_hash = compute_hash(str(task_input))
    cache_file = OUTPUT_CACHE_DIR / f"{task_hash}.json"
    
    if cache_file.exists():
        return load_json(cache_file)
    return None

def set_output_cache(task_input, result):
    """设置输出缓存"""
    task_hash = compute_hash(str(task_input))
    cache_file = OUTPUT_CACHE_DIR / f"{task_hash}.json"
    
    cache_data = {
        "task_input": task_input,
        "result": result,
        "cached_at": "2026-02-21T13:49:42Z"
    }
    save_json(cache_file, cache_data)

def get_token_budget():
    """获取Token预算"""
    config = load_json(CACHE_CONFIG)
    return config.get("token_budget", {}).get("default", 8000)

if __name__ == "__main__":
    print("Jarvis v5.1 Cache Manager initialized")
    print(f"Cache dir: {CACHE_DIR}")
    print(f"File hash index: {FILE_HASH_INDEX}")
    print(f"Output cache dir: {OUTPUT_CACHE_DIR}")
