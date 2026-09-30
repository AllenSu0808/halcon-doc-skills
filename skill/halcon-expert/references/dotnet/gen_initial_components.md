# GenInitialComponents (Operator)

## Name

`GenInitialComponents` — Extract the initial components of a component model.

## Warning

**`GenInitialComponents` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`static void HOperatorSet.GenInitialComponents(HObject modelImage, out HObject initialComponents, HTuple contrastLow, HTuple contrastHigh, HTuple minSize, HTuple mode, HTuple genericName, HTuple genericValue)`

`HRegion HImage.GenInitialComponents(HTuple contrastLow, HTuple contrastHigh, HTuple minSize, string mode, HTuple genericName, HTuple genericValue)`

`HRegion HImage.GenInitialComponents(int contrastLow, int contrastHigh, int minSize, string mode, string genericName, double genericValue)`

## Description

In general, there are two possibilities to use
`GenInitialComponents`. The first possibility should be
chosen if the components of the component model are not known. Then
`GenInitialComponents` automatically extracts the initial
components of a component model from a model image. The second
possibility can be chosen if the components of the component model
are approximately known. Then `GenInitialComponents` can be
used to find suitable parameter values for the model feature
extraction in [`TrainModelComponents`](train_model_components.md) and
[`CreateComponentModel`](create_component_model.md). Hence, the second possibility is
comparable to the function of [`InspectShapeModel`](inspect_shape_model.md) within the
shape-based matching.

When using the first possibility, `GenInitialComponents`
extracts the initial components of a component model from a model
image *`modelImage`*. As already mentioned, this is especially
useful if the components of the component model are not known. In
this case, the resulting initial components can be used to
automatically train the component model with
[`TrainModelComponents`](train_model_components.md), which extracts the (final) model
components and the relations between them.
`GenInitialComponents` returns the initial components in a
region object tuple *`initialComponents`* that contains a
representation for each initial component in form of contour
regions.

For the automatic determination of the initial components, the
domain of the model image *`modelImage`* must contain the
entire compound object including all components. *`mode`*
specifies the method used for the automatic computation. Currently,
only the mode *"connection"* is available. In this mode the
automatic computation is performed in two steps: In the first step,
features are extracted using the parameters *`contrastLow`*,
*`contrastHigh`*, and *`minSize`*. These three parameters
define the contours of which the initial components should consist
and should be chosen such that only the significant features of the
model image are contained in the initial components.
*`contrastLow`* and *`contrastHigh`* specify the gray
value contrast of the points that should be contained in the initial
components. The contrast is a measure for local gray value
differences between the object and the background and between
different parts of the object. The model image is segmented using a
method similar to the hysteresis threshold method used in
[`EdgesImage`](edges_image.md). Here, *`contrastLow`* determines the lower
threshold, while *`contrastHigh`* determines the upper
threshold. If the same value is passed for *`contrastLow`* and
*`contrastHigh`* a simple thresholding operation is
performed. For more information about the hysteresis threshold
method, see [`HysteresisThreshold`](hysteresis_threshold.md). *`minSize`* can be
used to select only significant features for the initial components
based on the size of the connected contour regions, i.e., connected
contour regions with fewer than *`minSize`* points are
suppressed.

The resulting connected contour regions are iteratively merged in
the second step. For this, two contour regions are merged if the
distance between both regions is smaller than a certain threshold
(see below). Finally, the merged regions are returned in
*`initialComponents`* and can be used to train the component
model by passing them to [`TrainModelComponents`](train_model_components.md).

To control the internal image processing, the parameters
*`genericName`* and *`genericValue`* are used. This is
done by passing the names of the control parameters to be changed in
*`genericName`* as a list of strings. In *`genericValue`*
the values are passed at the corresponding index positions.

Normally, none of the values needs to be changed. A change should
only be applied in case of unsatisfying results of the automatic
determination of the initial components. The two parameters that can
be changed are *"merge_distance"* and
*"merge_fraction"*; both are used during the iterative
merging of contour regions (see above). First, the fraction of
contour pixels of one contour region that at most have a distance of
*"merge_distance"* from another contour region is computed. If
this fraction exceeds the value that is passed in
*"merge_fraction"* the two contour regions are merged.
Consequently, the higher *"merge_distance"* and the lower
*"merge_fraction"* is chosen the more contour regions are
merged. The default value of *"merge_distance"* is *5*
and the default value of *"merge_fraction"* is *0.5*
(corresponds to 50 percent).

When using the second possibility, i.e., the components of the
component model are approximately known, the training by using
[`TrainModelComponents`](train_model_components.md) can be performed without previously
executing `GenInitialComponents`. If this is desired, the
initial components can be specified by the user and directly passed
to [`TrainModelComponents`](train_model_components.md). Furthermore, if the components as
well as the relative movements (relations) of the components are
known, `GenInitialComponents` as well as
[`TrainModelComponents`](train_model_components.md) need not be executed. In fact, by
immediately passing the components as well as the relations to
[`CreateComponentModel`](create_component_model.md), the component model can be created
without any training. In both cases, however,
`GenInitialComponents` can be used to evaluate the effect of
the feature extraction parameters *`contrastLow`*,
*`contrastHigh`*, and *`minSize`* of
[`TrainModelComponents`](train_model_components.md) and [`CreateComponentModel`](create_component_model.md),
and hence to find suitable parameter values for a certain
application.

For this, the image regions for the (initial) components must be
explicitly given, i.e., for each (initial) component a separate
image from which the (initial) component should be created is
passed. In this case, *`modelImage`* contains multiple image
objects. The domain of each image object is used as the region of
interest for calculating the corresponding (initial) component. The
image matrix of all image objects in the tuple must be identical,
i.e., *`modelImage`* cannot be constructed in an arbitrary
manner using [`ConcatObj`](concat_obj.md), but must be created from the same
image using [`AddChannels`](add_channels.md) or equivalent calls. If this is not
the case, an error message is returned. If the parameters
*`contrastLow`*, *`contrastHigh`*, or *`minSize`*
only contain one element, this value is applied to the creation of
all (initial) components. In contrast, if different values for
different (initial) components should be used, tuples of values can
be passed for these three parameters. In this case, the tuples must
have a length that corresponds to the number of (initial)
components, i.e., the number of image objects in
*`modelImage`*. The contour regions of the (initial) components
are returned in *`initialComponents`*.

Thus, the second possibility is equivalent to the function of
[`InspectShapeModel`](inspect_shape_model.md) within the shape-based
matching. However, in contrast to [`InspectShapeModel`](inspect_shape_model.md),
`GenInitialComponents` does not return the contour regions on
multiple image pyramid levels. Therefore, if the number of pyramid
levels to be used should be chosen manually, preferably
[`InspectShapeModel`](inspect_shape_model.md) should be called individually for each
(initial) component.

For both described possibilities the parameters
*`contrastLow`*, *`contrastHigh`*, and *`minSize`*
can be automatically determined. If both hysteresis threshold should
be automatically determined, both *`contrastLow`* and
*`contrastHigh`* must be set to *"auto"*. In contrast,
if only one threshold value should be determined,
*`contrastLow`* must be set to *"auto"* while
*`contrastHigh`* must be set to an arbitrary value different
from *"auto"*.

If the input image *`modelImage`* has one channel the
representation of the model is created with the method that is used
in [`CreateComponentModel`](create_component_model.md) or
[`CreateTrainedComponentModel`](create_trained_component_model.md) for the metrics
*"use_polarity"*, *"ignore_global_polarity"*, and
*"ignore_local_polarity"*. If the input image has more than
one channel the representation is created with the method that is
used for the metric *"ignore_color_polarity"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelImage`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2)

Input image from which the initial components should
be extracted.

**`initialComponents`** (output_object)  region-array `→` [HRegion](HRegion.md)

Contour regions of initial components.

**`contrastLow`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long / string)

Lower hysteresis threshold for the contrast of the
initial components in the image.

Default:
"auto"

Suggested values:
"auto", 10, 20, 30, 40, 60, 80, 100, 120, 140, 160

Restriction:
`ContrastLow > 0`

**`contrastHigh`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long / string)

Upper hysteresis threshold for the contrast of the
initial components in the image.

Default:
"auto"

Suggested values:
"auto", 10, 20, 30, 40, 60, 80, 100, 120, 140, 160

Restriction:
`ContrastHigh > 0 && ContrastHigh >= ContrastLow`

**`minSize`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long / string)

Minimum size of the initial components.

Default:
"auto"

Suggested values:
"auto", 0, 5, 10, 20, 30, 40

Restriction:
`MinSize >= 0`

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of automatic segmentation.

Default:
"connection"

List of values:
"connection"

**`genericName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Names of optional control parameters.

Default:
[]

List of values:
"merge_distance", "merge_fraction"

**`genericValue`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Values of optional control parameters.

Default:
[]

## Result

If the parameter values are correct, the operator
`GenInitialComponents` returns the value 2 (
H_MSG_TRUE)
. If the input
is empty (no input images are available) the behavior can be set via
`set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Alternatives

`InspectShapeModel`

## Module

Matching
