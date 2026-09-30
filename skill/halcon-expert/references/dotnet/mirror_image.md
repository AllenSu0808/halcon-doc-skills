# MirrorImage (Operator)

## Name

`MirrorImage` — Mirror an image.

## Signature

`static void HOperatorSet.MirrorImage(HObject image, out HObject imageMirror, HTuple mode)`

`HImage HImage.MirrorImage(string mode)`

## Description

`MirrorImage` reflects an image *`image`* about
one of three possible axes. If *`mode`* is set to
*"row"*, it is reflected about the horizontal axis,
if *`mode`* is set to *"column"*, about the vertical
axis, and if *`mode`* is set to *"diagonal"*, about
the main diagonal x=y.

## Attention

`MirrorImage` can be executed on OpenCL devices if the input
image does not exceed the maximum size of image objects of the selected
device. However, execution might be faster on the CPU, especially for the
mode *"row"*.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / int2* / uint2* / int4* / real*) **allowed for compute devices*

Input image.

**`imageMirror`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / int4 / real)

Reflected image.

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Axis of reflection.

Default:
"row"

List of values:
"column", "diagonal", "row"

## Example (HDevelop)

```
read_image(Image,'monkey')
dev_display (Image)
mirror_image(Image,MirrorImage,'row')
dev_display (MirrorImage)
```

## Alternatives

`HomMat2dRotate`,
`HomMat2dReflect`,
`AffineTransImage`,
`RotateImage`

## See also

`RotateImage`,
`HomMat2dRotate`

## Module

Foundation
