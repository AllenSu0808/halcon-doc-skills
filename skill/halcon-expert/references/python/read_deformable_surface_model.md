# read_deformable_surface_model (Operator)

## Name

`read_deformable_surface_model` — Read a deformable surface model from a file.

## Signature

`def read_deformable_surface_model(file_name: str) -> HHandle`

## Description

The operator `read_deformable_surface_model` reads the deformable
surface model, which has been written with
[`write_deformable_surface_model`](write_deformable_surface_model.md), from the file *`file_name`*.
The handle of the deformable surface model is returned in
*`deformable_surface_model`*.
If no absolute path is given in *`file_name`*, the file is searched
in the current directory of the HALCON process.
The default HALCON file extension for the deformable surface model file is
'dsfm'.
If no file named *`file_name`* exists, the default file extension is
appended to *`file_name`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`file_name`** (input_control)  filename.read `→` str

Name of the file to read.

File extension:
.`dsfm`

**`deformable_surface_model`** (output_control)  deformable_surface_model `→` HHandle

Handle of the read deformable surface model.

## Result

`read_deformable_surface_model` returns 2 (
H_MSG_TRUE)
if all parameters are
correct and the file can be read.
If the file is not a deformable surface model file, the error 9506 is raised.
If the file has a version that can not be read by this version of HALCON,
the error 9507 is raised.
If necessary, an exception is raised.

## Possible Predecessors

`write_deformable_surface_model`

## Possible Successors

`find_deformable_surface_model`,
`refine_deformable_surface_model`,
`get_deformable_surface_model_param`,
`clear_deformable_surface_model`

## Alternatives

`create_deformable_surface_model`

## See also

`create_deformable_surface_model`,
`write_deformable_surface_model`

## Module

3D Metrology
