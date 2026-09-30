# unwarp_image_vector_field (Operator)

## Name

`unwarp_image_vector_field` — Unwarp an image using a vector field.

## Signature

`def unwarp_image_vector_field(image: HObject, vector_field: HObject) -> HObject`

## Description

`unwarp_image_vector_field` unwarps the image *`image`*
using the vector field *`vector_field`* and returns the unwarped
image in *`image_unwarped`*. The vector field must be of the
semantic type `vector_field_relative` and is typically
determined with [`optical_flow_mg`](optical_flow_mg.md). Hence,
`unwarp_image_vector_field` can be used to unwarp the second
input image of [`optical_flow_mg`](optical_flow_mg.md) to the first input image. It
should be noted that because of the above semantics the vector field
image represents an inverse transformation from the destination
image of the vector field to the source image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on domain level.
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` HObject (byte / uint2 / real)

Input image.

**`vector_field`** (input_object)  singlechannelimage(-array) `→` HObject (vector_field)

Input vector field.

**`image_unwarped`** (output_object)  singlechannelimage(-array) `→` HObject (byte / uint2 / real)

Unwarped image.

## Example (HDevelop)

```
optical_flow_mg (Image1, Image2, VectorField, 'fdrig', 0.8, 1, 20, \
                 5, 'default_parameters', 'accurate')
unwarp_image_vector_field (Image2, VectorField, ImageUnwarped)
```

## Result

If the parameter values are correct, the operator
`unwarp_image_vector_field` returns the value 2 (
H_MSG_TRUE)
. If the
input is empty (no input images are available) the behavior can be
set via `set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Possible Predecessors

`optical_flow_mg`

## Module

Foundation
