# gen_dl_pruned_model (Operator)

## Name

`gen_dl_pruned_model` — Prune a deep learning model.

## Signature

`def gen_dl_pruned_model(dlmodel_handle_to_prune: HHandle, dlpruning_handle: HHandle) -> HHandle`

## Description

The operator `gen_dl_pruned_model` copies the input model
*`dlmodel_handle_to_prune`* and returns the pruned copy in
*`dlmodel_handle_pruned`*.
Note that `gen_dl_pruned_model` supports only deep learning
models of *"type"*=*"classification"*.

The parameter *`dlpruning_handle`* provides the necessary information
as e.g., the selected pruning mode, the percentage or the kernel scores.
See [`create_dl_pruning`](create_dl_pruning.md) for further information about
implemented pruning modes.

Behavior in special cases:

- In case the set amount of pruning *"percentage"* is too small to
  result in any removals, the returned model *`dlmodel_handle_pruned`*
  is simply a copy of the input model *`dlmodel_handle_to_prune`*.
- In case the model could not be pruned successfully, an empty handle is
  returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dlmodel_handle_to_prune`** (input_control)  dl_model `→` HHandle

Input model.

**`dlpruning_handle`** (input_control)  dl_pruning `→` HHandle

Pruning data handle.

**`dlmodel_handle_pruned`** (output_control)  dl_model `→` HHandle

Pruned model.

## Possible Predecessors

`add_dl_pruning_batch`,
`set_dl_pruning_param`

## Module

Deep Learning Professional
