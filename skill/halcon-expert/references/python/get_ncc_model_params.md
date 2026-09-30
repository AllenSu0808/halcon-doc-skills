# get_ncc_model_params (Operator)

## Name

`get_ncc_model_params` — Return the parameters of an NCC model.

## Signature

`def get_ncc_model_params(model_id: HHandle) -> Tuple[int, float, float, float, str]`

## Description

The operator `get_ncc_model_params` returns the parameters of
the NCC model *`model_id`* that were used to create it using
[`create_ncc_model`](create_ncc_model.md). In particular, this output can be used to
check the parameters *`num_levels`* and *`angle_step`* if
they were determined automatically during the model creation with
[`create_ncc_model`](create_ncc_model.md). Furthermore, this output can be used to
check the parameters if the model was read with
[`read_ncc_model`](read_ncc_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`model_id`** (input_control)  ncc_model `→` HHandle

Handle of the model.

**`num_levels`** (output_control)  integer `→` int

Number of pyramid levels.

**`angle_start`** (output_control)  angle.rad `→` float

Smallest rotation of the pattern.

**`angle_extent`** (output_control)  angle.rad `→` float

Extent of the rotation angles.

Assertion:
`AngleExtent >= 0`

**`angle_step`** (output_control)  angle.rad `→` float

Step length of the angles (resolution).

Assertion:
`AngleStep >= 0`

**`metric`** (output_control)  string `→` str

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
