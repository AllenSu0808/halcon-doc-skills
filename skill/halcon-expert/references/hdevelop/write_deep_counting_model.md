# write_deep_counting_model (Operator)

## Name

`write_deep_counting_model` — Write a Deep Counting model in a file.

## Signature

`write_deep_counting_model( : : DeepCountingHandle, FileName : )`

## Description

`write_deep_counting_model` writes the Deep Counting model
*`DeepCountingHandle`* to the file given by *`FileName`*.
Please note that the runtime specific parameters *'gpu'*,
*'runtime'*, and *'runtime_init'* are not written.

The default HALCON file extension for Deep Counting models is
`'.hdc'`.

The Deep Counting model can be read with [`read_deep_counting_model`](read_deep_counting_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DeepCountingHandle`** (input_control)  deep_counting `→`  (handle)

Handle of the Deep Counting model.

**`FileName`** (input_control)  filename.write `→`  (string)

Filename

File extension:
.`hdc`

## Result

If the parameters are valid, the operator `write_deep_counting_model`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_deep_counting_model`,
`set_deep_counting_model_param`

## Possible Successors

`clear_handle`

## Module

Matching
