# write_training_components (Operator)

## Name

`write_training_components` — Write a component training result to a file.

## Warning

**`write_training_components` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`def write_training_components(component_training_id: HHandle, file_name: str) -> None`

## Description

The operator `write_training_components` writes the component
training result *`component_training_id`* to the file
*`file_name`*. The training result can be read again with
[`read_training_components`](read_training_components.md).
The default HALCON file extension for the component training result
is 'ct'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`component_training_id`** (input_control)  component_training `→` HHandle

Handle of the training result.

**`file_name`** (input_control)  filename.write `→` str

File name.

File extension:
.`ct`

## Result

If the file name is valid (write permission), the operator
`write_training_components` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
