# SelectPointsObjectModel3d (Operator)

## Name

`SelectPointsObjectModel3d` — Apply a threshold to an attribute of 3D object models.

## Signature

`static void HOperatorSet.SelectPointsObjectModel3d(HTuple objectModel3D, HTuple attrib, HTuple minValue, HTuple maxValue, out HTuple objectModel3DThresholded)`

`static HObjectModel3D[] HObjectModel3D.SelectPointsObjectModel3d(HObjectModel3D[] objectModel3D, HTuple attrib, HTuple minValue, HTuple maxValue)`

`HObjectModel3D HObjectModel3D.SelectPointsObjectModel3d(string attrib, double minValue, double maxValue)`

## Description

`SelectPointsObjectModel3d` selects points of the 3D object
model *`objectModel3D`* according to the attributes and thresholds
passed in *`attrib`*, *`minValue`*, and *`maxValue`*
respectively.
The selected points are returned in the 3D object model
*`objectModel3DThresholded`*.
All attributes that are connected with the points
(e.g., polygons or triangles) are adapted in such a way that there is
no reference to the removed points left.

*`attrib`* can either contain a tuple of numbers that has the same
length as *`objectModel3D`* has points, or a list of attribute
names on which the thresholds are applied.

If *`attrib`* contains a tuple of numbers, exactly one number must
be passed in both *`minValue`* and *`maxValue`*.
All points for which the corresponding entry in *`attrib`* is between
the two thresholds are added to the output 3D object model
*`objectModel3DThresholded`*.

Otherwise, *`attrib`* can contain a list of attribute names that
refer to properties of the 3D object model *`objectModel3D`*.
All points, for which the value stored in the attribute *`attrib`*
is inside the interval specified in *`minValue`* and *`maxValue`*
are stored in the output 3D object model.
*`minValue`* and *`maxValue`* must contain exactly as many
values as *`attrib`*.
If *`attrib`* contains multiple values, only those points are stored
in the output 3D object model that fulfill all the criteria.

Depending on the properties of *`objectModel3D`*, the following
values are possible for *`attrib`*:

The following attributes are available:

- ***"point_coord_x"*:** —

  The x-coordinates of the set of 3D points.
- ***"point_coord_y"*:** —

  The y-coordinates of the set of 3D points.
- ***"point_coord_z"*:** —

  The z-coordinates of the set of 3D points.
- ***"point_normal_x"*:** —

  The x-components of the 3D point normals of the set of 3D points.
- ***"point_normal_y"*:** —

  The y-components of the 3D point normals of the set of 3D points.
- ***"point_normal_z"*:** —

  The z-components of the 3D point normals of the set of 3D points.
- ***"mapping_row"*:** —

  The row-components of the 2D mapping of the set of 3D points.
- ***"mapping_col"*:** —

  The column-components of the 2D mapping of the set of 3D points.
- ***"neighbor_distance"*:** —
- ***"neighbor_distance N"*:** —

  The distance of the N-th nearest point.
  N must be a positive integer and is by default 25.
  For every point, all other points are sorted according to their distance
  and the distance of the N-th point is used.
- ***"num_neighbors X"*:** —

  The number of neighbors within a distance of at most X.
  It can be used to remove sparsely populated parts of the 3D object model,
  such as outliers or points that are created by smoothing between 3D
  surfaces.
- ***"num_neighbors_fast X"*:** —

  The approximate number of neighbors within a distance of at most X.
  The distances are approximated using voxels, leading to a
  faster processing compared to *"num_neighbors"*.
- **Extended attribute:** —

  Enter the name of an extended attribute
  of the type *"vertices"* and
  the selection will be applied based on the values of the extended
  attribute.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`objectModel3D`** (input_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object models.

**`attrib`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Attributes the threshold is applied to.

Default:
"point_coord_z"

List of values:
"mapping_col", "mapping_row", "neighbor_distance", "num_neighbors", "num_neighbors_fast", "point_coord_x", "point_coord_y", "point_coord_z", "point_normal_x", "point_normal_y", "point_normal_z"

**`minValue`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Minimum value for the attributes specified by
*`attrib`*.

Default:
0.5

**`maxValue`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum value for the attributes specified
by *`attrib`*.

Default:
1.0

**`objectModel3DThresholded`** (output_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the reduced 3D object models.

## Example (HDevelop)

```
gen_object_model_3d_from_points (rand(100), rand(100),\
                                    rand(100), ObjectModel3D)
select_points_object_model_3d (ObjectModel3D, 'point_coord_z',\
                               0.5, 1, ObjectModel3DThresholded)
get_object_model_3d_params (ObjectModel3DThresholded, 'num_points',\
                            NumPoints)
```

## Result

`SelectPointsObjectModel3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.
If the required points are missing in the object model, i.e., an empty
object model is passed, the error 9515 is raised.

## Possible Predecessors

`ReadObjectModel3d`,
`XyzToObjectModel3d`

## Possible Successors

`ConnectionObjectModel3d`,
`ProjectObjectModel3d`,
`ObjectModel3dToXyz`

## See also

`ConnectionObjectModel3d`,
`ReduceObjectModel3dByView`

## Module

3D Metrology
