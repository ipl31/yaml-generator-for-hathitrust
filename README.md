# YAML Generator for HathiTrust Submissions

The HathiTrust submissions process requires a .yml file whose contents contain information about the scan and a detailed contents list. The contents list can include information about reading order, chapters, and page type.

## Project Goal

To allow one to input a small amount of information via the command line and generate a complete, or nearly-complete YML file. These files will still require manual review but the tool should greatly speed up the creation of a great deal of information.

## Project Phases

- **Phase 1.** (Completed, 2016-02-19) Generate the list of the filenames of scanned images. Takes filetype input, though this may be turned into a TIFF/JP2 switch, since only those filetypes are allowed. Presumes all filenames will be the same type. This is a core function, as it would be a real PITA to create the list manually. Takes input of final number of image. Handles leading 0s with a simple test to create standardized 8-digit-long filenames.
- **Phase 2.** (Completed, 2016-02-19) Print the list of images in proper syntax for the final process. Write list to file.
- **Phase 3.** (Completed, 2016-02-19) Add reading order input, which should be on what page the first page starts. Using numbers so far.
- **Phase 4.** Identify one-time page *types*. Develop a way to insert one, then duplicate.
- **Phase 5.** Come up with ways to handle multiple page *types*. Build on method of inserting.
- **Phase 6.** Identify all other information necessary for the file. Come up with a list of necessary information and structure questions to take its input and print it at the top of the file.

### Not in a phase yet:

- Handle Roman numeral preface page. Multiple input? Has preface pages? Starting page? Can Python print or do I need to add a dictionary?
