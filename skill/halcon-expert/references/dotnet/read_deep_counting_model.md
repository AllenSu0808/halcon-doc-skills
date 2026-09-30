# ReadDeepCountingModel (Operator)

## Name

`ReadDeepCountingModel` — Read a Deep Counting model from a file.

## Signature

`static void HOperatorSet.ReadDeepCountingModel(HTuple fileName, out HTuple deepCountingHandle)`

`public HDlModelCounting(string fileName)`

`void HDlModelCounting.ReadDeepCountingModel(string fileName)`

## Description

The operator `ReadDeepCountingModel` reads a Deep Counting model.
Such models have to be in the HALCON format.
As a result, the handle *`deepCountingHandle`* is returned.

The model is loaded from the file *`fileName`*.
This file is thereby searched in the directory `$HALCONROOT/dl/`
as well as in the currently used directory.
The default HALCON file extension for Deep Counting models is
`'.hdc'`.

Please note that the values of runtime specific parameters are not written
to file, see [`WriteDeepCountingModel`](write_deep_counting_model.md).
As a consequence when reading a model these parameters are initialized with
their default value, see [`GetDeepCountingModelParam`](get_deep_counting_model_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

Filename

File extension:
.`hdc`

**`deepCountingHandle`** (output_control)  deep_counting `→` [HDlModelCounting](HDlModelCounting.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the Deep Counting model.

## Result

If the parameters are valid, the operator `ReadDeepCountingModel`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateDeepCountingModel`

## Possible Successors

`SetDeepCountingModelParam`,
`GetDeepCountingModelParam`,
`PrepareDeepCountingModel`,
`ApplyDeepCountingModel`

## Alternatives

`CreateDeepCountingModel`

## Module

Matching
