import os
import shutil 
import time

dayinseconds = 24*60*60
current_time = time.time()
print(current_time)

def is_modified_last_24_hours(file):
    stats = os.stat(file)
    
    return max(stats.st_mtime, stats.st_ctime) >= current_time - dayinseconds

def update_file(file):
    # Append timestamp to file content
    with open(file, 'a') as f:
        f.write(f'\nModified at: {time.ctime(current_time)}')

files = [f for f in os.listdir('.') if os.path.isfile(f)]

recent_files = [f for f in files if is_modified_last_24_hours(f)]

# Update recent files
for file in recent_files:
    update_file(file)

if not os.path.exists('last_24hours'):
    os.makedirs('last_24hours')

for file in recent_files:
    shutil.move(file, 'last_24hours')