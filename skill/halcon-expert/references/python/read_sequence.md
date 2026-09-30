# read_sequence (Operator)

## Name

`read_sequence` — Read images.

## Signature

`def read_sequence(header_size: int, source_width: int, source_height: int, start_row: int, start_column: int, dest_width: int, dest_height: int, pixel_type: str, bit_order: str, byte_order: str, pad: str, index: int, file_name: str) -> HObject`

## Description

The operator `read_sequence` reads unformatted image data,
from a file and returns a “suitable” image. The image data must
be filled consecutively pixel by pixel and line by line.

Any file headers (with the length *`header_size`* bytes) are
skipped. The parameters *`source_width`* and
*`source_height`* indicate the size of the filled image.
*`dest_width`* and *`dest_height`* indicate the size of the
image. In the simplest case these parameters are the same. However,
areas can also be read. The upper left corner of the required image
area can be determined via *`start_row`* and
*`start_column`*.

The pixel types *"bit"*, *"byte"*, *"short"*
(16 bits, unsigned), *"signed_short"* (16 bits, signed),
*"long"* (32 bits, signed), *"swapped_long"* (32 bits,
with swapped segments), and *"real"* (32 bit floating point
numbers) are supported. Furthermore, the operator
`read_sequence` enables the extraction of components of a RBG
image, if a triple of three bytes (in the sequence “red”,
“green”, “blue”) was filed in the image file. For the red
component the pixel type *"r_byte"* must be chosen, and
correspondingly for the green and blue components *"g_byte"*
or *"b_byte"*, respectively.

*"MSBFirst"* (most significant bit first) or the inversion
thereof (*"LSBFirst"*) can be chosen for the bit order
(*`bit_order`*). The byte orders (*`byte_order`*)
*"MSBFirst"* (most significant byte first) or
*"LSBFirst"*, respectively, are processed analogously.
Finally an alignment (*`pad`*) can be set at the end of the
line: *"byte"*, *"short"* or *"long"*. If a
whole image sequence is stored in the file a single image (beginning
at Index 1) can be chosen via the parameter *`index`*.

Image files are searched in the current directory (determined by the
environment variable) and in the image directory of HALCON. The
image directory of HALCON is preset at `'.'` and
`'/usr/local/halcon/images'` in a Unix-like environment and can be
set via the operator [`set_system`](set_system.md). More than one image
directory can be indicated. This is done by separating the
individual directories by a colon.

Furthermore the search path can be set via the environment variable
HALCONIMAGES (same structure as *"image_dir"*). Example:

```
   setenv HALCONIMAGES "/usr/images:/usr/local/halcon/images"
```

HALCON also searches images in the subdirectory
`'images'` (Images for the program examples). The
environment variable HALCONROOT is used for the HALCON directory.

## Attention

If files of pixel type *"real"* are read and the byte order
is chosen incorrectly (i.e., differently from the byte order in
which the data is stored in the file) program error and even crashes
because of floating point exceptions may result.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (output_object)  image `→` HObject (byte / int2 / uint2 / int4)

Image read.

**`header_size`** (input_control)  integer `→` int

Number of bytes for file header.

Default:
0

Value range:
`0
≤
header_size`

**`source_width`** (input_control)  extent.x `→` int

Number of image columns of the filed image.

Default:
512

Value range:
`1
≤
source_width`

**`source_height`** (input_control)  extent.y `→` int

Number of image lines of the filed image.

Default:
512

Value range:
`1
≤
source_height`

**`start_row`** (input_control)  point.y `→` int

Starting point of image area (line).

Default:
0

Value range:
`0
≤
start_row`

Restriction:
`StartRow < SourceHeight`

**`start_column`** (input_control)  point.x `→` int

Starting point of image area (column).

Default:
0

Value range:
`0
≤
start_column`

Restriction:
`StartColumn < SourceWidth`

**`dest_width`** (input_control)  extent.x `→` int

Number of image columns of output image.

Default:
512

Value range:
`1
≤
dest_width`

Restriction:
`DestWidth <= SourceWidth`

**`dest_height`** (input_control)  extent.y `→` int

Number of image lines of output image.

Default:
512

Value range:
`1
≤
dest_height`

Restriction:
`DestHeight <= SourceHeight`

**`pixel_type`** (input_control)  string `→` str

Type of pixel values.

Default:
"byte"

List of values:
"b_byte", "bit", "byte", "g_byte", "long", "r_byte", "real", "short", "signed_short", "swapped_long"

**`bit_order`** (input_control)  string `→` str

Sequence of bits within one byte.

Default:
"MSBFirst"

List of values:
"LSBFirst", "MSBFirst"

**`byte_order`** (input_control)  string `→` str

Sequence of bytes within one
'short' unit.

Default:
"MSBFirst"

List of values:
"LSBFirst", "MSBFirst"

**`pad`** (input_control)  string `→` str

Data units within one image line (alignment).

Default:
"byte"

List of values:
"byte", "long", "short"

**`index`** (input_control)  integer `→` int

Number of images in the file.

Default:
1

Value range:
`1
≤
index` (lin)

**`file_name`** (input_control)  filename.read `→` str

Name of input file.

## Result

If the parameter values are correct the operator
`read_sequence` returns the value 2 (
H_MSG_TRUE)
. Otherwise an
exception is raised.

## Possible Successors

`disp_image`,
`count_channels`,
`decompose3`,
`write_image`,
`rgb1_to_gray`

## Alternatives

`read_image`

## See also

`read_image`

## Module

Foundation
