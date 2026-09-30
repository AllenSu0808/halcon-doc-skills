# get_object_model_3d_params (Operator)

## Name

`get_object_model_3d_params` — Return attributes of 3D object models.

## Signature

`def get_object_model_3d_params(object_model_3d: MaybeSequence[HHandle], gen_param_name: Sequence[str]) -> Sequence[Union[int, str, float]]`

`def get_object_model_3d_params_s(object_model_3d: MaybeSequence[HHandle], gen_param_name: Sequence[str]) -> Union[int, str, float]`

## Description

A 3D object model consists of a set of attributes and meta data.
The operator `get_object_model_3d_params` allows to access
attributes and meta data of the given 3D object models. The name
of the requested attribute or meta data is passed in the generic
parameter *`gen_param_name`*, the corresponding value is returned in
*`gen_param_value`*. If a requested attribute or meta data is not
available, an exception is raised.
`get_object_model_3d_params` supports to access several 3D object
models and several attributes at once. Note that the attributes or
meta data can have different lengths.
Some of the standard attributes have a defined length as noted in the
attribute description below.
The length of other attributes depends on the actual 3D object model, and can
be queried by setting the parameter *`gen_param_name`* to, e.g.,
*"num_points"*, *"num_triangles"*, *"num_polygons"*, or
*"num_lines"*.
Thus, to get the length of the standard attribute *"point_coord_x"*,
set *`gen_param_name`* to *"num_points"*.

### Standard attributes

The following standard attributes and meta data can be accessed:

- ***"point_coord_x"*:** —

  The x-coordinates of the set of the 3D points
  (length can be queried by *"num_points"*).
  This attribute is obtained typically from the operator
  [`xyz_to_object_model_3d`](xyz_to_object_model_3d.md) or [`read_object_model_3d`](read_object_model_3d.md).
- ***"point_coord_y"*:** —

  The y-coordinates of the set of the 3D points
  (length can be queried by *"num_points"*).
  This attribute is obtained typically from the operator
  [`xyz_to_object_model_3d`](xyz_to_object_model_3d.md) or [`read_object_model_3d`](read_object_model_3d.md).
- ***"point_coord_z"*:** —

  The z-coordinates of the set of the 3D points
  (length can be queried by *"num_points"*).
  This attribute is obtained typically from the operator
  [`xyz_to_object_model_3d`](xyz_to_object_model_3d.md) or [`read_object_model_3d`](read_object_model_3d.md).
- ***"point_normal_x"*:** —

  The x-components of 3D point normals of the set of the 3D points
  (length can be queried by *"num_points"*).
  This attribute is obtained typically from the operator
  [`smooth_object_model_3d`](smooth_object_model_3d.md).
- ***"point_normal_y"*:** —

  The y-components of 3D point normals of the set of the 3D points
  (length can be queried by *"num_points"*).
  This attribute is obtained typically from the operator
  [`smooth_object_model_3d`](smooth_object_model_3d.md).
- ***"point_normal_z"*:** —

  The z-components of 3D point normals of the set of the 3D points
  (length can be queried by *"num_points"*).
  This attribute is obtained typically from the operator
  [`smooth_object_model_3d`](smooth_object_model_3d.md).
- ***"mapping_row"*:** —

  The row-components of the 2D mapping of the set of 3D points.
  (length can be queried by *"num_points"*, height of the original
  image can be queried by *"mapping_size"*).
  This attribute is obtained typically from the operator
  [`xyz_to_object_model_3d`](xyz_to_object_model_3d.md).
- ***"mapping_col"*:** —

  The column-components of the 2D mapping of the set of 3D points.
  (length can be queried by *"num_points"*, width of the original
  image can be queried by *"mapping_size"*).
  This attribute is obtained typically from the operator
  [`xyz_to_object_model_3d`](xyz_to_object_model_3d.md).
- ***"mapping_size"*:** —

  The size of the original image.
  A tuple with the two entries width and height is returned.
- ***"triangles"*:** —

  The indices of the 3D points that represent triangles in the
  following order: The first three values (return values
  0,1,2) represent the first triangle. The next three
  values (return values 3,4,5) represent the second triangle etc.
  All indices correspond to the coordinates of the 3D points. Access to
  the coordinates of the 3D points is possible, e.g., with the generic
  parameter *`gen_param_name`* set to the values *"point_coord_x"*,
  *"point_coord_y"*, and *"point_coord_z"*, respectively.
  The length of this attribute corresponds to three times the number of
  triangles, which can be queried using *"num_triangles"*.
  This attribute is obtained typically from the operator
  [`triangulate_object_model_3d`](triangulate_object_model_3d.md) or [`read_object_model_3d`](read_object_model_3d.md).
- ***"polygons"*:** —

  The indices of the 3D points that represent polygons in the following
  order: The first return value contains the number n of the points
  of the first
  polygon. The following values (return values 1,2,..,n)
  represent the indices of the points of the first polygon.
  The next value
  (return value n+1) contains the number m of the points of the
  second polygon.
  The following m return values (return values n+2,n+3,..,n+1+m)
  represent the indices of the points of the second polygon etc.
  All indices
  correspond to the coordinates of the 3D points. Access to the
  coordinates of the 3D points is possible, e.g., with the generic
  parameter *`gen_param_name`* set to the values *"point_coord_x"*,
  *"point_coord_y"*, and *"point_coord_z"*, respectively.
  The number of polygons per 3D object model can be queried using
  *"num_polygons"*.
  This attribute is obtained typically from the operator
  [`read_object_model_3d`](read_object_model_3d.md).
- ***"lines"*:** —

  The indices of the 3D points that represent polylines in the following
  order: The first return value contains the number n of points of the
  first polyline. The following values (return values 1,2,..,n)
  represent the indices of the points of the first polyline.
  The next value
  (return value n+1) contains the number m of points of the second
  polyline. The following m values
  (return values n+2,n+3,..,n+1+m)
  represent the indices of the points of the second polyline etc.
  All indices
  correspond to the coordinates of the 3D points. Access to the
  coordinates of the 3D points is possible, e.g., with the generic
  parameter *`gen_param_name`* set to the values *"point_coord_x"*,
  *"point_coord_y"*, and *"point_coord_z"*, respectively.
  The number of lines per 3D object model can be queried using
  *"num_lines"*.
  This attribute is obtained typically from the operator
  [`intersect_plane_object_model_3d`](intersect_plane_object_model_3d.md).
- ***"diameter_axis_aligned_bounding_box"*:** —

  The diameter of the set of 3D points, defined as the length of
  the diagonal of the smallest enclosing axis-parallel cuboid
  (see parameter *"bounding_box1"*). This attribute has length 1.
- ***"center"*:** —

  3D coordinates of the center of the set of 3D points. These
  coordinates are the center of the smallest enclosing
  axis-parallel cuboid (see parameter *"bounding_box1"*).
  This attribute has length 3. If there are no 3D coordinates
  in the 3D object model the following rules are valid:

  If the 3D object model is a primitive of type cylinder
  (see [`gen_cylinder_object_model_3d`](gen_cylinder_object_model_3d.md)) and there are extensions,
  the center point between the extensions are returned. If there
  are no extensions the translation parameters of the pose are returned.

  If the 3D object model is a primitive of type plane
  (see [`gen_plane_object_model_3d`](gen_plane_object_model_3d.md)) and there are extensions,
  the center of gravity of the plane is computed from the extensions.
  If there are no extensions the translation parameters of the pose
  are returned.

  If the 3D object model is a primitive of type sphere or box
  (see [`gen_sphere_object_model_3d`](gen_sphere_object_model_3d.md) or
  [`gen_box_object_model_3d`](gen_box_object_model_3d.md)),
  the center point of the object model is returned.
- ***"primitive_type"*:** —

  The primitive type (e.g., obtained from the operator
  [`fit_primitives_object_model_3d`](fit_primitives_object_model_3d.md)).
  The return value of a sphere is *"sphere"*.
  The return value of a cylinder is *"cylinder"*.
  The return value of a plane is *"plane"*.
  The return value of a box is *"box"*.
  This attribute has length 1.
- ***"primitive_parameter"*:** —

  The parameters of the primitive (e.g., obtained from the operator
  [`fit_primitives_object_model_3d`](fit_primitives_object_model_3d.md)). The length of this attribute
  depends on *"primitive_type"* and is between 4 and 10 for
  each 3D object model.

  If the 3D object model is a primitive of type cylinder
  (see [`gen_cylinder_object_model_3d`](gen_cylinder_object_model_3d.md)),
  the return values are the
  (x-, y-, z-)coordinates of the center [`x_center`,
  `y_center`, `z_center`],
  the normed (x-, y-, z-)directions of the main axis of the cylinder
  [`x_axis`, `y_axis`, `z_axis`], and the radius
  [`radius`] of the cylinder.
  The order is [`x_center`, `y_center`, `z_center`,
  `x_axis`, `y_axis`, `z_axis`, `radius`].

  If the 3D object model is a primitive of type sphere
  (see [`gen_sphere_object_model_3d`](gen_sphere_object_model_3d.md)), the return values
  are the (x-, y-, z-)coordinates of the center [`x_center`,
  `y_center`, `z_center`] and the radius [`radius`]
  of the sphere. The order is [`x_center`, `y_center`,
  `z_center`, `radius`].

  If the 3D object model is a primitive of type
  plane (see [`gen_plane_object_model_3d`](gen_plane_object_model_3d.md)),
  the 4 parameters of the hessian normal form are returned,
  i.e., the unit normal (x-, y-, z-) vector [`x`, `y`,
  `z`] and the orthogonal distance (d) of the plane from
  the origin of the coordinate system. The order is [`x`,
  `y`, `z`, `d`]. The sign of the
  distance (`d`) determines the side of the plane on which the
  origin is located.

  If the 3D object model is a primitive of type box
  ([`gen_box_object_model_3d`](gen_box_object_model_3d.md)), the return values
  are the 3D pose (translation, rotation, type of the rotation) and
  the half edge lengths (`length1`, `length2`,
  `length3`) of the box.
  `length1` is the length of the box along the x axis of the pose.
  `length2` is the length of the box along the y axis of the pose.
  `length3` is the length of the box along the z axis of the pose.
  The order is [`trans_x`, `trans_y`, `trans_z`,
  `rot_x`, `rot_y`, `rot_z`,
  `rot_type`, `length1`, `length2`, `length3`].
  For details about 3D poses and the corresponding transformation matrices
  see the operator [`create_pose`](create_pose.md).
- ***"primitive_parameter_pose"*:** —

  The parameters of the primitive with format of a 3D pose (e.g.,
  obtained from the operator [`fit_primitives_object_model_3d`](fit_primitives_object_model_3d.md)).
  For all types of primitives the return values are the 3D pose
  (translation, rotation, type of the rotation). For details
  about 3D poses and the corresponding transformation matrices
  see the operator [`create_pose`](create_pose.md). The length of this attribute
  depends on *"primitive_type"* and is between 7 and 10 for
  each 3D object model.

  If the 3D object model is a primitive of type cylinder
  (see [`gen_cylinder_object_model_3d`](gen_cylinder_object_model_3d.md)), additionally, the radius
  [`radius`] of the cylinder is returned. The order is
  [`trans_x`, `trans_y`, `trans_z`, `rot_x`,
  `rot_y`, `rot_z`, `rot_type`, `radius`].

  If the 3D object model is a primitive of type sphere
  (see [`gen_sphere_object_model_3d`](gen_sphere_object_model_3d.md)), additionally, the radius
  [`radius`] of the sphere is returned. The order is
  [`trans_x`, `trans_y`, `trans_z`, `rot_x`,
  `rot_y`, `rot_z`, `rot_type`, `radius`].

  If the 3D object model is a primitive of type plane
  (see [`gen_plane_object_model_3d`](gen_plane_object_model_3d.md)), the order is [`trans_x`,
  `trans_y`, `trans_z`, `rot_x`, `rot_y`,
  `rot_z`, `rot_type`].

  If the 3D object model is a primitive of type box
  (see [`gen_box_object_model_3d`](gen_box_object_model_3d.md)), additionally the half
  edge lengths (`length1`, `length2`, `length3`) of the
  box are returned.
  `length1` is the length of the box along the x axis of the pose.
  `length2` is the length of the box along the y axis of the pose.
  `length3` is the length of the box along the z axis of the pose.
  The order is [`trans_x`, `trans_y`, `trans_z`,
  `rot_x`, `rot_y`, `rot_z`,
  `rot_type`, `length1`, `length2`, `length3`].
- ***"primitive_pose"*:** —

  The parameters of the primitive with format of a 3D pose (e.g.,
  obtained from the operator [`fit_primitives_object_model_3d`](fit_primitives_object_model_3d.md)).
  For all types of primitives the return values are the 3D pose
  (translation, rotation, type of the rotation). For details
  about 3D poses and the corresponding transformation matrices
  see the operator [`create_pose`](create_pose.md). The length of this attribute
  is 7 for each 3D object model. The order is
  [`trans_x`, `trans_y`, `trans_z`, `rot_x`,
  `rot_y`, `rot_z`, `rot_type`].
- ***"primitive_parameter_extension"*:** —

  The extents of the primitive of type cylinder and plane (e.g.,
  obtained from the operator [`fit_primitives_object_model_3d`](fit_primitives_object_model_3d.md)).
  The length of this attribute depends on *"primitive_type"*
  and can be queried using
  *"num_primitive_parameter_extension"*.

  If the 3D object model is a primitive of type cylinder
  (see [`gen_cylinder_object_model_3d`](gen_cylinder_object_model_3d.md)), the return values are
  the extents (MinExtent, MaxExtent) of the cylinder.
  They are returned in the order [MinExtent, MaxExtent]. MinExtent
  represents the length of the cylinder in negative direction of the
  rotation axis. MaxExtent represents the length of the cylinder in
  positive direction of the rotation axis.

  If the 3D object model is a primitive of type plane
  (created using [`fit_primitives_object_model_3d`](fit_primitives_object_model_3d.md)),
  the return value is a tuple
  of co-planar points regarding the fitted plane. The order is
  [x coordinate of point 1, x coordinate of point 2,
  x coordinate of point 3, ....,
  y coordinate of point 1, y coordinate of point 2,
  y coordinate of point 3, ....].
  The coordinate values describe the support points of a convex hull.
  This is computed based on the projections of those points on the fitted
  plane which contribute to the fitting.
  If the plane was created using [`gen_plane_object_model_3d`](gen_plane_object_model_3d.md), all
  points that were used to create the plane (XExtent, YExtent) are returned.
- ***"primitive_rms"*:** —

  The quadratic residual error of the primitive (e.g., obtained from
  the operator [`fit_primitives_object_model_3d`](fit_primitives_object_model_3d.md)). This attribute
  has length 1.
- ***"reference_point"*:** —

  3D coordinates of the reference point of the prepared
  3D shape model for shape-based 3D matching. The reference
  point is the center of the smallest enclosing axis-parallel
  cuboid (see parameter *"bounding_box1"*). This attribute has
  length 3.
- ***"bounding_box1"*:** —

  Smallest enclosing axis-parallel cuboid
  (min_x, min_y, min_z, max_x, max_y, max_z). This attribute has length 6.
- ***"num_points"*:** —

  The number of points.
  This attribute has length 1.
- ***"num_triangles"*:** —

  The number of triangles.
  This attribute has length 1.
- ***"num_polygons"*:** —

  The number of polygons.
  This attribute has length 1.
- ***"num_lines"*:** —

  The number of polylines.
  This attribute has length 1.
- ***"num_primitive_parameter_extension"*:** —

  The number of extended data of primitives.
  This attribute has length 1.
- ***"has_points"*:** —

  The existence of 3D points.
  This attribute has length 1.
- ***"has_point_normals"*:** —

  The existence of 3D point normals.
  This attribute has length 1.
- ***"has_triangles"*:** —

  The existence of triangles.
  This attribute has length 1.
- ***"has_polygons"*:** —

  The existence of polygons.
  This attribute has length 1.
- ***"has_lines"*:** —

  The existence of lines.
  This attribute has length 1.
- ***"has_xyz_mapping"*:** —

  The existence of a mapping of the 3D points to image
  coordinates. This attribute has length 1.
- ***"has_shape_based_matching_3d_data"*:** —

  The existence of a shape model for shape-based 3D matching.
  This attribute has length 1.
- ***"has_distance_computation_data"*:** —

  The existence of a precomputed data structure for 3D distance
  computation.
  This attribute has length 1.
  The data structure can be created with [`prepare_object_model_3d`](prepare_object_model_3d.md)
  using the purpose *"distance_computation"*.
  It is used by the operator [`distance_object_model_3d`](distance_object_model_3d.md).
- ***"has_surface_based_matching_data"*:** —

  The existence of data for the surface-based matching.
  This attribute has length 1.
- ***"has_segmentation_data"*:** —

  The existence of data for a 3D segmentation.
  This attribute has length 1.
- ***"has_primitive_data"*:** —

  The existence of a primitive.
  This attribute has length 1.
- ***"has_primitive_rms"*:** —

  The existence of a quadratic residual error of a primitive.
  This attribute has length 1.
- ***"neighbor_distance"*:** —
- ***"neighbor_distance N"*:** —

  For every point the distance of the N-th nearest point.
  N must be a positive integer and is by default 25.
  For every point, all other points are sorted according to their distance
  and the distance of the N-th point is returned.
- ***"num_neighbors X"*:** —

  For every point the number of neighbors within a distance of at most X.
- ***"num_neighbors_fast X"*:** —

  For every point the approximate number of neighbors within a distance of
  at most X. The distances are approximated using voxels, leading to a
  faster processing compared to *"num_neighbors"*.

### Extended attributes

Extended attributes are attributes, that can be derived from standard
attributes by special operators (e.g., [`distance_object_model_3d`](distance_object_model_3d.md)),
or user-defined attributes.
User-defined attributes can be created by
the operator [`set_object_model_3d_attrib`](set_object_model_3d_attrib.md).
The following extended attributes and meta data can be accessed:

- ***"extended_attribute_names"*:** —

  The names of all extended attributes.
  For each extended attribute name a value is returned.
- ***"extended_attribute_types"*:** —

  The type of all extended attributes.
  For each extended attribute type a value is returned,
  thereby the values are sorted as the output for the extended attribute
  names.
- ***"has_extended_attribute"*:** —

  The existence of at least one extended attribute.
  For each 3D object model a value is returned.
- ***"num_extended_attribute"*:** —

  The number of extended attributes.
  For each 3D object model a value is returned.
- ***"&attribute_name"*:** —

  The values stored under a user-defined extended attribute. Note that this
  name must start with *'&'*, e.g., *"&my_attrib"*.
  The data of the requested extended attributes are returned in
  *`gen_param_value`*. The order in which the data is returned is
  the same as the order of the attribute names specified in
  *`gen_param_name`*.
- ***"original_point_indices"*:** —

  Indices of the 3D points in a different 3D object model
  (length can be queried by *"num_points"*).
  This attribute is obtained typically from the operator
  [`triangulate_object_model_3d`](triangulate_object_model_3d.md).
- ***"score"*:** —

  The score of the set of the 3D points (length can be queried by
  *"num_points"*).
  This attribute is obtained typically from the operator
  [`reconstruct_surface_stereo`](reconstruct_surface_stereo.md).
- ***"red"*:** —

  The red channel of the set of the 3D points
  (length can be queried by *"num_points"*).
  This attribute is obtained typically from the operator
  [`reconstruct_surface_stereo`](reconstruct_surface_stereo.md).
- ***"green"*:** —

  The green channel of the set of the 3D points
  (length can be queried by *"num_points"*).
  This attribute is obtained typically from the operator
  [`reconstruct_surface_stereo`](reconstruct_surface_stereo.md).
- ***"blue"*:** —

  The blue channel of the set of the 3D points
  (length can be queried by *"num_points"*).
  This attribute is obtained typically from the operator
  [`reconstruct_surface_stereo`](reconstruct_surface_stereo.md).
- ***"edge_dir_x"*:** —

  The x-component of a vector that is perpendicular to the
  edge direction and the viewing direction.
  This attribute is obtained typically from the operator
  [`edges_object_model_3d`](edges_object_model_3d.md)
- ***"edge_dir_y"*:** —

  The y-component of a vector that is perpendicular to the
  edge direction and the viewing direction.
  This attribute is obtained typically from the operator
  [`edges_object_model_3d`](edges_object_model_3d.md)
- ***"edge_dir_z"*:** —

  The z-component of a vector that is perpendicular to the
  edge direction and the viewing direction.
  This attribute is obtained typically from the operator
  [`edges_object_model_3d`](edges_object_model_3d.md)
- ***"edge_amplitude"*:** —

  Contains the amplitude of edge points.
  This attribute is obtained typically from the operator
  [`edges_object_model_3d`](edges_object_model_3d.md)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`object_model_3d`** (input_control)  object_model_3d(-array) `→` MaybeSequence[HHandle]

Handle of the 3D object model.

**`gen_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

Names of the generic attributes that
are queried for the 3D object model.

Default:
"num_points"

List of values:
"blue", "bounding_box1", "center", "diameter_axis_aligned_bounding_box", "edge_amplitude", "edge_dir_x", "edge_dir_y", "edge_dir_z", "extended_attribute_names", "extended_attribute_types", "green", "has_distance_computation_data", "has_extended_attribute", "has_lines", "has_point_normals", "has_points", "has_polygons", "has_primitive_data", "has_primitive_rms", "has_segmentation_data", "has_shape_based_matching_3d_data", "has_surface_based_matching_data", "has_triangles", "has_xyz_mapping", "lines", "mapping_col", "mapping_row", "mapping_size", "neighbor_distance", "num_extended_attribute", "num_lines", "num_neighbors", "num_neighbors_fast", "num_points", "num_polygons", "num_primitive_parameter_extension", "num_triangles", "original_point_indices", "point_coord_x", "point_coord_y", "point_coord_z", "point_normal_x", "point_normal_y", "point_normal_z", "polygons", "primitive_parameter", "primitive_parameter_extension", "primitive_parameter_pose", "primitive_pose", "primitive_rms", "primitive_type", "red", "reference_point", "score", "triangles"

**`gen_param_value`** (output_control)  attribute.value(-array) `→` Sequence[Union[int, str, float]]

Values of the generic parameters.

## Result

The operator `get_object_model_3d_params` returns the value
2 (
H_MSG_TRUE)
if the given parameters are correct. Otherwise, an exception
will be raised.

## Possible Predecessors

`read_object_model_3d`,
`xyz_to_object_model_3d`,
`prepare_object_model_3d`,
`sample_object_model_3d`,
`triangulate_object_model_3d`,
`intersect_plane_object_model_3d`,
`set_object_model_3d_attrib`,
`fit_primitives_object_model_3d`,
`gen_plane_object_model_3d`,
`gen_sphere_object_model_3d`,
`gen_cylinder_object_model_3d`,
`gen_box_object_model_3d`,
`gen_sphere_object_model_3d_center`

## Possible Successors

`select_object_model_3d`,
`write_object_model_3d`,
`clear_object_model_3d`

## Module

3D Metrology
