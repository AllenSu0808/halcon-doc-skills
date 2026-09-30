# create_uncalib_descriptor_model (Operator)

## Name

`create_uncalib_descriptor_model` — Prepare a descriptor model for interest point matching.

## Signature

`create_uncalib_descriptor_model(Template : : DetectorType, DetectorParamName, DetectorParamValue, DescriptorParamName, DescriptorParamValue, Seed : ModelID)`

## Description

The operator `create_uncalib_descriptor_model` prepares a
descriptor model of an image region, which is passed in the image
*`Template`*, that can be used for descriptor-based matching.
By a subsequent call of [`find_uncalib_descriptor_model`](find_uncalib_descriptor_model.md) a
projective 2D transformation (homography) from *`Template`* to
a search image can be obtained. The center of gravity of the domain
region in *`Template`* is used as an origin of the model. In
contrast to [`create_calib_descriptor_model`](create_calib_descriptor_model.md), no calibrated
camera is needed and hence the result of a subsequent matching is
a 2D projection. Note that the part of the object that is visible in the
*`Template`* image needs to be planar.

The descriptor model describes a set of points of interest. It
stores their locations and discriminative descriptions of their local
gray value neighborhood. The interest point extraction is parametrized
by *`DetectorType`*, *`DetectorParamName`* and
*`DetectorParamValue`*. The respective descriptor around the
interest points is parametrized by *`DescriptorParamName`* and
*`DescriptorParamValue`*. The parameter *`Seed`* seeds the
random number generator, which is used during the construction of the
descriptor implemented with *randomized ferns*. The returned
*`ModelID`* is a reference to the generated
descriptor model. This model can be used for an efficient
detection of instances of the learned template with
[`find_uncalib_descriptor_model`](find_uncalib_descriptor_model.md), allowing perspective
transformation between model and search image. As descriptor-based
matching relies on the existence of stable and discriminative points
of interest, the object to be detected must be textured, but not in a
repetitive way.

### Detector parameters

As mentioned, the detector is used for the extraction of stable
interest points within the image. By the parameter
*`DetectorType`*, it is possible to select the interest point
operator to be used. Currently, [`points_lepetit`](points_lepetit.md),
[`points_harris`](points_harris.md), and its binomial approximation
[`points_harris_binomial`](points_harris_binomial.md) are supported ('lepetit', 'harris',
'harris_binomial'). In case of templates or search images with a
low contrast, one of the Harris point operators should be used.
Depending on the selected *`DetectorType`*, appropriate
parameter names and values can be set in *`DetectorParamName`*
and *`DetectorParamValue`*.

Possible parameter names for *`DetectorParamName`* and corresponding
default values are:

- ***'lepetit'* :** —
  - —

    [*'radius'*, *'check_neighbor'*,
    *'min_check_neighbor_diff'*, *'min_score'*,
    *'subpix'*]
  - —

    *[ 3, 1, 15, 30, 'interpolation']*
- ***'harris'* :** —
  - —

    [*'sigma_grad'*, *'sigma_smooth'*, *'alpha'*,
    *'threshold'*]
  - —

    *[0.7, 2.0, 0.08, 1000]*
- ***'harris_binomial'* :** —
  - —

    [*'mask_size_grd'*, *'mask_size_smooth'*,
    *'alpha'*, *'threshold'*, *'subpix'*]
  - —

    *[5, 15, 0.08, 1000, 'on']*

Further details on the meaning of those parameters can be found in the
descriptions of [`points_harris`](points_harris.md), [`points_harris_binomial`](points_harris_binomial.md)
and [`points_lepetit`](points_lepetit.md), respectively. If an empty tuple is passed
or a parameter is not provided in *`DetectorParamName`*, the above
mentioned default values are taken.

While adjusting the operator parameters it should be aimed that a set of
50 to 450 feature points is extracted (depending on the texture and size
of *`Template`*), which are uniformly distributed over the
template's ROI. Therefore, it is recommended to run the point operator
of choice in advance and visualize the results by
[`gen_cross_contour_xld`](gen_cross_contour_xld.md). In most cases it is sufficient to use the
default setting.

### Descriptor parameters

A point descriptor is a classifier, which builds characteristic
descriptions of the gray-value neighborhood for interest points.
Currently the descriptor is implemented with the so-called
*randomized ferns*, which learns the polarity of the
gray-value differences of pairs of pixels certain at *random*
locations in the surrounding area of the interest point. The descriptor
is later used in [`find_uncalib_descriptor_model`](find_uncalib_descriptor_model.md) to classify
interest points in the search image, or in other words: to identify
(match) potential model points in the search image.

The descriptor needs to store only the projectively *stable*
interest points (which will appear in many projective views of the
template). To assess the *stability* of the interest points,
a simulation is performed: *`Template`* undergoes many affine
transformations and points that can be extracted in most of the views
are considered *stable*. The affine transformations are a good
approximation of the projective transformations within a local
neighborhood of the interest points.

The following descriptor parameters can be set with
*`DescriptorParamName`* and *`DescriptorParamValue`*:

**Descriptor size parameters:**

- ***'depth'*:** —

  depth of a classification fern. A deeper randomized fern can better
  discriminate interest points. However, the memory requirement for the
  fern grows by a factor 2 to the power of *'depth'*.
  Typical values are [*5* .. *11*],
  default value is *11*.
- ***'number_ferns'*:** —

  number of fern structures used. Using more ferns increases the
  recognition robustness, however it also increases the runtime of
  the matching. If the memory needed for the descriptor should be small,
  many ferns with only a small depth should be used (e.g.,
  *'number_ferns'*=*150*, *'depth'*=*5*).
  If detection speed is more important, fewer ferns of larger depth
  should be used (e.g., *'number_ferns'*=*10*,
  *'depth'*=*11*).
  Typical values are [*1* .. *150*],
  default value is *30*.
- ***'patch_size'*:** —

  side length of a quadratic neighborhood describing a point of interest.
  Too large values of this parameter can influence the run time.
  Typical values are [*15* .. *33*],
  default value is *17*.

Summing up, the parameters *'depth'*, *'number_ferns'*
and *'patch_size'* allow a transparent control over detection
robustness, speed and memory consumption.

**Simulation parameters:**

- ***'tilt'*:** —

  switches on or off the projective
  transformations during the simulation phase. When switched on, the
  robustness of the model is improved and objects with bigger tilts can
  be found. When switched off, training time can be significantly reduced
  and the model is still able to recognize projectively invariant objects.
  Possible values are [*'on'*, *'off'*],
  default value is *'on'*.
- ***'min_rot'*:** —

  minimal angle of rotation around
  the normal vector of *`Template`*.
  Typical values are [*-180* .. *0*],
  default value is *-180*.
- ***'max_rot'*:** —

  maximal angle of rotation around
  the normal vector of *`Template`*.
  Typical values are [*0* .. *180*],
  default value is *180*.
- ***'min_scale'*:** —

  minimal scale of
  *`Template`*.
  Typical values are [*0.1* .. *1.0*],
  default value is *0.5*.
- ***'max_scale'*:** —

  maximal scale of
  *`Template`*.
  Typical values are [*1.0* .. *3.5*],
  default value is *1.4*.

The parameters *'min_rot'*, *'max_rot'*,
*'min_scale'*, and *'max_scale'* allow to manually set
which affine transformed views of the template are used to train the
descriptor. Setting these parameters is useful to reduce training time
especially in combination with the parameter *'tilt'*. Be aware
that these parameters have direct influence on the results of
[`find_uncalib_descriptor_model`](find_uncalib_descriptor_model.md) and therefore have to be set
carefully. If, for example, the range of rotation is restricted from
*'min_rot'* = -10 to *'max_rot'* = 10 it is not possible
to find views of *`Template`* rotated by an angle outside that
scope. A limited training range requires less ferns / ferns' depths to
find *`Template`*. In such a case the number and depth of the
ferns can be further reduced, which optimizes the model.

### Remarks

Please note that depending on your hardware, the processing time for
training the randomized ferns can vary between several seconds to some
minutes. Therefore, a once trained model can be saved and loaded with
[`write_descriptor_model`](write_descriptor_model.md) and [`read_descriptor_model`](read_descriptor_model.md).

The parameters and the location of the final descriptor points can be
determined with [`get_descriptor_model_params`](get_descriptor_model_params.md) and
[`get_descriptor_model_points`](get_descriptor_model_points.md).

`create_uncalib_descriptor_model` stores the detector type,
detector parameters, and descriptor parameters, which are used in
every succeeding call of [`find_uncalib_descriptor_model`](find_uncalib_descriptor_model.md).
The reference point (origin) of the model is the center of gravity
of the template's ROI. Its coordinates can be changed by
[`set_descriptor_model_origin`](set_descriptor_model_origin.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`Template`** (input_object)  singlechannelimage `→` object (byte / uint2)

Input image whose domain will be used to create
the model.

**`DetectorType`** (input_control)  string `→`  (string)

The type of the detector.

Default:
'lepetit'

List of values:
'harris', 'harris_binomial', 'lepetit'

**`DetectorParamName`** (input_control)  attribute.name-array `→`  (string)

The detector's parameter names.

Default:
[]

List of values:
'alpha', 'check_neighbor', 'mask_size_grd', 'mask_size_smooth', 'min_check_neighbor_diff', 'min_score', 'radius', 'sigma_grad', 'sigma_smooth', 'subpix', 'threshold'

**`DetectorParamValue`** (input_control)  attribute.value-array `→`  (integer / real / string)

Values of the detector's parameters.

Default:
[]

Suggested values:
0.08, 1, 1.2, 3, 15, 30, 1000, 'on', 'off', 'none', 'interpolation'

**`DescriptorParamName`** (input_control)  attribute.name-array `→`  (string)

The descriptor's parameter names.

Default:
[]

List of values:
'depth', 'max_rot', 'max_scale', 'min_rot', 'min_scale', 'number_ferns', 'patch_size', 'tilt'

**`DescriptorParamValue`** (input_control)  attribute.value-array `→`  (integer / real / string)

Values of the descriptor's parameters.

Default:
[]

Suggested values:
0.5, 1.4, 11, 21, 30, -180, 180, 'on', 'off'

**`Seed`** (input_control)  integer `→`  (integer)

The seed for the random number generator.

Default:
42

**`ModelID`** (output_control)  descriptor_model `→`  (handle)

The handle to the descriptor model.

## Possible Predecessors

`points_lepetit`,
`points_harris`,
`reduce_domain`

## Possible Successors

`get_descriptor_model_params`,
`find_uncalib_descriptor_model`

## See also

`get_descriptor_model_params`,
`find_uncalib_descriptor_model`

## References

V. Lepetit and P. Fua: “Keypoint Recognition using Randomized Trees.“
IEEE Transactions on Pattern Analysis and Machine Intelligence, Vol. 28,
Nr. 9, pp. 1465-1479, 2006.
  
M. Ozuysal, P. Fua, and V. Lepetit: “Fast Keypoint Recognition in Ten Lines
of Code.“
In Proceedings of Conference on Computer Vision and Pattern Recognition,
2007.

## Module

Matching
