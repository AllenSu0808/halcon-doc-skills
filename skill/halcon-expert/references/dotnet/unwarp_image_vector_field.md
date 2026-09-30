# UnwarpImageVectorField (Operator)

## Name

`UnwarpImageVectorField` — Unwarp an image using a vector field.

## Signature

`static void HOperatorSet.UnwarpImageVectorField(HObject image, HObject vectorField, out HObject imageUnwarped)`

`HImage HImage.UnwarpImageVectorField(HImage vectorField)`

## Description

`UnwarpImageVectorField` unwarps the image *`image`*
using the vector field *`vectorField`* and returns the unwarped
image in *`imageUnwarped`*. The vector field must be of the
semantic type `vector_field_relative` and is typically
determined with [`OpticalFlowMg`](optical_flow_mg.md). Hence,
`UnwarpImageVectorField` can be used to unwarp the second
input image of [`OpticalFlowMg`](optical_flow_mg.md) to the first input image. It
should be noted that because of the above semantics the vector field
image represents an inverse transformation from the destination
image of the vector field to the source image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on domain level.
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Input image.

**`vectorField`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (vector_field)

Input vector field.

**`imageUnwarped`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Unwarped image.

## Example (HDevelop)

```
optical_flow_mg (Image1, Image2, VectorField, 'fdrig', 0.8, 1, 20, \
                 5, 'default_parameters', 'accurate')
unwarp_image_vector_field (Image2, VectorField, ImageUnwarped)
```

## Result

If the parameter values are correct, the operator
`UnwarpImageVectorField` returns the value 2 (
H_MSG_TRUE)
. If the
input is empty (no input images are available) the behavior can be
set via `set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Possible Predecessors

`OpticalFlowMg`

## Module

Foundation
