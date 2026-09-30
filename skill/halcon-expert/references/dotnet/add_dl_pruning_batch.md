# AddDlPruningBatch (Operator)

## Name

`AddDlPruningBatch` — Calculate scores to prune a deep learning model.

## Signature

`static void HOperatorSet.AddDlPruningBatch(HTuple DLModelHandleToPrune, HTuple DLPruningHandle, HTuple DLSampleBatch)`

`void HDlModel.AddDlPruningBatch(HDlPrune DLPruningHandle, HDict[] DLSampleBatch)`

`void HDlPrune.AddDlPruningBatch(HDlModel DLModelHandleToPrune, HDict[] DLSampleBatch)`

## Description

`AddDlPruningBatch` calculates pruning scores for the deep
learning model *`DLModelHandleToPrune`*.
More precisely, the scores are calculated on the images given in
*`DLSampleBatch`* and internally accumulated by each call of
`AddDlPruningBatch` in the pruning data handle
*`DLPruningHandle`*.

The parameter *`DLModelHandleToPrune`* specifies the deep learning
model to use.
Note that `AddDlPruningBatch` supports only deep learning
models of type *"classification"*.

The parameter *`DLPruningHandle`* specifies the pruning data handle,
which is used to pass information as e.g., the accumulated scores or the
pruning mode.
See [`CreateDlPruning`](create_dl_pruning.md) for further information about implemented
pruning modes.

The parameter *`DLSampleBatch`* specifies the batch with input images
based on which the scores are calculated.
Note that the number of images in the tuple *`DLSampleBatch`* needs to
be equal to the value set for the model parameter *"batch_size"*.

For an explanation of the concept of deep learning see the introduction of
chapter [Deep Learning](toc_deeplearning.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLModelHandleToPrune`** (input_control)  dl_model `→` [HDlModel](HDlModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a deep learning model to prune.

**`DLPruningHandle`** (input_control)  dl_pruning `→` [HDlPrune](HDlPrune.md), [HTuple](HTuple.md) (*IntPtr*)

Pruning data handle.

**`DLSampleBatch`** (input_control)  dict-array `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Tuple of dictionaries with input images.

## Possible Predecessors

`ReadDlModel`,
`CreateDlPruning`,
`SetDlPruningParam`

## Possible Successors

`GetDlPruningParam`,
`GenDlPrunedModel`

## Module

Deep Learning Professional
