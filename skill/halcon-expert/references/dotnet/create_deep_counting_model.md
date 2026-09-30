# CreateDeepCountingModel (Operator)

## Name

`CreateDeepCountingModel` — Create a Deep Counting model for counting objects.

## Signature

`static void HOperatorSet.CreateDeepCountingModel(HTuple genParamName, HTuple genParamValue, out HTuple deepCountingHandle)`

`public HDlModelCounting(HTuple genParamName, HTuple genParamValue)`

`public HDlModelCounting(string genParamName, double genParamValue)`

`void HDlModelCounting.CreateDeepCountingModel(HTuple genParamName, HTuple genParamValue)`

`void HDlModelCounting.CreateDeepCountingModel(string genParamName, double genParamValue)`

## Description

`CreateDeepCountingModel` creates a Deep Counting model and returns
its handle in *`deepCountingHandle`*.

Internally `CreateDeepCountingModel` builds a backbone based on
the pretrained network *"pretrained_dl_classifier_resnet50.hdl"*,
which must be available.
See [`ReadDlModel`](read_dl_model.md) for details on where the file is searched.

Additional parameters of the Deep Counting model can be set using the
generic parameters *`genParamName`* and *`genParamValue`*.
See [`GetDeepCountingModelParam`](get_deep_counting_model_param.md) for a list of parameters and their
possible values. The parameters can either be set during model creation,
or later using [`SetDeepCountingModelParam`](set_deep_counting_model_param.md).

Note that before using the returned Deep Counting model with
[`ApplyDeepCountingModel`](apply_deep_counting_model.md), templates must be stored in the model
using [`PrepareDeepCountingModel`](prepare_deep_counting_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Parameter names.

Default:
[]

List of values:
"angle_end", "angle_start", "angle_step", "device", "max_overlap", "min_score", "scale_max", "scale_min", "scale_step"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Parameter values.

Default:
[]

**`deepCountingHandle`** (output_control)  deep_counting `→` [HDlModelCounting](HDlModelCounting.md), [HTuple](HTuple.md) (*IntPtr*)

Deep Counting model for counting objects.

## Result

If the parameters are valid, the operator `CreateDeepCountingModel`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Successors

`SetDeepCountingModelParam`,
`GetDeepCountingModelParam`,
`PrepareDeepCountingModel`,
`ApplyDeepCountingModel`

## Alternatives

`ReadDeepCountingModel`

## See also

`GetDeepCountingModelParam`

## Module

Matching
