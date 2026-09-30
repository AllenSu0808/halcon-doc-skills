# train_model_components (Operator)

## Name

`train_model_components` — Train components and relations for the component-based matching.

## Warning

**`train_model_components` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`def train_model_components(model_image: HObject, initial_components: HObject, training_images: HObject, contrast_low: MaybeSequence[Union[int, str]], contrast_high: MaybeSequence[Union[int, str]], min_size: MaybeSequence[Union[int, str]], min_score: MaybeSequence[float], search_row_tol: MaybeSequence[int], search_column_tol: MaybeSequence[int], search_angle_tol: MaybeSequence[float], training_emphasis: str, ambiguity_criterion: str, max_contour_overlap: float, cluster_threshold: float) -> Tuple[HObject, HHandle]`

## Description

`train_model_components` extracts the final (rigid) model
components and trains their mutual relations, i.e., their relative
movements, on the basis of the initial components by considering
several training images. The result of the training is returned in
the handle *`component_training_id`*. The training result can be
subsequently used to create the actual component model using
[`create_trained_component_model`](create_trained_component_model.md).

`train_model_components` should be used in cases where the
relations of the components are not known and should be trained
automatically. In contrast, if the relations are known no training
needs to be performed with `train_model_components`. Instead,
the component model can be directly created with
[`create_component_model`](create_component_model.md).

If the initial components have been automatically created by using
[`gen_initial_components`](gen_initial_components.md), *`initial_components`* contains
the contour regions of the initial components. In contrast, if the
initial components should be defined by the user, they can be
directly passed in *`initial_components`*. However, instead of
the contour regions for each initial component, its enclosing region
must be passed in the tuple. The (contour) regions refer to the
model image *`model_image`*. If the initial components have been
obtained using [`gen_initial_components`](gen_initial_components.md), the model image
should be the same as in [`gen_initial_components`](gen_initial_components.md). Please
note that each initial component is part of at most one rigid model
component. This is because during the training initial components
can be merged into rigid model components if required (see
below). However, they cannot be split and distributed to several
rigid model components.

`train_model_components` uses the following approach to
perform the training: In the first step, the initial components are
searched in all training images. In some cases, one initial
component may be found in an training image more than once. Thus, in
the second step, the resulting ambiguities are solved, i.e., the
most probable pose of each initial component is found. Consequently,
after solving the ambiguities, in all training images at most one
pose of each initial component is available. In the next step the
poses are analyzed and those initial components that do not show any
relative movement are clustered to the final rigid model
components. Finally, in the last step the relations between the
model components are computed by analyzing their relative poses over
the sequence of training images. The parameters that are associated
with the mentioned steps are explained in the following.

The training is performed based on several training images, which
are passed in *`training_images`*. Each training image must show
at most one instance of the compound object and should contain the
full range of allowed relative movements of the model components.
If, for example, the component model of an on/off switch should be
trained, one training image that shows the switch turned off is
sufficient if the switch in the model image is turned on, or vice
versa.

The principle of the training is to find the initial components in
all training images and to analyze their poses. For this, for each
initial component a shape model is created (see
[`create_shape_model`](create_shape_model.md)), which is then used to determine the
poses (position and orientation) of the initial components in the
training images (see [`find_shape_model`](find_shape_model.md)). Depending on the
mode that is set by using
`set_system('pregenerate_shape_models',...)`, the shape model
is either pregenerated completely or computed online during the
search. The mode influences the computation time as well as the
robustness of the training. Furthermore, it should be noted that if
single-channel image are used in *`model_image`* as well as in
*`training_images`* the metric *"use_polarity"* is used
internally for [`create_shape_model`](create_shape_model.md), while if multichannel
images are used in either *`model_image`* or
*`training_images`* the metric *"ignore_color_polarity"*
is used. Finally, it should be noted that while the number of
channels in *`model_image`* and *`training_images`* may be
different, e.g., to facilitate model generation from synthetically
generated images, the number of channels in all the images in
*`training_images`* must be identical. For further details see
[`create_shape_model`](create_shape_model.md). The creation of the shape models can be
influenced by choosing appropriate values for the parameters
*`contrast_low`*, *`contrast_high`*, and
*`min_size`*. These parameters have the same meaning as in
[`gen_initial_components`](gen_initial_components.md) and can be automatically determined
by passing *"auto"*: If both hysteresis threshold should be
automatically determined, both *`contrast_low`* and
*`contrast_high`* must be set to *"auto"*. In contrast,
if only one threshold value should be determined,
*`contrast_low`* must be set to *"auto"* while
*`contrast_high`* must be set to an arbitrary value different
from *"auto"*. If the initial components have been
automatically created by [`gen_initial_components`](gen_initial_components.md), the
parameters *`contrast_low`*, *`contrast_high`*, and
*`min_size`* should be set to the same values as in
[`gen_initial_components`](gen_initial_components.md).

To influence the search for the initial components, the parameters
*`min_score`*, *`search_row_tol`*, *`search_column_tol`*,
*`search_angle_tol`*, and *`training_emphasis`* can be set.
The parameter *`min_score`* determines what score a potential
match must at least have to be regarded as an instance of the
initial component in the training image. The larger
*`min_score`* is chosen, the faster the training is. If the
initial components can be expected never to be occluded in the
training images, *`min_score`* may be set as high as 0.8 or even
0.9 (see [`find_shape_model`](find_shape_model.md)).

By default, the components are searched only at points in which the
component lies completely within the respective training image.
This means that a component will not be found if it extends beyond
the borders of the image, even if it would achieve a score greater
than *`min_score`*. This behavior can be changed with
`set_system('border_shape_models','true')`, which will cause
components that extend beyond the image border to be found if they
achieve a score greater than *`min_score`*. Here, points lying
outside the image are regarded as being occluded, i.e., they lower
the score. It should be noted that the runtime of the training will
increase in this mode.

When dealing with a high number of initial components and many
training images, the training may take a long time (up to several
minutes). In order to speed up the training it is possible to
restrict the search space for the single initial components in the
training images. For this, the poses of the initial components in
the model image are used as reference pose. The parameters
*`search_row_tol`* and *`search_column_tol`* specify the
position tolerance region relative to the reference position in
which the search is performed. Assume, for example, that the
position of an initial component in the model image is (100,200) and
*`search_row_tol`* is set to *20* and
*`search_column_tol`* is set to *10*. Then, this initial
component is searched in the training images only within the
axis-aligned rectangle that is determined by the upper left corner
(80,190) and the lower right corner (120,210). The same holds for
the orientation angle range, which can be restricted by specifying
the angle tolerance *`search_angle_tol`* to the angle range of
[-*`search_angle_tol`*,+*`search_angle_tol`*]. Thus, it is
possible to considerably reduce the computational effort during the
training by an adequate acquisition of the training images. If one
of the three parameters is set to *-1*, no restriction of the
parameter space is applied in the corresponding dimension.

The input parameters *`contrast_low`*, *`contrast_high`*,
*`min_size`*, *`min_score`*, *`search_row_tol`*,
*`search_column_tol`*, and *`search_angle_tol`* must either
contain one element, in which case the parameter is used for all
initial components, or must contain the same number of elements as
the initial components contained in *`initial_components`*, in
which case each parameter element refers to the corresponding
initial component in *`initial_components`*.

The parameter *`training_emphasis`* offers another possibility
to influence the computation time of the training and to
simultaneously affect its robustness. If *`training_emphasis`*
is set to *"speed"*, on the one hand the training is
comparatively fast, on the other hand it may happen in some cases
that some initial components are not found in the training images or
are found at a wrong pose. Consequently, this would lead to an
incorrect computation of the rigid model components and their
relations. The poses of the found initial components in the
individual training images can be examined by using
[`get_training_components`](get_training_components.md). If erroneous matches occur the
training should be restarted with *`training_emphasis`* set to
*"reliability"*. This results in a higher robustness at the
cost of a longer computation time.

Furthermore, during the pose determination of the initial components
ambiguities may occur if the initial components are rotationally
symmetric or if several initial components are identical or at least
similar to each other. To solve the ambiguities, the most probable
pose is calculated for each initial component in each training
image. For this, the individual ambiguous poses are evaluated. The
pose of an initial component receives a good evaluation if the
relative pose of the initial component with respect to the other
initial components is similar to the corresponding relative pose in
the model image. The method to evaluate this similarity can be
chosen with *`ambiguity_criterion`*. In almost all cases the
best results are obtained with *"rigidity"*, which assumes
the rigidity of the compound object. The more the rigidity of the
compound object is violated by the pose of the initial component,
the worse its evaluation is. In the case of *"distance"*,
only the distance between the initial components is considered
during the evaluation. Hence, the pose of the initial component
receives a good evaluation if its distances to the other initial
components is similar to the corresponding distances in the model
image. Accordingly, when choosing *"orientation"*, only the
relative orientation is considered during the evaluation. Finally,
the simultaneous consideration of distance and orientation can be
achieved by choosing *"distance_orientation"*. In contrast
to *"rigidity"*, the relative pose of the initial components
is not considered when using *"distance_orientation"*.

The process of solving the ambiguities can be further influenced by
the parameter *`max_contour_overlap`*. This parameter describes
the extent by which the contours of two initial component matches
may overlap each other. Let the letters 'I' and 'T', for example, be
two initial components that should be searched in a training image
that shows the string 'IT'. Then, the initial component 'T' should
be found at its correct pose. In contrast, the initial component 'I'
will be found at its correct pose ('I') but also at the pose of the
'T' because of the similarity of the two components. To discard the
wrong match of the initial component 'I', an appropriate value for
*`max_contour_overlap`* can be chosen: If overlapping matches
should be tolerated, *`max_contour_overlap`* should be set to
*1*. If overlapping matches should be completely avoided,
*`max_contour_overlap`* should be set to *0*. By choosing
a value between *0* and *1*, the maximum percentage of
overlapping contour pixels can be adjusted.

The decision which initial components can be clustered to rigid
model components is made based on the poses of the initial
components in the model image and in the training images. Two
initial components are merged if they do not show any relative
movement over all images. Assume that in the case of the above
mentioned switch the training image would show the same switch state
as the model image, the algorithm would merge the respective initial
components because it assumes that the entire switch is one rigid
model component. The extent by which initial components are merged
can be influenced with the parameter *`cluster_threshold`*. This
cluster threshold is based on the probability that two initial
components belong to the same rigid model component. Thus,
*`cluster_threshold`* describes the minimum probability which
two initial components must have in order to be merged. Since the
threshold is based on a probability value, it must lie in the
interval between *0* and *1*. The greater the
threshold is chosen, the smaller the number of initial components
that are merged. If a threshold of *0* is chosen, all
initial components are merged into one rigid component, while for a
threshold of *1* no merging is performed and each initial
component is adopted as one rigid model component.

The final rigid model components are returned in
*`model_components`*. Later, the index of a component region in
*`model_components`* is used to denote the model component. The
poses of the components in the training images can be examined by
using [`get_training_components`](get_training_components.md).

After the determination of the model components their relative
movements are analyzed by determining the movement of one component
with respect to a second component for each pair of components. For
this, the components are referred to their reference points. The
reference point of a component is the center of gravity of its
contour region, which is returned in *`model_components`*. It
can be calculated by calling [`area_center`](area_center.md). Finally, the
relative movement is represented by the smallest enclosing rectangle
of arbitrary orientation of the reference point movement and by the
smallest enclosing angle interval of the relative orientation of the
second component over all images. The determined relations can be
inspected by using [`get_component_relations`](get_component_relations.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`model_image`** (input_object)  (multichannel-)image `→` HObject (byte / uint2)

Input image from which the shape models of the initial
components should be created.

**`initial_components`** (input_object)  region-array `→` HObject

Contour regions or enclosing regions of the
initial components.

**`training_images`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / uint2)

Training images that are used for training the
model components.

**`model_components`** (output_object)  region(-array) `→` HObject

Contour regions of rigid model components.

**`contrast_low`** (input_control)  integer(-array) `→` MaybeSequence[Union[int, str]]

Lower hysteresis threshold for the contrast of the
initial components in the image.

Default:
"auto"

Suggested values:
"auto", 10, 20, 30, 40, 60, 80, 100, 120, 140, 160

Restriction:
`ContrastLow > 0`

**`contrast_high`** (input_control)  integer(-array) `→` MaybeSequence[Union[int, str]]

Upper hysteresis threshold for the contrast of the
initial components in the image.

Default:
"auto"

Suggested values:
"auto", 10, 20, 30, 40, 60, 80, 100, 120, 140, 160

Restriction:
`ContrastHigh > 0 && ContrastHigh >= ContrastLow`

**`min_size`** (input_control)  integer(-array) `→` MaybeSequence[Union[int, str]]

Minimum size of connected contour regions.

Default:
"auto"

Suggested values:
"auto", 0, 5, 10, 20, 30, 40

Restriction:
`MinSize >= 0`

**`min_score`** (input_control)  real(-array) `→` MaybeSequence[float]

Minimum score of the instances of the initial
components to be found.

Default:
0.5

Suggested values:
0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Minimum increment:
0.01

Recommended increment:
0.05

Restriction:
`0 <= MinScore && MinScore <= 1`

**`search_row_tol`** (input_control)  integer(-array) `→` MaybeSequence[int]

Search tolerance in row direction.

Default:
-1

Suggested values:
0, 10, 20, 30, 50, 100

Restriction:
`SearchRowTol == -1 || SearchColumnTol >= 0`

**`search_column_tol`** (input_control)  integer(-array) `→` MaybeSequence[int]

Search tolerance in column direction.

Default:
-1

Suggested values:
0, 10, 20, 30, 50, 100

Restriction:
`SearchColumnTol == -1 || SearchColumnTol >= 0`

**`search_angle_tol`** (input_control)  angle.rad(-array) `→` MaybeSequence[float]

Angle search tolerance.

Default:
-1

Suggested values:
0.0, 0.17, 0.39, 0.78, 1.57

Restriction:
`SearchAngleTol == -1 || SearchAngleTol >= 0`

**`training_emphasis`** (input_control)  string `→` str

Decision whether the training emphasis should lie on
a fast computation or on a high robustness.

Default:
"speed"

List of values:
"reliability", "speed"

**`ambiguity_criterion`** (input_control)  string `→` str

Criterion for solving ambiguous matches of the initial
components in the training images.

Default:
"rigidity"

List of values:
"distance", "distance_orientation", "orientation", "rigidity"

**`max_contour_overlap`** (input_control)  real `→` float

Maximum contour overlap of the found initial components
in a training image.

Default:
0.2

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Minimum increment:
0.01

Recommended increment:
0.05

Restriction:
`0 <= MaxContourOverlap && MaxContourOverlap <= 1`

**`cluster_threshold`** (input_control)  real `→` float

Threshold for clustering the initial components.

Default:
0.5

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`0 <= ClusterThreshold && ClusterThreshold <= 1`

**`component_training_id`** (output_control)  component_training `→` HHandle

Handle of the training result.

## Result

If the parameter values are correct, the operator
`train_model_components` returns the value 2 (
H_MSG_TRUE)
. If the input is
empty (no input images are available) the behavior can be set via
`set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Module

Matching
