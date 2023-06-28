import pyAesCrypt
import os
import logging
import click

BUFFER_SIZE: int = 512 * 1024
ENC_SUFFIX: str = '.crp'


def file_decryption(file_path: str, password: str, buffer_size=BUFFER_SIZE) -> None:
    output_file, ext = os.path.splitext(file_path)

    if len(ext) == 0:
        raise ValueError('File without encryption extension')
    if ext[1] == ENC_SUFFIX:
        raise ValueError('Wrong encryption suffix')

    pyAesCrypt.decryptFile(
        file_path,
        output_file,
        password,
        buffer_size
    )

    logging.info(
        f"File: {file_path} decrypted"
    )

    os.remove(file_path)

    logging.info(
        f"File: {file_path} deleted"
    )


def dir_decryption(dir_path: str, password: str, buffer_size=BUFFER_SIZE):
    for name in os.listdir(dir_path):
        path = os.path.join(dir_path, name)

        if os.path.isfile(path):
            file_decryption(path, password, buffer_size)
        else:
            dir_decryption(path, password, buffer_size)


def decryption(path: str, password: str, buffer_size=BUFFER_SIZE):
    if os.path.isfile(path):
        file_decryption(path, password, buffer_size)
    else:
        dir_decryption(path, password, buffer_size)
