# threshold_sub_pix (Operator)

## Name

`threshold_sub_pix` — Extract level crossings from an image with subpixel accuracy.

## Signature

`threshold_sub_pix(Image : Border : Threshold : )`

## Description

`threshold_sub_pix` extracts the level crossings at the level
*`Threshold`* of the input image *`Image`* with subpixel
accuracy. The extracted level crossings are returned as
XLD-contours in *`Border`*. In contrast to the
operator [`threshold`](threshold.md), `threshold_sub_pix` does not
return regions, but the lines that separate regions with a gray
value less than *`Threshold`* from regions with a gray value
greater than *`Threshold`*.

For the extraction, the input image is regarded as a surface, in
which the gray values are interpolated bilinearly between the
centers of the individual pixels. Consistent with the surface thus
defined, level crossing lines are extracted for each pixel and
linked into topologically sound contours. This means that the level
crossing contours are correctly split at junction points. If the
image contains extended areas of constant gray value
*`Threshold`*, only the border of such areas is returned as
level crossings.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (byte / int1 / int2 / uint2 / int4 / real)

Input image.

**`Border`** (output_object)  xld_cont-array `→` object

Extracted level crossings.

**`Threshold`** (input_control)  number `→`  (real / integer)

Threshold for the level crossings.

Default:
128

Suggested values:
0.0, 10.0, 30.0, 64.0, 128.0, 200.0, 220.0, 255.0

## Example (HDevelop)

```
read_image(Image,'fabrik')
threshold_sub_pix(Image,Border,35)
dev_display(Border)
```

## Result

`threshold_sub_pix` usually returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Alternatives

`threshold`

## See also

`zero_crossing_sub_pix`

## Module

2D Metrology
