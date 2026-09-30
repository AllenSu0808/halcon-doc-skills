# ReadClassMlp (Operator)

## Name

`ReadClassMlp` — Read a multilayer perceptron from a file.

## Signature

`static void HOperatorSet.ReadClassMlp(HTuple fileName, out HTuple MLPHandle)`

`public HClassMlp(string fileName)`

`void HClassMlp.ReadClassMlp(string fileName)`

## Description

`ReadClassMlp` reads a multilayer perceptron (MLP) that has
been stored with [`WriteClassMlp`](write_class_mlp.md). Since the training of an
MLP can consume a relatively long time, the MLP is typically trained
in an offline process and written to a file with
[`WriteClassMlp`](write_class_mlp.md). In the online process the MLP is read with
`ReadClassMlp` and subsequently used for evaluation with
[`EvaluateClassMlp`](evaluate_class_mlp.md) or for classification with
[`ClassifyClassMlp`](classify_class_mlp.md).
The default HALCON file extension for the MLP classifier is 'gmc'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`gmc`

**`MLPHandle`** (output_control)  class_mlp `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

MLP handle.

## Result

If the parameters are valid, the operator `ReadClassMlp`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Successors

`ClassifyClassMlp`,
`EvaluateClassMlp`,
`CreateClassLutMlp`

## Alternatives

`ReadDlModel`

## See also

`CreateClassMlp`,
`WriteClassMlp`

## Module

Foundation
