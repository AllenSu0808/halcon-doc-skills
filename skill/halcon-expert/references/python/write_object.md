# write_object (Operator)

## Name

`write_object` — Write an iconic object.

## Signature

`def write_object(object: HObject, file_name: str) -> None`

## Description

`write_object` writes the iconic *`object`* to the file
*`file_name`*. The iconic object is a (possibly mixed) tuple of
images, regions, or XLDs. If no extension is specified in *`file_name`*,
the extension `'.hobj'` will be appended.
The iconic data is written in the HALCON Iconic Object format
described below.

- **HALCON Iconic Object (HOBJ):** —

  HOBJ is a binary file format, which provides the functionality to
  write and read all kinds of iconic HALCON objects (images, regions,
  and XLDs). Since data is written with neither compression nor
  conversion, writing this file format is faster than other supported file
  formats in most circumstances. Hence, if an application needs to read and
  write all kinds of iconic HALCON objects as fast as possible and no compression is
  required, this format should be used. The default file extension for
  this file format is `'.hobj'`. For images, all HALCON pixel types
  can be written. Multi-channel images are supported. The channels can have
  mixed pixel types but must have the same width and height. The domain of
  an image and it's creation date are stored in the file as well. An object
  tuple is written into a single file.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`object`** (input_object)  object(-array) `→` HObject

Iconic object.

**`file_name`** (input_control)  filename `→` str

Name of file.

File extension:
.`hobj`

## Result

If the parameters are valid, the operator
`write_object` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`read_object`,
`read_image`

## See also

`read_object`,
`write_image`,
`read_image`,
`write_region`,
`read_region`

## Module

Foundation
