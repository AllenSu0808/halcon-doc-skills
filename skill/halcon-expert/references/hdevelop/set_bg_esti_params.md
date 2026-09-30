# set_bg_esti_params (Operator)

## Name

`set_bg_esti_params` — Change the parameters of the data set.

## Signature

`set_bg_esti_params( : : BgEstiHandle, Syspar1, Syspar2, GainMode, Gain1, Gain2, AdaptMode, MinDiff, StatNum, ConfidenceC, TimeC : )`

## Description

`set_bg_esti_params` is used to change the parameters
of the data set. The parameters passed by
`set_bg_esti_params` are the same as in
[`create_bg_esti`](create_bg_esti.md) (see there for an explanation).

The image format cannot be changed! To do this, a new data set with
an initialization image of the appropriate format has to be
created.

To exchange the background image completely, use
[`update_bg_esti`](update_bg_esti.md). The current image then has to be passed
for both the input image and the update region.

## Attention

If *`GainMode`* was set to *'frame'*, the run-time
can be extremely long for large values of *`Gain1`* or
*`Gain2`*, because the values for the gains' table are
determined by a simple binary search.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`BgEstiHandle`** (input_control)  bg_estimation `→`  (handle)

ID of the BgEsti data set.

**`Syspar1`** (input_control)  real `→`  (real)

1. system matrix parameter.

Default:
0.7

Suggested values:
0.65, 0.7, 0.75

Value range:
`0.05
≤
Syspar1
≤
1.0`

Recommended increment:
0.05

**`Syspar2`** (input_control)  real `→`  (real)

2. system matrix parameter.

Default:
0.7

Suggested values:
0.65, 0.7, 0.75

Value range:
`0.05
≤
Syspar2
≤
1.0`

Recommended increment:
0.05

**`GainMode`** (input_control)  string `→`  (string)

Gain type.

Default:
'fixed'

List of values:
'fixed', 'frame'

**`Gain1`** (input_control)  real `→`  (real)

Kalman gain / foreground adaptation time.

Default:
0.002

Suggested values:
10.0, 20.0, 50.0, 0.1, 0.05, 0.01, 0.005, 0.001

Restriction:
`0.0 <= Gain1`

**`Gain2`** (input_control)  real `→`  (real)

Kalman gain / background adaptation time.

Default:
0.02

Suggested values:
2.0, 4.0, 8.0, 0.5, 0.1, 0.05, 0.01

Restriction:
`0.0 <= Gain2`

**`AdaptMode`** (input_control)  string `→`  (string)

Threshold adaptation.

Default:
'on'

List of values:
'off', 'on'

**`MinDiff`** (input_control)  real `→`  (real)

Foreground/background threshold.

Default:
7.0

Suggested values:
3.0, 5.0, 7.0, 9.0, 11.0

Recommended increment:
0.2

**`StatNum`** (input_control)  integer `→`  (integer)

Number of statistic data sets.

Default:
10

Suggested values:
5, 10, 20, 30

Value range:
`1
≤
StatNum`

Recommended increment:
5

**`ConfidenceC`** (input_control)  real `→`  (real)

Confidence constant.

Default:
3.25

Suggested values:
4.30, 3.25, 2.82, 2.62

Recommended increment:
0.01

Restriction:
`0.0 < ConfidenceC`

**`TimeC`** (input_control)  real `→`  (real)

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

`set_bg_esti_params` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`create_bg_esti`

## Possible Successors

`run_bg_esti`

## See also

`update_bg_esti`

## Module

Foundation
