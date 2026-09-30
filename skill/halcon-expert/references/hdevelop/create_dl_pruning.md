# create_dl_pruning (Operator)

## Name

`create_dl_pruning` — Create a pruning data handle.

## Signature

`create_dl_pruning( : : DLModelHandle, Mode, GenParam : DLPruningHandle)`

## Description

The operator `create_dl_pruning` creates a handle
*`DLPruningHandle`*.
This handle is used to pass information when pruning a deep learning model.

*`Mode`* specifies the pruning method.
The mode implies what will be removed and also which scores are needed.
Currently only the following *'mode'* is implemented:

- ***'oracle'*:** —

  Kernels of convolution layers are removed.
  In order to do so, a score is calculated for every (potentially removable)
  kernel, indicating its importance within the given network for the images
  used. See the given reference for details.

*`GenParam`* is a dictionary for setting generic parameters.
Currently no generic parameters are supported.

For an explanation of the concept of deep learning
see the introduction of chapter [Deep Learning](toc_deeplearning.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`DLModelHandle`** (input_control)  dl_model `→`  (handle)

Handle of a deep learning model.

**`Mode`** (input_control)  string `→`  (string)

Pruning method.

Default:
'oracle'

List of values:
'oracle'

**`GenParam`** (input_control)  dict `→`  (handle)

Dictionary with generic parameters.

Default:
[]

**`DLPruningHandle`** (output_control)  dl_pruning `→`  (handle)

Pruning data handle.

## Possible Predecessors

`read_dl_model`

## Possible Successors

`get_dl_pruning_param`,
`set_dl_model_param`

## References

Pavlo Molchanov, Stephen Tyree, Tero Karras, Timo Aila, Jan Kautz
"Pruning Convolutional Neural Networks for Resource Efficient Inference",
ICLR 2017, 5th International Conference on Learning Representations, Toulon,
France.

## Module

Deep Learning Professional
