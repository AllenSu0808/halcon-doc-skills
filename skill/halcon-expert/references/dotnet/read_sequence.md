# ReadSequence (Operator)

## Name

`ReadSequence` — Read images.

## Signature

`static void HOperatorSet.ReadSequence(out HObject image, HTuple headerSize, HTuple sourceWidth, HTuple sourceHeight, HTuple startRow, HTuple startColumn, HTuple destWidth, HTuple destHeight, HTuple pixelType, HTuple bitOrder, HTuple byteOrder, HTuple pad, HTuple index, HTuple fileName)`

`void HImage.ReadSequence(int headerSize, int sourceWidth, int sourceHeight, int startRow, int startColumn, int destWidth, int destHeight, string pixelType, string bitOrder, string byteOrder, string pad, int index, string fileName)`

## Description

The operator `ReadSequence` reads unformatted image data,
from a file and returns a “suitable” image. The image data must
be filled consecutively pixel by pixel and line by line.

Any file headers (with the length *`headerSize`* bytes) are
skipped. The parameters *`sourceWidth`* and
*`sourceHeight`* indicate the size of the filled image.
*`destWidth`* and *`destHeight`* indicate the size of the
image. In the simplest case these parameters are the same. However,
areas can also be read. The upper left corner of the required image
area can be determined via *`startRow`* and
*`startColumn`*.

The pixel types *"bit"*, *"byte"*, *"short"*
(16 bits, unsigned), *"signed_short"* (16 bits, signed),
*"long"* (32 bits, signed), *"swapped_long"* (32 bits,
with swapped segments), and *"real"* (32 bit floating point
numbers) are supported. Furthermore, the operator
`ReadSequence` enables the extraction of components of a RBG
image, if a triple of three bytes (in the sequence “red”,
“green”, “blue”) was filed in the image file. For the red
component the pixel type *"r_byte"* must be chosen, and
correspondingly for the green and blue components *"g_byte"*
or *"b_byte"*, respectively.

*"MSBFirst"* (most significant bit first) or the inversion
thereof (*"LSBFirst"*) can be chosen for the bit order
(*`bitOrder`*). The byte orders (*`byteOrder`*)
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
set via the operator [`SetSystem`](set_system.md). More than one image
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

**`image`** (output_object)  image `→` [HImage](HImage.md) (byte / int2 / uint2 / int4)

Image read.

**`headerSize`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of bytes for file header.

Default:
0

Value range:
`0
≤
headerSize`

**`sourceWidth`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Number of image columns of the filed image.

Default:
512

Value range:
`1
≤
sourceWidth`

**`sourceHeight`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Number of image lines of the filed image.

Default:
512

Value range:
`1
≤
sourceHeight`

**`startRow`** (input_control)  point.y `→` [HTuple](HTuple.md) (*int* / long)

Starting point of image area (line).

Default:
0

Value range:
`0
≤
startRow`

Restriction:
`StartRow < SourceHeight`

**`startColumn`** (input_control)  point.x `→` [HTuple](HTuple.md) (*int* / long)

Starting point of image area (column).

Default:
0

Value range:
`0
≤
startColumn`

Restriction:
`StartColumn < SourceWidth`

**`destWidth`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Number of image columns of output image.

Default:
512

Value range:
`1
≤
destWidth`

Restriction:
`DestWidth <= SourceWidth`

**`destHeight`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Number of image lines of output image.

Default:
512

Value range:
`1
≤
destHeight`

Restriction:
`DestHeight <= SourceHeight`

**`pixelType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of pixel values.

Default:
"byte"

List of values:
"b_byte", "bit", "byte", "g_byte", "long", "r_byte", "real", "short", "signed_short", "swapped_long"

**`bitOrder`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Sequence of bits within one byte.

Default:
"MSBFirst"

List of values:
"LSBFirst", "MSBFirst"

**`byteOrder`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Sequence of bytes within one
'short' unit.

Default:
"MSBFirst"

List of values:
"LSBFirst", "MSBFirst"

**`pad`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Data units within one image line (alignment).

Default:
"byte"

List of values:
"byte", "long", "short"

**`index`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of images in the file.

Default:
1

Value range:
`1
≤
index` (lin)

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

Name of input file.

## Result

If the parameter values are correct the operator
`ReadSequence` returns the value 2 (
H_MSG_TRUE)
. Otherwise an
exception is raised.

## Possible Successors

`DispImage`,
`CountChannels`,
`Decompose3`,
`WriteImage`,
`Rgb1ToGray`

## Alternatives

`ReadImage`

## See also

`ReadImage`

## Module

Foundation
