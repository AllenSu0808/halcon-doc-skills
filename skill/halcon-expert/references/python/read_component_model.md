# read_component_model (Operator)

## Name

`read_component_model` — Read a component model from a file.

## Warning

**`read_component_model` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`def read_component_model(file_name: str) -> HHandle`

## Description

The operator `read_component_model` reads a component model,
which has been written with [`write_component_model`](write_component_model.md), from the
file *`file_name`* and returns it in *`component_model_id`*.
The default HALCON file extension for the component model is 'cbm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`file_name`** (input_control)  filename.read `→` str

File name.

File extension:
.`cbm`

**`component_model_id`** (output_control)  component_model `→` HHandle

Handle of the component model.

## Result

If the file name is valid, the operator `read_component_model`
returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
