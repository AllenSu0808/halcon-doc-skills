# WriteDeepCountingModel (Operator)

## Name

`WriteDeepCountingModel` — Write a Deep Counting model in a file.

## Signature

`static void HOperatorSet.WriteDeepCountingModel(HTuple deepCountingHandle, HTuple fileName)`

`void HDlModelCounting.WriteDeepCountingModel(string fileName)`

## Description

`WriteDeepCountingModel` writes the Deep Counting model
*`deepCountingHandle`* to the file given by *`fileName`*.
Please note that the runtime specific parameters *"gpu"*,
*"runtime"*, and *"runtime_init"* are not written.

The default HALCON file extension for Deep Counting models is
`'.hdc'`.

The Deep Counting model can be read with [`ReadDeepCountingModel`](read_deep_counting_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`deepCountingHandle`** (input_control)  deep_counting `→` [HDlModelCounting](HDlModelCounting.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the Deep Counting model.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Filename

File extension:
.`hdc`

## Result

If the parameters are valid, the operator `WriteDeepCountingModel`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateDeepCountingModel`,
`SetDeepCountingModelParam`

## Possible Successors

`ClearHandle`

## Module

Matching
