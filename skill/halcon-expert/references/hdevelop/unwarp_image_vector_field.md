# unwarp_image_vector_field (Operator)

## Name

`unwarp_image_vector_field` — Unwarp an image using a vector field.

## Signature

`unwarp_image_vector_field(Image, VectorField : ImageUnwarped : : )`

## Description

`unwarp_image_vector_field` unwarps the image *`Image`*
using the vector field *`VectorField`* and returns the unwarped
image in *`ImageUnwarped`*. The vector field must be of the
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

**`Image`** (input_object)  singlechannelimage(-array) `→` object (byte / uint2 / real)

Input image.

**`VectorField`** (input_object)  singlechannelimage(-array) `→` object (vector_field)

Input vector field.

**`ImageUnwarped`** (output_object)  singlechannelimage(-array) `→` object (byte / uint2 / real)

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
