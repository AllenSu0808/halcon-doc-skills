# gen_dl_pruned_model (Operator)

## Name

`gen_dl_pruned_model` — Prune a deep learning model.

## Signature

`gen_dl_pruned_model( : : DLModelHandleToPrune, DLPruningHandle : DLModelHandlePruned)`

## Description

The operator `gen_dl_pruned_model` copies the input model
*`DLModelHandleToPrune`* and returns the pruned copy in
*`DLModelHandlePruned`*.
Note that `gen_dl_pruned_model` supports only deep learning
models of *'type'*=*'classification'*.

The parameter *`DLPruningHandle`* provides the necessary information
as e.g., the selected pruning mode, the percentage or the kernel scores.
See [`create_dl_pruning`](create_dl_pruning.md) for further information about
implemented pruning modes.

Behavior in special cases:

- In case the set amount of pruning *'percentage'* is too small to
  result in any removals, the returned model *`DLModelHandlePruned`*
  is simply a copy of the input model *`DLModelHandleToPrune`*.
- In case the model could not be pruned successfully, an empty handle is
  returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLModelHandleToPrune`** (input_control)  dl_model `→`  (handle)

Input model.

**`DLPruningHandle`** (input_control)  dl_pruning `→`  (handle)

Pruning data handle.

**`DLModelHandlePruned`** (output_control)  dl_model `→`  (handle)

Pruned model.

## Possible Predecessors

`add_dl_pruning_batch`,
`set_dl_pruning_param`

## Module

Deep Learning Professional
