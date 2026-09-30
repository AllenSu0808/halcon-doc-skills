# clear_class_lut (Operator)

## Name

`clear_class_lut` — Clear a look-up table classifier.

## Signature

`clear_class_lut( : : ClassLUTHandle : )`

## Description

`clear_class_lut` clears the look-up table (LUT) given
by *`ClassLUTHandle`* and frees all memory required for the LUT.
After calling `clear_class_lut`, the LUT classifier can no longer be
used. The handle *`ClassLUTHandle`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ClassLUTHandle`** (input_control)  class_lut(-array) `→`  (handle)

Handle of the LUT classifier.

## Result

If *`ClassLUTHandle`* is valid, the operator `clear_class_lut`
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
