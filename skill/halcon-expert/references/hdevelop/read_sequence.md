# read_sequence (Operator)

## Name

`read_sequence` — Read images.

## Signature

`read_sequence( : Image : HeaderSize, SourceWidth, SourceHeight, StartRow, StartColumn, DestWidth, DestHeight, PixelType, BitOrder, ByteOrder, Pad, Index, FileName : )`

## Description

The operator `read_sequence` reads unformatted image data,
from a file and returns a “suitable” image. The image data must
be filled consecutively pixel by pixel and line by line.

Any file headers (with the length *`HeaderSize`* bytes) are
skipped. The parameters *`SourceWidth`* and
*`SourceHeight`* indicate the size of the filled image.
*`DestWidth`* and *`DestHeight`* indicate the size of the
image. In the simplest case these parameters are the same. However,
areas can also be read. The upper left corner of the required image
area can be determined via *`StartRow`* and
*`StartColumn`*.

The pixel types *'bit'*, *'byte'*, *'short'*
(16 bits, unsigned), *'signed_short'* (16 bits, signed),
*'long'* (32 bits, signed), *'swapped_long'* (32 bits,
with swapped segments), and *'real'* (32 bit floating point
numbers) are supported. Furthermore, the operator
`read_sequence` enables the extraction of components of a RBG
image, if a triple of three bytes (in the sequence “red”,
“green”, “blue”) was filed in the image file. For the red
component the pixel type *'r_byte'* must be chosen, and
correspondingly for the green and blue components *'g_byte'*
or *'b_byte'*, respectively.

*'MSBFirst'* (most significant bit first) or the inversion
thereof (*'LSBFirst'*) can be chosen for the bit order
(*`BitOrder`*). The byte orders (*`ByteOrder`*)
*'MSBFirst'* (most significant byte first) or
*'LSBFirst'*, respectively, are processed analogously.
Finally an alignment (*`Pad`*) can be set at the end of the
line: *'byte'*, *'short'* or *'long'*. If a
whole image sequence is stored in the file a single image (beginning
at Index 1) can be chosen via the parameter *`Index`*.

Image files are searched in the current directory (determined by the
environment variable) and in the image directory of HALCON. The
image directory of HALCON is preset at `'.'` and
`'/usr/local/halcon/images'` in a Unix-like environment and can be
set via the operator [`set_system`](set_system.md). More than one image
directory can be indicated. This is done by separating the
individual directories by a colon.

Furthermore the search path can be set via the environment variable
HALCONIMAGES (same structure as *'image_dir'*). Example:

```
   setenv HALCONIMAGES "/usr/images:/usr/local/halcon/images"
```

HALCON also searches images in the subdirectory
`'images'` (Images for the program examples). The
environment variable HALCONROOT is used for the HALCON directory.

## Attention

If files of pixel type *'real'* are read and the byte order
is chosen incorrectly (i.e., differently from the byte order in
which the data is stored in the file) program error and even crashes
because of floating point exceptions may result.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (output_object)  image `→` object (byte / int2 / uint2 / int4)

Image read.

**`HeaderSize`** (input_control)  integer `→`  (integer)

Number of bytes for file header.

Default:
0

Value range:
`0
≤
HeaderSize`

**`SourceWidth`** (input_control)  extent.x `→`  (integer)

Number of image columns of the filed image.

Default:
512

Value range:
`1
≤
SourceWidth`

**`SourceHeight`** (input_control)  extent.y `→`  (integer)

Number of image lines of the filed image.

Default:
512

Value range:
`1
≤
SourceHeight`

**`StartRow`** (input_control)  point.y `→`  (integer)

Starting point of image area (line).

Default:
0

Value range:
`0
≤
StartRow`

Restriction:
`StartRow < SourceHeight`

**`StartColumn`** (input_control)  point.x `→`  (integer)

Starting point of image area (column).

Default:
0

Value range:
`0
≤
StartColumn`

Restriction:
`StartColumn < SourceWidth`

**`DestWidth`** (input_control)  extent.x `→`  (integer)

Number of image columns of output image.

Default:
512

Value range:
`1
≤
DestWidth`

Restriction:
`DestWidth <= SourceWidth`

**`DestHeight`** (input_control)  extent.y `→`  (integer)

Number of image lines of output image.

Default:
512

Value range:
`1
≤
DestHeight`

Restriction:
`DestHeight <= SourceHeight`

**`PixelType`** (input_control)  string `→`  (string)

Type of pixel values.

Default:
'byte'

List of values:
'b_byte', 'bit', 'byte', 'g_byte', 'long', 'r_byte', 'real', 'short', 'signed_short', 'swapped_long'

**`BitOrder`** (input_control)  string `→`  (string)

Sequence of bits within one byte.

Default:
'MSBFirst'

List of values:
'LSBFirst', 'MSBFirst'

**`ByteOrder`** (input_control)  string `→`  (string)

Sequence of bytes within one
'short' unit.

Default:
'MSBFirst'

List of values:
'LSBFirst', 'MSBFirst'

**`Pad`** (input_control)  string `→`  (string)

Data units within one image line (alignment).

Default:
'byte'

List of values:
'byte', 'long', 'short'

**`Index`** (input_control)  integer `→`  (integer)

Number of images in the file.

Default:
1

Value range:
`1
≤
Index` (lin)

**`FileName`** (input_control)  filename.read `→`  (string)

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
