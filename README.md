# YAML Generator for HathiTrust Submissions

The HathiTrust submissions process requires a .yml file whose contents contain information about the scan and a detailed contents list. The contents list can include information about reading order, chapters, and page type.

## Project Goal

To allow one to input a small amount of information via the command line and generate a complete, or nearly-complete YML file. These files will still require manual review but the tool should greatly speed up the creation of a great deal of information.

## Project Phases

- **Phase 1.** (Completed, 2016-02-19) Generate the list of the filenames of scanned images. Takes filetype input, though this may be turned into a TIFF/JP2 switch, since only those filetypes are allowed. Presumes all filenames will be the same type. This is a core function, as it would be a real PITA to create the list manually. Takes input of final number of image. Handles leading 0s with a simple test to create standardized 8-digit-long filenames.
- **Phase 2.** Print the list of images in proper syntax for the final process. Write list to file.
- **Phase 3.** Add reading order input, which should be on what page the first page starts. Using numbers so far.

### Not in a phase yet:

- Handle Roman numeral preface page. Multiple input? Has preface pages? Starting page? Can Python print or do I need to add a dictionary?
- Handle input of page TYPES. Will have to be able to handle things that get repeated like Chapters and Image-only pages as lists.