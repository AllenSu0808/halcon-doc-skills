# write_distance_transform_xld (Operator)

## Name

`write_distance_transform_xld` — Write an XLD distance transform into a file.

## Signature

`def write_distance_transform_xld(distance_transform_id: HHandle, file_name: str) -> None`

## Description

`write_distance_transform_xld` writes the XLD distance transform
*`distance_transform_id`* into the file given by *`file_name`*.
The default HALCON extension for the XLD distance transform is 'hdtc'.

The stored XLD distance transform can be read in with
[`read_distance_transform_xld`](read_distance_transform_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`distance_transform_id`** (input_control)  xld_dist_trans `→` HHandle

Handle of the XLD distance transform.

**`file_name`** (input_control)  filename.write `→` str

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
