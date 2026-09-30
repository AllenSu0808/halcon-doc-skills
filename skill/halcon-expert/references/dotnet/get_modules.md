# GetModules (Operator)

## Name

`GetModules` — Query of used modules and the module key.

## Signature

`static void HOperatorSet.GetModules(out HTuple usedModules, out HTuple moduleKey)`

`static HTuple HSystem.GetModules(out int moduleKey)`

## Description

`GetModules` returns the modules *`usedModules`* that were used
up to this point in the HALCON session. Based on the used modules, a key
is generated that is returned in *`moduleKey`*. Each operator belongs
to exactly one module.
The information which modules where used can be reset by calling
[`SetSystem`](set_system.md) with the *"reset_used_modules"* parameter.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`usedModules`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Names of used modules.

**`moduleKey`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Key for license manager.

## Module

Foundation
