# photometric_stereo (Operator)

## Name

`photometric_stereo` — Reconstruct a surface according to the photometric stereo technique.

## Signature

`def photometric_stereo(images: HObject, slants: Sequence[Union[float, int]], tilts: Sequence[Union[float, int]], result_type: Sequence[str], reconstruction_method: str, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, float, str]]) -> Tuple[HObject, HObject, HObject]`

## Description

`photometric_stereo` can be used to separate the three-dimensional shape
of an object from its two-dimensional texture, e.g., its print image. The
operator requires at least three images of the same object taken with
different and known directions of illumination. Note, that the point of view
of the camera must be the same for all images.

The three-dimensional shape of the object is primarily computed as the local
gradients of the three-dimensional surface. Those gradients can be further
integrated to obtain a height field, i.e., an image in which the pixel values
correspond to a relative height. The two-dimensional texture is called
albedo and corresponds to the local light absorption and reflection
characteristics of the surface exclusive of any shading effect.

**Typical applications of photometric stereo**

Typical applications of photometric stereo are to detect small
inconsistencies in a surface that represent, e.g., defects, or to exclude the
influence of the direction of light from images that are used, e.g., for the
print inspection of non flat characters. Note that photometric stereo is not
suitable for the reconstruction of absolute heights, i.e., it is no
alternative to typical 3D reconstruction algorithms like depth from focus
or sheet of light.

**Limitations of photometric stereo**

`photometric_stereo` is based on the algorithm of Woodham and
therefore assumes on the one hand that the camera performs an orthoscopic
projection. That is, you must use a telecentric lens or a lens with a long
focal distance. On the other hand, it assumes that each of the light sources
delivers a parallel and uniform beam of light. That is, you must use
telecentric illumination sources with uniform intensity or, as an
alternative, distant point light sources. Additionally, the object must have
Lambertian reflectance characteristics, i.e., it must reflect incoming light
in a diffuse way. Objects or regions of an object that have specular
reflectance characteristics (i.e., mirroring or glossy surfaces) cannot be
processed correctly and thus lead to erroneous results.

**The acquisition setup**

The camera with a telecentric lens must be placed orthogonally, i.e.,
perpendicular, to the scene that should be reconstructed. The orientation of
the camera with respect to the scene must not change during the acquisition
of the images. In contrast, the orientation of the illumination with respect
to the camera must change for at least three gray value images.

**Specifying the directions of illumination**

For each image, the directions of illumination must be specified as angles
within the parameters *`slants`* and *`tilts`*, which describe the
direction of the illumination in relation to the scene. To understand the
meaning of the parameters *`slants`* and *`tilts`*, remember that
the illumination source is assumed to produce parallel light rays, the camera
has a telecentric lens, and the camera is placed orthogonal to the scene to
reconstruct:

- ***`slants`*** —

  The *`slants`* angle is the angle between the optical
  axis of the camera and the direction of the illumination.

  ![figure](../assets/0657b1c61dffaf51.svg)

  Side view
- ***`tilts`*** —

  The *`tilts`* angle is measured within the object plane or any plane
  that is parallel to it, e.g., the image plane. In particular, it
  describes the angle between the direction that points from the center
  of the image to the right and the direction of light that is projected
  into the plane. That is, when looking at the image (or the
  corresponding scene), a tilt angle of 0 means that the light comes from
  the right, a tilt angle of 90 means that the light is coming from the
  top, a tilt angle of 180 means that the light is coming from the left,
  etc.

  ![figure](../assets/8a413ea3cd7f48e9.svg)

  Top view

As stated before, photometric stereo requires at least three images with
different directions of illumination. However, the three-dimensional geometry
of objects typically leads to shadow casting. In the shadow regions, the
number of effectively available directions of illumination is reduced, which
leads to ambiguities. To nevertheless get a robust result, redundancy is
needed. Therefore, typically more than three light sources with different
directions should be used. But note that an increasing number of illumination
directions also leads to a higher number of images to be processed and
therefore to a higher processing time. In most applications, a number of
four to six light sources is reasonable. As a rule of thumb, the slant angles
should be chosen between 30° and 60°. The tilt angles typically should be
equally distributed around the object to be measured. Please note that the
directions of illumination must be selected such that they do not lie in the
same plane (i.e., the illumination directions must be independent), otherwise
the computing fails and an exception is thrown.

**Input images and domains of definition**

The input images must be provided in an image array (*`images`*). Each
image must have been taken with a different direction of illumination as
stated above. If the images are primarily stored in a multi-channel image,
they can be easily converted to an image array using
[`image_to_channels`](image_to_channels.md). As an alternative, the image array can be created
using [`concat_obj`](concat_obj.md).

`photometric_stereo` relies on the evaluation of the "photometric
information", i.e., the gray values stored in the images. Therefore, this
information should be unbiased and accurate. We recommend to ensure that the
camera that is used to acquire the images has a linear characteristic. You
can use the operator [`radiometric_self_calibration`](radiometric_self_calibration.md) to determine the
characteristic of your camera and the operator [`lut_trans`](lut_trans.md) to correct
the gray value information in case of a non linear
characteristic. Additionally, if accurate measurements are required, we
recommend to utilize the full dynamic range of the camera since this leads to
more accurate gray value information. For the same reason, using images with
a bit depth higher than 8 (e.g., uint2 images instead of byte images) leads
to a better accuracy.

The domain of definition of the input images determines which algorithm is
used internally to process the *`images`*. Three algorithms are
available:

- If all images have a full domain, the fastest algorithm is used. This
  mode is recommended for most applications.
- If the input images share the same reduced domain of definition, only the
  pixels within the domain are processed. This mode can be used to exclude
  areas of the object from all images. Typically, areas are excluded that
  are known to show non-Lambertian reflectance characteristics or that are
  of no interest, e.g., holes in the surface.
- If images with distinct domains of definition are provided, only the gray
  values that are contained in the domains are used in the respective
  images. Then, only those pixels are processed that have independent slant
  and tilt angles in at least three images. This mode is suitable, e.g., to
  exclude specific regions of individual images from the processing. These
  can be, e.g., areas of the object for which is known that they show
  non-Lambertian reflectance characteristics or regions for which is known
  that they contain biased photometric information, e.g., shadows. To
  exclude such regions leads to more accurate results. Please note that
  this last mode requires significantly more processing time than the modes
  that use the full domain or the same domain for all images.

**Output images**

The operator can return the images for the reconstructed *`gradient`*, *`albedo`*,
and the *`height_field`* of the surface:

- The *`gradient`* image is a vector field that contains the
  partial derivative of the surface. Note that *`gradient`* can be
  used as input to [`reconstruct_height_field_from_gradient`](reconstruct_height_field_from_gradient.md). For
  visualization purposes, instead of the surface gradients normalized
  surface normals can be returned. Then, *`result_type`* must be
  set to *"normalized_surface_normal"*
  (legacy: *"normalized_gradient"*) instead of
  *"gradient"*. Here, the row and column components represent the
  row and column components of the normalized surface normal. If
  *`result_type`* is set to *"all"*, the default mode, i.e.,
  *"gradient"* and not *"normalized_surface_normal"* is used.
- The *`albedo`* image describes the ratio of reflected radiation
  to incident radiation and has a value between one (white surface) and
  zero (black surface). Thus, the albedo is a characteristic of the
  surface. For example, for a printed surface it corresponds to the
  print image exclusive of any influences of the incident light
  (shading).
- The *`height_field`* image is an image in which the pixel values
  correspond to a relative height.

By default, all of these iconic objects are returned, i.e., the parameter
*`result_type`* is set to *"all"*. In case that only some of these
results are needed, the parameter *`result_type`* can be set to a tuple
specifying only the required results among the values *"gradient"*,
*"albedo"*, and *"height_field"*. Note that in certain
applications like surface inspection tasks only the *`gradient`* or
*`albedo`* images are required. Here, one can significantly increase the
processing speed by not reconstructing the surface, i.e., by passing only
*"gradient"* and *"albedo"* but not *"height_field"* to
*`result_type`*.

Note that internally `photometric_stereo` first determines the gradient
values and, if required, integrates these values in order to obtain the
height field. This integration is performed by the same algorithms that are
provided by the operator [`reconstruct_height_field_from_gradient`](reconstruct_height_field_from_gradient.md) and
that can be controlled by the parameters *`reconstruction_method`*,
*`gen_param_name`*, and *`gen_param_value`*. Please, refer to the
operator [`reconstruct_height_field_from_gradient`](reconstruct_height_field_from_gradient.md) for more information
on these parameters. If *`result_type`* is set such that
*"height_field"* is not one of the results, the parameters
*`reconstruction_method`*, *`gen_param_name`*, and
*`gen_param_value`* are ignored.

## Attention

Note that `photometric_stereo` assumes square pixels. Additionally, it
assumes that the heights are computed on a lattice with step width 1 in
object space. If this is not the case, i.e., if the pixel size of the camera
projected into the object space differs from 1, the returned height values
must be multiplied by the actual step width (value of the pixel size
projected into the object space). The size of the pixel in object space is
computed by dividing the size of the pixel in the camera by the magnification
of the (telecentric) lens.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`images`** (input_object)  singlechannelimage(-array) `→` HObject (byte / uint2)

Array with at least three input images with different
directions of illumination.

**`height_field`** (output_object)  image `→` HObject (real)

Reconstructed height field.

**`gradient`** (output_object)  image `→` HObject (vector_field)

The gradient field of the surface.

**`albedo`** (output_object)  image `→` HObject (real)

The albedo of the surface.

**`slants`** (input_control)  angle.deg-array `→` Sequence[Union[float, int]]

Angle between the camera and the direction of
illumination (in degrees).

Default:
45.0

Suggested values:
1.0, 5.0, 10.0, 20.0, 40.0, 60.0, 90.0

Value range:
`0.0
≤
slants
≤
180.0` (lin)

Minimum increment:
0.01

Recommended increment:
10.0

**`tilts`** (input_control)  angle.deg-array `→` Sequence[Union[float, int]]

Angle of the direction of illumination within the
object plane (in degrees).

Default:
45.0

Suggested values:
1.0, 5.0, 10.0, 20.0, 40.0, 60.0, 90.0

Value range:
`0.0
≤
tilts
≤
360.0` (lin)

Minimum increment:
0.01

Recommended increment:
10.0

**`result_type`** (input_control)  string-array `→` Sequence[str]

Types of the requested results.

Default:
"all"

List of values:
[], "albedo", "all", "gradient", "height_field", "normalized_surface_normal"

**`reconstruction_method`** (input_control)  string `→` str

Type of the reconstruction method.

Default:
"poisson"

List of values:
"fft_cyclic", "poisson", "rft_cyclic"

**`gen_param_name`** (input_control)  string-array `→` Sequence[str]

Names of the generic parameters.

Default:
[]

List of values:
"caching", "optimize_speed"

**`gen_param_value`** (input_control)  integer-array `→` Sequence[Union[int, float, str]]

Values of the generic parameters.

Default:
[]

List of values:
"exhaustive", "free_cache", "no_cache", "patient", "standard", "use_cache"

## Result

If the parameters are valid, `photometric_stereo` returns the
value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`optimize_fft_speed`

## Module

3D Metrology
