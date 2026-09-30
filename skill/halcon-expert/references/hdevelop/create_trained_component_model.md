# create_trained_component_model (Operator)

## Name

`create_trained_component_model` — Prepare a component model for matching based on trained components.

## Warning

**`create_trained_component_model` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`create_trained_component_model( : : ComponentTrainingID, AngleStart, AngleExtent, MinContrastComp, MinScoreComp, NumLevelsComp, AngleStepComp, OptimizationComp, MetricComp, PregenerationComp : ComponentModelID, RootRanking)`

## Description

`create_trained_component_model` prepares the training result,
which is passed in *`ComponentTrainingID`*, as a component
model for matching. The output parameter *`ComponentModelID`*
is a handle for this model, which is used in subsequent calls to
[`find_component_model`](find_component_model.md). In contrast to
[`create_component_model`](create_component_model.md), the model components must have been
previously trained using [`train_model_components`](train_model_components.md) before
calling `create_trained_component_model`.

The parameters *`AngleStart`* and *`AngleExtent`*
determine the range of possible rotations of the component model in
an image.

Internally, a separate shape model is built for each model component
(see [`create_shape_model`](create_shape_model.md)). Therefore, the parameters
*`MinContrastComp`*, *`MinScoreComp`*,
*`NumLevelsComp`*, *`AngleStepComp`*,
*`OptimizationComp`*, *`MetricComp`*, and
*`PregenerationComp`* correspond to the parameters of
[`create_shape_model`](create_shape_model.md), with the following differences: First,
the parameter `Optimization` of [`create_shape_model`](create_shape_model.md)
provides the possibility to reduce the number of model points as
well as the possibility to completely pregenerate the shape
model. In contrast, the operator
`create_trained_component_model` uses a separate parameter
*`PregenerationComp`* in order to decide whether the shape
models should be completely pregenerated or not. A second difference
concerning the parameter *`MinScoreComp`* should be noted. When
using the shape-based matching, this parameter needs not be passed
when preparing the shape model using [`create_shape_model`](create_shape_model.md) but
only during the search using [`find_shape_model`](find_shape_model.md). In contrast,
when preparing the component model it is favorable to analyze
rotational symmetries of the model components and similarities
between the model components. However, this analysis only leads to
meaningful results if the value for *`MinScoreComp`* that is
used during the search (see [`find_component_model`](find_component_model.md)) is already
approximately known. After the search with
[`find_component_model`](find_component_model.md) the pose parameters of the components
in a search image are returned. Note that the pose parameters refer
to the reference points of the components. The reference point of a
component is the center of gravity of its associated region that is
returned in `ModelComponents` of
[`train_model_components`](train_model_components.md).

The parameters *`MinContrastComp`*, *`NumLevelsComp`*,
*`AngleStepComp`*, and *`OptimizationComp`* can be
automatically determined by passing *'auto'* for the
respective parameters.

All component-specific input parameters (parameter names terminate
with the suffix `Comp`) must either contain one element, in
which case the parameter is used for all model components, or must
contain the same number of elements as the number of model
components contained in *`ComponentTrainingID`*, in which case
each parameter element refers to the corresponding component in
*`ComponentTrainingID`*.

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
criterion is returned in *`RootRanking`*. In this parameter the indices
of the model components are sorted in descending order according to their
associated computation time, i.e., *`RootRanking`*[0] contains the index
of the model component that, chosen as root component, allows the fastest
search. Note that the ranking returned in *`RootRanking`* represents
only a coarse estimation. Furthermore, the calculation of the root ranking
assumes that the image size as well as the value of the system parameter
*'border_shape_models'* are identical when calling
`create_trained_component_model` and [`find_component_model`](find_component_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`ComponentTrainingID`** (input_control)  component_training `→`  (handle)

Handle of the training result.

**`AngleStart`** (input_control)  angle.rad `→`  (real)

Smallest rotation of the component model.

Default:
-0.39

Suggested values:
-3.14, -1.57, -0.79, -0.39, -0.20, 0.0

**`AngleExtent`** (input_control)  angle.rad `→`  (real)

Extent of the rotation of the component model.

Default:
0.79

Suggested values:
6.28, 3.14, 1.57, 0.79, 0.39

Restriction:
`AngleExtent >= 0`

**`MinContrastComp`** (input_control)  integer(-array) `→`  (integer / string)

Minimum contrast of the components in the search
images.

Default:
'auto'

Suggested values:
'auto', 10, 20, 20, 40

Restriction:
`MinContrastComp >= 0`

**`MinScoreComp`** (input_control)  real(-array) `→`  (real)

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

**`NumLevelsComp`** (input_control)  integer(-array) `→`  (integer / string)

Maximum number of pyramid levels for the components.

Default:
'auto'

List of values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'auto'

**`AngleStepComp`** (input_control)  angle.rad(-array) `→`  (real / string)

Step length of the angles (resolution) for the
components.

Default:
'auto'

Suggested values:
'auto', 0.0175, 0.0349, 0.0524, 0.0698, 0.0873

Restriction:
`AngleStepComp >= 0`

**`OptimizationComp`** (input_control)  string `→`  (string)

Kind of optimization for the components.

Default:
'auto'

List of values:
'auto', 'none', 'point_reduction_high', 'point_reduction_low', 'point_reduction_medium'

**`MetricComp`** (input_control)  string(-array) `→`  (string)

Match metric used for the components.

Default:
'use_polarity'

List of values:
'ignore_color_polarity', 'ignore_global_polarity', 'ignore_local_polarity', 'use_polarity'

**`PregenerationComp`** (input_control)  string(-array) `→`  (string)

Complete pregeneration of the shape models for the
components if equal to *'true'*.

Default:
'false'

List of values:
'false', 'true'

**`ComponentModelID`** (output_control)  component_model `→`  (handle)

Handle of the component model.

**`RootRanking`** (output_control)  integer(-array) `→`  (integer)

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
