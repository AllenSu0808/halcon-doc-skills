# GetParamsClassMlp (Operator)

## Name

`GetParamsClassMlp` — Return the parameters of a multilayer perceptron.

## Signature

`static void HOperatorSet.GetParamsClassMlp(HTuple MLPHandle, out HTuple numInput, out HTuple numHidden, out HTuple numOutput, out HTuple outputFunction, out HTuple preprocessing, out HTuple numComponents)`

`int HClassMlp.GetParamsClassMlp(out int numHidden, out int numOutput, out string outputFunction, out string preprocessing, out int numComponents)`

## Description

`GetParamsClassMlp` returns the parameters of a multilayer
perceptron (MLP) that were specified when the MLP was created with
[`CreateClassMlp`](create_class_mlp.md). This is particularly useful if the MLP
was read from a file with [`ReadClassMlp`](read_class_mlp.md). The output of
`GetParamsClassMlp` can, for example, be used to check
whether the feature vectors and, if necessary, the target data to be
used with the MLP have the correct lengths. For a description of
the parameters, see [`CreateClassMlp`](create_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MLPHandle`** (input_control)  class_mlp `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

MLP handle.

**`numInput`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of input variables (features) of the MLP.

**`numHidden`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of hidden units of the MLP.

**`numOutput`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of output variables (classes) of the MLP.

**`outputFunction`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of the activation function in the output
layer of the MLP.

**`preprocessing`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of preprocessing used to transform the
feature vectors.

**`numComponents`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Preprocessing parameter: Number of transformed
features.

## Result

If the parameters are valid, the operator
`GetParamsClassMlp` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`CreateClassMlp`,
`ReadClassMlp`

## Possible Successors

`AddSampleClassMlp`,
`TrainClassMlp`

## See also

`EvaluateClassMlp`,
`ClassifyClassMlp`

## Module

Foundation
