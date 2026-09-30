# create_deep_counting_model (Operator)

## Name

`create_deep_counting_model` — Create a Deep Counting model for counting objects.

## Signature

`create_deep_counting_model( : : GenParamName, GenParamValue : DeepCountingHandle)`

## Description

`create_deep_counting_model` creates a Deep Counting model and returns
its handle in *`DeepCountingHandle`*.

Internally `create_deep_counting_model` builds a backbone based on
the pretrained network *'pretrained_dl_classifier_resnet50.hdl'*,
which must be available.
See [`read_dl_model`](read_dl_model.md) for details on where the file is searched.

Additional parameters of the Deep Counting model can be set using the
generic parameters *`GenParamName`* and *`GenParamValue`*.
See [`get_deep_counting_model_param`](get_deep_counting_model_param.md) for a list of parameters and their
possible values. The parameters can either be set during model creation,
or later using [`set_deep_counting_model_param`](set_deep_counting_model_param.md).

Note that before using the returned Deep Counting model with
[`apply_deep_counting_model`](apply_deep_counting_model.md), templates must be stored in the model
using [`prepare_deep_counting_model`](prepare_deep_counting_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Parameter names.

Default:
[]

List of values:
'angle_end', 'angle_start', 'angle_step', 'device', 'max_overlap', 'min_score', 'scale_max', 'scale_min', 'scale_step'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (real / integer / string)

Parameter values.

Default:
[]

**`DeepCountingHandle`** (output_control)  deep_counting `→`  (handle)

Deep Counting model for counting objects.

## Result

If the parameters are valid, the operator `create_deep_counting_model`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Successors

`set_deep_counting_model_param`,
`get_deep_counting_model_param`,
`prepare_deep_counting_model`,
`apply_deep_counting_model`

## Alternatives

`read_deep_counting_model`

## See also

`get_deep_counting_model_param`

## Module

Matching
