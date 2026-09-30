# write_component_model (Operator)

## Name

`write_component_model` — Write a component model to a file.

## Warning

**`write_component_model` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`def write_component_model(component_model_id: HHandle, file_name: str) -> None`

## Description

The operator `write_component_model` writes the component
model *`component_model_id`* to the file *`file_name`*. The
model can be read again with [`read_component_model`](read_component_model.md).
The default HALCON file extension for the component model is 'cbm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`component_model_id`** (input_control)  component_model `→` HHandle

Handle of the component model.

**`file_name`** (input_control)  filename.write `→` str

File name.

File extension:
.`cbm`

## Result

If the file name is valid (write permission), the operator
`write_component_model` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
