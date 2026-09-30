# ReadComponentModel (Operator)

## Name

`ReadComponentModel` — Read a component model from a file.

## Warning

**`ReadComponentModel` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`static void HOperatorSet.ReadComponentModel(HTuple fileName, out HTuple componentModelID)`

`public HComponentModel(string fileName)`

`void HComponentModel.ReadComponentModel(string fileName)`

## Description

The operator `ReadComponentModel` reads a component model,
which has been written with [`WriteComponentModel`](write_component_model.md), from the
file *`fileName`* and returns it in *`componentModelID`*.
The default HALCON file extension for the component model is 'cbm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`cbm`

**`componentModelID`** (output_control)  component_model `→` [HComponentModel](HComponentModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the component model.

## Result

If the file name is valid, the operator `ReadComponentModel`
returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
