# update_bg_esti (Operator)

## Name

`update_bg_esti` — Change the estimated background image.

## Signature

`update_bg_esti(PresentImage, UpDateRegion : : BgEstiHandle : )`

## Description

`update_bg_esti` overwrites the image stored in the
current BgEsti data set with the gray values of
*`PresentImage`* within the bounds of
*`UpDateRegion`*. This can be used for a “hard” adaptation:
Image regions with a sudden change in (known) background can be
adapted very fast this way.

## Attention

The passed image (*`PresentImage`*) must have the same
type and size as the background image of the current data set
(initialized with [`create_bg_esti`](create_bg_esti.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`PresentImage`** (input_object)  singlechannelimage `→` object (byte / real)

Current image.

**`UpDateRegion`** (input_object)  region `→` object

Region describing areas to change.

**`BgEstiHandle`** (input_control)  bg_estimation `→`  (handle)

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

`update_bg_esti` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`run_bg_esti`

## Possible Successors

`run_bg_esti`

## See also

`run_bg_esti`,
`give_bg_esti`

## Module

Foundation
