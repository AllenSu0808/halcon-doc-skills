# gen_initial_components (Operator)

## Name

`gen_initial_components` — Extract the initial components of a component model.

## Warning

**`gen_initial_components` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`gen_initial_components(ModelImage : InitialComponents : ContrastLow, ContrastHigh, MinSize, Mode, GenericName, GenericValue : )`

## Description

In general, there are two possibilities to use
`gen_initial_components`. The first possibility should be
chosen if the components of the component model are not known. Then
`gen_initial_components` automatically extracts the initial
components of a component model from a model image. The second
possibility can be chosen if the components of the component model
are approximately known. Then `gen_initial_components` can be
used to find suitable parameter values for the model feature
extraction in [`train_model_components`](train_model_components.md) and
[`create_component_model`](create_component_model.md). Hence, the second possibility is
comparable to the function of [`inspect_shape_model`](inspect_shape_model.md) within the
shape-based matching.

When using the first possibility, `gen_initial_components`
extracts the initial components of a component model from a model
image *`ModelImage`*. As already mentioned, this is especially
useful if the components of the component model are not known. In
this case, the resulting initial components can be used to
automatically train the component model with
[`train_model_components`](train_model_components.md), which extracts the (final) model
components and the relations between them.
`gen_initial_components` returns the initial components in a
region object tuple *`InitialComponents`* that contains a
representation for each initial component in form of contour
regions.

For the automatic determination of the initial components, the
domain of the model image *`ModelImage`* must contain the
entire compound object including all components. *`Mode`*
specifies the method used for the automatic computation. Currently,
only the mode *'connection'* is available. In this mode the
automatic computation is performed in two steps: In the first step,
features are extracted using the parameters *`ContrastLow`*,
*`ContrastHigh`*, and *`MinSize`*. These three parameters
define the contours of which the initial components should consist
and should be chosen such that only the significant features of the
model image are contained in the initial components.
*`ContrastLow`* and *`ContrastHigh`* specify the gray
value contrast of the points that should be contained in the initial
components. The contrast is a measure for local gray value
differences between the object and the background and between
different parts of the object. The model image is segmented using a
method similar to the hysteresis threshold method used in
[`edges_image`](edges_image.md). Here, *`ContrastLow`* determines the lower
threshold, while *`ContrastHigh`* determines the upper
threshold. If the same value is passed for *`ContrastLow`* and
*`ContrastHigh`* a simple thresholding operation is
performed. For more information about the hysteresis threshold
method, see [`hysteresis_threshold`](hysteresis_threshold.md). *`MinSize`* can be
used to select only significant features for the initial components
based on the size of the connected contour regions, i.e., connected
contour regions with fewer than *`MinSize`* points are
suppressed.

The resulting connected contour regions are iteratively merged in
the second step. For this, two contour regions are merged if the
distance between both regions is smaller than a certain threshold
(see below). Finally, the merged regions are returned in
*`InitialComponents`* and can be used to train the component
model by passing them to [`train_model_components`](train_model_components.md).

To control the internal image processing, the parameters
*`GenericName`* and *`GenericValue`* are used. This is
done by passing the names of the control parameters to be changed in
*`GenericName`* as a list of strings. In *`GenericValue`*
the values are passed at the corresponding index positions.

Normally, none of the values needs to be changed. A change should
only be applied in case of unsatisfying results of the automatic
determination of the initial components. The two parameters that can
be changed are *'merge_distance'* and
*'merge_fraction'*; both are used during the iterative
merging of contour regions (see above). First, the fraction of
contour pixels of one contour region that at most have a distance of
*'merge_distance'* from another contour region is computed. If
this fraction exceeds the value that is passed in
*'merge_fraction'* the two contour regions are merged.
Consequently, the higher *'merge_distance'* and the lower
*'merge_fraction'* is chosen the more contour regions are
merged. The default value of *'merge_distance'* is *5*
and the default value of *'merge_fraction'* is *0.5*
(corresponds to 50 percent).

When using the second possibility, i.e., the components of the
component model are approximately known, the training by using
[`train_model_components`](train_model_components.md) can be performed without previously
executing `gen_initial_components`. If this is desired, the
initial components can be specified by the user and directly passed
to [`train_model_components`](train_model_components.md). Furthermore, if the components as
well as the relative movements (relations) of the components are
known, `gen_initial_components` as well as
[`train_model_components`](train_model_components.md) need not be executed. In fact, by
immediately passing the components as well as the relations to
[`create_component_model`](create_component_model.md), the component model can be created
without any training. In both cases, however,
`gen_initial_components` can be used to evaluate the effect of
the feature extraction parameters *`ContrastLow`*,
*`ContrastHigh`*, and *`MinSize`* of
[`train_model_components`](train_model_components.md) and [`create_component_model`](create_component_model.md),
and hence to find suitable parameter values for a certain
application.

For this, the image regions for the (initial) components must be
explicitly given, i.e., for each (initial) component a separate
image from which the (initial) component should be created is
passed. In this case, *`ModelImage`* contains multiple image
objects. The domain of each image object is used as the region of
interest for calculating the corresponding (initial) component. The
image matrix of all image objects in the tuple must be identical,
i.e., *`ModelImage`* cannot be constructed in an arbitrary
manner using [`concat_obj`](concat_obj.md), but must be created from the same
image using [`add_channels`](add_channels.md) or equivalent calls. If this is not
the case, an error message is returned. If the parameters
*`ContrastLow`*, *`ContrastHigh`*, or *`MinSize`*
only contain one element, this value is applied to the creation of
all (initial) components. In contrast, if different values for
different (initial) components should be used, tuples of values can
be passed for these three parameters. In this case, the tuples must
have a length that corresponds to the number of (initial)
components, i.e., the number of image objects in
*`ModelImage`*. The contour regions of the (initial) components
are returned in *`InitialComponents`*.

Thus, the second possibility is equivalent to the function of
[`inspect_shape_model`](inspect_shape_model.md) within the shape-based
matching. However, in contrast to [`inspect_shape_model`](inspect_shape_model.md),
`gen_initial_components` does not return the contour regions on
multiple image pyramid levels. Therefore, if the number of pyramid
levels to be used should be chosen manually, preferably
[`inspect_shape_model`](inspect_shape_model.md) should be called individually for each
(initial) component.

For both described possibilities the parameters
*`ContrastLow`*, *`ContrastHigh`*, and *`MinSize`*
can be automatically determined. If both hysteresis threshold should
be automatically determined, both *`ContrastLow`* and
*`ContrastHigh`* must be set to *'auto'*. In contrast,
if only one threshold value should be determined,
*`ContrastLow`* must be set to *'auto'* while
*`ContrastHigh`* must be set to an arbitrary value different
from *'auto'*.

If the input image *`ModelImage`* has one channel the
representation of the model is created with the method that is used
in [`create_component_model`](create_component_model.md) or
[`create_trained_component_model`](create_trained_component_model.md) for the metrics
*'use_polarity'*, *'ignore_global_polarity'*, and
*'ignore_local_polarity'*. If the input image has more than
one channel the representation is created with the method that is
used for the metric *'ignore_color_polarity'*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ModelImage`** (input_object)  (multichannel-)image(-array) `→` object (byte / uint2)

Input image from which the initial components should
be extracted.

**`InitialComponents`** (output_object)  region-array `→` object

Contour regions of initial components.

**`ContrastLow`** (input_control)  integer(-array) `→`  (integer / string)

Lower hysteresis threshold for the contrast of the
initial components in the image.

Default:
'auto'

Suggested values:
'auto', 10, 20, 30, 40, 60, 80, 100, 120, 140, 160

Restriction:
`ContrastLow > 0`

**`ContrastHigh`** (input_control)  integer(-array) `→`  (integer / string)

Upper hysteresis threshold for the contrast of the
initial components in the image.

Default:
'auto'

Suggested values:
'auto', 10, 20, 30, 40, 60, 80, 100, 120, 140, 160

Restriction:
`ContrastHigh > 0 && ContrastHigh >= ContrastLow`

**`MinSize`** (input_control)  integer(-array) `→`  (integer / string)

Minimum size of the initial components.

Default:
'auto'

Suggested values:
'auto', 0, 5, 10, 20, 30, 40

Restriction:
`MinSize >= 0`

**`Mode`** (input_control)  string `→`  (string)

Type of automatic segmentation.

Default:
'connection'

List of values:
'connection'

**`GenericName`** (input_control)  string(-array) `→`  (string)

Names of optional control parameters.

Default:
[]

List of values:
'merge_distance', 'merge_fraction'

**`GenericValue`** (input_control)  number(-array) `→`  (real / integer)

Values of optional control parameters.

Default:
[]

## Result

If the parameter values are correct, the operator
`gen_initial_components` returns the value 2 (
H_MSG_TRUE)
. If the input
is empty (no input images are available) the behavior can be set via
`set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Alternatives

`inspect_shape_model`

## Module

Matching
