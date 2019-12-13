import argparse
from os import path
from bs4 import BeautifulSoup


def extract_version(file_path):
    """
    Extract the version of the CrossRef schema from the DOI deposit file.
    """
    with open(file_path, 'r')as in_file:
        soup = BeautifulSoup(in_file, 'html.parser')

        return soup.find('doi_batch')['version']


def run():
    parser = argparse.ArgumentParser(description='Extract Schema Version')
    parser.add_argument('input_file', help='Input DOI deposit file')

    args = parser.parse_args()

    file_path = path.abspath(args.input_file)

    print(extract_version(file_path))


if __name__ == "__main__":
    run()
