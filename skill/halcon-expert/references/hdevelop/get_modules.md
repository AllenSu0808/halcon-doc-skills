# get_modules (Operator)

## Name

`get_modules` — Query of used modules and the module key.

## Signature

`get_modules( : : : UsedModules, ModuleKey)`

## Description

`get_modules` returns the modules *`UsedModules`* that were used
up to this point in the HALCON session. Based on the used modules, a key
is generated that is returned in *`ModuleKey`*. Each operator belongs
to exactly one module.
The information which modules where used can be reset by calling
[`set_system`](set_system.md) with the *'reset_used_modules'* parameter.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`UsedModules`** (output_control)  string-array `→`  (string)

Names of used modules.

**`ModuleKey`** (output_control)  integer `→`  (integer)

Key for license manager.

## Module

Foundation
