# set_metrology_object_fuzzy_param (Operator)

## Name

`set_metrology_object_fuzzy_param` — Set fuzzy parameters or fuzzy functions for a metrology model.

## Signature

`set_metrology_object_fuzzy_param( : : MetrologyHandle, Index, GenParamName, GenParamValue : )`

## Description

[`set_metrology_object_param`](set_metrology_object_param.md) is used to set or change the
fuzzy parameters or fuzzy functions of a metrology object in
order to adapt the model to a particular edge selection
before applying the operator [`apply_metrology_model`](apply_metrology_model.md).

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by the handle
*`MetrologyHandle`*. The parameter *`Index`* specifies
the metrology objects for which the parameters should be changed or set.
The parameters of all metrology objects are set if the parameter
*`Index`* is set to *'all'*.

The fuzzy parameter or the type of fuzzy function is passed
in the parameter *`GenParamName`*. The corresponding value or
the fuzzy function is passed in the parameter *`GenParamValue`*.
If at least one fuzzy function is set, internally the operator
[`fuzzy_measure_pos`](fuzzy_measure_pos.md) will be used when searching the objects
with the operator [`apply_metrology_model`](apply_metrology_model.md). More information
about fuzzy functions can be found with the operator
[`fuzzy_measure_pos`](fuzzy_measure_pos.md). The following generic
parameters and parameter values for *`GenParamName`* and
*`GenParamValue`* are possible:

- ***'fuzzy_thresh'*:** —

  The parameter specifies the
  minimum fuzzy value. The meaning and the use of this
  parameter is described with the operator [`fuzzy_measure_pos`](fuzzy_measure_pos.md).
  There, the parameter corresponds to the parameter
  `FuzzyThresh`.

  Default:
   *0.5*
- ***'function_contrast'*:** —

  The parameter specifies
  a fuzzy function of type `contrast`. The meaning and the
  use of this parameter is described with the operator
  [`set_fuzzy_measure`](set_fuzzy_measure.md). There, the parameter
  corresponds to the parameter `SetType` with the value
  *'contrast'* and its value corresponds to the parameter
  `Function`.

  Default:
   *'disabled'*
- ***'function_position'*:** —

  The parameter specifies
  a fuzzy function of type `position`. The meaning and the
  use of this parameter is described with the operator
  [`set_fuzzy_measure`](set_fuzzy_measure.md). There, the parameter corresponds to
  the parameter `SetType` with the value
  *'position'* and its value corresponds to the parameter
  `Function`.

  Default:
   *'disabled'*
- ***'function_position_center'*:** —

  The parameter
  specifies a fuzzy function of type `position_center`. The
  meaning and the use of this parameter is described with the
  operator [`set_fuzzy_measure`](set_fuzzy_measure.md). There, the parameter
  corresponds to the parameter `SetType` with the value
  *'position'* and its value corresponds to the parameter
  `Function`.

  Default:
   *'disabled'*
- ***'function_position_end'*:** —

  The parameter specifies
  a fuzzy function of type `position_end`. The meaning and
  the use of this parameter is described with the operator
  [`set_fuzzy_measure`](set_fuzzy_measure.md). There, the parameter corresponds to
  the parameter `SetType` with the value
  *'position_end'* and its value corresponds to the
  parameter `Function`.

  Default:
   *'disabled'*
- ***'function_position_first_edge'*:** —

  The parameter
  specifies a fuzzy function of type `position_first_edge`.
  The meaning and the use of this parameter is described with the
  operator [`set_fuzzy_measure`](set_fuzzy_measure.md). There, the parameter
  corresponds to the parameter `SetType` with the value
  *'position_first_edge'* and its value corresponds to the
  parameter `Function`.

  Default:
   *'disabled'*
- ***'function_position_last_edge'*:** —

  The parameter
  specifies a fuzzy function of type `position_last_edge`.
  The meaning and the use of this parameter is described with the
  operator [`set_fuzzy_measure`](set_fuzzy_measure.md). There, the parameter
  corresponds to the parameter `SetType` with the value
  *'position_last_edge'* and its value corresponds to the
  parameter `Function`.

  Default:
   *'disabled'*

A fuzzy function is discarded if the fuzzy function value
is set to *'disabled'*. All previously defined fuzzy
functions and fuzzy parameters can be discarded
completely using [`reset_metrology_object_fuzzy_param`](reset_metrology_object_fuzzy_param.md). The
current configuration of the metrology objects can
be accessed with [`get_metrology_object_fuzzy_param`](get_metrology_object_fuzzy_param.md). Note
that if at least one fuzzy function is specified, the operator
[`fuzzy_measure_pos`](fuzzy_measure_pos.md) is used for the edge detection.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MetrologyHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`MetrologyHandle`** (input_control, state is modified)  metrology_model `→`  (handle)

Handle of the metrology model.

**`Index`** (input_control)  integer(-array) `→`  (string / integer)

Index of the metrology objects.

Default:
'all'

Suggested values:
'all', 0, 1, 2

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Names of the generic parameters.

Default:
'fuzzy_thresh'

List of values:
'function_contrast', 'function_position', 'function_position_center', 'function_position_end', 'function_position_first_edge', 'function_position_last_edge', 'fuzzy_thresh'

**`GenParamValue`** (input_control)  attribute.value-array `→`  (real / integer)

Values of the generic parameters.

Default:
0.5

Suggested values:
0.1, 0.3, 0.5, 0.6, 0.7, 0.9, 1, 2, 3, 4, 5, 10, 20

## Result

If the parameters are valid, the operator
`set_metrology_object_fuzzy_param` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`get_metrology_object_fuzzy_param`

## Possible Successors

`apply_metrology_model`,
`reset_metrology_object_fuzzy_param`,
`get_metrology_object_fuzzy_param`

## See also

`set_metrology_object_param`

## Module

2D Metrology
