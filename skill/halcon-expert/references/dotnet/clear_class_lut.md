# ClearClassLut (Operator)

## Name

`ClearClassLut` — Clear a look-up table classifier.

## Signature

`static void HOperatorSet.ClearClassLut(HTuple classLUTHandle)`

`static void HClassLUT.ClearClassLut(HClassLUT[] classLUTHandle)`

`void HClassLUT.ClearClassLut()`

## Description

`ClearClassLut` clears the look-up table (LUT) given
by *`classLUTHandle`* and frees all memory required for the LUT.
After calling `ClearClassLut`, the LUT classifier can no longer be
used. The handle *`classLUTHandle`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`classLUTHandle`** (input_control)  class_lut(-array) `→` [HClassLUT](HClassLUT.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the LUT classifier.

## Result

If *`classLUTHandle`* is valid, the operator `ClearClassLut`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is
raised.

## Possible Predecessors

`ClassifyImageClassLut`

## See also

`CreateClassLutMlp`,
`CreateClassLutSvm`,
`CreateClassLutGmm`

## Module

Foundation
