# SimplifyObjectModel3d (Operator)

## Name

`SimplifyObjectModel3d` — Simplify a triangulated 3D object model.

## Signature

`static void HOperatorSet.SimplifyObjectModel3d(HTuple objectModel3D, HTuple method, HTuple amount, HTuple genParamName, HTuple genParamValue, out HTuple simplifiedObjectModel3D)`

`static HObjectModel3D[] HObjectModel3D.SimplifyObjectModel3d(HObjectModel3D[] objectModel3D, string method, HTuple amount, HTuple genParamName, HTuple genParamValue)`

`HObjectModel3D HObjectModel3D.SimplifyObjectModel3d(string method, double amount, HTuple genParamName, HTuple genParamValue)`

## Description

`SimplifyObjectModel3d` simplifies the triangulated 3D object model
*`objectModel3D`* by removing model points and
returns the result in *`simplifiedObjectModel3D`*. Note that in
contrast to [`SampleObjectModel3d`](sample_object_model_3d.md) points are removed
such that the original geometry of the object model is represented as good
as possible. Typically, this means that edges are preserved while the
point density within smooth parts is reduced.
This might be helpful, for example, to speed up subsequent operator calls
by using a 3D object model of reduced complexity.

The triangulation of the input 3D object model is preserved as opposed to
the operator [`SampleObjectModel3d`](sample_object_model_3d.md), which samples surfaces to
equidistant unconnected 3D points.

Currently, the operator offers only a single simplification method
(*"preserve_point_coordinates"*), which can be set in
*`method`*. This method ensures that the points in the
simplified object model *`simplifiedObjectModel3D`* have the same
coordinates as the respective points in the input object model
*`objectModel3D`*.

`SimplifyObjectModel3d` only works for triangulated object models.
Whether an object model contains a triangulation can be queried with
[`GetObjectModel3dParams`](get_object_model_3d_params.md)
(`genParamName`=*"has_triangles"*). Object models that
do not contain a triangulation must be triangulated beforehand, e.g., by
using [`TriangulateObjectModel3d`](triangulate_object_model_3d.md) or [`PrepareObjectModel3d`](prepare_object_model_3d.md)
(`purpose`=*"segmentation"*).

The degree of simplification can be set with *`amount`*. By default,
*`amount`* specifies the percentage of points of the input object
model that should be contained in the output object model. Thus, the
smaller the value of *`amount`* in this case is chosen the
stronger the object model will be simplified.

Alternatively, the meaning of the parameter *`amount`* can be
modified. For this, the generic parameter *"amount_type"* can
be set to one of the following values:

- **'percentage_remaining' (default):** —

  *`amount`* specifies the percentage of points of the input object
  model that should be contained in the output object model.

  Value range:
   [*0.0* ... *100.0*].
- **'percentage_to_remove':** —

  *`amount`* specifies the percentage of points of the input object
  model that should be removed.

  Value range:
   [*0.0* ... *100.0*].
- **'num_points_remaining':** —

  *`amount`* specifies the number of points of the input object model
  that should be contained in the output object model.

  Value range:
   [*0* ... number of points in the input object model].
- **'num_points_to_remove':** —

  *`amount`* specifies the number of points of the input object model
  that should be removed.

  Value range:
   [*0* ... number of points in the input object model].

Sometimes triangular meshes flip during the simplification, i.e., the
direction of their normal vectors changes by 180 degrees. This
especially happens for artificially created CAD models that consist of
planar parts. To avoid this flipping, the generic
parameter *"avoid_triangle_flips"* can be set to *"true"*
(the default is *"false"*). Note that in this case, the run-time of
`SimplifyObjectModel3d` will increase.

Note that multiple calls of `SimplifyObjectModel3d` with a
lower degree of simplification might result in a different simplified
object model compared to a single call with a higher degree of
simplification. Also note that isolated (i.e., non-triangulated) points
will be removed. This might result in a number of points in
*`simplifiedObjectModel3D`* that slightly deviates from the degree of
simplification that is specified in *`amount`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectModel3D`** (input_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model that should be
simplified.

**`method`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Method that should be used for simplification.

Default:
"preserve_point_coordinates"

List of values:
"preserve_point_coordinates"

**`amount`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Degree of simplification (default: percentage
of remaining model points).

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters.

Default:
[]

List of values:
"amount_type", "avoid_triangle_flips"

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*string* / double)

Values of the generic parameters.

Default:
[]

Suggested values:
"percentage_remaining", "percentage_to_remove", "num_points_remaining", "num_points_to_remove", "true", "false"

**`simplifiedObjectModel3D`** (output_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the simplified 3D object model.

## Example (HDevelop)

```
read_object_model_3d ('mvtec_bunny.om3', 'm', [], [], ObjectModel3D, Status)
visualize_object_model_3d (WindowHandle, ObjectModel3D, [], [], [], [], \
                           [], [], [], Pose)
simplify_object_model_3d (ObjectModel3D, 'preserve_point_coordinates', \
                          5.0, 'amount_type', 'percentage_remaining', \
                          SimplifiedObjectModel3D)
visualize_object_model_3d (WindowHandle, SimplifiedObjectModel3D, [], \
                           Pose, [], [], [], [], [], Pose)
```

## Result

`SimplifyObjectModel3d` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`PrepareObjectModel3d`,
`ReadObjectModel3d`,
`TriangulateObjectModel3d`,
`XyzToObjectModel3d`

## Possible Successors

`DispObjectModel3d`,
`SmallestBoundingBoxObjectModel3d`

## Alternatives

`SampleObjectModel3d`,
`SmoothObjectModel3d`

## References

Michael Garland, Paul S. Heckbert: Surface Simplification Using Quadric
Error Metrics, Proceedings of the 24th Annual Conference on Computer
Graphics and Interactive Techniques (SIGGRAPH '97), 209-216, ACM Press,
1997

## Module

3D Metrology
