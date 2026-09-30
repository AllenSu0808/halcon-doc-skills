# surface_normals_object_model_3d (Operator)

## Name

`surface_normals_object_model_3d` — Calculate the 3D surface normals of a 3D object model.

## Signature

`def surface_normals_object_model_3d(object_model_3d: MaybeSequence[HHandle], method: str, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[float, int, str]]) -> Sequence[HHandle]`

`def surface_normals_object_model_3d_s(object_model_3d: MaybeSequence[HHandle], method: str, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[float, int, str]]) -> HHandle`

## Description

The operator `surface_normals_object_model_3d` calculates the
3D surface normals for the object *`object_model_3d`* using the method
specified by *`method`*. The calculated normals are appended to the
input object and the resulting object is returned in
*`object_model_3dnormals`*.

For *`method`* *"mls"*, the normals estimation method Moving Least
Squares (MLS) is applied.
The MLS method for normals estimation is essentially identical with
the MLS method used by [`smooth_object_model_3d`](smooth_object_model_3d.md) with the exception
that in `surface_normals_object_model_3d` the 3D points are not
smoothed, i.e., the original 3D points of *`object_model_3d`* remain
unchanged. For more details on the MLS as well as a full list and
descriptions of the supported MLS parameters refer to
[`smooth_object_model_3d`](smooth_object_model_3d.md).

If the object *`object_model_3d`* contains triangles, the
*`method`* *"triangles"* can be used to obtain point normals
from the normals of the triangles neighboring a point.
The normals of the neighboring triangles are weighted according to
the angle which the triangle encloses at the point.
The triangle normals are returned in the extended attributes
'&triangle_normal_x', '&triangle_normal_y' and '&triangle_normal_z'.
If the extended attributes already exist, they will not be overwritten.

If the object *`object_model_3d`* contains a 2D mapping (for example a
3D object model that was created with [`xyz_to_object_model_3d`](xyz_to_object_model_3d.md)),
the *`method`* *"xyz_mapping"* can be used to obtain
point normals from the neighborhood of the points in the 2D mapping.
In an 11x11 neighborhood of the points in the 2D mapping, a plane is fit
through the corresponding 3D points. The normal of this plane then gets
switched in a direction consistent with the 2D mapping, for example
along the viewing direction of the sensor or in the opposite direction.

Note that for points where the normal vector cannot be estimated, it is
set to the zero vector. This happens, for example, if the 3D object model
contains an identical point more than *"mls_kNN"* times.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator supports canceling timeouts and interrupts.

## Parameters

**`object_model_3d`** (input_control)  object_model_3d(-array) `→` MaybeSequence[HHandle]

Handle of the 3D object model containing 3D point
data.

**`method`** (input_control)  string `→` str

Normals calculation method.

Default:
"mls"

List of values:
"mls", "triangles", "xyz_mapping"

**`gen_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

Names of generic smoothing parameters.

Default:
[]

List of values:
"mls_abs_sigma", "mls_force_inwards", "mls_kNN", "mls_order", "mls_relative_sigma"

**`gen_param_value`** (input_control)  attribute.value-array `→` Sequence[Union[float, int, str]]

Values of generic smoothing parameters.

Default:
[]

Suggested values:
10, 20, 40, 60, 0.1, 0.5, 1.0, 2.0, 0, 1, 2, "true", "false"

**`object_model_3dnormals`** (output_control)  object_model_3d(-array) `→` Sequence[HHandle]

Handle of the 3D object model with calculated
3D normals.

## Possible Predecessors

`sample_object_model_3d`

## Possible Successors

`create_surface_model`,
`fuse_object_model_3d`

## Alternatives

`smooth_object_model_3d`

## Module

3D Metrology
