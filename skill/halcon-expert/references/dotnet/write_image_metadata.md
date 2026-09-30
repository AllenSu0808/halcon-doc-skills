# WriteImageMetadata (Operator)

## Name

`WriteImageMetadata` — Write metadata of image files.

## Signature

`static void HOperatorSet.WriteImageMetadata(HTuple format, HTuple tagName, HTuple tagValue, HTuple fileName)`

`static void HImage.WriteImageMetadata(string format, HTuple tagName, HTuple tagValue, string fileName)`

## Description

The operator `WriteImageMetadata` saves the information in
*`tagValue`* with the tag *`tagName`* into the file
*`fileName`*.
In doing so, *`tagValue`* and *`tagName`* can be single values
or tuples of values.
The parameter *`format`* specifies, in which format
the metadata is to be written.

This operators supports for *`format`* the `TIFF` metadata
formats *"tiff"* and *"bigtiff"*.
A file extension `.tif` is expected.

A list of the supported tag names for *`tagName`* and the according
data types for *`tagValue`* is given in [`ReadImageMetadata`](read_image_metadata.md).

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
"tiff_image_description", "tiff_make", "tiff_software", "tiff_date_time", "tiff_copyright", "tiff_exposure_time", "tiff_aperture_value", "tiff_light_source"

**`tagValue`** (input_control)  tuple `→` [HTuple](HTuple.md) (*string* / int / long / double)

Value of the tag to be written in the image file.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Name of image file.

File extension:
.`tif`, .`tiff`

## Result

If *`tagValue`* can be correctly written for the specified parameters
the operator `WriteImageMetadata` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. In this case, an extended error
information, as e.g., the causative tag, may be set and can be queried with
the operator [`GetExtendedErrorInfo`](get_extended_error_info.md).

## Possible Predecessors

`WriteImage`

## Possible Successors

`ReadImageMetadata`

## Module

Foundation
