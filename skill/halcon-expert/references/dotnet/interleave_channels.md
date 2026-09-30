# InterleaveChannels (Operator)

## Name

`InterleaveChannels` — Create an interleaved image from a multichannel image.

## Signature

`static void HOperatorSet.InterleaveChannels(HObject multichannelImage, out HObject interleavedImage, HTuple pixelFormat, HTuple rowBytes, HTuple alpha)`

`HImage HImage.InterleaveChannels(string pixelFormat, HTuple rowBytes, int alpha)`

`HImage HImage.InterleaveChannels(string pixelFormat, string rowBytes, int alpha)`

## Description

The operator `InterleaveChannels` creates an *`interleavedImage`*
from the input *`multichannelImage`* containing three or four
channels. This is useful to prepare a color image for visualization, e.g., by
converting it to a .NET Bitmap.

### Pixel format

The format of the pixels in *`interleavedImage`* is specified with
*`pixelFormat`*. Possible formats are *"rgb"*, *"rgba"*,
*"argb"*, *"bgr"*, *"bgra"*, and *"abgr"* for
byte images and *"rgb48"*, *"bgr48"*, *"rgba64"*,
*"bgra64"*, *"argb64"* and *"abgr64"* for uint2
images, where 'a' denotes the 4th ('alpha') channel.
Be aware that, in contrast to [`GenImageInterleaved`](gen_image_interleaved.md), LittleEndian
byte ordering is used in *`pixelFormat`*.

### Alpha channel

The alpha channel can be defined in the following ways:

| channels | domain |  |
| --- | --- | --- |
| 3 | not specified/full | Value of *`alpha`* is set for the complete image. |
| 3 | reduced | Inside the domain: alpha is set to *`alpha`*. Outside the domain: alpha is set to zero. |
| 4 |  | Alpha is set to the respective value of the fourth channel, domain and *`alpha`* are ignored. |

### Row alignment

The number of bytes between the beginning of two rows in the output
image can be set in *`rowBytes`*, e.g., to fulfill specific
alignment criteria.
Set *`rowBytes`* to *"match"* if no additional padding is
required. *`rowBytes`* must be at least the number of bytes in
*`pixelFormat`* times the width of *`multichannelImage`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`multichannelImage`** (input_object)  multichannel-image `→` [HImage](HImage.md) (byte)

Input multichannel image.

**`interleavedImage`** (output_object)  singlechannelimage `→` [HImage](HImage.md) (byte)

Output interleaved image.

**`pixelFormat`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Target format for InterleavedImage.

Default:
"rgba"

List of values:
"abgr", "abgr64", "argb", "argb64", "bgr", "bgr48", "bgra", "bgra64", "rgb", "rgb48", "rgba", "rgba64"

**`rowBytes`** (input_control)  integer `→` [HTuple](HTuple.md) (*string* / int / long)

Number of bytes in a row of the output image.

Default:
"match"

Suggested values:
"match"

**`alpha`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

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

`GenImageInterleaved`

## Module

Foundation
