# find_box_3d (Operator)

## Name

`find_box_3d` — Find boxes in 3D data.

## Signature

`def find_box_3d(object_model_3dscene: HHandle, side_len_1: Sequence[float], side_len_2: Sequence[float], side_len_3: Sequence[float], min_score: Union[float, int], gen_param: HHandle) -> Tuple[Sequence[Union[float, int]], Sequence[float], Sequence[HHandle], HHandle]`

## Description

`find_box_3d` finds boxes in the 3D object model
*`object_model_3dscene`* and returns the pose of a gripping point
*`gripping_pose`*, a 3D object model *`object_model_3dbox`* a score
value *`score`* and a dictionary *`box_information`*, containing
further information about the found boxes, for each found box.

The side lengths of the boxes are passed
in *`side_len_1`*, *`side_len_2`*, and *`side_len_3`*.
Each length consists of a tuple of two values,
indicating the minimum and maximum length of that side.
If only a single face of the box is expected to be visible, or no restriction
should be applied to the remaining box length,
*`side_len_3`* can be set to *-1*.

The parameter *`min_score`* sets the minimum score for boxes to be
returned. Boxes with a score smaller than this value will not be returned.

*`object_model_3dscene`* must contain a XYZ-mapping, like it is, e.g., the
case, when creating it with [`xyz_to_object_model_3d`](xyz_to_object_model_3d.md).

### Typical Workflow

A typical workflow for detecting 3D boxes in 3D data looks as follows:

1. Obtain the 3D data either as XYZ-images, or directly as
   a 3D object model with XYZ-mapping.
2. Remove as much background and clutter that is not part of any box
   from the scene as possible, in order to increase robustness and speed.
   Therefore, e.g., use [`threshold`](threshold.md) and [`reduce_domain`](reduce_domain.md)
   on the XYZ-images before calling [`xyz_to_object_model_3d`](xyz_to_object_model_3d.md).
   Further options are described in the section “Troubleshooting” below.
3. If the 3D data exists in the form of XYZ-images, convert them to
   a 3D object model using [`xyz_to_object_model_3d`](xyz_to_object_model_3d.md).
4. Obtain the approximate box edge lengths that should be found.
   Note that changing those lengths later on might make it necessary
   to also change other parameters, such as *`min_score`*.
5. Call `find_box_3d`, passing the 3D object model with the
   scene and the approximate box edge lengths.
6. Use the procedure `visualize_object_model_3d` to visualize the
   results, if necessary.

### Understanding the Results

The boxes are returned in several ways.

First, the pose of a gripping point is returned in *`gripping_pose`*.
The used side of the box and the z-axis of the gripping pose are set
according to the XYZ-mapping. If only a single side of the box is visible,
the center of the gripping pose is in the center of that side, and its
z-axis is oriented away from the viewing point of the XYZ-mapping.
If multiple sides of the box are visible, the gripping pose lies in the
center of the side that is most parallel to the viewing point of the
XYZ-mapping. The z-axis is again oriented away from the viewing point
of the XYZ-mapping.
The x-axis of the gripping pose is set to the box axis that is roughly
the most aligned with the column direction of the XYZ-mapping. The
y-axis is computed based on the x- and z-axis.

The box is also returned in triangulated form in *`object_model_3dbox`*.
This allows a quick visualization of the results.

For each found box, a score between *0* and *1* is returned
in *`score`*.
The score indicates how well the box and its edges are visible, and how
well the found box matches the specified dimensions.

Finally, additional information about the results is returned in the
dictionary *`box_information`*.
[`get_dict_param`](get_dict_param.md) and [`get_dict_tuple`](get_dict_tuple.md) can be used to obtain
further information about the results.
Also, the HDevelop handle inspect window can be used to inspect
the returned dictionary.

The dictionary *`box_information`* contains the following keys:

- **`results`:** —

  This key references a dictionary containing the found boxes. They are
  sorted according to their score in descending order with ascending integer
  keys starting at `0`.

  Each box result is a dictionary with the following keys:

  - **`box_pose`:** —

    This is the box's pose in the coordinate system of the scene. This pose
    is used for visualizing the found box.
  - **`box_length_x`,
    `box_length_y`,
    `box_length_z`:** —

    The side lengths of the found box corresponding to `box_pose`.
    `box_length_x` and `box_length_y` will always
    contain a positive number. If only a single side of the box is visible,
    `box_length_z` will be set to *0*.
  - **`gripping_pose`:** —

    The same pose as returned in *`gripping_pose`*.
  - **`gripping_length_x`,
    `gripping_length_y`,
    `gripping_length_z`:** —

    The side lengths of the found box corresponding to *`gripping_pose`*.
    `gripping_length_x` and `gripping_length_y` will always
    contain a positive number. If only a single side of the box is visible,
    `gripping_length_z` will be set to *0*.
  - **`score`:** —

    The same score as returned in *`score`*.
  - **`one_side_only`:** —

    Boolean indicating whether only one side of the box is visible
    (*"true"*) or not (*"false"*).
- **`gen_param`:** —

  This is a dictionary with the parameters passed to `find_box_3d`.
  *`side_len_1`*, *`side_len_2`*, and *`side_len_3`* are pooled in
  a tuple with key `lengths`. The key `min_score`
  references *`min_score`*. The other keys are denoted analogously to the
  generic parameters of the dictionary *`gen_param`*.
- **`sampled_edges`:** —

  This is the 3D object model with sampled edges. It contains the viewing
  direction of the edge points as normal vectors.
- **`sampled_edges_direction`:** —

  This is the 3D object model with sampled edges (same as for key
  `sampled_edges`. It contains the edge directions of the edge
  points as normal vectors.
- **`sampled_scene`:** —

  This is the sampled scene in which the boxes are looked for. It can be used
  for visualization or debugging the sampling distance.
- **`sampled_reference_points`:** —

  This is a 3D object model with all points from the 3D scene that were
  used as reference points in the matching process. For each reference
  point, the optimum pose of the box is computed under the assumption that
  the reference point lies on the surface of the box.

### Generic Parameters

Additional parameters can be passed as key/tuple pairs in the dictionary
*`gen_param`* in order to improve the matching process.
The following parameter names serve as keys to their
corresponding tuples (see [`create_dict`](create_dict.md) and [`set_dict_tuple`](set_dict_tuple.md)).

- **`3d_edges`:** —

  Allows to manually set the 3D scene edges.
  The parameter must be a 3D object model handle.
  The edges are usually a result of the operator
  [`edges_object_model_3d`](edges_object_model_3d.md) but can further be filtered in order
  to remove outliers.
  If this parameter is not given, `find_box_3d` will
  internally extract the 3D edges similar to the operator
  [`edges_object_model_3d`](edges_object_model_3d.md).
- **`3d_edge_min_amplitude`:** —

  Sets the minimum amplitude of a discontinuity in order for it to be
  classified as an edge.
  Note that if edges were passed manually with the generic parameter
  `3d_edges`, this parameter is ignored.
  Otherwise, it behaves similar to the parameter `min_amplitude` of
  the operator [`edges_object_model_3d`](edges_object_model_3d.md).

  Restriction:
   `3d_edge_min_amplitude` >= *0*

  Default:
   10% of the smallest box diagonal.
- **`max_gap`:** —

  If no edges are passed with `3d_edges`, the operator will extract
  3D edges internally. The parameter can be used to control
  the edge extraction.

  `max_gap` has the same meaning as in
  [`edges_object_model_3d`](edges_object_model_3d.md).
- **`remove_outer_edges`:** —

  Removes the outermost edges when set to *"true"*. This is for
  example helpful for bin picking applications in order to remove the bin.

  List of values:
   *"false"*, *"true"*

  Default:
   *"false"*
- **`max_num_boxes`:** —

  Limits the number of returned boxes.
  By default, `find_box_3d` will return all detected boxes with a
  score larger than *`min_score`*.
  This parameter can be used to limit the number of boxes respectively.

  Default:
   *0* (return all boxes)
- **`box_type`:** —

  Sets the type of boxes to search for.
  For *"full_box_visible"* only boxes with more than one side visible
  are returned.
  If *"single_side_visible"* is set, boxes with only one visible side
  are searched for. If further box sides are visible nonetheless, they are
  ignored.
  For *"all"* both types are returned.

  List of values:
   *"all"*, *"single_side_visible"*,
  *"full_box_visible"*

  Default:
   *"all"*

### Troubleshooting

- ***Visualizing extracted edges and sampled scene*:** —

  To debug the box detector, some of the internally used data can be
  visualized by obtaining it from the returned dictionary
  *`box_information`*, using [`get_dict_tuple`](get_dict_tuple.md).

  The sampled 3D scene can be extracted with the key
  `sampled_scene`. Finding smaller boxes requires a denser
  sampling and subsequently slows down the box detection.

  The sampled 3D edges can be extracted with the key
  `sampled_edges` and `sampled_edges_directions`.
  Both 3D object models contain the same points, however,
  `sampled_edges` contains the viewing direction of the edge
  points as normal vectors, while `sampled_edges_directions`
  contains the edge directions of the edge points as normal vectors.
  Note that the edge directions should be perpendicular to the edges,
  pointing outwards of the boxes.
- ***Improve performance*:** —

  If `find_box_3d` is taking too long, the following steps
  might help to increase its performance.

  - **Remove more background and clutter**:
    A significant improvement in runtime and detection accuracy can
    usually be achieved by removing as much of the background and
    clutter from the 3D scene as possible.

    The most common approaches for removing unwanted data are:

    - Thresholding the X-, Y- and Z-coordinates, either by
      using [`threshold`](threshold.md) and [`reduce_domain`](reduce_domain.md)
      on the XYZ-images before calling [`xyz_to_object_model_3d`](xyz_to_object_model_3d.md),
      or by using [`select_points_object_model_3d`](select_points_object_model_3d.md) directly
      on the 3D object model that contains the scene.
    - Some sensors return an intensity image along with the 3D data.
      Filters on the intensity image can be used to remove parts of
      the image that contain background.
    - Use background subtraction. If the scene is static, for example,
      if the sensor is mounted in a fixed position over a conveyor belt,
      the XYZ-images of the background can be acquired once without
      any boxes in it. Afterwards, [`sub_image`](sub_image.md) and [`threshold`](threshold.md)
      can be used on the Z-images to select parts of the 3D data
      that are not part of the background.
  - **Increase minimum score**:
    An increased minimum score *`min_score`* might lead to more boxes
    being removed earlier in the detection pipeline.
  - **Increase the smallest possible box**:
    The smaller the smallest possible box side is, the slower
    `find_box_3d` runs.
    For example, if all boxes are usually seen from a single side,
    it might make sense to set *`side_len_3`* to *-1*.
    Additionally, `box_type` can be set to limit the
    type of boxes that are searched.
  - **Manually computing and filtering edges**:
    The edges of the scene can be extracted manually, using
    [`edges_object_model_3d`](edges_object_model_3d.md), and passed to `find_box_3d`
    using the generic parameter `3d_edges` (see above).
    Thus, the manual extraction can be used as a further way of
    filtering the edges.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator supports canceling timeouts and interrupts.

## Parameters

**`object_model_3dscene`** (input_control)  object_model_3d `→` HHandle

Handle of 3D object model where to search the box.

**`side_len_1`** (input_control)  real-array `→` Sequence[float]

Length of the first box side.

**`side_len_2`** (input_control)  real-array `→` Sequence[float]

Length of the second box side.

**`side_len_3`** (input_control)  real-array `→` Sequence[float]

Length of the third box side.

Default:
-1

**`min_score`** (input_control)  real `→` Union[float, int]

Minimum score of the returned boxes.

Default:
0.6

Restriction:
`0 <= MinScore <= 1`

**`gen_param`** (input_control)  dict `→` HHandle

Dictionary for generic parameters.

Default:
[]

**`gripping_pose`** (output_control)  pose(-array) `→` Sequence[Union[float, int]]

Gripping poses of the detected boxes.

**`score`** (output_control)  real-array `→` Sequence[float]

Scores of the detected boxes.

**`object_model_3dbox`** (output_control)  object_model_3d-array `→` Sequence[HHandle]

Detected boxes as triangulated 3D object models.

**`box_information`** (output_control)  dict `→` HHandle

Additional debug information as dictionary.

## Result

If all parameters are valid and no error occurs,
`find_box_3d` returns 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`xyz_to_object_model_3d`

## Possible Successors

`gen_box_object_model_3d`,
`get_dict_tuple`

## Alternatives

`find_surface_model`

## Module

3D Metrology
