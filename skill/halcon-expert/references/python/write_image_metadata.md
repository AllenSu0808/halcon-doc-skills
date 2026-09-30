# write_image_metadata (Operator)

## Name

`write_image_metadata` — Write metadata of image files.

## Signature

`def write_image_metadata(format: str, tag_name: str, tag_value: Union[int, float, str], file_name: str) -> None`

## Description

The operator `write_image_metadata` saves the information in
*`tag_value`* with the tag *`tag_name`* into the file
*`file_name`*.
In doing so, *`tag_value`* and *`tag_name`* can be single values
or tuples of values.
The parameter *`format`* specifies, in which format
the metadata is to be written.

This operators supports for *`format`* the `TIFF` metadata
formats *"tiff"* and *"bigtiff"*.
A file extension `.tif` is expected.

A list of the supported tag names for *`tag_name`* and the according
data types for *`tag_value`* is given in [`read_image_metadata`](read_image_metadata.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`format`** (input_control)  string `→` str

Graphic format.

Default:
"tiff"

Suggested values:
"tiff", "bigtiff"

**`tag_name`** (input_control)  tuple `→` str

Name of the tag to be written in the image file.

Default:
"tiff_image_description"

Suggested values:
"tiff_image_description", "tiff_make", "tiff_software", "tiff_date_time", "tiff_copyright", "tiff_exposure_time", "tiff_aperture_value", "tiff_light_source"

**`tag_value`** (input_control)  tuple `→` Union[int, float, str]

Value of the tag to be written in the image file.

**`file_name`** (input_control)  filename.write `→` str

Name of image file.

File extension:
.`tif`, .`tiff`

## Result

If *`tag_value`* can be correctly written for the specified parameters
the operator `write_image_metadata` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. In this case, an extended error
information, as e.g., the causative tag, may be set and can be queried with
the operator [`get_extended_error_info`](get_extended_error_info.md).

## Possible Predecessors

`write_image`

## Possible Successors

`read_image_metadata`

## Module

Foundation
