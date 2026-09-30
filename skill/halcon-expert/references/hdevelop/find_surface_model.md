# find_surface_model (Operator)

## Name

`find_surface_model` — Find the best matches of a surface model in a 3D scene.

## Signature

`find_surface_model( : : SurfaceModelID, ObjectModel3D, RelSamplingDistance, KeyPointFraction, MinScore, ReturnResultHandle, GenParamName, GenParamValue : Pose, Score, SurfaceMatchingResultID)`

## Description

The operator `find_surface_model` finds the best matches of
the surface model *`SurfaceModelID`* in the 3D scene
*`ObjectModel3D`* and returns their pose in *`Pose`*.

The matching is divided in three steps:

1. `Approximate matching`
2. `Sparse pose refinement`
3. `Dense pose refinement`

These steps are described in more detail in the technical note
`Surface-Based Matching`. The generic parameters used to control these
steps are described in the respective sections below.
The further paragraphs describe the parameters and mention further points to
note.

The matching process and the parameters can be visualized and inspected
using the HDevelop procedure `debug_find_surface_model`.

### Points to Note

Matching the surface model uses points and normals of the 3D scene
*`ObjectModel3D`*.
The scene shall provide one of the following options:

- points and point normals.
- points and a 2D-Mapping, e.g., an XYZ image triple converted with
  [`xyz_to_object_model_3d`](xyz_to_object_model_3d.md).
  In this case the normals are calculated using the 2D-Mapping.
- points only. The normals are estimated based on the 3D neighborhood.
  Note, this option is not recommended, since it generally leads to a
  longer processing time and additionally the computed normals are usually
  less accurate, leading to less accurate results.

It is important for an accurate *`Pose`* that the normals of the scene
and the model point in the same direction (see
*'scene_invert_normals'*).

If the model was trained for edge-supported surface-based matching and
the edge-supported matching has not been turned off via
*'use_3d_edges'*, only the
second combination is possible, i.e., the scene must contain a 2D mapping.

If the model was trained for edge-supported surface-based matching and
the scene contains a mapping, normals contained in the input point
cloud are not used (see *'scene_normal_computation'* below).

Further, for models which were trained for edge-supported surface-based
matching it is necessary that the normal vectors point inwards.

Note that triangles or polygons in the passed scene are ignored.
Instead, only the vertices are used for matching.
It is thus in general not recommended to use this operator on meshed scenes,
such as CAD data.
Instead, such a scene must be sampled beforehand using
[`sample_object_model_3d`](sample_object_model_3d.md) to create points and normals
(e.g., using the method *'fast_compute_normals'*).

When using noisy point clouds, e.g., from time-of-flight cameras, the
generic parameter *'scene_normal_computation'* could be set to
*'mls'* in order to obtain more robust results (see below).

### Parameter Description

*`SurfaceModelID`* is the handle of the surface model.
The model must have been created previously with
[`create_surface_model`](create_surface_model.md) or read in with [`read_surface_model`](read_surface_model.md),
respectively.
Certain surface model parameters influencing the matching can be set using
[`set_surface_model_param`](set_surface_model_param.md), such as
*'pose_restriction_max_angle_diff'* restricting the allowed range
of rotations.

*`ObjectModel3D`* is the handle of the 3D object model containing the
scene in which the matches are searched.
Note that in most cases, it is assumed the scene was observed from a camera
looking along the z-axis. This is important to align the scene normals if
they are re-computed (see *'scene_normal_computation'* below).
In contrast, when the model was trained
for edge-supported surface-based matching and the scene contains a mapping,
normals are automatically aligned consistently.

The parameter *`RelSamplingDistance`* controls the sampling distance
during the step `Approximate matching` and the *`Score`*
calculation during the step `Sparse pose refinement`.
Its value is given relative to the diameter of the surface model.
Decreasing *`RelSamplingDistance`* leads to more sampled points,
and in turn to a more stable but slower matching. Increasing
*`RelSamplingDistance`* reduces the number of sampled scene
points, which leads to a less stable but faster matching.
For an illustration showing different values for
*`RelSamplingDistance`*, please refer to the operator
[`create_surface_model`](create_surface_model.md).
The sampled scene points can be retrieved for a visual inspection
using the operator [`get_surface_matching_result`](get_surface_matching_result.md).
For a robust matching it is recommended that at least 50-100
scene points are sampled for each object instance.

The parameter *`KeyPointFraction`* controls how many
points out of the sampled scene points are selected as key points.
For example, if the value is set to *0.1*, 10% of the sampled
scene points are used as key points.
For stable results it is important that each instance of the object
is covered by several key points.
Increasing *`KeyPointFraction`* means that more key points
are selected from the scene, resulting in a slower but more stable
matching. Decreasing *`KeyPointFraction`* has the inverse effect
and results in a faster but less stable matching.
The operator [`get_surface_matching_result`](get_surface_matching_result.md) can be used to
retrieve the selected key points for visual inspection.

The parameter *`MinScore`* can be used to filter the results.
Only matches with a score exceeding the value of *`MinScore`* are
returned.
If *`MinScore`* is set to zero, all matches are returned.

For edged-supported surface-based matching (see
[`create_surface_model`](create_surface_model.md)) four different sub-scores are determined
(see their explanation below). For surface-based matching models where
view-based score computation is trained (see [`create_surface_model`](create_surface_model.md)),
an additional fifth sub-score is determined.
As a consequence, you can filter the results based on each of them by
passing a tuple with up to five threshold values to *`MinScore`*.
These threshold values are sorted in the order of the scores (see below)
and missing entries are regarded as *0*, meaning no filtering based
on this sub-score.
To find suitable values for the thresholds, the corresponding sub-scores
of found object instances can be obtained using
[`get_surface_matching_result`](get_surface_matching_result.md).
Depending on the settings, not all sub-scores might be available.
The thresholds for unavailable sub-scores are ignored.
The five sub-scores, whose threshold values have to be passed in exactly
this order in *`MinScore`*, are:

1. The overall score as returned in *`Score`* and
   through *'score'* by [`get_surface_matching_result`](get_surface_matching_result.md),
2. the surface fraction of the score, i.e., how much of the object's
   surface was detected in the scene, returned
   through *'score_surface'* by [`get_surface_matching_result`](get_surface_matching_result.md),
3. the 3D edge fraction of the score, i.e., how well the 3D edges of
   the object silhouette are aligned with the 3D edges detected in the scene
   returned through *'score_3d_edges'* by
   [`get_surface_matching_result`](get_surface_matching_result.md),
4. the 2D edge fraction of the score, i.e., how well the
   object silhouette projected into the images aligns with edges
   detected in the images (available only for the operators
   [`find_surface_model_image`](find_surface_model_image.md) and
   [`refine_surface_model_pose_image`](refine_surface_model_pose_image.md)), returned through
   *'score_2d_edges'* by [`get_surface_matching_result`](get_surface_matching_result.md), and
5. the view-based score, i.e., how many model points were detected in the
   scene, in relation to how many of the object points are potentially
   visible from the determined viewpoint, returned through
   *'score_view_based'* by [`get_surface_matching_result`](get_surface_matching_result.md).

The parameter *`ReturnResultHandle`* determines if a
surface matching result handle is returned or not.
If the parameter is set to *'true'*, the handle is returned in
the parameter *`SurfaceMatchingResultID`*.
Additional details of the matching
process can be queried with the operator
[`get_surface_matching_result`](get_surface_matching_result.md) using that handle.

The parameters *`GenParamName`* and *`GenParamValue`* are used
to set generic parameters. Both get a tuple of equal length, where the
tuple passed to *`GenParamName`* contains the names of the
parameters to set, and the tuple passed to *`GenParamValue`* contains
the corresponding values. The possible parameter names and values
are described in the paragraph `The three steps of the matching`.

The output parameter *`Pose`* gives the 3D poses of the found object
instances. For every found instance of the surface model its pose is given
in the scene coordinate system, thus the pose is in the form
$\mathrm{SCS} \; P_{\mathrm{mcs}}$ ![figure](../assets/77484e5f6f2c2646.svg), where
*scs* denote the coordinate system of the scene (which often is
identical with the coordinate system of the sensor, the camera coordinate
system) and *mcs* the model coordinate system (which is a 3D world
coordinate system), see [Transformations / Poses](toc_transformations_poses.md) and
`“Solution Guide III-C - 3D Vision”`.
Thereby, the pose refers to the original coordinate system of the 3D object
model that was passed to [`create_surface_model`](create_surface_model.md).

The output parameter *`Score`* returns a score for each match.
Its value and interpretation differs for the cases distinguished below.

- **With pose refinement**

  For a matching with pose refinement, the score depends on whether
  edge-support was activated:

  - Without edge-support, compute the surface fraction, i.e. the
    approximate fraction of the object's surface that is visible in
    the scene. This is done by counting the number of model points
    that have a corresponding scene point and dividing this number
    either by:

    - the total number of points on the model, if the
      surface-based model is not prepared for view-based score
      computation

      or by:
    - the maximum number of potentially visible model points based
      on the current viewpoint, if the surface-based model is prepared
      for view-based score computation.

    $0\le Score\le1$
  - With edge-support, compute the geometric mean of the surface
    fraction and the edge fraction. The surface fraction is affected
    by whether the surface-based model is prepared for view-based score
    computation or not, as explained above. The edge fraction is the number
    of points from the sampled model edges that are aligned with
    edges of the scene, divided by the maximum number of potentially
    visible points of edges on the model.
    Note that if the edges are extracted from multiple viewpoints, this
    might lead to score greater than 1.

    $0\le Score\le1$
    (if the scene was acquired from one single viewpoint)

    $0\le Score\le N$
    (if the scene was merged from scenes that were acquired from N
    different viewpoints)

  Note that for the computation of the score after the sparse pose
  refinement, the sampled scene points are used. For the
  computation of the score after the dense pose refinement, all scene
  points are used. Therefore, after the dense pose refinement, the
  score values does not depend on the sampling distance of
  the scene.
- **Without pose refinement**

  If only the first step, `Approximate Matching`, out of the three
  steps described in `The three steps of the matching` takes place,
  the possible score value and interpretation only differs whether there is
  edge-support or not:

  - Without edge-support:

    The score is the approximate number of points from the subsampled
    scene that lie on the found object.

    $Score\ge0$
  - With edge-support:

    The score is the approximate number of points from the subsampled
    scene that lie on the found object multiplied with the number of points
    from the sampled scene edges that are aligned with edges of the model.

    $Score\ge0$

The output parameter *`SurfaceMatchingResultID`* returns a handle
for the surface matching result. Using this handle, additional details of
the matching process can be queried with the operator
[`get_surface_matching_result`](get_surface_matching_result.md).
Note, that in order to return the handle, *`ReturnResultHandle`*
has to be set to *'true'*.

### The Three Steps of the Matching

The matching is divided into three steps:

- **1. Approximate matching** —

  The approximate poses of the instances of the surface model in the scene
  are searched.

  The following generic parameters control the approximate matching
  and can be set with *`GenParamName`* and
  *`GenParamValue`*:

  - ***'num_matches'*:** —

    Sets the maximum number of matches that are returned.

    Suggested values:
     *1*, *2*, *5*

    Default:
     *1*

    Restriction:
     *'num_matches'* > *0*
  - ***'max_overlap_dist_rel'*:** —

    For efficiency reasons, the maximum overlap can not be defined
    in 3D. Instead, only the minimum distance between the centers
    of the axis-aligned bounding boxes of two matches can be
    specified with *'max_overlap_dist_rel'*. The value is set
    relative to the diameter of the object. Once an object with a
    high *`Score`* is found, all other matches are suppressed
    if the centers of their bounding boxes lie too close to the
    center of the first object. If the resulting matches must
    not overlap, the value for *'max_overlap_dist_rel'*
    should be set to *1.0*.

    Note that only one of the parameters
    *'max_overlap_dist_rel'* and
    *'max_overlap_dist_abs'* should be set. If both are
    set, only the value of the last modified parameter is used.

    Suggested values:
     *0.1*, *0.5*, *1*

    Default:
     *0.5*

    Restriction:
     *'max_overlap_dist_rel'* >= *0*
  - ***'max_overlap_dist_abs'*:** —

    This parameter has the same effect as the parameter
    *'max_overlap_dist_rel'*. Note that in contrast to
    *'max_overlap_dist_rel'*, the value for
    *'max_overlap_dist_abs'* is set as an absolute value.
    See *'max_overlap_dist_rel'* above, for a description of the
    effect of this parameter.

    Note that only one of the parameters
    *'max_overlap_dist_rel'* and
    *'max_overlap_dist_abs'* should be set. If both are
    set, only the value of the last modified parameter is used.

    Suggested values:
     *1*, *2*, *3*

    Restriction:
     *'max_overlap_dist_abs'* >= *0*
  - ***'scene_normal_computation'*:** —

    This parameter controls the normal computation of the sampled
    scene.

    In the default mode *'fast'*, in most cases normals
    from the 3D scene are used (if it already contains
    normals) or computed based on
    a small neighborhood of points (if not).
    The computed normals $n$ are then oriented such that $n_{z}\ge0$ in case no original
    normals exist.
    This orientation of $n_{z}\ge0$ implies the assumption
    that the scene was observed from a camera looking along the
    z-axis.

    In the default mode *'fast'*, in case the model was trained
    for edge-supported surface-based matching and the scene contains a
    mapping, input normals are not used and normals are always computed
    from the mapping contained in the 3D scene. Further, the computed
    normals are oriented inwards consistently with respect to the mapping.

    In the mode *'mls'*, normals are recomputed based on a larger
    neighborhood and using the more complex but often more accurate
    *'mls'* method.
    A more detailed description of the *'mls'* method can be
    found in the description of the operator
    [`surface_normals_object_model_3d`](surface_normals_object_model_3d.md).
    The *'mls'* mode is intended for noisy data, such as images
    from time-of-flight cameras.
    The recomputed normals are oriented as the normals in mode *'fast'*.

    List of values:
     *'fast'*, *'mls'*

    Default:
     *'fast'*
  - ***'scene_sampling_mode'*:** —

    This parameter determines which method is used to sample the 3D points
    of the scene.
    The default method, *'fast'*, corresponds to the respective
    method from [`sample_object_model_3d`](sample_object_model_3d.md).
    It is not internally parallelized but invariant with respect to
    rigid movements of the scene.
    Alternatively, the method *'voxel'* can be selected,
    which uses a voxel-based approach. This method is
    internally parallelized and therefore especially recommended for larger
    point clouds.
    However, it is not invariant with respect to rigid movements of the
    scene.

    List of values:
     *'fast'*, *'voxel'*

    Default:
     *'fast'*
  - ***'scene_invert_normals'*:** —

    Invert the orientation of the surface normals of the scene.
    The orientation of surface normals of the scene have to match with the
    orientation of the model.
    If both the model and the scene are acquired with the same setup,
    the normals will already point in the same direction.
    If you experience the effect that the
    model is found on the 'outside' of the scene surface, try to set this
    parameter to *'true'*.
    Also, make sure that the normals in the scene all point either
    outward or inward, i.e., are oriented consistently.
    For edge-supported surface-based matching, the normal vectors have to
    point inwards, but typically are automatically generated flipped inwards
    consistently with respect to the mapping.
    The orientation of the normals can be inspected using the procedure
    `debug_find_surface_model`.

    List of values:
     *'false'*, *'true'*

    Default:
     *'false'*
  - ***'3d_edges'*:** —

    Allows to manually set the 3D scene edges for edge-supported
    surface-based matching, i.e. if the surface model was created with
    *'train_3d_edges'* enabled. The parameter must be a 3D object
    model handle.
    The edges are usually a result of the operator
    [`edges_object_model_3d`](edges_object_model_3d.md) but can further be filtered in order
    to remove outliers.
    If this parameter is not given, `find_surface_model` will
    internally extract the edges similar to the operator
    [`edges_object_model_3d`](edges_object_model_3d.md).
  - ***'3d_edge_min_amplitude_rel'*:** —

    Sets the threshold when extracting 3D edges for edge-supported
    surface-based matching, i.e. if the surface model was created with
    *'train_3d_edges'* enabled.
    The threshold is set relative to the diameter of the object.
    Note that if edges were passed manually with the generic parameter
    *'3d_edges'*, this parameter is ignored.
    Otherwise, it behaves identically to the parameter
    `MinAmplitude` of operator [`edges_object_model_3d`](edges_object_model_3d.md).

    Suggested values:
     *0.05*, *0.1*,
    *0.5*

    Default:
     *0.05*

    Restriction:
     *'3d_edge_min_amplitude_rel'* >= *0*
  - ***'3d_edge_min_amplitude_abs'*:** —

    Similar to *'3d_edge_min_amplitude_rel'*, however, the value
    is given as absolute distance and not relative to the object
    diameter.

    Restriction:
     *'3d_edge_min_amplitude_abs'* >= *0*
  - ***'viewpoint'*:** —

    This parameter specifies the viewpoint from which the 3D data is
    seen.
    It is used for surface models
    that are prepared for view-based score computation
    (i.e. with *'train_view_based'* enabled) to get the maximum number
    of potentially visible points of the model based on the current
    viewpoint.
    For this, *`GenParamValue`* must contain a string consisting of
    the three coordinates (x, y, and z) of the viewpoint, separated by
    spaces. The viewpoint is defined in the same coordinate frame as
    *`ObjectModel3D`* and should roughly correspond to the position the
    scene was acquired from.
    A visualization of the viewpoint can be created using the procedure
    `debug_find_surface_model` in order to inspect its position.

    Default:
     *'0 0 0'*
  - ***'max_gap'*:** —

    Gaps in the 3D data are closed, as far as they do not exceed the
    maximum gap size *'max_gap'* [pixels] and the surface model
    was created with *'train_3d_edges'* enabled.
    Larger gaps will contain edges at their boundary, while gaps smaller
    than this value will not.
    This suppresses edges around smaller patches that were not
    reconstructed by the sensor as well as edges at the more
    distant part of a discontinuity.
    For sensors with very large resolutions, the value should be
    increased to avoid spurious edges.
    Note that if edges were passed manually with the generic parameter
    *'3d_edges'*, this parameter is ignored.
    Otherwise, it behaves identically to the parameter
    `GenParamName` of the operator [`edges_object_model_3d`](edges_object_model_3d.md)
    when *'max_gap'* is set.

    The influence of *'max_gap'* can be inspected using the
    procedure `debug_find_surface_model`.

    Default:
     *30*
  - ***'use_3d_edges'*:** —

    Turns the edge-supported matching on or off.
    This can be used to perform matching without 3D edges, even though
    the model was created for edge-supported matching.
    If the model was not created for edge-supported surface-based
    matching, an error is returned.

    List of values:
     *'true'*, *'false'*

    Default:
     *'true'*
- **2. Sparse pose refinement** —

  In this second step, the approximate poses found in the previous step are
  further refined. This increases the accuracy of the poses and the
  significance of the score value.

  The following generic parameters control the sparse pose refinement
  and can be set with *`GenParamName`* and
  *`GenParamValue`*:

  - ***'sparse_pose_refinement'*:** —

    Enables or disables the sparse pose refinement.

    List of values:
     *'true'*, *'false'*

    Default:
     *'true'*
  - ***'pose_ref_use_scene_normals'*:** —

    Enables or disables the usage of scene normals for the pose
    refinement. If this parameter is enabled, and if the scene contains
    point normals, then those normals are used to increase the
    accuracy of the pose refinement.
    For this, the influence of scene points whose normal points in a
    different direction than the model normal is decreased.
    Note that the scene must contain point normals. Otherwise, this
    parameter is ignored.

    List of values:
     *'true'*, *'false'*

    Default:
     *'false'*
  - ***'use_view_based'*:** —

    Turns the view-based score computation for surface-based matching on or
    off. This can be used to perform matching without using the view-based
    score, even though the model was prepared for view-based score
    computation. The influence of *'use_view_based'* on the score is
    explained in the documentation of *`Score`* above.

    If the model was not prepared for view-based score computation,
    an error is returned.

    List of values:
     *'true'*, *'false'*

    Default:
     *'false'*, if *'train_view_based'*
    was disabled when creating the model, otherwise *'true'*.
- **3. Dense pose refinement** —

  Accurately refines the poses found in the previous steps.

  The following generic parameters influence the accuracy and speed of
  the dense pose refinement and can be set with *`GenParamName`*
  and *`GenParamValue`*:

  - ***'dense_pose_refinement'*:** —

    Enables or disables the dense pose refinement.

    List of values:
     *'true'*, *'false'*

    Default:
     *'true'*
  - ***'pose_ref_num_steps'*:** —

    Number of iterations for the dense pose refinement. Increasing the
    number of iteration leads to a more accurate pose at the expense of
    runtime.
    However, once convergence is reached, the accuracy can no longer be
    increased, even if the number of steps is increased.
    Note that this parameter is ignored if the dense pose refinement is
    disabled.

    Suggested values:
     *1*, *3*, *5*,
    *20*

    Default:
     *5*

    Restriction:
     *'pose_ref_num_steps'* > *0*
  - ***'pose_ref_sub_sampling'*:** —

    Set the rate of scene points to be used for the dense pose
    refinement.
    For example, if this value is set to *5*, every 5th point
    from the scene is used for pose refinement. This parameter allows an
    easy trade-off between speed and accuracy of the pose refinement:
    Increasing the value leads to less points being used and in turn
    to a faster but less accurate pose refinement. Decreasing the value
    has the inverse effect.
    Note that this parameter is ignored if the dense pose refinement is
    disabled.

    Suggested values:
     *1*, *2*, *5*,
    *10*

    Default:
     *2*

    Restriction:
     *'pose_ref_sub_sampling'* > *0*
  - ***'pose_ref_dist_threshold_rel'*:** —

    Set the distance threshold for dense pose refinement relative to the
    diameter of the surface model.
    Only scene points that are closer to the object than this distance
    are used for the optimization. Scene points further
    away are ignored.

    Note that only one of the parameters
    *'pose_ref_dist_threshold_rel'*
    and *'pose_ref_dist_threshold_abs'* should be set.
    If both are set, only the value of the last modified parameter is used.
    Note that this parameter is ignored if the dense pose refinement is
    disabled.

    Suggested values:
     *0.03*, *0.05*,
    *0.1*, *0.2*

    Default:
     *0.1*

    Restriction:
     *'pose_ref_dist_threshold_rel'* > *0*
  - ***'pose_ref_dist_threshold_abs'*:** —

    Set the distance threshold for dense pose refinement as an absolute
    value.
    See *'pose_ref_dist_threshold_rel'* for a detailed
    description.

    Note that only one of the parameters
    *'pose_ref_dist_threshold_rel'* and
    *'pose_ref_dist_threshold_abs'* should be set.
    If both are set, only the value of the modified last parameter is used.

    Restriction:
     *'pose_ref_dist_threshold_abs'* > *0*
  - ***'pose_ref_scoring_dist_rel'*:** —

    Set the distance threshold for scoring relative to the
    diameter of the surface model. See the following
    *'pose_ref_scoring_dist_abs'* for a detailed description.

    Note that only one of the parameters
    *'pose_ref_scoring_dist_rel'* and
    *'pose_ref_scoring_dist_abs'* should be set.
    If both are set, only the value of the last modified parameter is used.
    Note that this parameter is ignored if the dense pose refinement is
    disabled.

    Suggested values:
     *0.2*, *0.01*,
    *0.005*, *0.0001*

    Default:
     *0.005*

    Restriction:
     *'pose_ref_scoring_dist_rel'* > *0*
  - ***'pose_ref_scoring_dist_abs'*:** —

    Set the distance threshold for scoring.
    Only scene points that are closer to the object than this distance
    are considered to be 'on the model' when computing the score after
    the pose refinement. All other scene points are considered not to be
    on the model.
    The value should correspond to the amount of noise on the
    coordinates of the scene points.
    Note that this parameter is ignored if the dense pose refinement is
    disabled.

    Note that only one of the parameters
    *'pose_ref_scoring_dist_rel'* and
    *'pose_ref_scoring_dist_abs'* should be set.
    If both are set, only the value of the last modified parameter is used.
  - ***'pose_ref_use_scene_normals'*:** —

    Enables or disables the usage of scene normals for the pose
    refinement.
    This parameter is explained in more details in the section
    `Sparse pose refinement` above.

    List of values:
     *'true'*, *'false'*

    Default:
     *'false'*
  - ***'pose_ref_dist_threshold_edges_rel'*:** —

    Set the distance threshold of edges for dense pose refinement relative
    to the diameter of the surface model.
    Only scene edges that are closer to the object edges than this distance
    are used for the optimization. Scene edges further away are ignored.

    Note that only one of the parameters
    *'pose_ref_dist_threshold_edges_rel'*
    and *'pose_ref_dist_threshold_edges_abs'* should be set.
    If both are set, only the value of the last modified parameter is used.
    Note that this parameter is ignored if the dense pose refinement is
    disabled or if no edge-supported surface-based matching is used.

    Suggested values:
     *0.03*, *0.05*,
    *0.1*, *0.2*

    Default:
     *0.1*

    Restriction:
     *'pose_ref_dist_threshold_edges_rel'* > *0*
  - ***'pose_ref_dist_threshold_edges_abs'*:** —

    Set the distance threshold of edges for dense pose refinement as
    an absolute value.
    See *'pose_ref_dist_threshold_edges_rel'* for a detailed
    description.

    Note that only one of the parameters
    *'pose_ref_dist_threshold_edges_rel'*
    and *'pose_ref_dist_threshold_edges_abs'* should be set.
    If both are set, only the value of the last modified parameter is used.
    Note that this parameter is ignored if the dense pose refinement is
    disabled or if no edge-supported surface-based matching is used.

    Restriction:
     *'pose_ref_dist_threshold_edges_abs'* > *0*
  - ***'pose_ref_scoring_dist_edges_rel'*:** —

    Set the distance threshold of edges for scoring relative to the
    diameter of the surface model. See the following
    *'pose_ref_scoring_dist_edges_abs'* for a detailed description.

    Note that only one of the parameters
    *'pose_ref_scoring_dist_edges_rel'* and
    *'pose_ref_scoring_dist_edges_abs'* should be set.
    If both are set, only the value of the last modified parameter is used.
    Note that this parameter is ignored if the dense pose refinement is
    disabled or if no edge-supported surface-based matching is used.

    Suggested values:
     *0.2*, *0.01*,
    *0.005*, *0.0001*

    Default:
     *0.005*

    Restriction:
     *'pose_ref_scoring_dist_edges_rel'* > *0*
  - ***'pose_ref_scoring_dist_edges_abs'*:** —

    Set the distance threshold of edges for scoring as an absolute value.
    Only scene edges that are closer to the object edges than this distance
    are considered to be 'on the model' when computing the score after
    the pose refinement. All other scene edges are considered not to be
    on the model.
    The value should correspond to the expected inaccuracy of the extracted
    scene edges and the inaccuracy of the refined pose.

    Note that only one of the parameters
    *'pose_ref_scoring_dist_edges_rel'* and
    *'pose_ref_scoring_dist_edges_abs'* should be set.
    If both are set, only the value of the last modified parameter is used.
    Note that this parameter is ignored if the dense pose refinement is
    disabled or if no edge-supported surface-based matching is used.

    Restriction:
     *'pose_ref_scoring_dist_edges_abs'* > *0*
  - ***'use_view_based'*:** —

    Turns the view-based score computation for surface-based matching on or
    off. For further details, see the respective description in the section
    about the sparse pose refinement above.

    If the model was not prepared for view-based score computation,
    an error is returned.

    List of values:
     *'true'*, *'false'*

    Default:
     *'false'*, if *'train_view_based'*
    was disabled when creating the model, otherwise *'true'*.
  - ***'use_self_similar_poses'*:** —

    Turns the optimization regarding self-similar, almost symmetric poses
    on or off.

    If the model was not created with activated parameter
    *'train_self_similar_poses'*, an error is returned when setting
    *'use_self_similar_poses'* to *'true'*.

    List of values:
     *'true'*, *'false'*

    Default:
     *'false'*, if *'train_self_similar_poses'*
    was disabled when creating the model, otherwise *'true'*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

This operator supports canceling timeouts and interrupts.

## Parameters

**`SurfaceModelID`** (input_control)  surface_model `→`  (handle)

Handle of the surface model.

**`ObjectModel3D`** (input_control)  object_model_3d `→`  (handle)

Handle of the 3D object model containing the
scene.

**`RelSamplingDistance`** (input_control)  real `→`  (real)

Scene sampling distance relative to the diameter
of the surface model.

Default:
0.05

Suggested values:
0.1, 0.07, 0.05, 0.04, 0.03

Restriction:
`0 < RelSamplingDistance < 1`

**`KeyPointFraction`** (input_control)  real `→`  (real)

Fraction of sampled scene points used as
key points.

Default:
0.2

Suggested values:
0.3, 0.2, 0.1, 0.05

Restriction:
`0 < KeyPointFraction <= 1`

**`MinScore`** (input_control)  real(-array) `→`  (real / integer)

Minimum score of the returned poses.

Default:
0

Restriction:
`MinScore >= 0`

**`ReturnResultHandle`** (input_control)  string `→`  (string)

Enable returning a result handle in
*`SurfaceMatchingResultID`*.

Default:
'false'

Suggested values:
'true', 'false'

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Names of the generic parameters.

Default:
[]

List of values:
'3d_edge_min_amplitude_abs', '3d_edge_min_amplitude_rel', '3d_edges', 'dense_pose_refinement', 'max_gap', 'max_overlap_dist_abs', 'max_overlap_dist_rel', 'num_matches', 'pose_ref_dist_threshold_abs', 'pose_ref_dist_threshold_edges_abs', 'pose_ref_dist_threshold_edges_rel', 'pose_ref_dist_threshold_rel', 'pose_ref_num_steps', 'pose_ref_scoring_dist_abs', 'pose_ref_scoring_dist_edges_abs', 'pose_ref_scoring_dist_edges_rel', 'pose_ref_scoring_dist_rel', 'pose_ref_sub_sampling', 'pose_ref_use_scene_normals', 'scene_invert_normals', 'scene_normal_computation', 'scene_sampling_mode', 'sparse_pose_refinement', 'use_3d_edges', 'use_self_similar_poses', 'use_view_based', 'viewpoint'

**`GenParamValue`** (input_control)  attribute.value-array `→`  (string / real / integer)

Values of the generic parameters.

Default:
[]

Suggested values:
0, 1, 'true', 'false', 0.005, 0.01, 0.03, 0.05, 0.1, 'num_scene_points', 'model_point_fraction', 'num_model_points', 'voxel', 'fast', 'mls'

**`Pose`** (output_control)  pose(-array) `→`  (real / integer)

3D pose of the surface model in the scene.

**`Score`** (output_control)  real-array `→`  (real)

Score of the found instances of the surface
model.

**`SurfaceMatchingResultID`** (output_control)  surface_matching_result(-array) `→`  (handle)

Handle of the matching result, if enabled in
*`ReturnResultHandle`*.

## Result

`find_surface_model` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`xyz_to_object_model_3d`,
`get_object_model_3d_params`,
`read_surface_model`,
`create_surface_model`,
`get_surface_model_param`,
`edges_object_model_3d`

## Possible Successors

`refine_surface_model_pose`,
`get_surface_matching_result`,
`clear_surface_matching_result`,
`clear_object_model_3d`

## Alternatives

`refine_surface_model_pose`,
`find_surface_model_image`,
`refine_surface_model_pose_image`

## See also

`refine_surface_model_pose`,
`find_surface_model_image`

## Module

3D Metrology
