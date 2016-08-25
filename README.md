# YAML Generator for Digitized HathiTrust Submissions

The HathiTrust submissions process requires a .yml file whose contents contain information about the scan and a detailed contents list. The contents list can include information about reading order, chapters, and page type. This Python (2.7.x) script allows one to generate a valid .yml file for *digitized* (not born-digital) materials. With some minor modifications it could work for born-digital materials too.

## Files Included

- yaml_csv.py &mdash; Takes CSV input and outputs multiple YAML files, each named for the barcode of the object.
- yaml_generator.py &mdash; Python script for manually creating YAML files.
- field_guide.md &mdash; an explanation of the fields and data requested.
- HathiTrust_Submission_YAML_Data_Spreadsheet.xls &mdash; an XLS document with column headers for each piece of information required by the script. Can be used by student workers or others to record data before it's entered into the YAML generator. Ordering is key. Use field_guide.md to understand what each column represents and what it will output.
- HathiTrust_Submission_Sample.xls &mdash; a copy of the YAML Data Spreadsheet populated with a couple sets of values which can be used as sample information.
- sample_meta.yml &mdash; a YAML file generated from the data entered in HathiTrust_Submission_Sample.xls. Example of how the data in each field gets handled.
- sample_multiwork_meta.yml &mdash; a YAML file generated from data entered in the second line of HathiTrust_Submission_Sample.xls. Example of how multi-work issues get handled.
- SampleCSVData/SampleCSVData.csv &mdash; A sample CSV which works with yaml_csv.py, may be used for comparison and troubleshooting.

Originally the spreadsheets were conceived of as CSVs, but when used in Excel or Libre Office, one cannot save column data types for information and things like dates and barcodes were being "parsed" erroneously, leading to bad data. These allow persistent settings. However, before using yaml_csv.py, be sure to save your work as an actual CSV. **Note, Excel often changes barcodes into other kinds of numbers, so after saving as a CSV, open in a text editor to ensure your barcodes look correct.**

## Using YAML CSV Ingester

1. Clone repository to local machine. Python 2.7.x should be installed on the machine.
2. Use (or copy) HathiTrust_Submission_YAML_Data_Spreadsheet.xls to record the data about your books. For information on how the data will be used, see field_guide.md, although it specifically addresses the "generator" script. Always use the IMAGE number, rather than the PAGE number as a value. Separate multiple numbers with a comma and space, e.g. "2, 63". Use ISO-8601 for dates and 24-hour HH:MM for hours/minutes.
3. Save as CSV. Open in your preferred text editor to remove row 1 (headers) and ensure barcodes have saved properly.
4. Run `python yaml_csv.py` and input the directory path to your CSV file, followed by the directory path to the location where you would like outputs to appear. Be sure to escape any spaces in the directory paths.

See SampleCSVData/SampleCSVData.csv for comparison and troubleshooting.

## Using the Manual YAML Generator

1. Clone repository to local machine. Python 2.7.x should be installed on the machine.
2. Read field_guide.md and look over the CSV to understand the kind of data which the program will request.
3. Use the CSV or a local method to collect the relevant file numbers.
4. Make any necessary edits to yaml_generator.py (see **Personalizing** below).
5. In the command line, navigate to the directory in which the script resides and run script using: `python yaml_generator.py` (or other local python 2.7.x alias instead of "python", such as "py").
6. Follow instructions in the script and in field_guide.md to input information.
7. Check the output YAML file to ensure it looks right and matches your input.
8. Put in an Issue for any issues you encounter and I'll try to take them on. Additional features that aren't critical fixes or necessary for valid YAML files, however, will be added to possible phases later on. This includes refining multi-work issues.

### Personalizing the YAML Generator to Your Repository

The YAML generator contains certain pieces of hard-coded information and some assumptions specific to the institution. This section includes line numbers in yaml_generator.py and yaml_csv.py ("gen" and "csv" respectively) which should be examined and possibly changed for your institution.

#### Local Scanner Info

Lines (gen)303-304: Queries on each line reference "the Kirtas." Should be updated with name of in-house default scanner or a prompt to enter the Make (257) and Model (258) of the scanner.

Lines (gen, csv)11-19: The tests using variables set in (257-258) to output information about the scanner. Should be redone with new default values or redone entirely to remove tests and take the scanner name entirely as input.

#### Local Department Name

Lines (gen, csv)20-21: Scanner User is hard-coded as the name of the department which handles digitization. It should reflect the name of the department, unit, or other entity responsible for your institution's scanning.

#### Local Compression Agent

Lines (gen, csv)31-32: Image Compression Agent is hard-coded. Change it to your institution's HathiTrust organization code (or that of the institution doing your image compression).

## Overview of the Project

To allow one to input a small amount of information via the command line and generate a complete, or nearly-complete YML file. These files will still require manual review, but the tool should greatly speed up the creation of a great deal of information. This section provides an overview of the phases into which the project was broken in order to complete the process. Each phase is reflected in a Building Block file. This could have been done by specially-designated commits, but was instead broken into units, though commits were made at the time.

### Project Phases

- **Phase 1.** (Completed, 2016-02-19) Generate the list of the filenames of scanned images. Takes filetype input, though this may be turned into a TIFF/JP2 switch, since only those filetypes are allowed. Presumes all filenames will be the same type. This is a core function, as it would be a real PITA to create the list manually. Takes input of final number of image. Handles leading 0s with a simple test to create standardized 8-digit-long filenames.
- **Phase 2.** (Completed, 2016-02-19) Print the list of images in proper syntax for the final process. Write list to file.
- **Phase 3.** (Completed, 2016-02-19) Add reading order input, which should be on what page the first page starts. Using numbers so far.
- **Phase 4.** (Completed, 2016-02-22) Identify one-time page *types*. Develop a way to insert one, then duplicate.
- **Phase 5.** (Completed, 2016-02-22) Roman numeral pages before reading order. Use test on reading order to stop them too.
- **Phase 6.** (Completed, 2016-02-29) Identify all other information necessary for the file. Come up with a list of necessary information and structure questions to take its input and print it at the top of the file.
- **Phase 7.** (Completed, 2016-03-01) Add number of final page. Handle cases where a page number is skipped (for example cases where a group of images in the middle of the book have page numbers and pagination picks up right after).
- **Phase 8.** (Completed, 2016-03-01) Documentation and creation of data capture CSVs and sample CSVs. And sample YAML.
- **Phase 9.** (Completed, 2016-03-15) Added support for creating the YAML file in any particular directory so it can be used better. Also adds success message saying where the file has been made.
- **Phase 10.** (Completed, 2016-03-28) Now handles both regular and roman numerals for multi-work issues. Added sample multi-work YAML.
- **Phase 11.** (Completed, 2016-03-29) Discovered bug in which ingests aren't cast to lists until after page 1, which is a problem because front/back cover are always INT but if there's a Page 1 or Page 1, it doesn't work. Moved inputToLists to writeFile itself. Found proper place to put it to avoid any other tests that might be interrupted.
- **Phase 12.** (Completed, 2016-08-24) Takes input of CSV with as many pieces of book information as you want.

### Not in a phase yet

Things for future work?

- **Priority.** Handling simplified use cases. Work with team to select core elements (things related to pagination, chapters) vs. extraneous elements (foldouts, ?). Write a switch to allow one to just go through the most important/basic elements. (probably easiest then to autofill all other variables with 0.)
- Handling right-to-left READING order with left-to-right scanning order.
- Do we care about not printing order number on pages which are within the book's pagination (no skip) but aren't actually numbered? I think not. However for reference, the way to handle this would be collecting with skipOrderLabel = input(), casting to list if integer in inputToLists(), and testing "and not in skipOrderLabel" in generateOrderLabel() along with "if readingStartNum <= fileNum <= readingEndNum and fileNum not in unpaginatedPages:"
