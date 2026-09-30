# create_component_model (Operator)

## Name

`create_component_model` — Prepare a component model for matching based on explicitly specified
components and relations.

## Warning

**`create_component_model` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`def create_component_model(model_image: HObject, component_regions: HObject, variation_row: MaybeSequence[int], variation_column: MaybeSequence[int], variation_angle: MaybeSequence[float], angle_start: float, angle_extent: float, contrast_low_comp: MaybeSequence[Union[int, str]], contrast_high_comp: MaybeSequence[Union[int, str]], min_size_comp: MaybeSequence[Union[int, str]], min_contrast_comp: MaybeSequence[Union[int, str]], min_score_comp: MaybeSequence[float], num_levels_comp: MaybeSequence[Union[int, str]], angle_step_comp: MaybeSequence[Union[float, str]], optimization_comp: str, metric_comp: MaybeSequence[str], pregeneration_comp: MaybeSequence[str]) -> Tuple[HHandle, Sequence[int]]`

`def create_component_model_s(model_image: HObject, component_regions: HObject, variation_row: MaybeSequence[int], variation_column: MaybeSequence[int], variation_angle: MaybeSequence[float], angle_start: float, angle_extent: float, contrast_low_comp: MaybeSequence[Union[int, str]], contrast_high_comp: MaybeSequence[Union[int, str]], min_size_comp: MaybeSequence[Union[int, str]], min_contrast_comp: MaybeSequence[Union[int, str]], min_score_comp: MaybeSequence[float], num_levels_comp: MaybeSequence[Union[int, str]], angle_step_comp: MaybeSequence[Union[float, str]], optimization_comp: str, metric_comp: MaybeSequence[str], pregeneration_comp: MaybeSequence[str]) -> Tuple[HHandle, int]`

## Description

`create_component_model` prepares patterns, which are passed
in the form of a model image *`model_image`* and several regions
*`component_regions`*, as a component model for matching. The
output parameter *`component_model_id`* is a handle for this
model, which is used in subsequent calls to
[`find_component_model`](find_component_model.md). In contrast to
[`create_trained_component_model`](create_trained_component_model.md), no preceding training with
[`train_model_components`](train_model_components.md) needs to be performed before calling
`create_component_model`.

Each of the regions passed in *`component_regions`* describes a
separate model component. Later, the index of a component region in
*`component_regions`* is used to denote the model component.
The reference point of a component is the center of gravity of its
associated region, which is passed in *`component_regions`*. It
can be calculated by calling [`area_center`](area_center.md).

The relative movements (relations) of the model components can be
set by passing *`variation_row`*, *`variation_column`*, and
*`variation_angle`*. Because directly passing the relations is
complicated, instead of the relations the variations of the model
components are passed. The variations describe the movements of the
components independently from each other relative to their poses in
the model image *`model_image`*. The parameters
*`variation_row`* and *`variation_column`* describe the
movement of the components in row and column direction by
$\pm\tfrac{1}{2}\mathrm{VariationRow}$ ![figure](../assets/19716e15731413d8.svg) and
$\pm\frac{1}{2}VariationColumn$ ![figure](../assets/5f9f712f3872809a.svg),
respectively.
The parameter *`variation_angle`* describes the angle variation
of the component by
$\pm \tfrac{1}{2} VariationAngle$ ![figure](../assets/0187e898088fb74a.svg).
Based on these values, the relations are automatically computed. The three
parameters must either contain one element, in which case the
parameter is used for all model components, or must contain the same
number of elements as *`component_regions`*, in which case each
parameter element refers to the corresponding model component in
*`component_regions`*.

The parameters *`angle_start`* and *`angle_extent`*
determine the range of possible rotations of the component model in
an image.

Internally, a separate shape model is built for each model component
(see [`create_shape_model`](create_shape_model.md)). Therefore, the parameters
*`contrast_low_comp`*, *`contrast_high_comp`*,
*`min_size_comp`*, *`min_contrast_comp`*,
*`min_score_comp`*, *`num_levels_comp`*,
*`angle_step_comp`*, *`optimization_comp`*,
*`metric_comp`*, and *`pregeneration_comp`* correspond to
the parameters of [`create_shape_model`](create_shape_model.md), with the following
differences: First, in the parameter `contrast` of
[`create_shape_model`](create_shape_model.md) the upper as well as the lower threshold
for the hysteresis threshold method can be passed. Additionally, a
third value, which suppresses small connected contour regions, can
be passed. In contrast, the operator `create_component_model`
offers three separate parameters *`contrast_high_comp`*,
*`contrast_low_comp`*, and *`min_score_comp`* in order to set
these three values. Consequently, also the automatic computation of
the contrast threshold(s) is different. If both hysteresis threshold
should be automatically determined, both *`contrast_low_comp`*
and *`contrast_high_comp`* must be set to *"auto"*. In
contrast, if only one threshold value should be determined,
*`contrast_low_comp`* must be set to *"auto"* while
*`contrast_high_comp`* must be set to an arbitrary value
different from *"auto"*. Secondly, the parameter
`optimization` of [`create_shape_model`](create_shape_model.md) provides the
possibility to reduce the number of model points as well as the
possibility to completely pregenerate the shape model. In contrast,
the operator [`create_trained_component_model`](create_trained_component_model.md) uses a separate
parameter *`pregeneration_comp`* in order to decide whether the
shape models should be completely pregenerated or not. A third
difference concerning the parameter *`min_score_comp`* should be
noted. When using the shape-based matching, this parameter needs not
be passed when preparing the shape model using
[`create_shape_model`](create_shape_model.md), but only during the search using
[`find_shape_model`](find_shape_model.md). In contrast, when preparing the component
model it is favorable to analyze rotational symmetries of the model
components and similarities between the model components. However,
this analysis only leads to meaningful results if the value for
*`min_score_comp`* that is used during the search (see
[`find_component_model`](find_component_model.md)) is already approximately known.

In addition to the parameters *`contrast_low_comp`*,
*`contrast_high_comp`*, and *`min_size_comp`* also the
parameters *`min_contrast_comp`*, *`num_levels_comp`*,
*`angle_step_comp`*, and *`optimization_comp`* can be
automatically determined by passing *"auto"* for the
respective parameters.

All component-specific input parameters (parameter names terminate
with the suffix `Comp`) must either contain one element, in
which case the parameter is used for all model components, or must
contain the same number of elements as the number of regions in
*`component_regions`*, in which case each parameter element
refers to the corresponding element in *`component_regions`*.

In addition to the individual shape models, the component model also
contains information about the way the single model components must
be searched relative to each other using
[`find_component_model`](find_component_model.md) in order to minimize the computation
time of the search. For this, the components are represented in a
tree structure. First, the component that stands at the root of this
search tree (root component) is searched. Then, the remaining
components are searched relative to the pose of their predecessor in
the search tree.

The root component can be passed as an input parameter of
[`find_component_model`](find_component_model.md) during the search. To what extent a model
component is suited to act as the root component depends on several factors.
In principle, a model component that can be found in the image with a high
probability should be chosen. Therefore, a component that is sometimes
occluded to a high degree or that is missing in some cases is not well suited
to act as the root component. Additionally, the computation time that is
associated with the root component during the search can serve as a
criterion. A ranking of the model components that is based on the latter
criterion is returned in *`root_ranking`*. In this parameter the indices
of the model components are sorted in descending order according to their
associated search time, i.e., *`root_ranking`*[0] contains the index of
the model component that, chosen as root component, allows the fastest
search. Note that the ranking returned in *`root_ranking`* represents
only a coarse estimation. Furthermore, the calculation of the root ranking
assumes that the image size as well as the value of the system parameter
*"border_shape_models"* are identical when calling
`create_component_model` and [`find_component_model`](find_component_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`model_image`** (input_object)  (multichannel-)image `→` HObject (byte / uint2)

Input image from which the shape models of the
model components should be created.

**`component_regions`** (input_object)  region-array `→` HObject

Input regions from which the shape models of the
model components should be created.

**`variation_row`** (input_control)  integer(-array) `→` MaybeSequence[int]

Variation of the model components in row direction.

Suggested values:
0, 1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 100, 150

Restriction:
`VariationRow >= 0`

**`variation_column`** (input_control)  integer(-array) `→` MaybeSequence[int]

Variation of the model components in column direction.

Suggested values:
0, 1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 100, 150

Restriction:
`VariationColumn >= 0`

**`variation_angle`** (input_control)  angle.rad(-array) `→` MaybeSequence[float]

Angle variation of the model components.

Suggested values:
0.0, 0.017, 0.035, 0.05, 0.07, 0.09, 0.17, 0.35, 0.52, 0.67, 0.87

Restriction:
`VariationAngle >= 0`

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

**`contrast_low_comp`** (input_control)  integer(-array) `→` MaybeSequence[Union[int, str]]

Lower hysteresis threshold for the contrast of the
components in the model image.

Default:
"auto"

Suggested values:
"auto", 10, 20, 30, 40, 60, 80, 100, 120, 140, 160

Restriction:
`ContrastLowComp > 0`

**`contrast_high_comp`** (input_control)  integer(-array) `→` MaybeSequence[Union[int, str]]

Upper hysteresis threshold for the contrast of the
components in the model image.

Default:
"auto"

Suggested values:
"auto", 10, 20, 30, 40, 60, 80, 100, 120, 140, 160

Restriction:
`ContrastHighComp > 0 && ContrastHighComp >= ContrastLowComp`

**`min_size_comp`** (input_control)  integer(-array) `→` MaybeSequence[Union[int, str]]

Minimum size of the contour regions in the model.

Default:
"auto"

Suggested values:
"auto", 0, 5, 10, 20, 30, 40

Restriction:
`MinSizeComp >= 0`

**`min_contrast_comp`** (input_control)  integer(-array) `→` MaybeSequence[Union[int, str]]

Minimum contrast of the components in the search
images.

Default:
"auto"

Suggested values:
"auto", 10, 20, 20, 40

Restriction:
`MinContrastComp <= ContrastLowComp && MinContrastComp >= 0`

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
`create_component_model` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
