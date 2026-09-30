# set_structured_light_model_param (Operator)

## Name

`set_structured_light_model_param` — Set parameters of a structured light model.

## Signature

`set_structured_light_model_param( : : StructuredLightModel, GenParamName, GenParamValue : )`

## Description

The operator `set_structured_light_model_param` is used to
manipulate the parameters of a structured light model
*`StructuredLightModel`*. The current parameter settings
can be queried with the operator [`get_structured_light_model_param`](get_structured_light_model_param.md).

For an explanation of the concept of structured light and its supported
applications, see the introduction of chapter
[Inspection / Structured Light](toc_inspection_structuredlight.md).

**General parameters:**

- ***'persistence'*:** —

  Enables
  (*`GenParamValue`*=*'true'*) or disables
  (*`GenParamValue`*=*'false'*) the *'persistence'*
  mode of the structured light model. When in persistence mode, the model
  stores intermediate results of the decoding, which can be inspected
  later by [`get_structured_light_object`](get_structured_light_object.md).

  Note that the model might need significant memory space in this mode.
  Therefore, we recommend to enable this mode only during the setup and
  for debugging a structured light model setup.

  If *'persistence'* is changed, all results of the
  model are cleared.

  List of values:
   *'true'*, *'false'*, *1*, *0*

  Default:
   *'false'*

**Parameters which influence the appearance of the generated
pattern images:**

- ***'pattern_width'*:** —

  Sets the width of the pattern images
  that are generated while calling [`gen_structured_light_pattern`](gen_structured_light_pattern.md).
  Usually, the value should be set to the width of the monitor or projector
  that is used to display the pattern images.

  The value of *'pattern_width'* has to be larger than
  the value *'min_stripe_width'*/2.
  In case that *'pattern_type'* is *'single_stripe'*,
  it also has to be larger than *'single_stripe_width'*/2.
  In case that a *'camera_setup_model'* is set in the structured
  light model, the value of *'pattern_width'* has to match
  the width of the projector parameters stored in the camera setup model
  (at Index *1*).

  If *'pattern_width'* is changed, the model is not decodable
  anymore and all possibly available results are cleared.
  Therefore, [`gen_structured_light_pattern`](gen_structured_light_pattern.md) has to be called before
  decoding the model using [`decode_structured_light_pattern`](decode_structured_light_pattern.md).

  Value range:
   integer values larger or equal to *1*

  Default:
   *1024*
- ***'pattern_height'*:** —

  Sets the height of the pattern images
  that are generated while calling [`gen_structured_light_pattern`](gen_structured_light_pattern.md).
  Usually, the value should be set to the height of the monitor or
  projector that is used to display the pattern images.

  The value of *'pattern_height'* has to be larger than
  the value *'min_stripe_width'*/2.
  In case that *'pattern_type'* is *'single_stripe'*,
  it also has to be larger than *'single_stripe_width'*/2.
  In case that a *'camera_setup_model'* is set in the structured
  light model, the value of *'pattern_height'* has to match
  the height of the projector parameters stored in the camera setup model
  (at Index *1*).

  If *'pattern_height'* is changed, the model is not decodable
  anymore and all possibly available results are cleared.
  Therefore, [`gen_structured_light_pattern`](gen_structured_light_pattern.md) has to be called before
  decoding the model using [`decode_structured_light_pattern`](decode_structured_light_pattern.md).

  Value range:
   integer values larger or equal to *1*

  Default:
   *1024*
- ***'min_stripe_width'*:** —

  Sets the width (in pixels) of the
  finest stripe of the pattern images that are generated while calling
  [`gen_structured_light_pattern`](gen_structured_light_pattern.md).

  The value has to be a power of two. Furthermore, it has to be
  smaller or equal the minimum of the parameters
  *'pattern_width'* and *'pattern_height'*
  after rounding both up to their next power of two.
  In case that *'pattern_type'* is *'single_stripe'*,
  it also has to be smaller or equal the *'single_stripe_width'*.

  If *'min_stripe_width'* is changed, the model is not decodable
  anymore and all possibly available results are cleared.
  Therefore, [`gen_structured_light_pattern`](gen_structured_light_pattern.md) has to be called before
  decoding the model using [`decode_structured_light_pattern`](decode_structured_light_pattern.md).

  Value range:
   integer values larger or equal to *4* and a power of 2

  Default:
   *32*
- ***'normalization'*:** —

  Sets the normalization mode of the
  structured light model. If the parameter is set to *'global'*,
  [`gen_structured_light_pattern`](gen_structured_light_pattern.md) generates two additional pattern
  images composed of a black and a white image. These images are then used
  in the decoding process to determine the actual pattern region.
  If instead, the value *'inverted_pattern'* is chosen, each Gray
  code image is additionally inverted and the pattern region is segmented
  iteratively using the Gray code images and their inverted version.

  If *'normalization'* is changed, the model is not decodable
  anymore and all possibly available results are cleared.
  Therefore, [`gen_structured_light_pattern`](gen_structured_light_pattern.md) has to be called before
  decoding the model using [`decode_structured_light_pattern`](decode_structured_light_pattern.md).

  List of values:
   *'global'*, *'inverted_pattern'*

  Default:
   *'global'*
- ***'pattern_orientation'*:** —

  Sets the orientation of the
  pattern images that are generated while calling
  [`gen_structured_light_pattern`](gen_structured_light_pattern.md). If the parameter is set to
  *'both'*, pattern images with vertical stripes as well as
  pattern images with horizontal stripes are created.
  For *'vertical'* the pattern images consist of vertical stripes
  only, whereas for *'horizontal'* only horizontal stripes are
  generated.

  If *'pattern_orientation'* is changed, the model is not decodable
  anymore and all possibly available results are cleared.
  Therefore, [`gen_structured_light_pattern`](gen_structured_light_pattern.md) has to be called before
  decoding the model using [`decode_structured_light_pattern`](decode_structured_light_pattern.md).

  List of values:
   *'both'*, *'vertical'*,
  *'horizontal'*

  Default:
   *'both'*
- ***'pattern_type'*:** —

  Sets the type of the pattern images that
  are generated while calling [`gen_structured_light_pattern`](gen_structured_light_pattern.md).

  |  |  |
  | --- | --- |
  | **'pattern_type'** | **Generated Images** |
  | *'gray_code'* | Gray code images |
  | *'gray_code_and_phase_shift'* | Gray code images and phase shift images |
  | *'single_stripe'* | Single stripe images, Gray code images and phase shift images |

  Usually, *'gray_code_and_phase_shift'* leads to more accurate
  results than *'gray_code'* because the combination between Gray
  code and phase images yields sub-pixel precise monitor or projector coordinates.
  *'single_stripe'* can increase robustness in case of only
  partially specular surfaces.

  If *'pattern_type'* is changed, the model is not decodable
  anymore and all possibly available results are cleared.
  Therefore, [`gen_structured_light_pattern`](gen_structured_light_pattern.md) has to be called before
  decoding the model using [`decode_structured_light_pattern`](decode_structured_light_pattern.md).

  List of values:
   *'gray_code_and_phase_shift'*,
  *'gray_code'*, *'single_stripe'*

  Default:
   *'gray_code_and_phase_shift'*
- ***'single_stripe_width'*:** —

  Sets the width (in pixels) of the
  single stripe that is generated while calling
  [`gen_structured_light_pattern`](gen_structured_light_pattern.md) using the *'pattern_type'*
  *'single_stripe'*.

  The value has to be a power of two and has to be greater or equal
  *'min_stripe_width'*.
  Furthermore, it has to be smaller or equal the minimum of the
  parameters *'pattern_width'* and *'pattern_height'*
  after rounding both up to their next power of two.

  Note that *'single_stripe_width'* can only be set in case that
  *'pattern_type'* is *'single_stripe'*.
  When *'pattern_type'* is changed to *'single_stripe'*,
  *'single_stripe_width'* is set to some power of two roughly
  halfway between the currently set *'min_stripe_width'* and
  the minimum of *'pattern_width'* and *'pattern_height'*.

  If *'single_stripe_width'* is changed,
  the model is not decodable anymore and all possibly available
  results are cleared.
  Therefore, [`gen_structured_light_pattern`](gen_structured_light_pattern.md) has to be
  called before decoding the model using
  [`decode_structured_light_pattern`](decode_structured_light_pattern.md).

  Value range:
   integer values larger or equal to *4* and a power of 2

  Default:
   power of two roughly halfway between the currently
  set *'min_stripe_width'* and
  *'pattern_width'*, *'pattern_height'*

**Parameters which influence the segmentation of the pattern region:**

- ***'min_gray_difference'*:** —

  Sets the minimum gray value
  difference for the Gray code images. This value is used within
  [`decode_structured_light_pattern`](decode_structured_light_pattern.md) to determine the binarized
  images.
  Thereby, for each pixel of the camera images the gray value difference
  between the lighted and the unlighted case is calculated. If the
  gray value difference of a pixel is smaller than
  *'min_gray_difference'*, it is excluded from the domain of the
  binarized images (see [`get_structured_light_object`](get_structured_light_object.md)) and thus also
  from further calculations.

  If *'min_gray_difference'* is set to the value 0, the segmented
  region is identical to the input region of the camera images with the
  only exception that pixels with a decoding result outside the pattern
  images are excluded.

  Value range:
   integer values larger or equal to *0*

  Default:
   *30*

**Parameters for structured light models of type 'deflectometry':**

- ***'derivative_sigma'*:** —

  Sets the sigma of the Gaussian
  (i.e. the amount of smoothing) that is used for the convolution of
  the correspondence image(s) to calculate the defect image.

  Value range:
   float or integer value larger or equal *0.01*

  Default:
   *2*

**Parameters for structured light models of type '3d_reconstruction':**

- ***'camera_setup_model'*:** —

  Sets a copy of the calibrated
  camera setup model containing the calibration parameters of the
  structured light sensor, such as its camera and projector parameters
  and poses. Here, the projector of the sensor is modeled as an
  'inverse camera'. [`reconstruct_surface_structured_light`](reconstruct_surface_structured_light.md) uses
  the calibration parameters to determine the reconstructed surface
  in world coordinates. Please refer to the example program on structured
  light calibration in order to obtain the calibrated camera setup model
  (for further details on calibration of multiple cameras see
  [Calibration / Multi-View](toc_calibration_multiview.md)).

  The camera of the sensor has to correspond to Index 0 in the
  camera setup model, the projector of the sensor to Index 1.
  In order to delete a set camera setup model from
  *`StructuredLightModel`*, HNULL has to be passed.

  Note that the width and height of the projector parameters stored in
  the camera setup model (at Index 1) have to match the set
  *'pattern_width'* and *'pattern_height'* of the structured
  light model. In subsequent calls to [`decode_structured_light_pattern`](decode_structured_light_pattern.md)
  and [`reconstruct_surface_structured_light`](reconstruct_surface_structured_light.md), the width and height of
  the camera parameters stored in the camera setup model (at Index 0)
  have to match the dimensions of the input images of
  [`decode_structured_light_pattern`](decode_structured_light_pattern.md).

  So far, only projectors
  are supported which can be modeled as an inverse pinhole camera, i.e., only
  projectors of type *'area_scan_division'* and
  *'area_scan_polynomial'*. For the camera, all area scan types except
  hypercentric ones are allowed.

  If *'camera_setup_model'* is changed, all possibly available results
  are cleared, so [`decode_structured_light_pattern`](decode_structured_light_pattern.md) has to be
  called before reconstructing the model using
  [`reconstruct_surface_structured_light`](reconstruct_surface_structured_light.md).

  Default:
   HNULL

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- StructuredLightModel

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`StructuredLightModel`** (input_control, state is modified)  structured_light_model `→`  (handle)

Handle of the structured light model.

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Name of the model parameter to be adjusted.

Default:
'min_stripe_width'

List of values:
'camera_setup_model', 'derivative_sigma', 'min_gray_difference', 'min_stripe_width', 'normalization', 'pattern_height', 'pattern_orientation', 'pattern_type', 'pattern_width', 'persistence', 'single_stripe_width'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (integer / real / string)

New value of the model parameter.

Default:
32

Suggested values:
0, 0.01, 0.5, 0.7, 1, 1.4, 5, 50.0, 64, 128, 256, 1024, 'true', 'false', 'both', 'vertical', 'horizontal', 'global', 'inverted_pattern', 'gray_code_and_phase_shift', 'gray_code', 'single_stripe'

## Example (HDevelop)

```
* Create the model
create_structured_light_model ('deflectometry', StructuredLightModel)
* Set the size of the monitor
set_structured_light_model_param (StructuredLightModel, \
                                  'pattern_width', 1600)
set_structured_light_model_param (StructuredLightModel, \
                                  'pattern_height', 1200)
* Set the smallest width of the stripes in the pattern
set_structured_light_model_param (StructuredLightModel, \
                                  'min_stripe_width', 8)
* Generate the patterns to project
gen_structured_light_pattern (PatternImages, StructuredLightModel)
* Set the expected black/white contrast in the region of interest
set_structured_light_model_param (StructuredLightModel, \
                                  'min_gray_difference', 70)
* Decode the camera images
decode_structured_light_pattern (CameraImages, StructuredLightModel)
* Get the computed correspondences and defects
get_structured_light_object (CorrespondenceImages, StructuredLightModel, \
                             'correspondence_image')
set_structured_light_model_param (StructuredLightModel, 'derivative_sigma', \
                                  Sigma)
get_structured_light_object (DefectImage, StructuredLightModel, \
                             'defect_image')
```

## Result

The operator `set_structured_light_model_param` returns the value
2 (
H_MSG_TRUE)
if the given parameters are valid and within acceptable range.
Otherwise, an exception will be raised.

## Possible Predecessors

`create_structured_light_model`

## See also

`get_structured_light_model_param`

## Module

3D Metrology
