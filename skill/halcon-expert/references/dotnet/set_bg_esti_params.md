# SetBgEstiParams (Operator)

## Name

`SetBgEstiParams` — Change the parameters of the data set.

## Signature

`static void HOperatorSet.SetBgEstiParams(HTuple bgEstiHandle, HTuple syspar1, HTuple syspar2, HTuple gainMode, HTuple gain1, HTuple gain2, HTuple adaptMode, HTuple minDiff, HTuple statNum, HTuple confidenceC, HTuple timeC)`

`void HBgEsti.SetBgEstiParams(double syspar1, double syspar2, string gainMode, double gain1, double gain2, string adaptMode, double minDiff, int statNum, double confidenceC, double timeC)`

## Description

`SetBgEstiParams` is used to change the parameters
of the data set. The parameters passed by
`SetBgEstiParams` are the same as in
[`CreateBgEsti`](create_bg_esti.md) (see there for an explanation).

The image format cannot be changed! To do this, a new data set with
an initialization image of the appropriate format has to be
created.

To exchange the background image completely, use
[`UpdateBgEsti`](update_bg_esti.md). The current image then has to be passed
for both the input image and the update region.

## Attention

If *`gainMode`* was set to *"frame"*, the run-time
can be extremely long for large values of *`gain1`* or
*`gain2`*, because the values for the gains' table are
determined by a simple binary search.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`bgEstiHandle`** (input_control)  bg_estimation `→` [HBgEsti](HBgEsti.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the BgEsti data set.

**`syspar1`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

1. system matrix parameter.

Default:
0.7

Suggested values:
0.65, 0.7, 0.75

Value range:
`0.05
≤
syspar1
≤
1.0`

Recommended increment:
0.05

**`syspar2`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

2. system matrix parameter.

Default:
0.7

Suggested values:
0.65, 0.7, 0.75

Value range:
`0.05
≤
syspar2
≤
1.0`

Recommended increment:
0.05

**`gainMode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Gain type.

Default:
"fixed"

List of values:
"fixed", "frame"

**`gain1`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Kalman gain / foreground adaptation time.

Default:
0.002

Suggested values:
10.0, 20.0, 50.0, 0.1, 0.05, 0.01, 0.005, 0.001

Restriction:
`0.0 <= Gain1`

**`gain2`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Kalman gain / background adaptation time.

Default:
0.02

Suggested values:
2.0, 4.0, 8.0, 0.5, 0.1, 0.05, 0.01

Restriction:
`0.0 <= Gain2`

**`adaptMode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Threshold adaptation.

Default:
"on"

List of values:
"off", "on"

**`minDiff`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Foreground/background threshold.

Default:
7.0

Suggested values:
3.0, 5.0, 7.0, 9.0, 11.0

Recommended increment:
0.2

**`statNum`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of statistic data sets.

Default:
10

Suggested values:
5, 10, 20, 30

Value range:
`1
≤
statNum`

Recommended increment:
5

**`confidenceC`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Confidence constant.

Default:
3.25

Suggested values:
4.30, 3.25, 2.82, 2.62

Recommended increment:
0.01

Restriction:
`0.0 < ConfidenceC`

**`timeC`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Constant for decay time.

Default:
15.0

Suggested values:
10.0, 15.0, 20.0

Recommended increment:
5.0

Restriction:
`0.0 < TimeC`

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
* Change parameter in dataset:
set_bg_esti_params(BgEstiHandle,0.7,0.7,'fixed', \
                    0.004,0.08,'on',9.0,10,3.25,20.0)
* Read the next image in sequence:
read_image(Image2,'xing/xing002')
* Estimate the background:
run_bg_esti(Image2,ForegroundRegion3,BgEstiHandle)
* Display the foreground region:
dev_display(ForegroundRegion3)
* etc.
```

## Result

`SetBgEstiParams` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`CreateBgEsti`

## Possible Successors

`RunBgEsti`

## See also

`UpdateBgEsti`

## Module

Foundation
