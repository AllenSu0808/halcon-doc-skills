# depth_from_focus (Operator)

## Name

`depth_from_focus` — Extract depth using multiple focus levels.

## Signature

`depth_from_focus(MultiFocusImage : Depth, Confidence : Filter, Selection : )`

## Description

The operator `depth_from_focus` extracts the depth using a
focus sequence. The images of the focus sequence have to be passed as
a multi channel image (*`MultiFocusImage`*). The depth for
each pixel will be returned in *`Depth`* as the channel
number. The parameter *`Confidence`* returns a confidence
value for each depth estimation: The larger this value, the higher
the confidence of the depth estimation is.

`depth_from_focus` selects the pixels with the best focus of
all focus levels. The method used to extract these pixels is
specified by the parameters *`Filter`* and *`Selection`*.

For the parameter *`Filter`*, you can choose between the values
*'highpass'* and *'bandpass'*. To determine the focus
within the image a high- or a bandpass filter can be applied. The
larger the filter response, the more in focus is the image at this
location. Compared to the highpass filter, the bandpass filter
suppresses high frequencies. This is useful in particular in images
containing strong noise.

Optionally, you can smooth the filtered image using the mean filter
by passing two additional integer values for the mask size in the
parameter *`Filter`* (e.g., [*'highpass'*, *7*,
*7*]). This blurs the in-focus region with neighboring pixels
and thus allows to bridge small areas with no texture within the
image. Note, however, that this smoothing does not suppress noise in
the original image, since it is applied only after high- or bandpass
filtering.

The parameter *`Selection`* determines how the optimum focus
level is selected. If you pass the value *'next_maximum'*,
the closest focus maximum in the neighborhood is used. In contrast,
if you pass the value *'local'*, the focus level is
determined based on the focus values of all focus levels of the
pixel. With *'next_maximum'*, you typically achieve a
slightly smoothed and more robust result.

This additional smoothing is useful if no telecentric lenses are used to
take the input images. In this case, the position of an object will
slightly shift within the sequence. By adding appropriate smoothing, this
effect can be partially compensated.

## Attention

If *`MultiFocusImage`* contains more than 255 channels (focus
levels), *`Depth`* is clipped at 255, i.e. depth values higher
than 255 are ignored.

If the filter mask for *`Filter`* is specified with even values, the
routine uses the next larger odd values instead (this way the center of the
filter mask is always explicitly determined).

If *`Selection`* is set to *'local'* and *`Filter`* is
set to *'highpass'* or *'bandpass'*, `depth_from_focus`
can be executed on OpenCL devices. If smoothing is enabled, the same
restrictions and limitations as for [`mean_image`](mean_image.md) apply.

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`MultiFocusImage`** (input_object)  multichannel-image(-array) `→` object (byte)

Multichannel gray image consisting of multiple
focus levels.

**`Depth`** (output_object)  singlechannelimage(-array) `→` object (byte)

Depth image.

**`Confidence`** (output_object)  singlechannelimage(-array) `→` object (byte)

Confidence of depth estimation.

**`Filter`** (input_control)  string(-array) `→`  (string / integer)

Filter used to find sharp pixels.

Default:
'highpass'

Suggested values:
'highpass', 'bandpass', 3, 5, 7, 9

**`Selection`** (input_control)  string(-array) `→`  (string)

Method used to find sharp pixels.

Default:
'next_maximum'

List of values:
'local', 'next_maximum'

List of values (for compute devices):
'local'

## Example (C++)

```
compose3(Focus0,Focus1,Focus2,&MultiFocus);
depth_from_focus(MultiFocus,&Depth,&Confidence,'highpass','next_maximum');
mean_image(Depth,&Smooth,15,15);
select_grayvalues_from_channels(MultiChannel,Smooth,SharpImage);
threshold(Confidence,HighConfidence,10,255);
reduce_domain(SharpImage,HighConfidence,ConfidentSharp);
```

## Possible Predecessors

`compose2`,
`compose3`,
`compose4`,
`add_channels`,
`read_image`,
`read_sequence`

## Possible Successors

`select_grayvalues_from_channels`,
`mean_image`,
`binomial_filter`,
`gauss_filter`,
`threshold`

## See also

`count_channels`

## Module

3D Metrology
