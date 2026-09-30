# GenBundleAdjustedMosaic (Operator)

## Name

`GenBundleAdjustedMosaic` — Combine multiple images into a mosaic image.

## Signature

`static void HOperatorSet.GenBundleAdjustedMosaic(HObject images, out HObject mosaicImage, HTuple homMatrices2D, HTuple stackingOrder, HTuple transformDomain, out HTuple transMat2D)`

`HImage HImage.GenBundleAdjustedMosaic(HHomMat2D[] homMatrices2D, HTuple stackingOrder, string transformDomain, out HHomMat2D transMat2D)`

`HImage HImage.GenBundleAdjustedMosaic(HHomMat2D[] homMatrices2D, string stackingOrder, string transformDomain, out HHomMat2D transMat2D)`

## Description

`GenBundleAdjustedMosaic` combines the input images
contained in the object *`images`* into a mosaic image
*`mosaicImage`*. The relative positions of the images are
defined by 3x3 projective transformation matrices.
The array *`homMatrices2D`* contains a sequence of these
linearized matrices. The transformation matrices can be computed
with [`BundleAdjustMosaic`](bundle_adjust_mosaic.md).

The origin of *`mosaicImage`* and its size are automatically
chosen so that all of the input images are completely visible.

The order in which the images are added to the mosaic is given by
the array *`stackingOrder`*. The first index in this array
will end up at the bottom of the image stack while the last one will
be on top. If *"default"* is given instead of an array of
integers, the canonical order (images in the order used in
*`images`*) will be used.

The parameter *`transformDomain`* can be used to determine
whether the domains of *`images`* are also transformed. Since
the transformation of the domains costs runtime, this parameter
should be used to specify whether this is desired or not. If
*`transformDomain`* is set to *"false"* the domain of
the input images is ignored and the complete images are
transformed.

On output, the parameter *`transMat2D`* contains a
3x3 projective transformation matrix that describes
the translation that was necessary to transform all images
completely into the output image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`images`** (input_object)  (multichannel-)image-array `→` [HImage](HImage.md) (byte / uint2 / real)

Input images.

**`mosaicImage`** (output_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / uint2 / real)

Output image.

**`homMatrices2D`** (input_control)  hom_mat2d-array `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Array of 3x3 projective
transformation matrices.

**`stackingOrder`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Stacking order of the images in the mosaic.

Default:
"default"

Suggested values:
"default"

**`transformDomain`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Should the domains of the input images also be
transformed?

Default:
"false"

List of values:
"false", "true"

**`transMat2D`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

3x3 projective transformation matrix
that describes the translation that was necessary to
transform all images completely into the output image.

## Possible Predecessors

`BundleAdjustMosaic`

## Alternatives

`GenProjectiveMosaic`

## See also

`ProjectiveTransImage`,
`ProjectiveTransImageSize`,
`ProjectiveTransRegion`,
`ProjectiveTransContourXld`,
`ProjectiveTransPoint2d`,
`ProjectiveTransPixel`

## References

Richard Hartley, Andrew Zisserman: “Multiple View Geometry in
Computer Vision”; Cambridge University Press, Cambridge; 2000.
  
Olivier Faugeras, Quang-Tuan Luong: “The Geometry of Multiple
Images: The Laws That Govern the Formation of Multiple Images of a
Scene and Some of Their Applications”; MIT Press, Cambridge, MA;
2001.

## Module

Matching
