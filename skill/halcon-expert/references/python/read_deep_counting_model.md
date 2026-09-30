# read_deep_counting_model (Operator)

## Name

`read_deep_counting_model` — Read a Deep Counting model from a file.

## Signature

`def read_deep_counting_model(file_name: str) -> HHandle`

## Description

The operator `read_deep_counting_model` reads a Deep Counting model.
Such models have to be in the HALCON format.
As a result, the handle *`deep_counting_handle`* is returned.

The model is loaded from the file *`file_name`*.
This file is thereby searched in the directory `$HALCONROOT/dl/`
as well as in the currently used directory.
The default HALCON file extension for Deep Counting models is
`'.hdc'`.

Please note that the values of runtime specific parameters are not written
to file, see [`write_deep_counting_model`](write_deep_counting_model.md).
As a consequence when reading a model these parameters are initialized with
their default value, see [`get_deep_counting_model_param`](get_deep_counting_model_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`file_name`** (input_control)  filename.read `→` str

Filename

File extension:
.`hdc`

**`deep_counting_handle`** (output_control)  deep_counting `→` HHandle

Handle of the Deep Counting model.

## Result

If the parameters are valid, the operator `read_deep_counting_model`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_deep_counting_model`

## Possible Successors

`set_deep_counting_model_param`,
`get_deep_counting_model_param`,
`prepare_deep_counting_model`,
`apply_deep_counting_model`

## Alternatives

`create_deep_counting_model`

## Module

Matching
