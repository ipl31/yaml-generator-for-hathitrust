# YAML Generator for Digitized HathiTrust Submissions

The HathiTrust submissions process requires a .yml file whose contents contain information about the scan and a detailed contents list. The contents list can include information about reading order, chapters, and page type. This Python (2.7.x) script allows one to generate a valid .yml file for *digitized* (not born-digital) materials. With some minor modifications it could work for born-digital materials too.

## Files Included

yaml_generator.py &mdash; Main python script.
HathiTrust_Submission_YAML_Data_Spreadsheet.csv &mdash; a CSV document with column headers for each piece of information required by the script. Can be used by student workers or others to record data before it's entered into the YAML generator. Ordering reflects the order in which information is requested by the script.
HathiTrust_Submission_Sample.csv &mdash; a copy of the YAML Data Spreadsheet populated with a couple sets of values which can be used as sample information.

## Using the YAML Generator



### Personalizing the YAML Generator to Your Repository

The YAML generator contains certain pieces of hard-coded information and some assumptions specific to Notre Dame. This section includes line numbers in yaml_generator.py which should be examined and possibly changed.

instances of Notre DAme/Kirtas scanner/DST assumptions

## Overview of the Project

To allow one to input a small amount of information via the command line and generate a complete, or nearly-complete YML file. These files will still require manual review, but the tool should greatly speed up the creation of a great deal of information.

### Project Phases

- **Phase 1.** (Completed, 2016-02-19) Generate the list of the filenames of scanned images. Takes filetype input, though this may be turned into a TIFF/JP2 switch, since only those filetypes are allowed. Presumes all filenames will be the same type. This is a core function, as it would be a real PITA to create the list manually. Takes input of final number of image. Handles leading 0s with a simple test to create standardized 8-digit-long filenames.
- **Phase 2.** (Completed, 2016-02-19) Print the list of images in proper syntax for the final process. Write list to file.
- **Phase 3.** (Completed, 2016-02-19) Add reading order input, which should be on what page the first page starts. Using numbers so far.
- **Phase 4.** (Completed, 2016-02-22) Identify one-time page *types*. Develop a way to insert one, then duplicate.
- **Phase 5.** (Completed, 2016-02-22) Roman numeral pages before reading order. Use test on reading order to stop them too.
- **Phase 6.** (Completed, 2016-02-29) Identify all other information necessary for the file. Come up with a list of necessary information and structure questions to take its input and print it at the top of the file.
- **Phase 7.** Add number of final page. Handle cases where a page number is skipped (for example cases where a group of images in the middle of the book have page numbers and pagination picks up right after).

### Not in a phase yet

Things for future work:

- Handling multiwork issues. First need to get more information from HT on how multiwork issues affect pagination. How do they handle two Page 1s?
