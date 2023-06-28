import click
import encyptor
import decryptor
import click
import logging

logging.basicConfig(level=logging.INFO, filename="codec.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


@click.group
def codec():
    pass


@click.command()
@click.option(
    "--buffer-size",
    "buffer_size",
    default=512,
    required=False,
    help="""
            Optional buffer size, must be a multiple of AES block size (16) using a larger buffer speeds up things when dealing with big files

            Default is 512KB.
        """
)
@click.argument("input", type=click.Path(exists=True))
@click.argument("password")
def decrypt(input, password, buffer_size):
    logging.info(f"Starting decryption...")

    decryptor.decryption(input, password, buffer_size)

    logging.info(f"Decrypted!")


@click.command()
@click.option("-o", "--output", "output", required=False, type=str, help="The output dir for result")
@click.option(
    "--buffer-size",
    "buffer_size",
    default=512,
    required=False,
    help="""
            Optional buffer size, must be a multiple of AES block size (16) using a larger buffer speeds up things when dealing with big files

            Default is 512KB.
        """
)
@click.argument("input", type=click.Path(exists=True))
@click.argument("password")
def encrypt(input, password, output, buffer_size):
    logging.info(f"Starting encryption...")
    
    encyptor.encryption(input, password, output, buffer_size)
    
    logging.info(f"Encrypted!")


codec.add_command(encrypt)
codec.add_command(decrypt)

if __name__ == "__main__":
    codec()
