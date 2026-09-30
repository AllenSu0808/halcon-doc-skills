# mirror_image (Operator)

## Name

`mirror_image` — Mirror an image.

## Signature

`mirror_image(Image : ImageMirror : Mode : )`

## Description

`mirror_image` reflects an image *`Image`* about
one of three possible axes. If *`Mode`* is set to
*'row'*, it is reflected about the horizontal axis,
if *`Mode`* is set to *'column'*, about the vertical
axis, and if *`Mode`* is set to *'diagonal'*, about
the main diagonal x=y.

## Attention

`mirror_image` can be executed on OpenCL devices if the input
image does not exceed the maximum size of image objects of the selected
device. However, execution might be faster on the CPU, especially for the
mode *'row'*.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on internal data level.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte* / int2* / uint2* / int4* / real*) **allowed for compute devices*

Input image.

**`ImageMirror`** (output_object)  (multichannel-)image(-array) `→` object (byte / int2 / uint2 / int4 / real)

Reflected image.

**`Mode`** (input_control)  string `→`  (string)

Axis of reflection.

Default:
'row'

List of values:
'column', 'diagonal', 'row'

## Example (HDevelop)

```
read_image(Image,'monkey')
dev_display (Image)
mirror_image(Image,MirrorImage,'row')
dev_display (MirrorImage)
```

## Alternatives

`hom_mat2d_rotate`,
`hom_mat2d_reflect`,
`affine_trans_image`,
`rotate_image`

## See also

`rotate_image`,
`hom_mat2d_rotate`

## Module

Foundation
