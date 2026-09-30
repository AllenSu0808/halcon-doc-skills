# get_modules (Operator)

## Name

`get_modules` — Query of used modules and the module key.

## Signature

`def get_modules() -> Tuple[Sequence[str], int]`

## Description

`get_modules` returns the modules *`used_modules`* that were used
up to this point in the HALCON session. Based on the used modules, a key
is generated that is returned in *`module_key`*. Each operator belongs
to exactly one module.
The information which modules where used can be reset by calling
[`set_system`](set_system.md) with the *"reset_used_modules"* parameter.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`used_modules`** (output_control)  string-array `→` Sequence[str]

Names of used modules.

**`module_key`** (output_control)  integer `→` int

Key for license manager.

## Module

Foundation
