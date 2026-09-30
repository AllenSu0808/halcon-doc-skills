# SetStereoModelParam (Operator)

## Name

`SetStereoModelParam` — Set stereo model parameters.

## Signature

`static void HOperatorSet.SetStereoModelParam(HTuple stereoModelID, HTuple genParamName, HTuple genParamValue)`

`void HStereoModel.SetStereoModelParam(HTuple genParamName, HTuple genParamValue)`

`void HStereoModel.SetStereoModelParam(string genParamName, HTuple genParamValue)`

## Description

The operator `SetStereoModelParam` can be used to set diverse
parameters for the stereo model *`stereoModelID`*.
Several types of parameters can be set with this operator depending on
type of the stereo model which was specified in [`CreateStereoModel`](create_stereo_model.md).
Note that no specific parameters are provided for *"points_3d"*.

### General parameters:

By setting *`genParamName`* to one of the following values,
general stereo model parameters can be set to the value passed in
*`genParamValue`*:

- ***"bounding_box"*:** —

  A tuple `[x1,y1,z1,x2,y2,z2]` specifying two opposite corner
  points `P1=[x1,y1,z1]` and `P2=[x2,y2,z2]` of a
  bounding box for the reconstructions. The bounding box defines a
  box in the space in the coordinate frame of the camera setup model
  used for the reconstruction (specified by `cameraSetupModelID`
  in [`CreateStereoModel`](create_stereo_model.md)). The reconstruction algorithms then clip
  any resulting reconstruction to this bounding box.

  Furthermore, if the parameters *"min_disparity"* and
  *"max_disparity"* are not set manually by using
  [`CreateStereoModel`](create_stereo_model.md) or `SetStereoModelParam`, the
  operator [`ReconstructSurfaceStereo`](reconstruct_surface_stereo.md) requires a valid bounding
  box for the estimation of the minimal and maximal disparity parameters
  for the pairwise disparity estimation (see
  [`SetStereoModelImagePairs`](set_stereo_model_image_pairs.md) for more details).

  Note that the values of parameters for the fusion of surfaces are reset
  to default values each time the bounding box is reset.

  You can use the procedure
  `estimate_bounding_box_3d_reconstruction`
  to get initial values for the bounding box of your 3D reconstruction.
  This bounding box is based on the pose of a reference calibration plate
  and the cones of sight of the cameras. Later, the bounding box should be
  set as tight as possible around the object that is to be to be
  reconstructed.

  Additionally, the procedures `gen_bounding_box_object_model_3d`
  and `gen_camera_setup_object_model_3d` can be used
  to visualize your camera setup.

  For a valid bounding box, `P1` must be the point on the front
  lower left corner and `P2` on the back upper right corner of the
  bounding box, i.e., `x1<x2`, `y1<y2` and `z1<z2`.
  While the surface reconstruction (see [`ReconstructSurfaceStereo`](reconstruct_surface_stereo.md))
  will terminate in the case of an invalid bounding box, the 3D point
  reconstruction algorithm (see [`ReconstructPointsStereo`](reconstruct_points_stereo.md))
  simply ignores it, and it reconstructs all points (it can), without
  clipping them. Thus, you can turn off the result clipping for the 3D
  points reconstruction by passing the tuple `[0,0,0,0,0,-1]`.

  Note that because *"bounding_box"* is a tuple-valued parameter, it
  cannot be set in a single call of `SetStereoModelParam` together
  with other model parameters (see the paragraph "A note on tuple-valued
  model parameters" below).

  *Tuple format:* *[x1,y1,z1,x2,y2,z2]*
- ***"persistence"*:** —

  Enables (*`genParamValue`*=*1*) or disables
  (*`genParamValue`*=*0*) the *"persistence"* mode of the
  stereo model. When in persistence mode, the model stores
  intermediate results of the reconstruction (only for
  [`ReconstructSurfaceStereo`](reconstruct_surface_stereo.md)), which can be inspected later
  by [`GetStereoModelObject`](get_stereo_model_object.md) and
  [`GetStereoModelObjectModel3d`](get_stereo_model_object_model_3d.md).

  Note that the model might need
  significant memory space in this mode. This can worsen the performance
  of the reconstruction algorithms and even lead to running out of
  memory, in particular for setups with many cameras and/or large images.
  Therefore, we recommend to enable this mode only for inspection and
  debugging a reconstruction with small data sets.

  List of values:
   *0* , *1*.

  Default:
   *0*.

### Parameters for the surface reconstruction using 'surface_pairwise' or 'surface_fusion':

By setting *`genParamName`* to one of the following values, additional
parameters specific for surface reconstruction can be set with
*`genParamValue`* for a stereo model of type *"surface_pairwise"*
or *"surface_fusion"*:

- ***"color"*:** —

  By setting this parameter to one of the following values, the coloring
  of the reconstructed 3D object model is either enabled or disabled
  (*"none"*). See [`ReconstructSurfaceStereo`](reconstruct_surface_stereo.md) on how to
  access the resulting color information.

  - ***"median"*** —

    The color value of a 3D point is the median of the color values of
    all cameras where the 3D point is visible.
  - ***"smallest_distance"*** —

    The color value of a 3D point corresponds to the color value of the
    camera that exhibits the smallest distance to this 3D point.
  - ***"mean_weighted_distances"*** —

    All cameras that contribute to the reconstruction of a 3D point are
    weighted according to their distance to the 3D point. Cameras with a
    smaller distance receive a higher weight, whereas cameras with a
    larger distance get a lower weight.
    The color value of a 3D point is then computed by averaging the
    weighted color values of the cameras.
  - ***"line_of_sight"*** —

    The color value of a 3D point corresponds to the color value of the
    camera that exhibits the smallest angle between the point normal and
    the line of sight.
  - ***"mean_weighted_lines_of_sight"*** —

    All cameras that contribute to the reconstruction of a 3D point are
    weighted according to their angle between the point normal and the
    line of sight. Cameras with a smaller angle receive a higher weight.
    The color value of a 3D point is then computed by averaging the
    weighted color values of the cameras.

  List of values:
   *"none"*,
  *"smallest_distance"*,
  *"mean_weighted_distances"*,
  *"line_of_sight"*,
  *"mean_weighted_lines_of_sight"*,
  *"median"*.

  Default:
   *"none"*.
- ***"color_invisible"*:** —

  If stereo models of type *"surface_fusion"* are used, the
  reconstruction will contain points without a direct correspondence to
  points in the images. These points are not seen by any of the cameras of
  the stereo
  system and are therefore "invisible". A color value for these points has
  to be calculated using the color of points in the vicinity. Coloring these
  "invisible" points can be switched off by setting
  this parameter to *"false"*. In this case invisible points are
  assigned 255 as gray value.
  Normally, coloring of "invisible" points is not very time-consuming and can
  remain active. However, it may happen that the value for the parameter
  *"resolution"* is considerably finer than the available image
  resolution.
  In this case, many invisible 3D points are reconstructed making the nearest
  neighbor search very time consuming. In order to avoid an increased
  runtime, it is recommended to either adapt the value of
  *"resolution"* or to switch off the calculation for invisible
  points.
  Please note that for stereo models of type *"surface_pairwise"*,
  this parameter will not have any effect.

  List of values:
   *"true"*, *"false"*.

  Default:
   *"true"*.
- ***"rectif_interpolation"*:** —

  Interpolation mode for the rectification maps (see
  [`SetStereoModelImagePairs`](set_stereo_model_image_pairs.md)). Note that after changing this
  parameter, you must call [`SetStereoModelImagePairs`](set_stereo_model_image_pairs.md) again
  for the changes to take effect.

  List of values:
   *"none"*, *"bilinear"*.

  Default:
   *"bilinear"*.
- ***"rectif_sub_sampling"*:** —

  Sub-sampling factor for the rectification maps (see
  [`SetStereoModelImagePairs`](set_stereo_model_image_pairs.md)). Note that after changing this
  parameter, you must call [`SetStereoModelImagePairs`](set_stereo_model_image_pairs.md) again
  for the changes to take effect.

  Suggested values:
   *0.5*, *0.66*, *1.0*,
  *1.5*, *2.0*, *3.0*,
  *4.0*.

  Default:
   *1.0*.
- ***"rectif_method"*:** —

  Rectification method for the rectification maps (see
  [`SetStereoModelImagePairs`](set_stereo_model_image_pairs.md)). Note that after changing this
  parameter, you must call [`SetStereoModelImagePairs`](set_stereo_model_image_pairs.md) again
  for the changes to take effect.

  List of values:
   *"viewing_direction"*,
  *"geometric"*.

  Default:
   *"viewing_direction"*.
- ***"disparity_method"*:** —

  Method used to create disparity images from
  the image pairs (see [`ReconstructSurfaceStereo`](reconstruct_surface_stereo.md)). Currently,
  the three methods *"binocular"*, *"binocular_mg"* and
  *"binocular_ms"* are supported. Dependent on the chosen method,
  the HALCON operator [`BinocularDisparity`](binocular_disparity.md),
  [`BinocularDisparityMg`](binocular_disparity_mg.md) or [`BinocularDisparityMs`](binocular_disparity_ms.md) is
  called internally.

  List of values:
   *"binocular"*, *"binocular_mg"*,
  *"binocular_ms"*.

  Default:
   *"binocular"*.
- ***"min_disparity"*, *"max_disparity"*:** —

  Minimum and maximum disparity values that are used in the
  operator [`ReconstructSurfaceStereo`](reconstruct_surface_stereo.md).
  The number of minimum and maximum disparity values
  must correspond to the number of image pairs.
  If *"min_disparity"* and *"max_disparity"*
  are not set by the operator `SetStereoModelParam`,
  the disparity values are estimated internally by using the underlying
  bounding box.

  Note that because *"min_disparity"* and *"max_disparity"*
  are tuple-valued parameters, they cannot be set in a single call of
  `SetStereoModelParam` together with other model parameters
  (see the paragraph "A note on tuple-valued model parameters" below).
- ***"binocular_score_thresh"*:** —

  For the methods *"binocular_mg"* and *"binocular_ms"* the
  disparities that have a score above the passed threshold
  are excluded from further processing steps and do not end up in the
  reconstructed 3D point cloud.
  For the method *"binocular"* the disparities below the passed
  threshold are excluded.

  - **For stereo models with the method *"binocular"*:** —

    List of values:
     positive and negative integer or float value.

    Default:
     *0.5*.
  - **For stereo models with the method *"binocular_mg"* or
    *"binocular_ms"*:** —

    List of values:
     integer or float value greater or equal
    to 0.0.

    Default:
     *-1*.

  Depending on the selected disparity method, a set of different
  parameters is available for the user. These parameters allow a fine
  tuning to the used data set. More information about the parameters can
  be found in the respective operator reference of
  [`BinocularDisparity`](binocular_disparity.md), [`BinocularDisparityMg`](binocular_disparity_mg.md) or
  [`BinocularDisparityMs`](binocular_disparity_ms.md).

  - **Set of parameters for stereo models with method =
    *"binocular"*** —
    - ***"binocular_method"*:** —

      Sets the desired matching method.

      List of values:
       *"ncc"*, *"sad"*,
      *"ssd"*.

      Default:
       *"ncc"*.
    - ***"binocular_num_levels"*:** —

      Number of used image pyramids.
      List of values:
       integer value greater or equal to 1.

      Default:
       *1*.
    - ***"binocular_mask_width"*:** —

      Width of the correlation window.

      List of values:
       Odd integer value greater or equal to 3.

      Default:
       *11*.
    - ***"binocular_mask_height"*:** —

      Height of the correlation window.

      List of values:
       Odd integer value greater or equal to 3.

      Default:
       *11*.
    - ***"binocular_texture_thresh"*:** —

      Variance threshold of textured image regions.

      List of values:
       integer or float value greater or equal to
      0.0.

      Default:
       *0.0*.
    - ***"binocular_filter"*:** —

      Downstream filters.

      List of values:
       *"none"*,
      *"left_right_check"*.

      Default:
       *"none"*.
    - ***"binocular_sub_disparity"*:** —

      Subpixel interpolation of disparities.

      List of values:
       *"none"*, *"interpolation"*.

      Default:
       *"none"*.
  - **Set of parameters for stereo models with method =
    *"binocular_mg"*** —
    - ***"binocular_mg_gray_constancy"*:** —

      Weight of the gray value constancy in the data term.

      List of values:
       integer or float value greater or equal to
      *0.0*.

      Default:
       *1.0*.
    - ***"binocular_mg_gradient_constancy"*:** —

      Weight of the gradient constancy in the data term.

      List of values:
       integer or float value greater or equal to
      *0.0*.

      Default:
       *30.0*.
    - ***"binocular_mg_smoothness"*:** —

      Weight of the smoothness term in relation to the data term.

      List of values:
       integer or float value greater *0.0*.

      Default:
       *5.0*.
    - ***"binocular_mg_initial_guess"*:** —

      Initial guess of the disparity.

      List of values:
       integer or float value.

      Default:
       *0.0*.

  The subsequent parameters control the behavior of the used multigrid
  method.

  - ***"binocular_mg_default_parameters"*:** —

    Sets predefined values for the following parameters of the used
    multigrid method:
    *"binocular_mg_solver"*, *"binocular_mg_cycle_type"*,
    *"binocular_mg_pre_relax"*,
    *"binocular_mg_post_relax"*,
    *"binocular_mg_initial_level"*,
    *"binocular_mg_iterations"*,
    *"binocular_mg_pyramid_factor"*. The exact values of these
    parameters can be found in the operator reference of
    [`BinocularDisparityMg`](binocular_disparity_mg.md).

    List of values:
     *"very_accurate"*, *"accurate"*,
    *"fast_accurate"*, *"fast"*.

    Default:
     *"fast_accurate"*.
  - ***"binocular_mg_solver"*:** —

    Solver for the linear system.

    List of values:
     *"multigrid"*,
    *"full_multigrid"*,
    *"gauss_seidel"*.

    Default:
     *"full_multigrid"*.
  - ***"binocular_mg_cycle_type"*:** —

    Selects the type of recursion for the multigrid solvers.

    List of values:
     *"v"*,*"w"*,
    *"none"*.

    Default:
     *"v"*.
  - ***"binocular_mg_pre_relax"*:** —

    Sets the number of iterations of the pre-relaxation step in
    multigrid solvers, or the number of iterations for the Gauss-Seidel
    solver, depending on which is selected.

    List of values:
     integer or float value greater *0.0*.

    Default:
     *1*.
  - ***"binocular_mg_post_relax"*:** —

    Sets the number of iterations of the post-relaxation step.

    List of values:
     integer or float value.

    Default:
     *1*.
  - ***"binocular_mg_initial_level"*:** —

    Sets the coarsest level of the image pyramid where the coarse-to-fine
    process starts.

    List of values:
     integer value.

    Default:
     *-2*.
  - ***"binocular_mg_iterations"*:** —

    Sets the number of iterations of the fixed point iteration per
    pyramid level.

    List of values:
     integer or float value greater or equal to *0*.

    Default:
     *1*
  - ***"binocular_mg_pyramid_factor"*:** —

    Determines the factor by which the images are scaled when creating
    the image pyramid for the coarse-to-fine process.

    List of values:
     integer or float value between *0.1* and *0.9*.

    Default:
     *0.6*.
  - **Set of parameters for stereo models with method =
    *"binocular_ms"*** —
    - ***"binocular_ms_surface_smoothing"*:** —

      Smoothing of surfaces.

      List of values:
       integer value greater or equal to *0*.

      Default:
       *50*.
    - ***"binocular_ms_edge_smoothing"*:** —

      Smoothing of edges.

      List of values:
       integer value greater or equal to *0*.

      Default:
       *50*.
    - ***"binocular_ms_consistency_check"*:** —

      This parameter increases the robustness of the returned matches
      since the result relies on a concurrent direct and reverse match.

      List of values:
       *"true"*, *"false"*.

      Default:
       *"true"*.
    - ***"binocular_ms_similarity_measure"*:** —

      Sets the method of the similarity measure.

      List of values:
       *"census_dense"*,
      *"census_sparse"*.

      Default:
       *"census_dense"*.
    - ***"binocular_ms_sub_disparity"*:** —

      Enables or disables the sub-pixel refinement of disparities.

      List of values:
       *"true"*, *"false"*.

      Default:
       *"true"*.
- ***"point_meshing"*:** —

  Enables the post-processing step for meshing the reconstructed
  surface points. For a stereo model of type *"surface_pairwise"*,
  a Poisson solver is supported. For a stereo model of type
  *"surface_fusion"*, a meshing of the isosurface is supported
  (see [`ReconstructSurfaceStereo`](reconstruct_surface_stereo.md) for more details).

  List of values:
   *"none"*,
  *"poisson"*, *"isosurface"*.

  Default:
   *"none"*.

  If the Poisson-based meshing is enabled, the following parameters can be
  set:

  - *"poisson_depth"*:
    Depth of the solver octree. More detail (i.e., a higher resolution)
    of the resulting mesh is achieved with deeper trees. However, this
    requires more time and memory.

    Suggested values:
    *6*, *8*, *10*.

    Default:
     *8*.

    Restriction:
     *3* <= *"poisson_depth"* <=
    *12*
  - *"poisson_solver_divide"*:
    Depth of block Gauss-Seidel solver used for solving the Poisson
    equation. At the price of a small time overhead, this parameter
    reduces the memory consumption of the underlying meshing
    algorithm. Proposed values are depths by 0 to 2 smaller compared to
    the main octree depth.

    Suggested values:
     *6*, *8*,
    *10*.

    Default:
     *8*.

    Restriction:
     *3* <= *"poisson_solver_divide"*
    <= *"poisson_depth"*
  - *"poisson_samples_per_node"*:
    Minimum number of points that should fall in a single octree
    leaf. This parameter is used to handle noisy data, e.g., noise-free
    data can be distributed over many leaves, whereas more noisy data
    should be stored in a single leaf to compensate for the noise. As a
    side effect, bigger values of this parameter distribute the data in
    fewer leaves, which results in a smaller octree, which means a speedup
    but possibly less detail of the reconstruction.

    Suggested values:
     *1*, *5*, *10*,
    *30*, *40*.

    Default:
     *30*.

### Parameters only for 'surface_pairwise':

By setting *`genParamName`* to one of the following values, additional
parameters specific for surface reconstruction can be set with
*`genParamValue`* for a stereo model of type *"surface_pairwise"*:

- ***"sub_sampling_step"*:** —

  sub-sampling step for the X, Y and Z image data resulting from
  the pairwise disparity estimation, before this data is used
  in its turn for the surface reconstruction (see
  [`ReconstructSurfaceStereo`](reconstruct_surface_stereo.md)).

  Suggested values:
   *1*, *2*,
  *3*.

  Default:
   *2*.

### Parameters only for 'surface_fusion':

By setting *`genParamName`* to one of the following values, additional
parameters specific for surface reconstruction can be set with
*`genParamValue`* for a stereo model of type *"surface_fusion"*:

- ***"resolution"*:** —

  Distance of neighboring sample points in each coordinate direction in
  discretization of bounding box. *"resolution"* is set in [m].
  See [`ReconstructSurfaceStereo`](reconstruct_surface_stereo.md) for more details.

  Too small values will unnecessarily increase the runtime.
  Too large values will lead to a reconstruction with too few details.
  Per default, it is set to a coarse resolution depending on the bounding
  box. The parameter will be reset if the bounding box is reset.

  *"smoothing"* may need to be adapted when *"resolution"*
  is changed.

  *"surface_tolerance"* should always be a bit larger than
  *"resolution"* in order to avoid effects of discretization.

  Suggested values:
   *0.001*, *0.01*
- ***"surface_tolerance"*:** —

  Specifies how much noise around the input point cloud should be combined
  to a surface. Points in a cone of sight of a camera are considered surely
  outside of the object (in front of the surface) or surely inside the
  object (behind the surface) with respect to the given camera if their
  distance to the initial surface exceeds *"surface_tolerance"*.
  *"surface_tolerance"* is set in [m].
  See [`ReconstructSurfaceStereo`](reconstruct_surface_stereo.md) for more details and a figure.

  Too small values lead to an uneven surface. Too large values smudge
  distinct surfaces into one. Per default, it is set to three times
  *"resolution"*. The parameter will be reset if the bounding box
  is reset.

  *"surface_tolerance"* should always be a bit larger than
  *"resolution"* in order to avoid effects of discretization.
  *"min_thickness"* always has to be larger than or equal
  to *"surface_tolerance"*. If *"min_thickness"*
  is set too small, *"surface_tolerance"* is automatically set to
  the same value as *"min_thickness"*.
  If *"surface_tolerance"* is set too big, an error is
  raised.

  Suggested values:
   *0.003*, *0.03*

  Restriction:
   *"surface_tolerance"* <
  *"min_thickness"*
- ***"min_thickness"*:** —

  Length of considered cone of sight of a camera behind the initial
  surface obtained by pairwise reconstruction. Points behind the surface
  (viewed from the given camera) are only considered to lie inside the
  object if their distance to the initial surface does not exceed
  *"min_thickness"*. *"min_thickness"* is set in [m].
  See [`ReconstructSurfaceStereo`](reconstruct_surface_stereo.md) for more details and a figure.

  If lines of sight are expected to intersect the closed object only once
  (cameras all observe the object head-on from one side), this parameter
  should remain at the very large default setting.

  If lines of sight are expected
  to intersect the object more often (cameras observe the object
  from different sides), only the interior of the object of interest should
  be marked as lying behind the surface. Thus, a first guess for the
  parameter could be less than the thickness of your object.

  The method *"surface_fusion"* will try to produce a closed surface.
  If you observe several distinct objects from only one side, you may want
  to reduce the parameter *"min_thickness"* to restrict the
  depth of reconstructed objects and thus keep them from being smudged into
  one surface. The backside of the objects is not observed and thus its
  reconstruction will probably be incorrect.

  Too small values can result in holes in the reconstructed point cloud or
  double walls. Too large values can result in a distorted point cloud or
  blow up the surface towards the outside of the object (if the surface is
  blown up beyond the bounding box, no points will be reconstructed). Per
  default set to the diameter of the bounding box. The parameter will be
  reset if the bounding box is reset.

  *"min_thickness"* always has to be larger than or equal
  to *"surface_tolerance"*. If *"min_thickness"*
  is set too small, *"surface_tolerance"* is automatically set to
  the same value as *"min_thickness"*.
  If *"surface_tolerance"* is set too big, an error is
  raised.

  Suggested values:
   *0.005*, *0.05*.
- ***"smoothing"*:** —

  The parameter *"smoothing"* determines how important a small total
  variation of the distance function is compared to data fidelity. Thus,
  *"smoothing"* regulates the 'jumpiness' of the resulting surface
  (see [`ReconstructSurfaceStereo`](reconstruct_surface_stereo.md) for more details).

  Note that the actual value of *"smoothing"* for a given data set
  to be visually pleasing has to be found by try and error.
  Too small values lead to integrating many outliers into the surface even
  if the surface then exhibits many jumps. Too large values lead to lost
  fidelity towards the point clouds of pairwise reconstruction (how the
  algorithm views distances to the input point clouds depends heavily on
  *"surface_tolerance"* and *"min_thickness"*).

  The parameter will be reset if the bounding box is reset.
  *"smoothing"* may need to be adapted when *"resolution"*
  is changed.

  Suggested values:
   *15.0*, *1.0*,
  *0.1*.

  Default:
   *1.0*.

All parameters except *"binocular_mg_default_parameters"* can be read
back by [`GetStereoModelParam`](get_stereo_model_param.md).

### A note on tuple-valued model parameters

Most of the stereo model parameters are single-valued. Thus,
you can provide a list (i.e., tuple) of parameter names and a
list (tuple) of values that has the same length as the input tuple.
In contrast, when setting a tuple-valued parameter, you must pass a
tuple of values. When setting such a parameter together with
other parameters, the value-to-parameter-name correspondence is not
obvious anymore. Thus, tuple-valued parameters like
*"bounding_box"*, *"min_disparity"* or *"max_disparity"* should always be set in a separate call to
`SetStereoModelParam`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- stereoModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`stereoModelID`** (input_control, state is modified)  stereo_model `→` [HStereoModel](HStereoModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the stereo model.

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the parameters to be set.

List of values:
"binocular_filter", "binocular_mask_height", "binocular_mask_width", "binocular_method", "binocular_mg_cycle_type", "binocular_mg_default_parameters", "binocular_mg_gradient_constancy", "binocular_mg_gray_constancy", "binocular_mg_initial_guess", "binocular_mg_initial_level", "binocular_mg_iterations", "binocular_mg_post_relax", "binocular_mg_pre_relax", "binocular_mg_pyramid_factor", "binocular_mg_smoothness", "binocular_mg_solver", "binocular_ms_consistency_check", "binocular_ms_edge_smoothing", "binocular_ms_similarity_measure", "binocular_ms_sub_disparity", "binocular_ms_surface_smoothing", "binocular_num_levels", "binocular_score_thresh", "binocular_sub_disparity", "binocular_texture_thresh", "bounding_box", "color", "color_invisible", "disparity_method", "max_disparity", "min_disparity", "min_thickness", "persistence", "point_meshing", "poisson_depth", "poisson_samples_per_node", "poisson_solver_divide", "rectif_interpolation", "rectif_method", "rectif_sub_sampling", "resolution", "smoothing", "sub_sampling_step", "surface_tolerance"

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*double* / int / long / string)

Values of the parameters to be set.

Suggested values:
1, -2, -5, 0, 0.3, 0.5, 0.9, 1, 2, 3, "census_dense", "census_sparse", "binocular", "ncc", "none", "sad", "ssd", "bilinear", "false", "viewing_direction", "geometric", "very_accurate", "accurate", "fast_accurate", "fast", "v", "w", "none", "gauss_seidel", "multigrid", "true", "poisson", "isosurface", "interpolation", "left_right_check", "full_multigrid", "binocular_mg", "binocular_ms", "smallest_distance", "mean_weighted_distances", "line_of_sight", "mean_weighted_lines_of_sight", "median"

## Possible Predecessors

`CreateStereoModel`

## Possible Successors

`ReconstructSurfaceStereo`,
`ReconstructPointsStereo`

## See also

`GetStereoModelParam`,
`SetStereoModelImagePairs`

## Module

3D Metrology
