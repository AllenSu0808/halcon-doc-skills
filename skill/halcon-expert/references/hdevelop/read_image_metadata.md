# read_image_metadata (Operator)

## Name

`read_image_metadata` — Read metadata from image files.

## Signature

`read_image_metadata( : : Format, TagName, FileName : TagValue)`

## Description

The operator `read_image_metadata` reads the metadata of the file
*`FileName`* and returns the information in *`TagValue`*.
With *`TagName`* you specify, for which single tag or tuple of tags
you want to retrieve the information.
The parameter *`Format`* specifies, in which format the metadata is
encoded.

This operators supports for *`Format`* the `TIFF` metadata
formats *'tiff'* and *'bigtiff'*.
The file extension `.tif` is expected.

The following tags are readable:

|  |  |
| --- | --- |
| *`TagName`* | *`TagValue`* **data type** |
| *'tiff_aperture_value'* | double |
| *'tiff_copyright'* | string |
| *'tiff_date_time'* | string |
| *'tiff_exposure_time'* | double |
| *'tiff_image_description'* | string |
| *'tiff_light_source'* | integer |
| *'tiff_make'* | string |
| *'tiff_software'* | string |

Note, the operator returns an error in case the tag specified by
*`TagName`* has no value set.

You can retrieve all readable tags with the string
*'tiff_tags_supported_for_reading'* for *`TagName`* as well as
retrieve all writable tags with the string
*'tiff_tags_supported_for_writing'*. Each of both strings can be used
only as single value for *`TagName`*.

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
'tiff_image_description', 'tiff_make', 'tiff_software', 'tiff_date_time', 'tiff_copyright', 'tiff_exposure_time', 'tiff_aperture_value', 'tiff_light_source', 'tiff_tags_supported_for_reading', 'tiff_tags_supported_for_writing'

**`FileName`** (input_control)  filename.read `→`  (string)

Name of image file.

File extension:
.`tif`, .`tiff`

**`TagValue`** (output_control)  tuple `→`  (string / integer / real)

Output tag value read from the image file.

## Result

If *`TagValue`* can be correctly read for the specified input
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
