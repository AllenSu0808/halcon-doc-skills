# GetMetrologyObjectFuzzyParam (Operator)

## Name

`GetMetrologyObjectFuzzyParam` — Get a fuzzy parameter of a metrology model.

## Signature

`static void HOperatorSet.GetMetrologyObjectFuzzyParam(HTuple metrologyHandle, HTuple index, HTuple genParamName, out HTuple genParamValue)`

`HTuple HMetrologyModel.GetMetrologyObjectFuzzyParam(HTuple index, HTuple genParamName)`

`HTuple HMetrologyModel.GetMetrologyObjectFuzzyParam(string index, HTuple genParamName)`

## Description

[`GetMetrologyObjectParam`](get_metrology_object_param.md) allows to access the fuzzy
parameters of metrology objects.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by the handle
*`metrologyHandle`*. The parameter *`index`* specifies
for which metrology objects the information is accessed. With
*`index`* set to *"all"*, the parameters of all metrology
objects are accessed. The names of the desired parameters are passed
in the generic parameter *`genParamName`*, the corresponding values
are returned in *`genParamValue`* in the same order. All these
fuzzy parameters can be set and changed at any time with the operator
[`SetMetrologyObjectFuzzyParam`](set_metrology_object_fuzzy_param.md).

The following parameters can be accessed:

- ***"fuzzy_thresh"*:** —

  The meaning and the use of this
  parameter is equivalent to the parameter `fuzzyThresh` of
  the operator [`FuzzyMeasurePos`](fuzzy_measure_pos.md) and is described there.
- ***"function_contrast"*:** —

  With this parameter the
  fuzzy function of type contrast that is set in the operator
  [`SetMetrologyObjectParam`](set_metrology_object_param.md) can be queried. The meaning
  and the use of this parameter is equivalent to the parameter
  `setType` with the value *"contrast"* of the
  operator [`SetFuzzyMeasure`](set_fuzzy_measure.md) and is described there. The
  return value *`genParamValue`* contains the function of the
  metrology object.
- ***"function_position"*:** —

  With this parameter the
  fuzzy function of type position that is set in the operator
  [`SetMetrologyObjectParam`](set_metrology_object_param.md) can be queried.
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

**`metrologyHandle`** (input_control)  metrology_model `→` [HMetrologyModel](HMetrologyModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the metrology model.

**`index`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Index of the metrology objects.

Default:
"all"

Suggested values:
"all", 0, 1, 2

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters.

Default:
"fuzzy_thresh"

List of values:
"function_contrast", "function_position", "fuzzy_thresh"

**`genParamValue`** (output_control)  attribute.value-array `→` [HTuple](HTuple.md) (*double* / int / long)

Values of the generic parameters.

## Result

If the parameters are valid, the operator
`GetMetrologyObjectFuzzyParam` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`GetMetrologyObjectIndices`,
`SetMetrologyObjectFuzzyParam`

## Possible Successors

`SetMetrologyObjectFuzzyParam`

## See also

`GetMetrologyObjectParam`

## Module

2D Metrology
