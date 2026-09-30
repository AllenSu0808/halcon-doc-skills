# write_distance_transform_xld (Operator)

## Name

`write_distance_transform_xld` — Write an XLD distance transform into a file.

## Signature

`write_distance_transform_xld( : : DistanceTransformID, FileName : )`

## Description

`write_distance_transform_xld` writes the XLD distance transform
*`DistanceTransformID`* into the file given by *`FileName`*.
The default HALCON extension for the XLD distance transform is 'hdtc'.

The stored XLD distance transform can be read in with
[`read_distance_transform_xld`](read_distance_transform_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DistanceTransformID`** (input_control)  xld_dist_trans `→`  (handle)

Handle of the XLD distance transform.

**`FileName`** (input_control)  filename.write `→`  (string)

Name of the file.

File extension:
.`hdtc`

## Result

If all parameters are correct, the operator returns the
value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`create_distance_transform_xld`

## Possible Successors

`clear_distance_transform_xld`

## Alternatives

`serialize_distance_transform_xld`

## See also

`read_distance_transform_xld`,
`deserialize_distance_transform_xld`,
`get_distance_transform_xld_contour`,
`apply_distance_transform_xld`,
`get_distance_transform_xld_param`,
`set_distance_transform_xld_param`

## Module

Foundation
