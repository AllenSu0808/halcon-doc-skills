# create_trained_component_model (Operator)

## Name

`create_trained_component_model` — Prepare a component model for matching based on trained components.

## Warning

**`create_trained_component_model` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`def create_trained_component_model(component_training_id: HHandle, angle_start: float, angle_extent: float, min_contrast_comp: MaybeSequence[Union[int, str]], min_score_comp: MaybeSequence[float], num_levels_comp: MaybeSequence[Union[int, str]], angle_step_comp: MaybeSequence[Union[float, str]], optimization_comp: str, metric_comp: MaybeSequence[str], pregeneration_comp: MaybeSequence[str]) -> Tuple[HHandle, Sequence[int]]`

`def create_trained_component_model_s(component_training_id: HHandle, angle_start: float, angle_extent: float, min_contrast_comp: MaybeSequence[Union[int, str]], min_score_comp: MaybeSequence[float], num_levels_comp: MaybeSequence[Union[int, str]], angle_step_comp: MaybeSequence[Union[float, str]], optimization_comp: str, metric_comp: MaybeSequence[str], pregeneration_comp: MaybeSequence[str]) -> Tuple[HHandle, int]`

## Description

`create_trained_component_model` prepares the training result,
which is passed in *`component_training_id`*, as a component
model for matching. The output parameter *`component_model_id`*
is a handle for this model, which is used in subsequent calls to
[`find_component_model`](find_component_model.md). In contrast to
[`create_component_model`](create_component_model.md), the model components must have been
previously trained using [`train_model_components`](train_model_components.md) before
calling `create_trained_component_model`.

The parameters *`angle_start`* and *`angle_extent`*
determine the range of possible rotations of the component model in
an image.

Internally, a separate shape model is built for each model component
(see [`create_shape_model`](create_shape_model.md)). Therefore, the parameters
*`min_contrast_comp`*, *`min_score_comp`*,
*`num_levels_comp`*, *`angle_step_comp`*,
*`optimization_comp`*, *`metric_comp`*, and
*`pregeneration_comp`* correspond to the parameters of
[`create_shape_model`](create_shape_model.md), with the following differences: First,
the parameter `optimization` of [`create_shape_model`](create_shape_model.md)
provides the possibility to reduce the number of model points as
well as the possibility to completely pregenerate the shape
model. In contrast, the operator
`create_trained_component_model` uses a separate parameter
*`pregeneration_comp`* in order to decide whether the shape
models should be completely pregenerated or not. A second difference
concerning the parameter *`min_score_comp`* should be noted. When
using the shape-based matching, this parameter needs not be passed
when preparing the shape model using [`create_shape_model`](create_shape_model.md) but
only during the search using [`find_shape_model`](find_shape_model.md). In contrast,
when preparing the component model it is favorable to analyze
rotational symmetries of the model components and similarities
between the model components. However, this analysis only leads to
meaningful results if the value for *`min_score_comp`* that is
used during the search (see [`find_component_model`](find_component_model.md)) is already
approximately known. After the search with
[`find_component_model`](find_component_model.md) the pose parameters of the components
in a search image are returned. Note that the pose parameters refer
to the reference points of the components. The reference point of a
component is the center of gravity of its associated region that is
returned in `model_components` of
[`train_model_components`](train_model_components.md).

The parameters *`min_contrast_comp`*, *`num_levels_comp`*,
*`angle_step_comp`*, and *`optimization_comp`* can be
automatically determined by passing *"auto"* for the
respective parameters.

All component-specific input parameters (parameter names terminate
with the suffix `Comp`) must either contain one element, in
which case the parameter is used for all model components, or must
contain the same number of elements as the number of model
components contained in *`component_training_id`*, in which case
each parameter element refers to the corresponding component in
*`component_training_id`*.

In addition to the individual shape models, the component model also
contains information about the way the single model components must
be searched relative to each other using
[`find_component_model`](find_component_model.md) in order to minimize the computation
time of the search. For this, the components are represented in a
tree structure. First, the component that stands at the root of
this search tree (root component) is searched. Then, the remaining
components are searched relative to the pose of their predecessor in
the search tree.

The root component can be passed as an input parameter of
[`find_component_model`](find_component_model.md) during the search. To what extent a model
component is suited to act as root component depends on several factors.
In principle, a model component that can be found in the image with a high
probability should be chosen. Therefore, a component that is sometimes
occluded to a high degree or that is missing in some cases is not well suited
to act as root component. Additionally, the computation time that is
associated with the root component during the search can serve as a
criterion. A ranking of the model components that is based on the latter
criterion is returned in *`root_ranking`*. In this parameter the indices
of the model components are sorted in descending order according to their
associated computation time, i.e., *`root_ranking`*[0] contains the index
of the model component that, chosen as root component, allows the fastest
search. Note that the ranking returned in *`root_ranking`* represents
only a coarse estimation. Furthermore, the calculation of the root ranking
assumes that the image size as well as the value of the system parameter
*"border_shape_models"* are identical when calling
`create_trained_component_model` and [`find_component_model`](find_component_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`component_training_id`** (input_control)  component_training `→` HHandle

Handle of the training result.

**`angle_start`** (input_control)  angle.rad `→` float

Smallest rotation of the component model.

Default:
-0.39

Suggested values:
-3.14, -1.57, -0.79, -0.39, -0.20, 0.0

**`angle_extent`** (input_control)  angle.rad `→` float

Extent of the rotation of the component model.

Default:
0.79

Suggested values:
6.28, 3.14, 1.57, 0.79, 0.39

Restriction:
`AngleExtent >= 0`

**`min_contrast_comp`** (input_control)  integer(-array) `→` MaybeSequence[Union[int, str]]

Minimum contrast of the components in the search
images.

Default:
"auto"

Suggested values:
"auto", 10, 20, 20, 40

Restriction:
`MinContrastComp >= 0`

**`min_score_comp`** (input_control)  real(-array) `→` MaybeSequence[float]

Minimum score of the instances of the components to
be found.

Default:
0.5

Suggested values:
0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Minimum increment:
0.01

Recommended increment:
0.05

Restriction:
`0 <= MinScoreComp && MinScoreComp <= 1`

**`num_levels_comp`** (input_control)  integer(-array) `→` MaybeSequence[Union[int, str]]

Maximum number of pyramid levels for the components.

Default:
"auto"

List of values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "auto"

**`angle_step_comp`** (input_control)  angle.rad(-array) `→` MaybeSequence[Union[float, str]]

Step length of the angles (resolution) for the
components.

Default:
"auto"

Suggested values:
"auto", 0.0175, 0.0349, 0.0524, 0.0698, 0.0873

Restriction:
`AngleStepComp >= 0`

**`optimization_comp`** (input_control)  string `→` str

Kind of optimization for the components.

Default:
"auto"

List of values:
"auto", "none", "point_reduction_high", "point_reduction_low", "point_reduction_medium"

**`metric_comp`** (input_control)  string(-array) `→` MaybeSequence[str]

Match metric used for the components.

Default:
"use_polarity"

List of values:
"ignore_color_polarity", "ignore_global_polarity", "ignore_local_polarity", "use_polarity"

**`pregeneration_comp`** (input_control)  string(-array) `→` MaybeSequence[str]

Complete pregeneration of the shape models for the
components if equal to *"true"*.

Default:
"false"

List of values:
"false", "true"

**`component_model_id`** (output_control)  component_model `→` HHandle

Handle of the component model.

**`root_ranking`** (output_control)  integer(-array) `→` Sequence[int]

Ranking of the model components expressing the
suitability to act as the root component.

## Result

If the parameters are valid, the operator
`create_trained_component_model` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
