# WriteComponentModel (Operator)

## Name

`WriteComponentModel` — Write a component model to a file.

## Warning

**`WriteComponentModel` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`static void HOperatorSet.WriteComponentModel(HTuple componentModelID, HTuple fileName)`

`void HComponentModel.WriteComponentModel(string fileName)`

## Description

The operator `WriteComponentModel` writes the component
model *`componentModelID`* to the file *`fileName`*. The
model can be read again with [`ReadComponentModel`](read_component_model.md).
The default HALCON file extension for the component model is 'cbm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`componentModelID`** (input_control)  component_model `→` [HComponentModel](HComponentModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the component model.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`cbm`

## Result

If the file name is valid (write permission), the operator
`WriteComponentModel` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
