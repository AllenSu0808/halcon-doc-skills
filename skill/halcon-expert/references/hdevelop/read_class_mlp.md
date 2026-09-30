# read_class_mlp (Operator)

## Name

`read_class_mlp` — Read a multilayer perceptron from a file.

## Signature

`read_class_mlp( : : FileName : MLPHandle)`

## Description

`read_class_mlp` reads a multilayer perceptron (MLP) that has
been stored with [`write_class_mlp`](write_class_mlp.md). Since the training of an
MLP can consume a relatively long time, the MLP is typically trained
in an offline process and written to a file with
[`write_class_mlp`](write_class_mlp.md). In the online process the MLP is read with
`read_class_mlp` and subsequently used for evaluation with
[`evaluate_class_mlp`](evaluate_class_mlp.md) or for classification with
[`classify_class_mlp`](classify_class_mlp.md).
The default HALCON file extension for the MLP classifier is 'gmc'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`FileName`** (input_control)  filename.read `→`  (string)

File name.

File extension:
.`gmc`

**`MLPHandle`** (output_control)  class_mlp `→`  (handle)

MLP handle.

## Result

If the parameters are valid, the operator `read_class_mlp`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Successors

`classify_class_mlp`,
`evaluate_class_mlp`,
`create_class_lut_mlp`

## Alternatives

`read_dl_model`

## See also

`create_class_mlp`,
`write_class_mlp`

## Module

Foundation
