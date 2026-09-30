# get_ncc_model_params (Operator)

## Name

`get_ncc_model_params` — Return the parameters of an NCC model.

## Signature

`get_ncc_model_params( : : ModelID : NumLevels, AngleStart, AngleExtent, AngleStep, Metric)`

## Description

The operator `get_ncc_model_params` returns the parameters of
the NCC model *`ModelID`* that were used to create it using
[`create_ncc_model`](create_ncc_model.md). In particular, this output can be used to
check the parameters *`NumLevels`* and *`AngleStep`* if
they were determined automatically during the model creation with
[`create_ncc_model`](create_ncc_model.md). Furthermore, this output can be used to
check the parameters if the model was read with
[`read_ncc_model`](read_ncc_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ModelID`** (input_control)  ncc_model `→`  (handle)

Handle of the model.

**`NumLevels`** (output_control)  integer `→`  (integer)

Number of pyramid levels.

**`AngleStart`** (output_control)  angle.rad `→`  (real)

Smallest rotation of the pattern.

**`AngleExtent`** (output_control)  angle.rad `→`  (real)

Extent of the rotation angles.

Assertion:
`AngleExtent >= 0`

**`AngleStep`** (output_control)  angle.rad `→`  (real)

Step length of the angles (resolution).

Assertion:
`AngleStep >= 0`

**`Metric`** (output_control)  string `→`  (string)

Match metric.

## Result

If the handle of the model is valid, the operator
`get_ncc_model_params` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`create_ncc_model`,
`read_ncc_model`

## See also

`find_ncc_model`

## Module

Matching
