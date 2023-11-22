import os
import zipfile
import shutil

sturcture_zip_path = '/mnt/sdc/lanwei/ADIPOR/colabfold/output'
top_pose_path = '/mnt/sdc/lanwei/ADIPOR/colabfold/top-pdb'

if not os.path.exists(top_pose_path):
    os.makedirs(top_pose_path)

for file_name in os.listdir(sturcture_zip_path):
    if file_name.endswith('.zip'):
        file_path = os.path.join(sturcture_zip_path, file_name)
        
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            for f in zip_ref.namelist():
                if 'rank_001' and '.pdb' in f:
                    name_parts = f.split('_')
                    pdb_name = name_parts[0] + '.pdb'
                    zip_ref.extract(f, sturcture_zip_path)  
                    shutil.move(os.path.join(sturcture_zip_path, f), os.path.join(top_pose_path, pdb_name))
os.chdir(top_pose_path)
os.system('zip -r top-pdb.zip .')