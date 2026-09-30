# real_to_vector_field (Operator)

## Name

`real_to_vector_field` — Convert two real-valued images into a vector field image.

## Signature

`real_to_vector_field(Row, Col : VectorField : Type : )`

## Description

`real_to_vector_field` converts two real-valued images
*`Row`* and *`Col`* into a vector field image
*`VectorField`*. The input images contain the vector
components in the row and column direction, respectively. The semantic
type of *`VectorField`* is set with *`Type`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Row`** (input_object)  singlechannelimage(-array) `→` object (real)

Vector component in the row direction.

**`Col`** (input_object)  singlechannelimage(-array) `→` object (real)

Vector component in the column direction.

**`VectorField`** (output_object)  image(-array) `→` object (vector_field)

Displacement vector field.

**`Type`** (input_control)  string `→`  (string)

Semantic kind of the vector field.

Default:
'vector_field_relative'

List of values:
'vector_field_absolute', 'vector_field_relative'

## Possible Predecessors

`vector_field_to_real`

## Module

Foundation
