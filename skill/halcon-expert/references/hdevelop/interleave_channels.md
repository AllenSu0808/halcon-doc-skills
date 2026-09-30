# interleave_channels (Operator)

## Name

`interleave_channels` — Create an interleaved image from a multichannel image.

## Signature

`interleave_channels(MultichannelImage : InterleavedImage : PixelFormat, RowBytes, Alpha : )`

## Description

The operator `interleave_channels` creates an *`InterleavedImage`*
from the input *`MultichannelImage`* containing three or four
channels. This is useful to prepare a color image for visualization, e.g., by
converting it to a .NET Bitmap.

### Pixel format

The format of the pixels in *`InterleavedImage`* is specified with
*`PixelFormat`*. Possible formats are *'rgb'*, *'rgba'*,
*'argb'*, *'bgr'*, *'bgra'*, and *'abgr'* for
byte images and *'rgb48'*, *'bgr48'*, *'rgba64'*,
*'bgra64'*, *'argb64'* and *'abgr64'* for uint2
images, where 'a' denotes the 4th ('alpha') channel.
Be aware that, in contrast to [`gen_image_interleaved`](gen_image_interleaved.md), LittleEndian
byte ordering is used in *`PixelFormat`*.

### Alpha channel

The alpha channel can be defined in the following ways:

| channels | domain |  |
| --- | --- | --- |
| 3 | not specified/full | Value of *`Alpha`* is set for the complete image. |
| 3 | reduced | Inside the domain: alpha is set to *`Alpha`*. Outside the domain: alpha is set to zero. |
| 4 |  | Alpha is set to the respective value of the fourth channel, domain and *`Alpha`* are ignored. |

### Row alignment

The number of bytes between the beginning of two rows in the output
image can be set in *`RowBytes`*, e.g., to fulfill specific
alignment criteria.
Set *`RowBytes`* to *'match'* if no additional padding is
required. *`RowBytes`* must be at least the number of bytes in
*`PixelFormat`* times the width of *`MultichannelImage`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`MultichannelImage`** (input_object)  multichannel-image `→` object (byte)

Input multichannel image.

**`InterleavedImage`** (output_object)  singlechannelimage `→` object (byte)

Output interleaved image.

**`PixelFormat`** (input_control)  string `→`  (string)

Target format for InterleavedImage.

Default:
'rgba'

List of values:
'abgr', 'abgr64', 'argb', 'argb64', 'bgr', 'bgr48', 'bgra', 'bgra64', 'rgb', 'rgb48', 'rgba', 'rgba64'

**`RowBytes`** (input_control)  integer `→`  (string / integer)

Number of bytes in a row of the output image.

Default:
'match'

Suggested values:
'match'

**`Alpha`** (input_control)  integer `→`  (integer)

Alpha value for three channel input images.

Default:
255

Suggested values:
255, 0

## Example (C#)

```
  HTuple type, width, height;
  HImage patras = new HImage("patras");

  HImage interleaved = patras.InterleaveChannels("argb", "match", 255);
  IntPtr ptr = interleaved.GetImagePointer1(out type, out width, out height);

  Image img = new Bitmap(width/4, height, width,
                         PixelFormat.Format32bppArgb, ptr);

  pictureBox.Image = img;
```

## See also

`gen_image_interleaved`

## Module

Foundation
