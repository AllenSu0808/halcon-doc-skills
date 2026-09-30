# VectorFieldToReal (Operator)

## Name

`VectorFieldToReal` — Convert a vector field image into two real-valued images.

## Signature

`static void HOperatorSet.VectorFieldToReal(HObject vectorField, out HObject row, out HObject col)`

`HImage HImage.VectorFieldToReal(out HImage col)`

## Description

`VectorFieldToReal` converts the vector field image
*`vectorField`* into two real-valued images *`row`* and
*`col`*. The output images contain the vector components in
the row and column direction, respectively.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`vectorField`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (vector_field)

Vector field.

**`row`** (output_object)  image(-array) `→` [HImage](HImage.md) (real)

Vector component in the row direction.

**`col`** (output_object)  image(-array) `→` [HImage](HImage.md) (real)

Vector component in the column direction.

## Possible Predecessors

`OpticalFlowMg`

## See also

`OpticalFlowMg`

## Module

Foundation
