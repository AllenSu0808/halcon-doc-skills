# gen_bundle_adjusted_mosaic (Operator)

## Name

`gen_bundle_adjusted_mosaic` — Combine multiple images into a mosaic image.

## Signature

`gen_bundle_adjusted_mosaic(Images : MosaicImage : HomMatrices2D, StackingOrder, TransformDomain : TransMat2D)`

## Description

`gen_bundle_adjusted_mosaic` combines the input images
contained in the object *`Images`* into a mosaic image
*`MosaicImage`*. The relative positions of the images are
defined by 3x3 projective transformation matrices.
The array *`HomMatrices2D`* contains a sequence of these
linearized matrices. The transformation matrices can be computed
with [`bundle_adjust_mosaic`](bundle_adjust_mosaic.md).

The origin of *`MosaicImage`* and its size are automatically
chosen so that all of the input images are completely visible.

The order in which the images are added to the mosaic is given by
the array *`StackingOrder`*. The first index in this array
will end up at the bottom of the image stack while the last one will
be on top. If *'default'* is given instead of an array of
integers, the canonical order (images in the order used in
*`Images`*) will be used.

The parameter *`TransformDomain`* can be used to determine
whether the domains of *`Images`* are also transformed. Since
the transformation of the domains costs runtime, this parameter
should be used to specify whether this is desired or not. If
*`TransformDomain`* is set to *'false'* the domain of
the input images is ignored and the complete images are
transformed.

On output, the parameter *`TransMat2D`* contains a
3x3 projective transformation matrix that describes
the translation that was necessary to transform all images
completely into the output image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Images`** (input_object)  (multichannel-)image-array `→` object (byte / uint2 / real)

Input images.

**`MosaicImage`** (output_object)  (multichannel-)image `→` object (byte / uint2 / real)

Output image.

**`HomMatrices2D`** (input_control)  hom_mat2d-array `→`  (real)

Array of 3x3 projective
transformation matrices.

**`StackingOrder`** (input_control)  string(-array) `→`  (string / integer)

Stacking order of the images in the mosaic.

Default:
'default'

Suggested values:
'default'

**`TransformDomain`** (input_control)  string `→`  (string)

Should the domains of the input images also be
transformed?

Default:
'false'

List of values:
'false', 'true'

**`TransMat2D`** (output_control)  hom_mat2d `→`  (real)

3x3 projective transformation matrix
that describes the translation that was necessary to
transform all images completely into the output image.

## Possible Predecessors

`bundle_adjust_mosaic`

## Alternatives

`gen_projective_mosaic`

## See also

`projective_trans_image`,
`projective_trans_image_size`,
`projective_trans_region`,
`projective_trans_contour_xld`,
`projective_trans_point_2d`,
`projective_trans_pixel`

## References

Richard Hartley, Andrew Zisserman: “Multiple View Geometry in
Computer Vision”; Cambridge University Press, Cambridge; 2000.
  
Olivier Faugeras, Quang-Tuan Luong: “The Geometry of Multiple
Images: The Laws That Govern the Formation of Multiple Images of a
Scene and Some of Their Applications”; MIT Press, Cambridge, MA;
2001.

## Module

Matching
