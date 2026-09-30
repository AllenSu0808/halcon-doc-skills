# GetRejectionParamsClassMlp (Operator)

## Name

`GetRejectionParamsClassMlp` — Get the parameters of a rejection class.

## Signature

`static void HOperatorSet.GetRejectionParamsClassMlp(HTuple MLPHandle, HTuple genParamName, out HTuple genParamValue)`

`HTuple HClassMlp.GetRejectionParamsClassMlp(HTuple genParamName)`

`HTuple HClassMlp.GetRejectionParamsClassMlp(string genParamName)`

## Description

`GetRejectionParamsClassMlp` returns the rejection class
parameters of a multilayer perceptron (MLP) that were specified with
[`SetRejectionParamsClassMlp`](set_rejection_params_class_mlp.md). For a description of the
parameters, see [`SetRejectionParamsClassMlp`](set_rejection_params_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MLPHandle`** (input_control)  class_mlp `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

MLP handle.

**`genParamName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters to return.

Default:
"sampling_strategy"

List of values:
"hyperbox_tolerance", "random_seed", "rejection_class_index", "rejection_sample_factor", "sampling_strategy"

**`genParamValue`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long)

Values of the generic parameters.

## Result

If the parameters are valid, the operator
`GetRejectionParamsClassMlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`CreateClassMlp`

## Possible Successors

`TrainClassMlp`

## Module

Foundation
