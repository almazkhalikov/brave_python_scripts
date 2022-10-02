from pathlib import Path, PurePosixPath
from loguru import logger
import subprocess
import shutil
import os
'''
Для работы в windows. Должен быть установлен Git Bash
'''

def make_archive(src_dir: Path, dst_dir: Path, name: str):
    shutil.make_archive(base_name=name, format='zip', root_dir=src_dir)
    full_src = Path(f'{os.getcwd()}/{name}.zip')
    full_dst = Path(f'{dst_dir}/{name}.zip')

    shutil.move(src=full_src, dst=full_dst)


def split_archive(name: str, dst_dir: Path):
    bash_split_cmd = f'split -b 27m --numeric-suffixes=1 -a 3 {name}.zip {name}.zip'
    splited_dir = Path(f'{result_dir}/splited')
    os.makedirs(splited_dir, exist_ok=True)
    archive_file = Path(f'{dst_dir}/{name}.zip')
    shutil.copy2(src=archive_file, dst=splited_dir)

    # convert windows path to unix
    unix_path = PurePosixPath(splited_dir)

    subprocess.run(f'bash.exe -c "cd {unix_path} && {bash_split_cmd}"', cwd=r'C:\Program Files\Git\bin', shell=True)
    subprocess.run(f'bash.exe -c "cd {unix_path} && rm {name}.zip"', cwd=r'C:\Program Files\Git\bin', shell=True)

    logger.info(f'done! {result_dir}')


if __name__ == '__main__':
    # имя без расширения .zip
    archive_name = 'app'
    source_files_dir = Path(r'C:\Users\user\Desktop\source')
    result_dir = Path(r'C:\Users\user\Desktop\result')

    make_archive(src_dir=source_files_dir, dst_dir=result_dir, name=archive_name)
    split_archive(name=archive_name, dst_dir=result_dir)
