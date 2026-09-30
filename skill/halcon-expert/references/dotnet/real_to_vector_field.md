# RealToVectorField (Operator)

## Name

`RealToVectorField` — Convert two real-valued images into a vector field image.

## Signature

`static void HOperatorSet.RealToVectorField(HObject row, HObject col, out HObject vectorField, HTuple type)`

`HImage HImage.RealToVectorField(HImage col, string type)`

## Description

`RealToVectorField` converts two real-valued images
*`row`* and *`col`* into a vector field image
*`vectorField`*. The input images contain the vector
components in the row and column direction, respectively. The semantic
type of *`vectorField`* is set with *`type`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`row`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (real)

Vector component in the row direction.

**`col`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (real)

Vector component in the column direction.

**`vectorField`** (output_object)  image(-array) `→` [HImage](HImage.md) (vector_field)

Displacement vector field.

**`type`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Semantic kind of the vector field.

Default:
"vector_field_relative"

List of values:
"vector_field_absolute", "vector_field_relative"

## Possible Predecessors

`VectorFieldToReal`

## Module

Foundation
