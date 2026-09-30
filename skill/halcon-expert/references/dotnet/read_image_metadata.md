# ReadImageMetadata (Operator)

## Name

`ReadImageMetadata` — Read metadata from image files.

## Signature

`static void HOperatorSet.ReadImageMetadata(HTuple format, HTuple tagName, HTuple fileName, out HTuple tagValue)`

`static HTuple HImage.ReadImageMetadata(string format, HTuple tagName, string fileName)`

## Description

The operator `ReadImageMetadata` reads the metadata of the file
*`fileName`* and returns the information in *`tagValue`*.
With *`tagName`* you specify, for which single tag or tuple of tags
you want to retrieve the information.
The parameter *`format`* specifies, in which format the metadata is
encoded.

This operators supports for *`format`* the `TIFF` metadata
formats *"tiff"* and *"bigtiff"*.
The file extension `.tif` is expected.

The following tags are readable:

|  |  |
| --- | --- |
| *`tagName`* | *`tagValue`* **data type** |
| *"tiff_aperture_value"* | double |
| *"tiff_copyright"* | string |
| *"tiff_date_time"* | string |
| *"tiff_exposure_time"* | double |
| *"tiff_image_description"* | string |
| *"tiff_light_source"* | integer |
| *"tiff_make"* | string |
| *"tiff_software"* | string |

Note, the operator returns an error in case the tag specified by
*`tagName`* has no value set.

You can retrieve all readable tags with the string
*"tiff_tags_supported_for_reading"* for *`tagName`* as well as
retrieve all writable tags with the string
*"tiff_tags_supported_for_writing"*. Each of both strings can be used
only as single value for *`tagName`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`format`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Graphic format.

Default:
"tiff"

Suggested values:
"tiff", "bigtiff"

**`tagName`** (input_control)  tuple `→` [HTuple](HTuple.md) (*string*)

Name of the tag to be written in the image file.

Default:
"tiff_image_description"

Suggested values:
"tiff_image_description", "tiff_make", "tiff_software", "tiff_date_time", "tiff_copyright", "tiff_exposure_time", "tiff_aperture_value", "tiff_light_source", "tiff_tags_supported_for_reading", "tiff_tags_supported_for_writing"

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

Name of image file.

File extension:
.`tif`, .`tiff`

**`tagValue`** (output_control)  tuple `→` [HTuple](HTuple.md) (*string* / int / long / double)

Output tag value read from the image file.

## Result

If *`tagValue`* can be correctly read for the specified input
parameters the operator `ReadImageMetadata` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. In this case, an extended error
information, as e.g., the causative tag, may be set and can be queried with
the operator [`GetExtendedErrorInfo`](get_extended_error_info.md).

## Possible Predecessors

`WriteImageMetadata`

## Possible Successors

`ReadImage`

## Module

Foundation
