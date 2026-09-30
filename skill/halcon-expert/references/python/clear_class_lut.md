# clear_class_lut (Operator)

## Name

`clear_class_lut` — Clear a look-up table classifier.

## Signature

`def clear_class_lut(class_luthandle: MaybeSequence[HHandle]) -> None`

## Description

`clear_class_lut` clears the look-up table (LUT) given
by *`class_luthandle`* and frees all memory required for the LUT.
After calling `clear_class_lut`, the LUT classifier can no longer be
used. The handle *`class_luthandle`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`class_luthandle`** (input_control)  class_lut(-array) `→` MaybeSequence[HHandle]

Handle of the LUT classifier.

## Result

If *`class_luthandle`* is valid, the operator `clear_class_lut`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is
raised.

## Possible Predecessors

`classify_image_class_lut`

## See also

`create_class_lut_mlp`,
`create_class_lut_svm`,
`create_class_lut_gmm`

## Module

Foundation
