# CreateComponentModel (Operator)

## Name

`CreateComponentModel` — Prepare a component model for matching based on explicitly specified
components and relations.

## Warning

**`CreateComponentModel` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`static void HOperatorSet.CreateComponentModel(HObject modelImage, HObject componentRegions, HTuple variationRow, HTuple variationColumn, HTuple variationAngle, HTuple angleStart, HTuple angleExtent, HTuple contrastLowComp, HTuple contrastHighComp, HTuple minSizeComp, HTuple minContrastComp, HTuple minScoreComp, HTuple numLevelsComp, HTuple angleStepComp, HTuple optimizationComp, HTuple metricComp, HTuple pregenerationComp, out HTuple componentModelID, out HTuple rootRanking)`

`public HComponentModel(HImage modelImage, HRegion componentRegions, HTuple variationRow, HTuple variationColumn, HTuple variationAngle, double angleStart, double angleExtent, HTuple contrastLowComp, HTuple contrastHighComp, HTuple minSizeComp, HTuple minContrastComp, HTuple minScoreComp, HTuple numLevelsComp, HTuple angleStepComp, string optimizationComp, HTuple metricComp, HTuple pregenerationComp, out HTuple rootRanking)`

`public HComponentModel(HImage modelImage, HRegion componentRegions, int variationRow, int variationColumn, double variationAngle, double angleStart, double angleExtent, int contrastLowComp, int contrastHighComp, int minSizeComp, int minContrastComp, double minScoreComp, int numLevelsComp, double angleStepComp, string optimizationComp, string metricComp, string pregenerationComp, out int rootRanking)`

`HTuple HComponentModel.CreateComponentModel(HImage modelImage, HRegion componentRegions, HTuple variationRow, HTuple variationColumn, HTuple variationAngle, double angleStart, double angleExtent, HTuple contrastLowComp, HTuple contrastHighComp, HTuple minSizeComp, HTuple minContrastComp, HTuple minScoreComp, HTuple numLevelsComp, HTuple angleStepComp, string optimizationComp, HTuple metricComp, HTuple pregenerationComp)`

`int HComponentModel.CreateComponentModel(HImage modelImage, HRegion componentRegions, int variationRow, int variationColumn, double variationAngle, double angleStart, double angleExtent, int contrastLowComp, int contrastHighComp, int minSizeComp, int minContrastComp, double minScoreComp, int numLevelsComp, double angleStepComp, string optimizationComp, string metricComp, string pregenerationComp)`

`HComponentModel HImage.CreateComponentModel(HRegion componentRegions, HTuple variationRow, HTuple variationColumn, HTuple variationAngle, double angleStart, double angleExtent, HTuple contrastLowComp, HTuple contrastHighComp, HTuple minSizeComp, HTuple minContrastComp, HTuple minScoreComp, HTuple numLevelsComp, HTuple angleStepComp, string optimizationComp, HTuple metricComp, HTuple pregenerationComp, out HTuple rootRanking)`

`HComponentModel HImage.CreateComponentModel(HRegion componentRegions, int variationRow, int variationColumn, double variationAngle, double angleStart, double angleExtent, int contrastLowComp, int contrastHighComp, int minSizeComp, int minContrastComp, double minScoreComp, int numLevelsComp, double angleStepComp, string optimizationComp, string metricComp, string pregenerationComp, out int rootRanking)`

## Description

`CreateComponentModel` prepares patterns, which are passed
in the form of a model image *`modelImage`* and several regions
*`componentRegions`*, as a component model for matching. The
output parameter *`componentModelID`* is a handle for this
model, which is used in subsequent calls to
[`FindComponentModel`](find_component_model.md). In contrast to
[`CreateTrainedComponentModel`](create_trained_component_model.md), no preceding training with
[`TrainModelComponents`](train_model_components.md) needs to be performed before calling
`CreateComponentModel`.

Each of the regions passed in *`componentRegions`* describes a
separate model component. Later, the index of a component region in
*`componentRegions`* is used to denote the model component.
The reference point of a component is the center of gravity of its
associated region, which is passed in *`componentRegions`*. It
can be calculated by calling [`AreaCenter`](area_center.md).

The relative movements (relations) of the model components can be
set by passing *`variationRow`*, *`variationColumn`*, and
*`variationAngle`*. Because directly passing the relations is
complicated, instead of the relations the variations of the model
components are passed. The variations describe the movements of the
components independently from each other relative to their poses in
the model image *`modelImage`*. The parameters
*`variationRow`* and *`variationColumn`* describe the
movement of the components in row and column direction by
$\pm\tfrac{1}{2}\mathrm{VariationRow}$ ![figure](../assets/19716e15731413d8.svg) and
$\pm\frac{1}{2}VariationColumn$ ![figure](../assets/5f9f712f3872809a.svg),
respectively.
The parameter *`variationAngle`* describes the angle variation
of the component by
$\pm \tfrac{1}{2} VariationAngle$ ![figure](../assets/0187e898088fb74a.svg).
Based on these values, the relations are automatically computed. The three
parameters must either contain one element, in which case the
parameter is used for all model components, or must contain the same
number of elements as *`componentRegions`*, in which case each
parameter element refers to the corresponding model component in
*`componentRegions`*.

The parameters *`angleStart`* and *`angleExtent`*
determine the range of possible rotations of the component model in
an image.

Internally, a separate shape model is built for each model component
(see [`CreateShapeModel`](create_shape_model.md)). Therefore, the parameters
*`contrastLowComp`*, *`contrastHighComp`*,
*`minSizeComp`*, *`minContrastComp`*,
*`minScoreComp`*, *`numLevelsComp`*,
*`angleStepComp`*, *`optimizationComp`*,
*`metricComp`*, and *`pregenerationComp`* correspond to
the parameters of [`CreateShapeModel`](create_shape_model.md), with the following
differences: First, in the parameter `contrast` of
[`CreateShapeModel`](create_shape_model.md) the upper as well as the lower threshold
for the hysteresis threshold method can be passed. Additionally, a
third value, which suppresses small connected contour regions, can
be passed. In contrast, the operator `CreateComponentModel`
offers three separate parameters *`contrastHighComp`*,
*`contrastLowComp`*, and *`minScoreComp`* in order to set
these three values. Consequently, also the automatic computation of
the contrast threshold(s) is different. If both hysteresis threshold
should be automatically determined, both *`contrastLowComp`*
and *`contrastHighComp`* must be set to *"auto"*. In
contrast, if only one threshold value should be determined,
*`contrastLowComp`* must be set to *"auto"* while
*`contrastHighComp`* must be set to an arbitrary value
different from *"auto"*. Secondly, the parameter
`optimization` of [`CreateShapeModel`](create_shape_model.md) provides the
possibility to reduce the number of model points as well as the
possibility to completely pregenerate the shape model. In contrast,
the operator [`CreateTrainedComponentModel`](create_trained_component_model.md) uses a separate
parameter *`pregenerationComp`* in order to decide whether the
shape models should be completely pregenerated or not. A third
difference concerning the parameter *`minScoreComp`* should be
noted. When using the shape-based matching, this parameter needs not
be passed when preparing the shape model using
[`CreateShapeModel`](create_shape_model.md), but only during the search using
[`FindShapeModel`](find_shape_model.md). In contrast, when preparing the component
model it is favorable to analyze rotational symmetries of the model
components and similarities between the model components. However,
this analysis only leads to meaningful results if the value for
*`minScoreComp`* that is used during the search (see
[`FindComponentModel`](find_component_model.md)) is already approximately known.

In addition to the parameters *`contrastLowComp`*,
*`contrastHighComp`*, and *`minSizeComp`* also the
parameters *`minContrastComp`*, *`numLevelsComp`*,
*`angleStepComp`*, and *`optimizationComp`* can be
automatically determined by passing *"auto"* for the
respective parameters.

All component-specific input parameters (parameter names terminate
with the suffix `Comp`) must either contain one element, in
which case the parameter is used for all model components, or must
contain the same number of elements as the number of regions in
*`componentRegions`*, in which case each parameter element
refers to the corresponding element in *`componentRegions`*.

In addition to the individual shape models, the component model also
contains information about the way the single model components must
be searched relative to each other using
[`FindComponentModel`](find_component_model.md) in order to minimize the computation
time of the search. For this, the components are represented in a
tree structure. First, the component that stands at the root of this
search tree (root component) is searched. Then, the remaining
components are searched relative to the pose of their predecessor in
the search tree.

The root component can be passed as an input parameter of
[`FindComponentModel`](find_component_model.md) during the search. To what extent a model
component is suited to act as the root component depends on several factors.
In principle, a model component that can be found in the image with a high
probability should be chosen. Therefore, a component that is sometimes
occluded to a high degree or that is missing in some cases is not well suited
to act as the root component. Additionally, the computation time that is
associated with the root component during the search can serve as a
criterion. A ranking of the model components that is based on the latter
criterion is returned in *`rootRanking`*. In this parameter the indices
of the model components are sorted in descending order according to their
associated search time, i.e., *`rootRanking`*[0] contains the index of
the model component that, chosen as root component, allows the fastest
search. Note that the ranking returned in *`rootRanking`* represents
only a coarse estimation. Furthermore, the calculation of the root ranking
assumes that the image size as well as the value of the system parameter
*"border_shape_models"* are identical when calling
`CreateComponentModel` and [`FindComponentModel`](find_component_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`modelImage`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / uint2)

Input image from which the shape models of the
model components should be created.

**`componentRegions`** (input_object)  region-array `→` [HRegion](HRegion.md)

Input regions from which the shape models of the
model components should be created.

**`variationRow`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Variation of the model components in row direction.

Suggested values:
0, 1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 100, 150

Restriction:
`VariationRow >= 0`

**`variationColumn`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Variation of the model components in column direction.

Suggested values:
0, 1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 100, 150

Restriction:
`VariationColumn >= 0`

**`variationAngle`** (input_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Angle variation of the model components.

Suggested values:
0.0, 0.017, 0.035, 0.05, 0.07, 0.09, 0.17, 0.35, 0.52, 0.67, 0.87

Restriction:
`VariationAngle >= 0`

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

**`contrastLowComp`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long / string)

Lower hysteresis threshold for the contrast of the
components in the model image.

Default:
"auto"

Suggested values:
"auto", 10, 20, 30, 40, 60, 80, 100, 120, 140, 160

Restriction:
`ContrastLowComp > 0`

**`contrastHighComp`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long / string)

Upper hysteresis threshold for the contrast of the
components in the model image.

Default:
"auto"

Suggested values:
"auto", 10, 20, 30, 40, 60, 80, 100, 120, 140, 160

Restriction:
`ContrastHighComp > 0 && ContrastHighComp >= ContrastLowComp`

**`minSizeComp`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long / string)

Minimum size of the contour regions in the model.

Default:
"auto"

Suggested values:
"auto", 0, 5, 10, 20, 30, 40

Restriction:
`MinSizeComp >= 0`

**`minContrastComp`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long / string)

Minimum contrast of the components in the search
images.

Default:
"auto"

Suggested values:
"auto", 10, 20, 20, 40

Restriction:
`MinContrastComp <= ContrastLowComp && MinContrastComp >= 0`

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
`CreateComponentModel` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
