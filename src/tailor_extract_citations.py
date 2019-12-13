import argparse
from urllib.parse import urljoin
from bs4 import BeautifulSoup


def replace_version(file_path, schema_version):
    """
    Find the schema URL in the xsl file and replace the version with
    the one supplied to the function.
    """
    with open(file_path, 'r') as in_file:
        soup = BeautifulSoup(in_file, 'html.parser')

        # Replace schema version for URI values
        # i.e. <xsl:stylesheet xmlns="https://example.org/1.2.3">
        entries = {
            # i.e. {tag_name: [attribute1, attribute2]}
            'xsl:stylesheet': ['xmlns', 'xmlns:doi'],
            'doi_batch': ['xmlns']
        }

        for tag in entries:
            for attribute in entries[tag]:
                xsl_schema = soup.find(tag)[attribute]
                doi_schema = urljoin(xsl_schema, schema_version)

                soup.find(tag)[attribute] = doi_schema

        # Special case - Replace schema version for <doi_batch>
        # i.e. <doi_batch version="1.2.3">
        soup.find('doi_batch')['version'] = schema_version

        # Special case - Replace schema version in xsi:schemalocation
        # i.e. <doi_batch xsi:schemaLocation="url1 url2">
        urls = soup.find('doi_batch')['xsi:schemalocation'].split(' ')
        new_urls = [urljoin(url, schema_version) for url in urls]

        soup.find('doi_batch')['xsi:schemalocation'] = ' '.join(new_urls)

        return soup


def write_output(file_path, soup):
    with open(file_path, 'w+') as out_file:
        out_file.write(soup.prettify(formatter='minimal'))


def run():
    desc='Tailor Section Transformation'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('input_file',
                        help='Input book-transformation xsl file')
    parser.add_argument('output_file',
                        help='Output book-transformation xsl file')
    parser.add_argument('-v', '--version',
		        help='CrossRef schema version',
		        required = True)
    
    args = parser.parse_args()

    soup_version = replace_version(args.input_file, args.version)
    write_output(args.output_file, soup_version)


if __name__ == "__main__":
    run()
