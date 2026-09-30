# GetNccModelParams (Operator)

## Name

`GetNccModelParams` — Return the parameters of an NCC model.

## Signature

`static void HOperatorSet.GetNccModelParams(HTuple modelID, out HTuple numLevels, out HTuple angleStart, out HTuple angleExtent, out HTuple angleStep, out HTuple metric)`

`int HNCCModel.GetNccModelParams(out double angleStart, out double angleExtent, out double angleStep, out string metric)`

## Description

The operator `GetNccModelParams` returns the parameters of
the NCC model *`modelID`* that were used to create it using
[`CreateNccModel`](create_ncc_model.md). In particular, this output can be used to
check the parameters *`numLevels`* and *`angleStep`* if
they were determined automatically during the model creation with
[`CreateNccModel`](create_ncc_model.md). Furthermore, this output can be used to
check the parameters if the model was read with
[`ReadNccModel`](read_ncc_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelID`** (input_control)  ncc_model `→` [HNCCModel](HNCCModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

**`numLevels`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of pyramid levels.

**`angleStart`** (output_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Smallest rotation of the pattern.

**`angleExtent`** (output_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Extent of the rotation angles.

Assertion:
`AngleExtent >= 0`

**`angleStep`** (output_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Step length of the angles (resolution).

Assertion:
`AngleStep >= 0`

**`metric`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Match metric.

## Result

If the handle of the model is valid, the operator
`GetNccModelParams` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`CreateNccModel`,
`ReadNccModel`

## See also

`FindNccModel`

## Module

Matching
