# dev_open_file_dialog (Operator)

## Name

`dev_open_file_dialog` — Opens a file selection dialog.

## Signature

`dev_open_file_dialog( : : Filter, Mode, Path : Selection)`

## Description

`dev_open_file_dialog` opens a file selection dialog for
reading one file (*`Mode`* = *'read'*), reading one or more
files (*`Mode`* = *'read_multi'*), writing
(*`Mode`* = *'write'*) a file or choosing
(*`Mode`* = *'dir'*) a directory.
If *`Mode`* is set to *'default'* and *`Filter`* is set to
an HALCON operator the type is set to the value the operator would use.

The *`Filter`* can be used to select the types of the files which shall
be selected for reading or writing. The *`Filter`* can be set to
an HALCON operator, for example [`read_image`](read_image.md), which should read or write
the selected file. In that case, the filter is set appropriate to the files
used by the HALCON operator.
To select images of type JPEG and TIFF the filter could be set to
*'Images (*.jpg *.tif *.tiff)'*
or *'JPEG Files (*.jpg);;TIFF-Files (*.tif *.tiff)'*.
In the first case, by selecting the entry 'Images' all supported
images files are displayed together. In the
second case it is possible to choose between JPEG Files or TIFF Files.
The Filter is not case sensitive, therefore the same results
are supplied by *'JPEG Files (*.jpg)'* and
*'JPEG Files (*.JPG)'*.
The *'All Files (*)'* is always added.
To combine more than one filter you have to separate them
by *';;'*.

Examples:

The filter *'Images (*.jpg *.tiff *.tif)'* lists all files with
the extensions jpg, tiff and tif.

The filter *'JPEG Files (*.jpg)'* lists all files with the
extension jpg.

Combination of 3 filters:
*'Images (*.jpg *.tiff *.tif);;JPEG Files (*.jpg);;TIFF Files
(*.tiff *.tif)'*

The *`Path`* can be used to set the working directory.
If *`Path`* is set to *'default'* the working directory is
set to the last one used for this type of *`Mode`*.

After a successful execution the *`Selection`* contains the
selected files or file.

## Attention

This operator is not supported for code export.

## Parameters

**`Filter`** (input_control)  string `→`  (string)

Type of file or files to select.

**`Mode`** (input_control)  string `→`  (string)

Mode of the file selection dialog.

Default:
'default'

List of values:
'default', 'dir', 'read', 'read_multi', 'write'

**`Path`** (input_control)  string `→`  (string)

Working directory.

Default:
'default'

**`Selection`** (output_control)  string(-array) `→`  (string)

Selected file names.

Default:
'default'

## Example (HDevelop)

```
dev_open_file_dialog ('read_image', 'default','c:/',Selection)
read_image(ToolId, Selection)
```

## Result

If the values of the specified parameters are correct,
`dev_open_file_dialog` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Alternatives

`dev_open_dialog`

## See also

`dev_open_dialog`

## Module

Foundation
