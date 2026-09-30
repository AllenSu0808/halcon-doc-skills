# vector_field_to_real (Operator)

## Name

`vector_field_to_real` — Convert a vector field image into two real-valued images.

## Signature

`def vector_field_to_real(vector_field: HObject) -> Tuple[HObject, HObject]`

## Description

`vector_field_to_real` converts the vector field image
*`vector_field`* into two real-valued images *`row`* and
*`col`*. The output images contain the vector components in
the row and column direction, respectively.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`vector_field`** (input_object)  singlechannelimage(-array) `→` HObject (vector_field)

Vector field.

**`row`** (output_object)  image(-array) `→` HObject (real)

Vector component in the row direction.

**`col`** (output_object)  image(-array) `→` HObject (real)

Vector component in the column direction.

## Possible Predecessors

`optical_flow_mg`

## See also

`optical_flow_mg`

## Module

Foundation
