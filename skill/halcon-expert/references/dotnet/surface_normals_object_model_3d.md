# SurfaceNormalsObjectModel3d (Operator)

## Name

`SurfaceNormalsObjectModel3d` — Calculate the 3D surface normals of a 3D object model.

## Signature

`static void HOperatorSet.SurfaceNormalsObjectModel3d(HTuple objectModel3D, HTuple method, HTuple genParamName, HTuple genParamValue, out HTuple objectModel3DNormals)`

`static HObjectModel3D[] HObjectModel3D.SurfaceNormalsObjectModel3d(HObjectModel3D[] objectModel3D, string method, HTuple genParamName, HTuple genParamValue)`

`HObjectModel3D HObjectModel3D.SurfaceNormalsObjectModel3d(string method, HTuple genParamName, HTuple genParamValue)`

## Description

The operator `SurfaceNormalsObjectModel3d` calculates the
3D surface normals for the object *`objectModel3D`* using the method
specified by *`method`*. The calculated normals are appended to the
input object and the resulting object is returned in
*`objectModel3DNormals`*.

For *`method`* *"mls"*, the normals estimation method Moving Least
Squares (MLS) is applied.
The MLS method for normals estimation is essentially identical with
the MLS method used by [`SmoothObjectModel3d`](smooth_object_model_3d.md) with the exception
that in `SurfaceNormalsObjectModel3d` the 3D points are not
smoothed, i.e., the original 3D points of *`objectModel3D`* remain
unchanged. For more details on the MLS as well as a full list and
descriptions of the supported MLS parameters refer to
[`SmoothObjectModel3d`](smooth_object_model_3d.md).

If the object *`objectModel3D`* contains triangles, the
*`method`* *"triangles"* can be used to obtain point normals
from the normals of the triangles neighboring a point.
The normals of the neighboring triangles are weighted according to
the angle which the triangle encloses at the point.
The triangle normals are returned in the extended attributes
'&triangle_normal_x', '&triangle_normal_y' and '&triangle_normal_z'.
If the extended attributes already exist, they will not be overwritten.

If the object *`objectModel3D`* contains a 2D mapping (for example a
3D object model that was created with [`XyzToObjectModel3d`](xyz_to_object_model_3d.md)),
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

**`objectModel3D`** (input_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model containing 3D point
data.

**`method`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Normals calculation method.

Default:
"mls"

List of values:
"mls", "triangles", "xyz_mapping"

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Names of generic smoothing parameters.

Default:
[]

List of values:
"mls_abs_sigma", "mls_force_inwards", "mls_kNN", "mls_order", "mls_relative_sigma"

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*double* / int / long / string)

Values of generic smoothing parameters.

Default:
[]

Suggested values:
10, 20, 40, 60, 0.1, 0.5, 1.0, 2.0, 0, 1, 2, "true", "false"

**`objectModel3DNormals`** (output_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model with calculated
3D normals.

## Possible Predecessors

`SampleObjectModel3d`

## Possible Successors

`CreateSurfaceModel`,
`FuseObjectModel3d`

## Alternatives

`SmoothObjectModel3d`

## Module

3D Metrology
