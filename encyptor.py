import pyAesCrypt
import os
import logging


BUFFER_SIZE: int = 512 * 1024
ENC_SUFFIX: str = '.crp'


def file_encryption(file_path: str, password: str, output_dir: str = None, buffer_size=BUFFER_SIZE) -> None:
    output_path = (file_path if output_dir is None else os.path.join(
        output_dir, os.path.basename(file_path)
    )) + ENC_SUFFIX

    pyAesCrypt.encryptFile(
        file_path,
        output_path,
        password,
        buffer_size
    )

    logging.info(
        f"File: {os.path.splitext(file_path)[0]} encrypted, located in: {os.path.realpath(output_path)}",
    )


def dir_encryption(dir_path: str, password: str, output_dir: str = None, buffer_size=BUFFER_SIZE):
    logging.info(
        f"Starting to encrypt directory: {dir_path}",
    )
    
    for name in os.listdir(dir_path):
        path = os.path.join(dir_path, name)

        if os.path.isfile(path):
            file_encryption(path, password, output_dir, buffer_size)
        else:
            output = os.path.join(dir_path if output_dir is None else output_dir, name)
            if not os.path.exists(output):
                os.mkdir(output)

            dir_encryption(path, password, output, buffer_size)


def encryption(path: str, password: str, output_dir: str = None, buffer_size=BUFFER_SIZE):
    if os.path.isfile(path):
        file_encryption(path, password, output_dir, buffer_size)
    else:
        dir_encryption(path, password, output_dir, buffer_size)
