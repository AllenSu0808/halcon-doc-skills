# add_dl_pruning_batch (Operator)

## Name

`add_dl_pruning_batch` — Calculate scores to prune a deep learning model.

## Signature

`def add_dl_pruning_batch(dlmodel_handle_to_prune: HHandle, dlpruning_handle: HHandle, dlsample_batch: Sequence[HHandle]) -> None`

## Description

`add_dl_pruning_batch` calculates pruning scores for the deep
learning model *`dlmodel_handle_to_prune`*.
More precisely, the scores are calculated on the images given in
*`dlsample_batch`* and internally accumulated by each call of
`add_dl_pruning_batch` in the pruning data handle
*`dlpruning_handle`*.

The parameter *`dlmodel_handle_to_prune`* specifies the deep learning
model to use.
Note that `add_dl_pruning_batch` supports only deep learning
models of type *"classification"*.

The parameter *`dlpruning_handle`* specifies the pruning data handle,
which is used to pass information as e.g., the accumulated scores or the
pruning mode.
See [`create_dl_pruning`](create_dl_pruning.md) for further information about implemented
pruning modes.

The parameter *`dlsample_batch`* specifies the batch with input images
based on which the scores are calculated.
Note that the number of images in the tuple *`dlsample_batch`* needs to
be equal to the value set for the model parameter *"batch_size"*.

For an explanation of the concept of deep learning see the introduction of
chapter [Deep Learning](toc_deeplearning.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dlmodel_handle_to_prune`** (input_control)  dl_model `→` HHandle

Handle of a deep learning model to prune.

**`dlpruning_handle`** (input_control)  dl_pruning `→` HHandle

Pruning data handle.

**`dlsample_batch`** (input_control)  dict-array `→` Sequence[HHandle]

Tuple of dictionaries with input images.

## Possible Predecessors

`read_dl_model`,
`create_dl_pruning`,
`set_dl_pruning_param`

## Possible Successors

`get_dl_pruning_param`,
`gen_dl_pruned_model`

## Module

Deep Learning Professional
