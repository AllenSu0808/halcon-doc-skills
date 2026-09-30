# RunBgEsti (Operator)

## Name

`RunBgEsti` — Estimate the background and return the foreground region.

## Signature

`static void HOperatorSet.RunBgEsti(HObject presentImage, out HObject foregroundRegion, HTuple bgEstiHandle)`

`HRegion HImage.RunBgEsti(HBgEsti bgEstiHandle)`

`HRegion HBgEsti.RunBgEsti(HImage presentImage)`

## Description

`RunBgEsti` adapts the background image stored in the
BgEsti data set using a Kalman filter on each pixel and
returns a region of the foreground (detected moving objects).

For every pixel an estimation of its gray value is computed using the
values of the current data set and its stored background image and
the current image (*`presentImage`*). By comparison to the
threshold (fixed or adaptive, see [`CreateBgEsti`](create_bg_esti.md)) the
pixels are classified as either foreground or background.

The background estimation processes only single-channel
images. Therefore the background has to be adapted separately for
every channel.

The background estimation should be used on half- or even
quarter-sized images. For this, the input images (and the
initialization image!) has to be reduced using
[`ZoomImageFactor`](zoom_image_factor.md). The advantage is a shorter run-time on one
hand and a low-band filtering on the other. The filtering eliminates
high frequency noise and results in a more reliable estimation. As a
result the threshold (see [`CreateBgEsti`](create_bg_esti.md)) can be
lowered. The foreground region returned by `RunBgEsti`
then has to be enlarged again for further processing.

## Attention

The passed image (*`presentImage`*) must have the same
type and size as the background image of the current data set
(initialized with [`CreateBgEsti`](create_bg_esti.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`presentImage`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / real)

Current image.

**`foregroundRegion`** (output_object)  region `→` [HRegion](HRegion.md)

Region of the detected foreground.

**`bgEstiHandle`** (input_control)  bg_estimation `→` [HBgEsti](HBgEsti.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the BgEsti data set.

## Example (HDevelop)

```
* Read image for initialization:
read_image(InitImage,'xing/init')
* Initialize BgEsti dataset with
* fixed gains and threshold adaption:
create_bg_esti(InitImage,0.7,0.7,'fixed',0.002,0.02, \
               'on',7.0,10,3.25,15.0,BgEstiHandle)
* Read the next image in sequence:
read_image(Image0,'xing/xing000')
* Estimate the background:
run_bg_esti(Image0,ForegroundRegion1,BgEstiHandle)
* Display the foreground region:
dev_display (ForegroundRegion1)
* Read the next image in sequence:
read_image(Image1,'xing/xing001')
* Estimate the background:
run_bg_esti(Image1,ForegroundRegion2,BgEstiHandle)
* Display the foreground region:
dev_display (ForegroundRegion2)
* etc.
```

## Result

`RunBgEsti` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`CreateBgEsti`,
`UpdateBgEsti`

## Possible Successors

`GiveBgEsti`,
`UpdateBgEsti`

## See also

`SetBgEstiParams`,
`CreateBgEsti`,
`UpdateBgEsti`,
`GiveBgEsti`

## Module

Foundation
