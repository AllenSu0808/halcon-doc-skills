# add_dl_pruning_batch (Operator)

## Name

`add_dl_pruning_batch` — Calculate scores to prune a deep learning model.

## Signature

`add_dl_pruning_batch( : : DLModelHandleToPrune, DLPruningHandle, DLSampleBatch : )`

## Description

`add_dl_pruning_batch` calculates pruning scores for the deep
learning model *`DLModelHandleToPrune`*.
More precisely, the scores are calculated on the images given in
*`DLSampleBatch`* and internally accumulated by each call of
`add_dl_pruning_batch` in the pruning data handle
*`DLPruningHandle`*.

The parameter *`DLModelHandleToPrune`* specifies the deep learning
model to use.
Note that `add_dl_pruning_batch` supports only deep learning
models of type *'classification'*.

The parameter *`DLPruningHandle`* specifies the pruning data handle,
which is used to pass information as e.g., the accumulated scores or the
pruning mode.
See [`create_dl_pruning`](create_dl_pruning.md) for further information about implemented
pruning modes.

The parameter *`DLSampleBatch`* specifies the batch with input images
based on which the scores are calculated.
Note that the number of images in the tuple *`DLSampleBatch`* needs to
be equal to the value set for the model parameter *'batch_size'*.

For an explanation of the concept of deep learning see the introduction of
chapter [Deep Learning](toc_deeplearning.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLModelHandleToPrune`** (input_control)  dl_model `→`  (handle)

Handle of a deep learning model to prune.

**`DLPruningHandle`** (input_control)  dl_pruning `→`  (handle)

Pruning data handle.

**`DLSampleBatch`** (input_control)  dict-array `→`  (handle)

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
