# CreateDlPruning (Operator)

## Name

`CreateDlPruning` — Create a pruning data handle.

## Signature

`static void HOperatorSet.CreateDlPruning(HTuple DLModelHandle, HTuple mode, HTuple genParam, out HTuple DLPruningHandle)`

`HDlPrune HDlModel.CreateDlPruning(string mode, HDict genParam)`

`public HDlPrune(HDlModel DLModelHandle, string mode, HDict genParam)`

`void HDlPrune.CreateDlPruning(HDlModel DLModelHandle, string mode, HDict genParam)`

## Description

The operator `CreateDlPruning` creates a handle
*`DLPruningHandle`*.
This handle is used to pass information when pruning a deep learning model.

*`mode`* specifies the pruning method.
The mode implies what will be removed and also which scores are needed.
Currently only the following *"mode"* is implemented:

- ***"oracle"*:** —

  Kernels of convolution layers are removed.
  In order to do so, a score is calculated for every (potentially removable)
  kernel, indicating its importance within the given network for the images
  used. See the given reference for details.

*`genParam`* is a dictionary for setting generic parameters.
Currently no generic parameters are supported.

For an explanation of the concept of deep learning
see the introduction of chapter [Deep Learning](toc_deeplearning.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`DLModelHandle`** (input_control)  dl_model `→` [HDlModel](HDlModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a deep learning model.

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Pruning method.

Default:
"oracle"

List of values:
"oracle"

**`genParam`** (input_control)  dict `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Dictionary with generic parameters.

Default:
[]

**`DLPruningHandle`** (output_control)  dl_pruning `→` [HDlPrune](HDlPrune.md), [HTuple](HTuple.md) (*IntPtr*)

Pruning data handle.

## Possible Predecessors

`ReadDlModel`

## Possible Successors

`GetDlPruningParam`,
`SetDlModelParam`

## References

Pavlo Molchanov, Stephen Tyree, Tero Karras, Timo Aila, Jan Kautz
"Pruning Convolutional Neural Networks for Resource Efficient Inference",
ICLR 2017, 5th International Conference on Learning Representations, Toulon,
France.

## Module

Deep Learning Professional
