# get_metrology_object_fuzzy_param (Operator)

## Name

`get_metrology_object_fuzzy_param` — Get a fuzzy parameter of a metrology model.

## Signature

`def get_metrology_object_fuzzy_param(metrology_handle: HHandle, index: MaybeSequence[Union[str, int]], gen_param_name: Sequence[str]) -> Sequence[Union[float, int]]`

## Description

[`get_metrology_object_param`](get_metrology_object_param.md) allows to access the fuzzy
parameters of metrology objects.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by the handle
*`metrology_handle`*. The parameter *`index`* specifies
for which metrology objects the information is accessed. With
*`index`* set to *"all"*, the parameters of all metrology
objects are accessed. The names of the desired parameters are passed
in the generic parameter *`gen_param_name`*, the corresponding values
are returned in *`gen_param_value`* in the same order. All these
fuzzy parameters can be set and changed at any time with the operator
[`set_metrology_object_fuzzy_param`](set_metrology_object_fuzzy_param.md).

The following parameters can be accessed:

- ***"fuzzy_thresh"*:** —

  The meaning and the use of this
  parameter is equivalent to the parameter `fuzzy_thresh` of
  the operator [`fuzzy_measure_pos`](fuzzy_measure_pos.md) and is described there.
- ***"function_contrast"*:** —

  With this parameter the
  fuzzy function of type contrast that is set in the operator
  [`set_metrology_object_param`](set_metrology_object_param.md) can be queried. The meaning
  and the use of this parameter is equivalent to the parameter
  `set_type` with the value *"contrast"* of the
  operator [`set_fuzzy_measure`](set_fuzzy_measure.md) and is described there. The
  return value *`gen_param_value`* contains the function of the
  metrology object.
- ***"function_position"*:** —

  With this parameter the
  fuzzy function of type position that is set in the operator
  [`set_metrology_object_param`](set_metrology_object_param.md) can be queried.
  Because only one fuzzy function of a type can be set, only the
  last set function can be returned. The type can be
  *"function_position"*, *"function_position_center"*,
  *"function_position_end"*,
  *"function_position_first_edge"*, or
  *"function_position_last_edge"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`metrology_handle`** (input_control)  metrology_model `→` HHandle

Handle of the metrology model.

**`index`** (input_control)  integer(-array) `→` MaybeSequence[Union[str, int]]

Index of the metrology objects.

Default:
"all"

Suggested values:
"all", 0, 1, 2

**`gen_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

Names of the generic parameters.

Default:
"fuzzy_thresh"

List of values:
"function_contrast", "function_position", "fuzzy_thresh"

**`gen_param_value`** (output_control)  attribute.value-array `→` Sequence[Union[float, int]]

Values of the generic parameters.

## Result

If the parameters are valid, the operator
`get_metrology_object_fuzzy_param` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`get_metrology_object_indices`,
`set_metrology_object_fuzzy_param`

## Possible Successors

`set_metrology_object_fuzzy_param`

## See also

`get_metrology_object_param`

## Module

2D Metrology
