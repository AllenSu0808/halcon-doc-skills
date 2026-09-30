# real_to_vector_field (Operator)

## Name

`real_to_vector_field` — Convert two real-valued images into a vector field image.

## Signature

`def real_to_vector_field(row: HObject, col: HObject, type: str) -> HObject`

## Description

`real_to_vector_field` converts two real-valued images
*`row`* and *`col`* into a vector field image
*`vector_field`*. The input images contain the vector
components in the row and column direction, respectively. The semantic
type of *`vector_field`* is set with *`type`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`row`** (input_object)  singlechannelimage(-array) `→` HObject (real)

Vector component in the row direction.

**`col`** (input_object)  singlechannelimage(-array) `→` HObject (real)

Vector component in the column direction.

**`vector_field`** (output_object)  image(-array) `→` HObject (vector_field)

Displacement vector field.

**`type`** (input_control)  string `→` str

Semantic kind of the vector field.

Default:
"vector_field_relative"

List of values:
"vector_field_absolute", "vector_field_relative"

## Possible Predecessors

`vector_field_to_real`

## Module

Foundation
