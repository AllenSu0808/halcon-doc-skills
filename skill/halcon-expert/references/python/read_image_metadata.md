# read_image_metadata (Operator)

## Name

`read_image_metadata` — Read metadata from image files.

## Signature

`def read_image_metadata(format: str, tag_name: str, file_name: str) -> Union[int, float, str]`

## Description

The operator `read_image_metadata` reads the metadata of the file
*`file_name`* and returns the information in *`tag_value`*.
With *`tag_name`* you specify, for which single tag or tuple of tags
you want to retrieve the information.
The parameter *`format`* specifies, in which format the metadata is
encoded.

This operators supports for *`format`* the `TIFF` metadata
formats *"tiff"* and *"bigtiff"*.
The file extension `.tif` is expected.

The following tags are readable:

|  |  |
| --- | --- |
| *`tag_name`* | *`tag_value`* **data type** |
| *"tiff_aperture_value"* | double |
| *"tiff_copyright"* | string |
| *"tiff_date_time"* | string |
| *"tiff_exposure_time"* | double |
| *"tiff_image_description"* | string |
| *"tiff_light_source"* | integer |
| *"tiff_make"* | string |
| *"tiff_software"* | string |

Note, the operator returns an error in case the tag specified by
*`tag_name`* has no value set.

You can retrieve all readable tags with the string
*"tiff_tags_supported_for_reading"* for *`tag_name`* as well as
retrieve all writable tags with the string
*"tiff_tags_supported_for_writing"*. Each of both strings can be used
only as single value for *`tag_name`*.

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
"tiff_image_description", "tiff_make", "tiff_software", "tiff_date_time", "tiff_copyright", "tiff_exposure_time", "tiff_aperture_value", "tiff_light_source", "tiff_tags_supported_for_reading", "tiff_tags_supported_for_writing"

**`file_name`** (input_control)  filename.read `→` str

Name of image file.

File extension:
.`tif`, .`tiff`

**`tag_value`** (output_control)  tuple `→` Union[int, float, str]

Output tag value read from the image file.

## Result

If *`tag_value`* can be correctly read for the specified input
parameters the operator `read_image_metadata` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. In this case, an extended error
information, as e.g., the causative tag, may be set and can be queried with
the operator [`get_extended_error_info`](get_extended_error_info.md).

## Possible Predecessors

`write_image_metadata`

## Possible Successors

`read_image`

## Module

Foundation
