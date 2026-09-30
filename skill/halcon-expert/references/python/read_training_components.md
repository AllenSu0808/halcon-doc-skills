# read_training_components (Operator)

## Name

`read_training_components` — Read a component training result from a file.

## Warning

**`read_training_components` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`def read_training_components(file_name: str) -> HHandle`

## Description

The operator `read_training_components` reads a component
training result, which has been written with
[`write_training_components`](write_training_components.md), from the file *`file_name`*
and returns it in *`component_training_id`*.
The default HALCON file extension for the component training result
is 'ct'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`file_name`** (input_control)  filename.read `→` str

File name.

File extension:
.`ct`

**`component_training_id`** (output_control)  component_training `→` HHandle

Handle of the training result.

## Result

If the file name is valid, the operator `read_training_components`
returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
