import pyAesCrypt
import os

BUFFER_SIZE: int = 512 * 1024
ENC_SUFFIX: str = '.crp'


def file_decryption(file_path: str, password: str, buffer_size=BUFFER_SIZE) -> None:
    output_file, ext = os.path.splitext(file_path)

    if len(ext) == 0 or ext[1] != ENC_SUFFIX:
        print(
            f"Ignore file: {file_path}, cause it is without enc suffix {ENC_SUFFIX}"
        )
        
        return

    pyAesCrypt.decryptFile(
        file_path,
        output_file,
        password,
        buffer_size
    )

    print(f"File: {file_path} decrypted")

    os.remove(file_path)

    print(f"File: {file_path} deleted")


def dir_decryption(dir_path: str, password: str, buffer_size=BUFFER_SIZE):
    for name in os.listdir(dir_path):
        path = os.path.join(dir_path, name)

        if os.path.isfile(path):
            try:
                file_decryption(path, password, buffer_size)
            except Exception as e:
                print(f"Problem with file: {path}, can't decrypt, cause: {e}")
        else:
            dir_decryption(path, password, buffer_size)


def decryption(path: str, password: str, buffer_size=BUFFER_SIZE):
    if os.path.isfile(path):
        file_decryption(path, password, buffer_size)
    else:
        dir_decryption(path, password, buffer_size)
