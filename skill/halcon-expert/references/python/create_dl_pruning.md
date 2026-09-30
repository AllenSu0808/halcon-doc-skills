# create_dl_pruning (Operator)

## Name

`create_dl_pruning` — Create a pruning data handle.

## Signature

`def create_dl_pruning(dlmodel_handle: HHandle, mode: str, gen_param: HHandle) -> HHandle`

## Description

The operator `create_dl_pruning` creates a handle
*`dlpruning_handle`*.
This handle is used to pass information when pruning a deep learning model.

*`mode`* specifies the pruning method.
The mode implies what will be removed and also which scores are needed.
Currently only the following *"mode"* is implemented:

- ***"oracle"*:** —

  Kernels of convolution layers are removed.
  In order to do so, a score is calculated for every (potentially removable)
  kernel, indicating its importance within the given network for the images
  used. See the given reference for details.

*`gen_param`* is a dictionary for setting generic parameters.
Currently no generic parameters are supported.

For an explanation of the concept of deep learning
see the introduction of chapter [Deep Learning](toc_deeplearning.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`dlmodel_handle`** (input_control)  dl_model `→` HHandle

Handle of a deep learning model.

**`mode`** (input_control)  string `→` str

Pruning method.

Default:
"oracle"

List of values:
"oracle"

**`gen_param`** (input_control)  dict `→` HHandle

Dictionary with generic parameters.

Default:
[]

**`dlpruning_handle`** (output_control)  dl_pruning `→` HHandle

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
