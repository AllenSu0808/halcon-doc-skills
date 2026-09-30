# create_ncc_model (Operator)

## Name

`create_ncc_model` — Prepare an NCC model for matching.

## Signature

`create_ncc_model(Template : : NumLevels, AngleStart, AngleExtent, AngleStep, Metric : ModelID)`

## Description

The operator `create_ncc_model` prepares a template, which is
passed in the image *`Template`*, as an NCC model used for
matching using the normalized cross correlation (NCC). The ROI of
the model is passed as the domain of *`Template`*.

The model is generated using multiple image pyramid levels at
multiple rotations on each level and is stored in memory. The
output parameter *`ModelID`* is a handle for this model, which
is used in subsequent calls to [`find_ncc_model`](find_ncc_model.md).

The number of pyramid levels is determined with the parameter
*`NumLevels`*. It should be chosen as large as possible
because by this the time necessary to find the object is
significantly reduced. On the other hand, *`NumLevels`* must
be chosen such that the model is still recognizable and contains a
sufficient number of points (at least eight) on the highest pyramid
level. This can be checked using the domains of the output images
of [`gen_gauss_pyramid`](gen_gauss_pyramid.md). If not enough model points are
generated, the number of pyramid levels is reduced internally until
enough model points are found on the highest pyramid level. If this
procedure would lead to a model with no pyramid levels, i.e., if the
number of model points is already too small on the lowest pyramid
level, `create_ncc_model` returns an error message. If
*`NumLevels`* is set to *'auto'* or *0*,
`create_ncc_model` determines the number of pyramid levels
automatically. The automatically computed number of pyramid levels
can be queried using [`get_ncc_model_params`](get_ncc_model_params.md). In rare cases,
it might happen that `create_ncc_model` determines a value for
the number of pyramid levels that is too large or too small. If the
number of pyramid levels is chosen too large, the model may not be
recognized in the image or it may be necessary to select very low
parameters for `MinScore` in [`find_ncc_model`](find_ncc_model.md) in order
to find the model. If the number of pyramid levels is chosen too
small, the time required to find the model in [`find_ncc_model`](find_ncc_model.md)
may increase. In these cases, the number of pyramid levels should
be selected by inspecting the output of [`gen_gauss_pyramid`](gen_gauss_pyramid.md).
Here, `Mode` = *'constant'* and
`Scale` = *0.5* should be used.

The parameters *`AngleStart`* and *`AngleExtent`*
determine the range of possible rotations, in which the model can
occur in the image. Note that the model can only be found in this
range of angles by [`find_ncc_model`](find_ncc_model.md). The parameter
*`AngleStep`* determines the step length within the selected
range of angles. Hence, if subpixel accuracy is not specified in
[`find_ncc_model`](find_ncc_model.md), this parameter specifies the accuracy that
is achievable for the angles in [`find_ncc_model`](find_ncc_model.md).
*`AngleStep`* should be chosen based on the size of the object.
Smaller models do not possess many different discrete rotations in
the image, and hence *`AngleStep`* should be chosen larger for
smaller models. If *`AngleExtent`* is not an integer multiple
of *`AngleStep`*, *`AngleStep`* is modified accordingly.
To ensure a sampling of the range of possible rotations that is
independent of the given *`AngleStart`*, the range of possible
rotations is modified as follows: If there is no positive integer
value n such that *`AngleStart`* plus n times
*`AngleStep`* is exactly 0.0, *`AngleStart`* is decreased
by up to *`AngleStep`* and *`AngleExtent`* is increased by
*`AngleStep`*.

The model is pre-generated for the selected angle range and stored
in memory. The memory required to store the model is proportional
to the number of angle steps and the number of points in the model.
Hence, if *`AngleStep`* is too small or *`AngleExtent`*
too big, it may happen that the model no longer fits into the
(virtual) memory. In this case, either *`AngleStep`* must be
enlarged or *`AngleExtent`* must be reduced. In any case, it
is desirable that the model completely fits into the main memory,
because this avoids paging by the operating system, and hence the
time to find the object will be much smaller. Since angles can be
determined with subpixel resolution by [`find_ncc_model`](find_ncc_model.md),
*`AngleStep`* >= 1 can be
selected for models of a diameter smaller than about 200 pixels. If
*`AngleStep`* =
*'auto'* or *0* is selected,
`create_ncc_model` automatically determines a suitable angle
step length based on the size of the model. The automatically
computed angle step length can be queried using
[`get_ncc_model_params`](get_ncc_model_params.md).

The parameter *`Metric`* determines the conditions under which
the model is recognized in the image. If *`Metric`* =
*'use_polarity'*, the object in the image and the model must
have the same contrast. If, for example, the model is a bright
object on a dark background, the object is found only if it is also
brighter than the background. If *`Metric`* =
*'ignore_global_polarity'*, the object is found in the image
also if the contrast reverses globally. In the above example, the
object hence is also found if it is darker than the background. The
runtime of [`find_ncc_model`](find_ncc_model.md) will increase slightly in this
case.

The center of gravity of the domain (region) of the model image
*`Template`* is used as the origin (reference point) of the
model. A different origin can be set with
[`set_ncc_model_origin`](set_ncc_model_origin.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`Template`** (input_object)  singlechannelimage `→` object (byte / uint2)

Input image whose domain will be used to create
the model.

**`NumLevels`** (input_control)  integer `→`  (integer / string)

Maximum number of pyramid levels.

Default:
'auto'

List of values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'auto'

**`AngleStart`** (input_control)  angle.rad `→`  (real)

Smallest rotation of the pattern.

Default:
-0.39

Suggested values:
-3.14, -1.57, -0.79, -0.39, -0.20, 0.0

**`AngleExtent`** (input_control)  angle.rad `→`  (real)

Extent of the rotation angles.

Default:
0.79

Suggested values:
6.29, 3.14, 1.57, 0.79, 0.39

Restriction:
`AngleExtent >= 0`

**`AngleStep`** (input_control)  angle.rad `→`  (real / string)

Step length of the angles (resolution).

Default:
'auto'

Suggested values:
'auto', 0.0, 0.0175, 0.0349, 0.0524, 0.0698, 0.0873

Restriction:
`AngleStep >= 0 && AngleStep <= pi / 16`

**`Metric`** (input_control)  string `→`  (string)

Match metric.

Default:
'use_polarity'

List of values:
'ignore_global_polarity', 'use_polarity'

**`ModelID`** (output_control)  ncc_model `→`  (handle)

Handle of the model.

## Result

If the parameters are valid, the operator `create_ncc_model`
returns the value 2 (
H_MSG_TRUE)
. If the parameter *`NumLevels`* are
chosen such that the model contains too few points, the error 8506
is raised.

## Possible Predecessors

`draw_region`,
`reduce_domain`,
`threshold`

## Possible Successors

`find_ncc_model`,
`get_ncc_model_params`,
`clear_ncc_model`,
`write_ncc_model`,
`set_ncc_model_origin`,
`set_ncc_model_param`,
`find_ncc_models`

## Alternatives

`create_generic_shape_model`

## Module

Matching
