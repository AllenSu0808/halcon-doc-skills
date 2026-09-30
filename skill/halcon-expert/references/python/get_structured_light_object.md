# get_structured_light_object (Operator)

## Name

`get_structured_light_object` — Get (intermediate) iconic results of a structured light model.

## Signature

`def get_structured_light_object(structured_light_model: HHandle, object_name: MaybeSequence[str]) -> HObject`

## Description

With the operator `get_structured_light_object` you can
access and inspect (intermediate) iconic results of a structured light
measurement setup that has already been decoded using
[`decode_structured_light_pattern`](decode_structured_light_pattern.md).

On the one hand, this is useful to query the results of the decoding process
(*"correspondence_image"*) together with further processed results
i.e. the defect image (*"defect_image"*).
On the other hand, `get_structured_light_object` is also useful for
troubleshooting the decoding process.
Note that to collect the intermediate results, the *"persistence"*
mode has to be enabled for the *`structured_light_model`*
(see [`set_structured_light_model_param`](set_structured_light_model_param.md)) *before*
decoding the model.

### Objects that can be accessed without persistence mode enabled:

- ***"correspondence_image"*:** —

  Image that describes the correspondences between the monitor or projector
  and the
  camera. If the decoding has been performed in vertical and horizontal
  direction, both correspondence images are returned in an array.
  Otherwise, only the image of the appropriate direction is returned.
- ***"pattern_region"*:** —

  Segmented region in which the camera images have been decoded. This
  region is identical to the domain of the correspondence images.
- ***"defect_image"* (for structured light models of type
  *"deflectometry"*):** —

  Image that describes possible defects on the surface which reflects
  the displayed patterns towards the camera. Basically,
  high gray values in the defect image indicate that the gradients of
  the correspondence images differ significantly from gradients in the
  neighborhood. Note that this object is only available for structured
  light models of type *"deflectometry"*.

### Objects that can be accessed only when in persistence mode:

If the decoding has been performed in vertical and horizontal
direction, images of both directions are returned in an array.
Otherwise, only the images of the appropriate direction are returned.

- ***"binarized_image"*:** —

  Images of the Gray code sequence where white and black gray values
  indicate that the camera pixel observed a surface point illuminated
  by white or black
  regions of the displayed or projected patterns. If *"normalization"*
  was set to *"inverted_pattern"* using
  [`set_structured_light_model_param`](set_structured_light_model_param.md), this refers to the first image
  of an inverted pair.
- ***"decoded_phase_shift_image"*:** —

  Decoded phase shift images containing the phase or angle corresponding
  to the displayed or projected phase images. One phase period covers stripes
  in the pattern of an extent *"min_stripe_width"*.
- ***"decoded_single_stripe_image"*:** —

  Decoded single stripe image computed solely from the single stripe
  images. The correspondence image is a combination of this image with the
  Gray code and phase shift images, if *"pattern_type"* is set to
  *"single_stripe"*.
- ***"gray_code_correspondence_image"*:** —

  Correspondence image computed solely from the Gray code images.
  If *"pattern_type"* is set to
  *"gray_code_and_phase_shift"*, the
  actual correspondence image is a combination of this image with the
  decoded phase shift images.
  If *"pattern_type"* is set to *"single_stripe"*, the
  actual correspondence image is a combination of this image with the
  decoded phase shift images and the decoded single stripe images.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`object`** (output_object)  (multichannel-)object(-array) `→` HObject

Iconic result.

**`structured_light_model`** (input_control)  structured_light_model `→` HHandle

Handle of the structured light model.

**`object_name`** (input_control)  string(-array) `→` MaybeSequence[str]

Name of the iconic result to be returned.

Default:
"correspondence_image"

Suggested values:
"correspondence_image", "pattern_region", "decoded_single_stripe_image", "binarized_image", "decoded_phase_shift_image", "gray_code_correspondence_image", "defect_image"

## Example (HDevelop)

```
* Create the model
create_structured_light_model ('deflectometry', StructuredLightModel)
* Generate the patterns to project
gen_structured_light_pattern (PatternImages, StructuredLightModel)
* Decode the camera images
decode_structured_light_pattern (CameraImages, StructuredLightModel)
* Get the computed correspondences and defects
get_structured_light_object (CorrespondenceImages, StructuredLightModel, \
                             'correspondence_image')
set_structured_light_model_param (StructuredLightModel, \
                                  'derivative_sigma', Sigma)
get_structured_light_object (DefectImage, StructuredLightModel, \
                             'defect_image')
```

## Result

The operator `get_structured_light_object` returns the value
2 (
H_MSG_TRUE)
if the given parameters are valid. Otherwise, an exception will be
raised.

## Possible Predecessors

`decode_structured_light_pattern`

## Possible Successors

`clear_structured_light_model`

## See also

`gen_structured_light_pattern`

## Module

3D Metrology
