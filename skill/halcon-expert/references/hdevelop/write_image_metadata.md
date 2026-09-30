# write_image_metadata (Operator)

## Name

`write_image_metadata` — Write metadata of image files.

## Signature

`write_image_metadata( : : Format, TagName, TagValue, FileName : )`

## Description

The operator `write_image_metadata` saves the information in
*`TagValue`* with the tag *`TagName`* into the file
*`FileName`*.
In doing so, *`TagValue`* and *`TagName`* can be single values
or tuples of values.
The parameter *`Format`* specifies, in which format
the metadata is to be written.

This operators supports for *`Format`* the `TIFF` metadata
formats *'tiff'* and *'bigtiff'*.
A file extension `.tif` is expected.

A list of the supported tag names for *`TagName`* and the according
data types for *`TagValue`* is given in [`read_image_metadata`](read_image_metadata.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Format`** (input_control)  string `→`  (string)

Graphic format.

Default:
'tiff'

Suggested values:
'tiff', 'bigtiff'

**`TagName`** (input_control)  tuple `→`  (string)

Name of the tag to be written in the image file.

Default:
'tiff_image_description'

Suggested values:
'tiff_image_description', 'tiff_make', 'tiff_software', 'tiff_date_time', 'tiff_copyright', 'tiff_exposure_time', 'tiff_aperture_value', 'tiff_light_source'

**`TagValue`** (input_control)  tuple `→`  (string / integer / real)

Value of the tag to be written in the image file.

**`FileName`** (input_control)  filename.write `→`  (string)

Name of image file.

File extension:
.`tif`, .`tiff`

## Result

If *`TagValue`* can be correctly written for the specified parameters
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
