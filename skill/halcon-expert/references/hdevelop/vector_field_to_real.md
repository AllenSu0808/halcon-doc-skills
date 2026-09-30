# vector_field_to_real (Operator)

## Name

`vector_field_to_real` — Convert a vector field image into two real-valued images.

## Signature

`vector_field_to_real(VectorField : Row, Col : : )`

## Description

`vector_field_to_real` converts the vector field image
*`VectorField`* into two real-valued images *`Row`* and
*`Col`*. The output images contain the vector components in
the row and column direction, respectively.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`VectorField`** (input_object)  singlechannelimage(-array) `→` object (vector_field)

Vector field.

**`Row`** (output_object)  image(-array) `→` object (real)

Vector component in the row direction.

**`Col`** (output_object)  image(-array) `→` object (real)

Vector component in the column direction.

## Possible Predecessors

`optical_flow_mg`

## See also

`optical_flow_mg`

## Module

Foundation
