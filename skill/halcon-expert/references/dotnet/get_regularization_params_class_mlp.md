# GetRegularizationParamsClassMlp (Operator)

## Name

`GetRegularizationParamsClassMlp` — Return the regularization parameters of a multilayer perceptron.

## Signature

`static void HOperatorSet.GetRegularizationParamsClassMlp(HTuple MLPHandle, HTuple genParamName, out HTuple genParamValue)`

`HTuple HClassMlp.GetRegularizationParamsClassMlp(string genParamName)`

## Description

`GetRegularizationParamsClassMlp` returns the
regularization parameters of a multilayer perceptron (MLP) that were
specified with [`SetRegularizationParamsClassMlp`](set_regularization_params_class_mlp.md).
Furthermore, `GetRegularizationParamsClassMlp` returns the
parameters that were determined by an automatic determination of the
regularization parameters. For a description of the parameters, see
[`SetRegularizationParamsClassMlp`](set_regularization_params_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MLPHandle`** (input_control)  class_mlp `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

MLP handle.

**`genParamName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the regularization parameter to return.

Default:
"weight_prior"

List of values:
"fraction_well_determined_params", "noise_prior", "num_inner_iterations", "num_outer_iterations", "num_well_determined_params", "weight_prior"

**`genParamValue`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Value of the regularization parameter.

## Result

If the parameters are valid, the operator
`GetRegularizationParamsClassMlp` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`SetRegularizationParamsClassMlp`,
`ReadClassMlp`

## Possible Successors

`TrainClassMlp`

## Module

Foundation
