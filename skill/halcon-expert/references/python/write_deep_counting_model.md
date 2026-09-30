# write_deep_counting_model (Operator)

## Name

`write_deep_counting_model` — Write a Deep Counting model in a file.

## Signature

`def write_deep_counting_model(deep_counting_handle: HHandle, file_name: str) -> None`

## Description

`write_deep_counting_model` writes the Deep Counting model
*`deep_counting_handle`* to the file given by *`file_name`*.
Please note that the runtime specific parameters *"gpu"*,
*"runtime"*, and *"runtime_init"* are not written.

The default HALCON file extension for Deep Counting models is
`'.hdc'`.

The Deep Counting model can be read with [`read_deep_counting_model`](read_deep_counting_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`deep_counting_handle`** (input_control)  deep_counting `→` HHandle

Handle of the Deep Counting model.

**`file_name`** (input_control)  filename.write `→` str

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
