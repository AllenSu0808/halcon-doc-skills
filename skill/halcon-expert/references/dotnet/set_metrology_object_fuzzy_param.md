# SetMetrologyObjectFuzzyParam (Operator)

## Name

`SetMetrologyObjectFuzzyParam` — Set fuzzy parameters or fuzzy functions for a metrology model.

## Signature

`static void HOperatorSet.SetMetrologyObjectFuzzyParam(HTuple metrologyHandle, HTuple index, HTuple genParamName, HTuple genParamValue)`

`void HMetrologyModel.SetMetrologyObjectFuzzyParam(HTuple index, HTuple genParamName, HTuple genParamValue)`

`void HMetrologyModel.SetMetrologyObjectFuzzyParam(string index, HTuple genParamName, HTuple genParamValue)`

## Description

[`SetMetrologyObjectParam`](set_metrology_object_param.md) is used to set or change the
fuzzy parameters or fuzzy functions of a metrology object in
order to adapt the model to a particular edge selection
before applying the operator [`ApplyMetrologyModel`](apply_metrology_model.md).

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by the handle
*`metrologyHandle`*. The parameter *`index`* specifies
the metrology objects for which the parameters should be changed or set.
The parameters of all metrology objects are set if the parameter
*`index`* is set to *"all"*.

The fuzzy parameter or the type of fuzzy function is passed
in the parameter *`genParamName`*. The corresponding value or
the fuzzy function is passed in the parameter *`genParamValue`*.
If at least one fuzzy function is set, internally the operator
[`FuzzyMeasurePos`](fuzzy_measure_pos.md) will be used when searching the objects
with the operator [`ApplyMetrologyModel`](apply_metrology_model.md). More information
about fuzzy functions can be found with the operator
[`FuzzyMeasurePos`](fuzzy_measure_pos.md). The following generic
parameters and parameter values for *`genParamName`* and
*`genParamValue`* are possible:

- ***"fuzzy_thresh"*:** —

  The parameter specifies the
  minimum fuzzy value. The meaning and the use of this
  parameter is described with the operator [`FuzzyMeasurePos`](fuzzy_measure_pos.md).
  There, the parameter corresponds to the parameter
  `fuzzyThresh`.

  Default:
   *0.5*
- ***"function_contrast"*:** —

  The parameter specifies
  a fuzzy function of type `contrast`. The meaning and the
  use of this parameter is described with the operator
  [`SetFuzzyMeasure`](set_fuzzy_measure.md). There, the parameter
  corresponds to the parameter `setType` with the value
  *"contrast"* and its value corresponds to the parameter
  `function`.

  Default:
   *"disabled"*
- ***"function_position"*:** —

  The parameter specifies
  a fuzzy function of type `position`. The meaning and the
  use of this parameter is described with the operator
  [`SetFuzzyMeasure`](set_fuzzy_measure.md). There, the parameter corresponds to
  the parameter `setType` with the value
  *"position"* and its value corresponds to the parameter
  `function`.

  Default:
   *"disabled"*
- ***"function_position_center"*:** —

  The parameter
  specifies a fuzzy function of type `position_center`. The
  meaning and the use of this parameter is described with the
  operator [`SetFuzzyMeasure`](set_fuzzy_measure.md). There, the parameter
  corresponds to the parameter `setType` with the value
  *"position"* and its value corresponds to the parameter
  `function`.

  Default:
   *"disabled"*
- ***"function_position_end"*:** —

  The parameter specifies
  a fuzzy function of type `position_end`. The meaning and
  the use of this parameter is described with the operator
  [`SetFuzzyMeasure`](set_fuzzy_measure.md). There, the parameter corresponds to
  the parameter `setType` with the value
  *"position_end"* and its value corresponds to the
  parameter `function`.

  Default:
   *"disabled"*
- ***"function_position_first_edge"*:** —

  The parameter
  specifies a fuzzy function of type `position_first_edge`.
  The meaning and the use of this parameter is described with the
  operator [`SetFuzzyMeasure`](set_fuzzy_measure.md). There, the parameter
  corresponds to the parameter `setType` with the value
  *"position_first_edge"* and its value corresponds to the
  parameter `function`.

  Default:
   *"disabled"*
- ***"function_position_last_edge"*:** —

  The parameter
  specifies a fuzzy function of type `position_last_edge`.
  The meaning and the use of this parameter is described with the
  operator [`SetFuzzyMeasure`](set_fuzzy_measure.md). There, the parameter
  corresponds to the parameter `setType` with the value
  *"position_last_edge"* and its value corresponds to the
  parameter `function`.

  Default:
   *"disabled"*

A fuzzy function is discarded if the fuzzy function value
is set to *"disabled"*. All previously defined fuzzy
functions and fuzzy parameters can be discarded
completely using [`ResetMetrologyObjectFuzzyParam`](reset_metrology_object_fuzzy_param.md). The
current configuration of the metrology objects can
be accessed with [`GetMetrologyObjectFuzzyParam`](get_metrology_object_fuzzy_param.md). Note
that if at least one fuzzy function is specified, the operator
[`FuzzyMeasurePos`](fuzzy_measure_pos.md) is used for the edge detection.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- metrologyHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`metrologyHandle`** (input_control, state is modified)  metrology_model `→` [HMetrologyModel](HMetrologyModel.md), [HTuple](HTuple.md) (*IntPtr*)

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
"function_contrast", "function_position", "function_position_center", "function_position_end", "function_position_first_edge", "function_position_last_edge", "fuzzy_thresh"

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*double* / int / long)

Values of the generic parameters.

Default:
0.5

Suggested values:
0.1, 0.3, 0.5, 0.6, 0.7, 0.9, 1, 2, 3, 4, 5, 10, 20

## Result

If the parameters are valid, the operator
`SetMetrologyObjectFuzzyParam` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`GetMetrologyObjectFuzzyParam`

## Possible Successors

`ApplyMetrologyModel`,
`ResetMetrologyObjectFuzzyParam`,
`GetMetrologyObjectFuzzyParam`

## See also

`SetMetrologyObjectParam`

## Module

2D Metrology
