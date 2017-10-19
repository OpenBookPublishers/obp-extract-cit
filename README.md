# Extract-citations

This repository contains a simple tool to extract bibliographic citations from content encoded in XML TEI and creates a file for submission to CrossRef's cited-by service (see the repo's [wiki](https://github.com/OpenBookPublishers/extract-citations/wiki)).

## Files and directories in this repository
* __Extract-citations-from-book.xsl__: the script that extracts bibliographic citations
* __LICENSE__
* __README.md__: this file


## Extracting citations
This XSL transformation has been developed in cunjunction with the conversion tools hosted at https://github.com/OpenBookPublishers/XML-last but can be used on any XML TEI file where bibliographic citations have been encoded as `<bibl>` elements (see http://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-bibl.html). 
This program:
* individuates every element that has been tagged as a bibliographic entry within the input file
* extracts and numbers them sequentially
* converts each of them to a `<citation>` or `<unstructured_citation>` element (see the repo's [wiki](https://github.com/OpenBookPublishers/extract-citations/wiki)).
	
To run it:
1. Copy your input files to the project folder:
	* the XML TEI file containing the book or article you wish to extract citations from
	* a XML file recording the book or article metadata and following the CrossRef schema, version 4.3.5 or newer ( https://support.crossref.org/hc/en-us/articles/214530063). This is the same file that is often used to register content to the CrossRef database (see https://support.crossref.org/hc/en-us/articles/215577783-Creating-content-registration-XML)
2. Run 'Extract-citations-from-book.xsl'. To run this transformation (XSLT 2.0) a processor such as SaxonHE will be needed (https://sourceforge.net/projects/saxon/files/Saxon-HE/9.8/). Saxon can be run (1) from within a product that provides a graphical user interface (such as oXygen, https://www.oxygenxml.com/), (2) from the command line or (3) from within a Java or .NET application.
	* (1) select your input file and the XSL; the output field can be left blank
	* (2) type `java -jar _dir_/saxon9he.jar -s:_your_dir_/Extract-citations/_your_input_file_ -xsl:_your_dir_/Extract-citations/Extract-citations-from-book.xsl -o:_your_dir_/Extract-citations/Extract-citations-from-book.xsl`
	* (3) see eg http://www.oracle.com/technetwork/java/gazfm-138953.html
	
## Further reading
Visit the repo's [wiki](https://github.com/OpenBookPublishers/Extract-citation/wiki) to read more about the structure of the output file.