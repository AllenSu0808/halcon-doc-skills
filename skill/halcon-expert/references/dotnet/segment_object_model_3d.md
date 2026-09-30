# SegmentObjectModel3d (Operator)

## Name

`SegmentObjectModel3d` — Segment a set of 3D points into sub-sets with similar characteristics.

## Signature

`static void HOperatorSet.SegmentObjectModel3d(HTuple objectModel3D, HTuple genParamName, HTuple genParamValue, out HTuple objectModel3DOut)`

`static HObjectModel3D[] HObjectModel3D.SegmentObjectModel3d(HObjectModel3D[] objectModel3D, HTuple genParamName, HTuple genParamValue)`

`HObjectModel3D HObjectModel3D.SegmentObjectModel3d(HTuple genParamName, HTuple genParamValue)`

## Description

The operator `SegmentObjectModel3d` segments a set of 3D points
given by a 3D object model with the handle *`objectModel3D`* into
several sub-sets of neighbored 3D points with similar characteristics like
the same normal orientation or curvature. By default, the operator then
tries to fit a 3D primitive, i.e., a simple 3D shape like a plane,
a sphere, or a cylinder, into each of these sub-sets. As result, the
operator returns a tuple of handles for the 3D object models that
represent the individual sub-sets of 3D points
(*`objectModel3DOut`*). Within these 3D object models information
is stored that concern, e.g., the success of the fitting and the type
and parameters of the fitted 3D primitive. This information can be queried
from the individual 3D object model with [`GetObjectModel3dParams`](get_object_model_3d_params.md).

Before calling `SegmentObjectModel3d`, the input 3D object model
should be prepared for the segmentation using the operator
[`PrepareObjectModel3d`](prepare_object_model_3d.md) with the parameter `purpose` set
to *"segmentation"*. If the input 3D object model is not
prepared this way, the operator [`PrepareObjectModel3d`](prepare_object_model_3d.md) is called
internally within `SegmentObjectModel3d` to extend the
3D object model with attributes that were not explicitly but only implicitly
contained in the 3D object model.

To control the segmentation and the fitting, you can adjust some
generic parameters within *`genParamName`* and *`genParamValue`*.
But note that for a lot of applications the default
values are sufficient and no adjustment is necessary.
The following values for *`genParamName`* and *`genParamValue`*
are possible:

- ***"max_orientation_diff"*:** —

  The parameter specifies
  the maximum angle between the point normals of two neighbored 3D points
  (in radians) that is allowed so that the two points belong to the
  same sub-set of 3D points. For a cylinder or sphere, the parameter
  value depends on the dimension of the object and on the distance of
  the neighbored 3D points. I.e., if the cylinder or sphere has a
  very small radius or if the 3D points are not very dense, the value
  must be chosen higher. For a plane the value is independent from
  the dimension of the object and can be set to a small value.

  Suggested values:
   *0.10*, *0.15*,
  *0.20*

  Default:
   *0.15*
- ***"max_curvature_diff"*:** —

  The parameter specifies the
  maximum difference between the curvatures of the surface at the
  positions of two neighbored 3D points that is allowed so that
  the two points belong to the same sub-set of 3D points.
  The value depends on the noise of the 3D points. I.e.,
  if the noise level of the 3D points is very high, the value must
  be set to a higher value. Generally, the number of
  resulting 3D object models decreases for a higher value, because
  more 3D points are merged to a sub-set of 3D points.

  Suggested values:
   *0.03*, *0.04*,
  *0.05*

  Default:
   *0.05*
- ***"min_area"*:** —

  The parameter specifies the minimum
  number of 3D points needed for a sub-set of connected 3D points
  to be returned by the segmentation. Thus, for a sub-set with
  fewer points the points are deleted and no output handle is created.

  Suggested values:
   *1*, *10*, *100*

  Default:
   *100*
- ***"fitting"*:** —

  The parameter specifies whether after the
  segmentation 3D primitives are fitted into the sub-sets of 3D
  points. If *"fitting"* is set
  to *"true"*, which is the default, the fitting is calculated
  and the 3D object models with the resulting handles contain the
  parameters of the corresponding 3D primitives. The output parameters
  of a cylinder, a sphere, or a plane are described with the operator
  [`FitPrimitivesObjectModel3d`](fit_primitives_object_model_3d.md). If *"fitting"*
  is set to *"false"*, only a segmentation is performed and
  the output 3D object models contain the segmented sub-sets of 3D points.
  A later fitting can be performed with the operator
  [`FitPrimitivesObjectModel3d`](fit_primitives_object_model_3d.md).

  List of values:
   *"false"*, *"true"*

  Default:
   *"true"*
- ***"output_xyz_mapping"*:** —

  The parameter determines
  if a mapping from the segmented 3D points to image coordinates
  is copied to the output 3D object model. This information is
  needed, e.g., when using the operator [`ObjectModel3dToXyz`](object_model_3d_to_xyz.md)
  after the segmentation (e.g., for a visualization). If
  *"output_xyz_mapping"* is set to *"true"*,
  the image coordinate mapping is copied. Note that the parameter is
  only valid, if the image coordinate mapping is available in the input
  3D object model. Make sure that, if you derive the input 3D object
  model by copying it with the operator [`CopyObjectModel3d`](copy_object_model_3d.md)
  from a 3D object model that contains such a mapping, the mapping is
  copied, too. Furthermore, the parameter is only valid, if
  the 3D points are copied to the output 3D object model, which is set
  with the parameter *"output_point_coord"*.
  If *"output_xyz_mapping"* is set to *"false"*,
  the image coordinate mapping is not copied.

  List of values:
   *"true"*, *"false"*

  Default:
   *"false"*
- ***"primitive_type"*, *"fitting_algorithm"*,
  *"min_radius"*, *"max_radius"*,
  *"output_point_coord"*:** —

  These parameters are used, if *"fitting"* is set
  to *"true"*, which is the default.
  The meaning and the use of these parameters
  is described with the operator [`FitPrimitivesObjectModel3d`](fit_primitives_object_model_3d.md).
- ***"surface_check"*:** —

  The parameter determines whether the
  surface of a triangulated input object model is checked regarding
  its conformity to the expected requirements.
  If the input 3D object model contains triangles that are topologically
  invalid an error message is raised.
  If the triangulation was created ([`TriangulateObjectModel3d`](triangulate_object_model_3d.md))
  or edited (e.g., by [`SimplifyObjectModel3d`](simplify_object_model_3d.md)) by a HALCON
  operator, a surface check should not be necessary.
  The check can be disabled in order to enhance the runtime by setting
  *"surface_check"* to *"false"*.

  List of values:
   *"true"*, *"false"*

  Default:
   *"true"*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectModel3D`** (input_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the input 3D object model.

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters.

Number of elements:
GenParamName == GenParamValue

List of values:
"fitting_algorithm", "max_curvature_diff", "max_orientation_diff", "max_radius", "min_area", "min_radius", "output_point_coord", "output_xyz_mapping", "primitive_type", "surface_check"

**`genParamValue`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string* / double / int / long)

Values of the generic parameters.

Number of elements:
GenParamValue == GenParamName

Suggested values:
0.15, 0.05, 100, "true", "false", "cylinder", "sphere", "plane", "all", "least_squares", "least_squares_huber", "least_squares_tukey"

**`objectModel3DOut`** (output_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the output 3D object model.

## Result

`SegmentObjectModel3d` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`XyzToObjectModel3d`,
`ReadObjectModel3d`,
`PrepareObjectModel3d`

## Possible Successors

`GetObjectModel3dParams`,
`ObjectModel3dToXyz`,
`WriteObjectModel3d`,
`ClearObjectModel3d`

## See also

`FitPrimitivesObjectModel3d`

## Module

3D Metrology
