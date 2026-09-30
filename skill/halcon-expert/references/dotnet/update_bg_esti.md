# UpdateBgEsti (Operator)

## Name

`UpdateBgEsti` — Change the estimated background image.

## Signature

`static void HOperatorSet.UpdateBgEsti(HObject presentImage, HObject upDateRegion, HTuple bgEstiHandle)`

`void HImage.UpdateBgEsti(HRegion upDateRegion, HBgEsti bgEstiHandle)`

`void HBgEsti.UpdateBgEsti(HImage presentImage, HRegion upDateRegion)`

## Description

`UpdateBgEsti` overwrites the image stored in the
current BgEsti data set with the gray values of
*`presentImage`* within the bounds of
*`upDateRegion`*. This can be used for a “hard” adaptation:
Image regions with a sudden change in (known) background can be
adapted very fast this way.

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

**`upDateRegion`** (input_object)  region `→` [HRegion](HRegion.md)

Region describing areas to change.

**`bgEstiHandle`** (input_control)  bg_estimation `→` [HBgEsti](HBgEsti.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the BgEsti data set.

## Example (HDevelop)

```
* read Init-Image:
read_image(InitImage,'xing/init')
* initialize BgEsti-Dataset with
* fixed gains and threshold adaption
create_bg_esti(InitImage,0.7,0.7,'fixed',0.002,0.02, \
               'on',7,10,3.25,15.0,BgEstiHandle)
* read the next image in sequence:
read_image(Image0,'xing/xing000')
* estimate the Background:
run_bg_esti(Image0,Region1,BgEstiHandle)
* use the Region and the information of a knowledge base
* to calculate the UpDateRegion
update_bg_esti(Image0,UpdateRegion,BgEstiHandle)
* then read the next image in sequence:
read_image(Image1,'xing/xing001')
* estimate the Background:
run_bg_esti(Image1,Region2,BgEstiHandle)
* etc.
```

## Result

`UpdateBgEsti` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`RunBgEsti`

## Possible Successors

`RunBgEsti`

## See also

`RunBgEsti`,
`GiveBgEsti`

## Module

Foundation
