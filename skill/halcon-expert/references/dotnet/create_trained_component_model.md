# CreateTrainedComponentModel (Operator)

## Name

`CreateTrainedComponentModel` — Prepare a component model for matching based on trained components.

## Warning

**`CreateTrainedComponentModel` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`static void HOperatorSet.CreateTrainedComponentModel(HTuple componentTrainingID, HTuple angleStart, HTuple angleExtent, HTuple minContrastComp, HTuple minScoreComp, HTuple numLevelsComp, HTuple angleStepComp, HTuple optimizationComp, HTuple metricComp, HTuple pregenerationComp, out HTuple componentModelID, out HTuple rootRanking)`

`HComponentModel HComponentTraining.CreateTrainedComponentModel(double angleStart, double angleExtent, HTuple minContrastComp, HTuple minScoreComp, HTuple numLevelsComp, HTuple angleStepComp, string optimizationComp, HTuple metricComp, HTuple pregenerationComp, out HTuple rootRanking)`

`HComponentModel HComponentTraining.CreateTrainedComponentModel(double angleStart, double angleExtent, int minContrastComp, double minScoreComp, int numLevelsComp, double angleStepComp, string optimizationComp, string metricComp, string pregenerationComp, out int rootRanking)`

`public HComponentModel(HComponentTraining componentTrainingID, double angleStart, double angleExtent, HTuple minContrastComp, HTuple minScoreComp, HTuple numLevelsComp, HTuple angleStepComp, string optimizationComp, HTuple metricComp, HTuple pregenerationComp, out HTuple rootRanking)`

`public HComponentModel(HComponentTraining componentTrainingID, double angleStart, double angleExtent, int minContrastComp, double minScoreComp, int numLevelsComp, double angleStepComp, string optimizationComp, string metricComp, string pregenerationComp, out int rootRanking)`

`HTuple HComponentModel.CreateTrainedComponentModel(HComponentTraining componentTrainingID, double angleStart, double angleExtent, HTuple minContrastComp, HTuple minScoreComp, HTuple numLevelsComp, HTuple angleStepComp, string optimizationComp, HTuple metricComp, HTuple pregenerationComp)`

`int HComponentModel.CreateTrainedComponentModel(HComponentTraining componentTrainingID, double angleStart, double angleExtent, int minContrastComp, double minScoreComp, int numLevelsComp, double angleStepComp, string optimizationComp, string metricComp, string pregenerationComp)`

## Description

`CreateTrainedComponentModel` prepares the training result,
which is passed in *`componentTrainingID`*, as a component
model for matching. The output parameter *`componentModelID`*
is a handle for this model, which is used in subsequent calls to
[`FindComponentModel`](find_component_model.md). In contrast to
[`CreateComponentModel`](create_component_model.md), the model components must have been
previously trained using [`TrainModelComponents`](train_model_components.md) before
calling `CreateTrainedComponentModel`.

The parameters *`angleStart`* and *`angleExtent`*
determine the range of possible rotations of the component model in
an image.

Internally, a separate shape model is built for each model component
(see [`CreateShapeModel`](create_shape_model.md)). Therefore, the parameters
*`minContrastComp`*, *`minScoreComp`*,
*`numLevelsComp`*, *`angleStepComp`*,
*`optimizationComp`*, *`metricComp`*, and
*`pregenerationComp`* correspond to the parameters of
[`CreateShapeModel`](create_shape_model.md), with the following differences: First,
the parameter `optimization` of [`CreateShapeModel`](create_shape_model.md)
provides the possibility to reduce the number of model points as
well as the possibility to completely pregenerate the shape
model. In contrast, the operator
`CreateTrainedComponentModel` uses a separate parameter
*`pregenerationComp`* in order to decide whether the shape
models should be completely pregenerated or not. A second difference
concerning the parameter *`minScoreComp`* should be noted. When
using the shape-based matching, this parameter needs not be passed
when preparing the shape model using [`CreateShapeModel`](create_shape_model.md) but
only during the search using [`FindShapeModel`](find_shape_model.md). In contrast,
when preparing the component model it is favorable to analyze
rotational symmetries of the model components and similarities
between the model components. However, this analysis only leads to
meaningful results if the value for *`minScoreComp`* that is
used during the search (see [`FindComponentModel`](find_component_model.md)) is already
approximately known. After the search with
[`FindComponentModel`](find_component_model.md) the pose parameters of the components
in a search image are returned. Note that the pose parameters refer
to the reference points of the components. The reference point of a
component is the center of gravity of its associated region that is
returned in `modelComponents` of
[`TrainModelComponents`](train_model_components.md).

The parameters *`minContrastComp`*, *`numLevelsComp`*,
*`angleStepComp`*, and *`optimizationComp`* can be
automatically determined by passing *"auto"* for the
respective parameters.

All component-specific input parameters (parameter names terminate
with the suffix `Comp`) must either contain one element, in
which case the parameter is used for all model components, or must
contain the same number of elements as the number of model
components contained in *`componentTrainingID`*, in which case
each parameter element refers to the corresponding component in
*`componentTrainingID`*.

In addition to the individual shape models, the component model also
contains information about the way the single model components must
be searched relative to each other using
[`FindComponentModel`](find_component_model.md) in order to minimize the computation
time of the search. For this, the components are represented in a
tree structure. First, the component that stands at the root of
this search tree (root component) is searched. Then, the remaining
components are searched relative to the pose of their predecessor in
the search tree.

The root component can be passed as an input parameter of
[`FindComponentModel`](find_component_model.md) during the search. To what extent a model
component is suited to act as root component depends on several factors.
In principle, a model component that can be found in the image with a high
probability should be chosen. Therefore, a component that is sometimes
occluded to a high degree or that is missing in some cases is not well suited
to act as root component. Additionally, the computation time that is
associated with the root component during the search can serve as a
criterion. A ranking of the model components that is based on the latter
criterion is returned in *`rootRanking`*. In this parameter the indices
of the model components are sorted in descending order according to their
associated computation time, i.e., *`rootRanking`*[0] contains the index
of the model component that, chosen as root component, allows the fastest
search. Note that the ranking returned in *`rootRanking`* represents
only a coarse estimation. Furthermore, the calculation of the root ranking
assumes that the image size as well as the value of the system parameter
*"border_shape_models"* are identical when calling
`CreateTrainedComponentModel` and [`FindComponentModel`](find_component_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`componentTrainingID`** (input_control)  component_training `→` [HComponentTraining](HComponentTraining.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the training result.

**`angleStart`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Smallest rotation of the component model.

Default:
-0.39

Suggested values:
-3.14, -1.57, -0.79, -0.39, -0.20, 0.0

**`angleExtent`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Extent of the rotation of the component model.

Default:
0.79

Suggested values:
6.28, 3.14, 1.57, 0.79, 0.39

Restriction:
`AngleExtent >= 0`

**`minContrastComp`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long / string)

Minimum contrast of the components in the search
images.

Default:
"auto"

Suggested values:
"auto", 10, 20, 20, 40

Restriction:
`MinContrastComp >= 0`

**`minScoreComp`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

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

**`numLevelsComp`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long / string)

Maximum number of pyramid levels for the components.

Default:
"auto"

List of values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "auto"

**`angleStepComp`** (input_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double* / string)

Step length of the angles (resolution) for the
components.

Default:
"auto"

Suggested values:
"auto", 0.0175, 0.0349, 0.0524, 0.0698, 0.0873

Restriction:
`AngleStepComp >= 0`

**`optimizationComp`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Kind of optimization for the components.

Default:
"auto"

List of values:
"auto", "none", "point_reduction_high", "point_reduction_low", "point_reduction_medium"

**`metricComp`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Match metric used for the components.

Default:
"use_polarity"

List of values:
"ignore_color_polarity", "ignore_global_polarity", "ignore_local_polarity", "use_polarity"

**`pregenerationComp`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Complete pregeneration of the shape models for the
components if equal to *"true"*.

Default:
"false"

List of values:
"false", "true"

**`componentModelID`** (output_control)  component_model `→` [HComponentModel](HComponentModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the component model.

**`rootRanking`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Ranking of the model components expressing the
suitability to act as the root component.

## Result

If the parameters are valid, the operator
`CreateTrainedComponentModel` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
