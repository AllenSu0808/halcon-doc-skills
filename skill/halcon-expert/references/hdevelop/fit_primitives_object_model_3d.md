# fit_primitives_object_model_3d (Operator)

## Name

`fit_primitives_object_model_3d` — Fit 3D primitives into a set of 3D points.

## Signature

`fit_primitives_object_model_3d( : : ObjectModel3D, GenParamName, GenParamValue : ObjectModel3DOut)`

## Description

The operator `fit_primitives_object_model_3d` fits a 3D primitive,
i.e., a simple 3D shape, into a set of 3D points given by a 3D object
model with the handle *`ObjectModel3D`*. The shapes that are
available as 3D primitives comprise a cylinder, a sphere, and a plane.
As the operator does not perform a segmentation of the set of 3D points
that is contained in the input 3D object model, you have to make sure
that the contained 3D points already correspond to a 3D primitive.
A segmentation can be performed, e.g., with the
operator [`segment_object_model_3d`](segment_object_model_3d.md).

`fit_primitives_object_model_3d` returns the handle
`ObjectModel3DOut` for the output 3D object model, which
contains information that concern, e.g., the type and parameters
of the fitted 3D primitive.
This information can be queried from the 3D object model with
[`get_object_model_3d_params`](get_object_model_3d_params.md). Note that the extent of primitives
of the type plane and cylinder can be queried with
[`get_object_model_3d_params`](get_object_model_3d_params.md), as well.

The parameters of a cylinder are the (x-, y-, z-)coordinates
of the center, the normed (x-, y-, z-)directions
of the main axis of the cylinder, and the radius of the cylinder. The
center does not necessarily lie in the center of gravity of the
cylinder (see the explanation of the parameters MinExtent and
MaxExtent of the operator [`gen_cylinder_object_model_3d`](gen_cylinder_object_model_3d.md)).
The sign of the main axis is determined such that the main axis points
towards the half space in which the origin is located.
For a sphere the parameters are the (x-, y-, z-)coordinates of the
center and the radius of the sphere.
A plane is given by the 4 parameters of the hessian normal form,
i.e., the unit normal (x-, y-, z-) vector and the orthogonal
distance of the plane from the origin of the coordinate system.
The sign of the hessian normal form is determined such that the normal
vector points towards the side of the plane on which the origin is located
and the distance is not positive.

If no primitive can be fitted to the set of 3D points, the returned object
model will not contain a primitive. However, depending on the parameter
values for *'output_point_coord'* and *'output_xyz_mapping'*
(see below), the returned object model is either empty, or contains
the 3D points, or contains the 3D points and the mapping from the 3D
points to image coordinates of the input object model
*`ObjectModel3D`*.

To control the fitting, you can adjust some
generic parameters within *`GenParamName`* and *`GenParamValue`*.
But note that for a lot of applications the default
values are sufficient and no adjustment is necessary.
The following values for *`GenParamName`* and *`GenParamValue`*
are possible:

- ***'primitive_type'*:** —

  The parameter specifies which
  type of 3D primitive should be fitted into the set of 3D points.
  You can specify a specific primitive type by setting
  *'primitive_type'* to *'cylinder'*, *'sphere'*,
  or *'plane'*. Then, only the selected type of 3D primitive
  is fitted into the set of 3D points. You can also specify a set of
  specific 3D primitives that should be fitted by setting
  *'primitive_type'* to a tuple consisting of different
  primitive types. If all types of 3D primitives should be fitted,
  you can set *'primitive_type'* to *'all'*. Note that
  if more than one primitive type is selected, only
  the best fitting 3D primitive, i.e., the 3D primitive with
  the smallest quadratic residual error, is returned.

  List of values:
   *'cylinder'*, *'sphere'*,
  *'plane'*, *'all'*

  Default:
   *'cylinder'*
- ***'fitting_algorithm'*:** —

  The parameter specifies the
  used algorithm for the fitting of the 3D primitive. When fitting
  a plane, the results are identical for the different algorithms. If
  *'fitting_algorithm'* is set to *'least_squares'*, the
  approach minimizes the quadratic distance between the 3D points and the
  resulting primitive. If *'fitting_algorithm'* is set to
  *'least_squares_huber'*, the approach is similar to
  *'least_squares'*, but the points are
  weighted to decrease the impact of outliers based on the approach of
  Huber (see below). If *'fitting_algorithm'* is set to
  *'least_squares_tukey'*, the approach is also similar to
  *'least_squares'*, but the points are
  weighted and outliers are ignored based on the approach
  of Tukey (see below).

  For *'least_squares_huber'* and *'least_squares_tukey'*
  a robust error statistics is used to estimate the standard deviation
  of the distances from the object points without outliers from the
  fitting primitive. The Tukey algorithm removes outliers,
  whereas the Huber algorithm only damps them, or more
  precisely, weights them linearly. In practice, the approach of
  Tukey is recommended.

  List of values:
   *'least_squares'*, *'least_squares_huber'*,
  *'least_squares_tukey'*

  Default:
   *'least_squares'*
- ***'min_radius'*:** —

  The parameter specifies the minimum
  radius of a cylinder or a sphere. If a cylinder or a sphere with
  a smaller radius is fitted, the resulting 3D object model is empty.
  The parameter is ignored when fitting a plane. The unit is meter.

  Suggested values:
   *0.01*, *0.02*,
  *0.1*

  Default:
   *0.01*
- ***'max_radius'*:** —

  The parameter specifies the maximum
  radius of a cylinder or a sphere. If a cylinder or a sphere with
  a larger radius is fitted, the resulting 3D object model is empty.
  The parameter is ignored when fitting a plane. The unit is
  meter.

  Suggested values:
   *0.02*, *0.04*,
  *0.2*

  Default:
   *0.2*
- ***'output_point_coord'*:** —

  The parameter determines
  if the 3D points used for the fitting are copied to the
  output 3D object model. If *'copy_point_coord'* is
  set to *'true'*, the 3D points are copied. If
  *'copy_point_coord'* is set to *'false'*, no
  3D points are copied.

  List of values:
   *'true'*, *'false'*

  Default:
   *'true'*
- ***'output_xyz_mapping'*:** —

  The parameter determines
  if a mapping from the 3D points to image coordinates is
  copied to the output 3D object model. This information is
  needed, e.g., when using the operator [`object_model_3d_to_xyz`](object_model_3d_to_xyz.md)
  after the fitting (e.g., for a visualization). If
  *'output_xyz_mapping'* is set to *'true'*,
  the image coordinate mapping is copied. Note that the parameter is
  only valid, if the image coordinate mapping is available in the input
  3D object model. Make sure that, if you derive the input 3D object
  model by copying it with the operator [`copy_object_model_3d`](copy_object_model_3d.md)
  from a 3D object model that contains such a mapping, the mapping is
  copied, too. Furthermore, the parameter is only valid, if
  the 3D points are copied to the output 3D object model, which is set
  with the parameter *'output_point_coord'*.

  List of values:
   *'true'*, *'false'*

  Default:
   *'false'*

The minimum number of 3D points that are necessary to fit a plane is
three. The minimum number of 3D points that is necessary to fit a
sphere is four. The minimum number of 3D points that is necessary to
fit a cylinder is five.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ObjectModel3D`** (input_control)  object_model_3d(-array) `→`  (handle)

Handle of the input 3D object model.

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Names of the generic parameters.

Number of elements:
GenParamName == GenParamValue

List of values:
'fitting_algorithm', 'max_radius', 'min_radius', 'output_point_coord', 'output_xyz_mapping', 'primitive_type'

**`GenParamValue`** (input_control)  attribute.name-array `→`  (string / real / integer)

Values of the generic parameters.

Number of elements:
GenParamValue == GenParamName

Suggested values:
'cylinder', 'sphere', 'plane', 'all', 'least_squares', 'least_squares_huber', 'least_squares_tukey', 0.01, 0.05, 0.1, 0.2, 'true', 'false'

**`ObjectModel3DOut`** (output_control)  object_model_3d(-array) `→`  (handle)

Handle of the output 3D object model.

## Result

`fit_primitives_object_model_3d` returns 2 (
H_MSG_TRUE)
if all parameter
values are correct. If necessary, an exception is raised.

## Possible Predecessors

`xyz_to_object_model_3d`,
`read_object_model_3d`

## Possible Successors

`get_object_model_3d_params`,
`object_model_3d_to_xyz`,
`write_object_model_3d`,
`clear_object_model_3d`

## Alternatives

`segment_object_model_3d`

## Module

3D Metrology
