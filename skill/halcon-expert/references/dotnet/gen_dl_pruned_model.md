# GenDlPrunedModel (Operator)

## Name

`GenDlPrunedModel` — Prune a deep learning model.

## Signature

`static void HOperatorSet.GenDlPrunedModel(HTuple DLModelHandleToPrune, HTuple DLPruningHandle, out HTuple DLModelHandlePruned)`

`HDlModel HDlModel.GenDlPrunedModel(HDlPrune DLPruningHandle)`

## Description

The operator `GenDlPrunedModel` copies the input model
*`DLModelHandleToPrune`* and returns the pruned copy in
*`DLModelHandlePruned`*.
Note that `GenDlPrunedModel` supports only deep learning
models of *"type"*=*"classification"*.

The parameter *`DLPruningHandle`* provides the necessary information
as e.g., the selected pruning mode, the percentage or the kernel scores.
See [`CreateDlPruning`](create_dl_pruning.md) for further information about
implemented pruning modes.

Behavior in special cases:

- In case the set amount of pruning *"percentage"* is too small to
  result in any removals, the returned model *`DLModelHandlePruned`*
  is simply a copy of the input model *`DLModelHandleToPrune`*.
- In case the model could not be pruned successfully, an empty handle is
  returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLModelHandleToPrune`** (input_control)  dl_model `→` [HDlModel](HDlModel.md), [HTuple](HTuple.md) (*IntPtr*)

Input model.

**`DLPruningHandle`** (input_control)  dl_pruning `→` [HDlPrune](HDlPrune.md), [HTuple](HTuple.md) (*IntPtr*)

Pruning data handle.

**`DLModelHandlePruned`** (output_control)  dl_model `→` [HDlModel](HDlModel.md), [HTuple](HTuple.md) (*IntPtr*)

Pruned model.

## Possible Predecessors

`AddDlPruningBatch`,
`SetDlPruningParam`

## Module

Deep Learning Professional
