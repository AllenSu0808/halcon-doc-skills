# ReadDeepMatching3d (Operator)

## Name

`ReadDeepMatching3d` — Read a Deep 3D Matching model from a file.

## Signature

`static void HOperatorSet.ReadDeepMatching3d(HTuple fileName, out HTuple deep3DMatchingModel)`

`public HDeepMatching3D(string fileName)`

`void HDeepMatching3D.ReadDeepMatching3d(string fileName)`

## Description

The operator `ReadDeepMatching3d` reads a Deep 3D Matching model.
Such models have to be in the HALCON format.
As a result, the handle *`deep3DMatchingModel`* is returned.

The model is loaded from the file *`fileName`*.
The default HALCON file extension for Deep 3D Matching models is
`'.dm3'`.

Please note that the values of runtime specific parameters are not written
to file, see [`WriteDeepMatching3d`](write_deep_matching_3d.md).
As a consequence when reading a model these parameters are initialized with
their default value, see [`GetDeepMatching3dParam`](get_deep_matching_3d_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

Filename

File extension:
.`dm3`

**`deep3DMatchingModel`** (output_control)  deep_matching_3d `→` [HDeepMatching3D](HDeepMatching3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the Deep 3D Matching model.

## Result

If the parameters are valid, the operator `ReadDeepMatching3d`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateDeepMatching3d`

## Possible Successors

`SetDeepMatching3dParam`,
`GetDeepMatching3dParam`,
`ApplyDeepMatching3d`

## Alternatives

`CreateDeepMatching3d`

## Module

3D Metrology
