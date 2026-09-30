# GiveBgEsti (Operator)

## Name

`GiveBgEsti` — Return the estimated background image.

## Signature

`static void HOperatorSet.GiveBgEsti(out HObject backgroundImage, HTuple bgEstiHandle)`

`void HImage.GiveBgEsti(HBgEsti bgEstiHandle)`

`HImage HBgEsti.GiveBgEsti()`

## Description

`GiveBgEsti` returns the estimated background image of
the current BgEsti data set. The background image has the same type
and size as the initialization image passed in
[`CreateBgEsti`](create_bg_esti.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`backgroundImage`** (output_object)  image `→` [HImage](HImage.md) (byte / real)

Estimated background image of the current data set.

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
* Give the background image from the aktive dataset:
give_bg_esti(BgImage,BgEstiHandle)
* Display the background image:
dev_display(BgImage)
```

## Result

`GiveBgEsti` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`RunBgEsti`

## Possible Successors

`RunBgEsti`,
`CreateBgEsti`,
`UpdateBgEsti`

## See also

`RunBgEsti`,
`UpdateBgEsti`,
`CreateBgEsti`

## Module

Foundation
