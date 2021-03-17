import shutil
import os
    
source_dir = './papers'
target_dir = '.'
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    if file_name.endswith('.pdf'):
        key_old = os.path.splitext(file_name)[0]
        key = key_old.lower().replace('_', '-')
        print(f'{key_old} -> {key}')
        try:
            shutil.copy(os.path.join(source_dir, file_name), os.path.join(key, key+'.pdf'))
        except IOError as e:
            print(f'Failed: {e}')
