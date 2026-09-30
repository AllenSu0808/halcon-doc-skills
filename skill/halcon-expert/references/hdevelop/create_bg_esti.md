# create_bg_esti (Operator)

## Name

`create_bg_esti` — Generate and initialize a data set for the background estimation.

## Signature

`create_bg_esti(InitializeImage : : Syspar1, Syspar2, GainMode, Gain1, Gain2, AdaptMode, MinDiff, StatNum, ConfidenceC, TimeC : BgEstiHandle)`

## Description

`create_bg_esti` creates a new data set for the background
estimation and initializes it with the appropriate parameters. The
estimated background image is part of this data set. The newly
created set automatically becomes the current set.

*`InitializeImage`* is used as an initial prediction for the
background image. For a good prediction an image of the
observed scene without moving objects should be passed in
*`InitializeImage`*. That way the foreground adaptation rate
can be held low. If there is no empty scene image available, a
homogeneous gray image can be used instead. In that case the
adaptation rate for the foreground image must be raised, because
initially most of the image will be detected as foreground. The
initialization image must to be of type `byte` or
`real`.
Because of processing single-channel images, data sets must be created for
every channel. Size and region of *`InitializeImage`*
determines size and region for all background estimations
([`run_bg_esti`](run_bg_esti.md)) that are performed with this data set.

*`Syspar1`* and *`Syspar2`* are the parameters of the
Kalman system matrix. The system matrix describes the system of the
gray value changes according to Kalman filter theory. The background
estimator implements a different system for each pixel.

*`GainMode`* defines whether a fixed Kalman gain should be
used for the estimation or whether the gain should adapt itself
depending on the difference between estimation and actual value. If
*`GainMode`* is set to *'fixed'*, then
*`Gain1`* is used as Kalman gain for pixels predicted as
foreground and *`Gain2`* as gain for pixels predicted as
background. *`Gain1`* should be smaller than
*`Gain2`*, because adaptation of the foreground should be
slower than adaptation of the background. Both *`Gain1`* and
*`Gain2`* should be smaller than *1.0*.

If *`GainMode`* is set to *'frame'*, then tables for
foreground and background estimation are computed containing
Kalman gains for all the 256 possible gray value
changes. *`Gain1`* and *`Gain2`* then denote the
number of frames necessary to adapt the difference between estimated
value and actual value. So with a fixed time for adaptation (i.e. number
of frames) the needed Kalman gain grows with the gray value
difference. *`Gain1`* should therefore be larger than
*`Gain2`*. Different gains for different gray value
differences are useful if the background estimator is used for
generating an 'empty' scene assuming that there are always moving
objects in the observed area. In that case the adaptation time for
foreground adaptation (*`Gain1`*) must not be too
big. *`Gain1`* and *`Gain2`* should be bigger than
*1.0*.

*`AdaptMode`* denotes, whether the foreground/background
decision threshold applied to the gray value difference between
estimation and actual value is fixed or whether it adapts itself
depending on the gray value deviation of the background pixels.

If *`AdaptMode`* is set to *'off'*, the parameter
*`MinDiff`* denotes a fixed threshold. The parameters
*`StatNum`*, *`ConfidenceC`* and *`TimeC`* are
meaningless in this case.

If *`AdaptMode`* is set to *'on'*, then
*`MinDiff`* is interpreted as a base threshold. For each
pixel an offset is added to this threshold depending on the
statistical evaluation of the pixel value over
time. *`StatNum`* holds the number of data sets (past frames)
that are used for computing the gray value variance
(FIR-Filter). *`ConfidenceC`* is used to determine the
confidence interval.

The confidence interval determines the values of the background
statistics if background pixels are hidden by a foreground object
and thus are detected as foreground. According to the student
t-distribution the confidence constant is *4.30*
(*3.25*, *2.82*, *2.26*) for a confidence
interval of *99,8%* (*99,0%*, *98,0%*,
*95,0%*). *`TimeC`* holds a time constant for the
exp-function that raises the threshold in case of a foreground
estimation of the pixel. That means, the threshold is raised in
regions where movement is detected in the foreground. That way larger
changes in illumination are tolerated if the background becomes
visible again. The main reason for increasing this tolerance is the
impossibility for a prediction of illumination changes while the
background is hidden. Therefore no adaptation of the estimated
background image is possible.

## Attention

If *`GainMode`* was set to *'frame'*, the run-time
can be extremely long for large values of *`Gain1`* or
*`Gain2`*, because the values for the gains' table are
determined by a simple binary search.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`InitializeImage`** (input_object)  singlechannelimage `→` object (byte / real)

initialization image.

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

**`BgEstiHandle`** (output_control)  bg_estimation `→`  (handle)

ID of the BgEsti data set.

## Example (HDevelop)

```
* read Init-Image:
read_image (InitImage, 'xing/init')
* initialize 1. BgEsti-Dataset with
* fixed gains and threshold adaption:
create_bg_esti(InitImage,0.7,0.7,'fixed',0.002,0.02, \
               'on',7.0,10,3.25,15.0,BgEstiHandle1)
* initialize 2. BgEsti-Dataset with
* frame orientated gains and fixed threshold
create_bg_esti(InitImage,0.7,0.7,'frame',30.0,4.0, \
               'off',9.0,10,3.25,15.0,BgEstiHandle2)
```

## Result

`create_bg_esti` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Successors

`run_bg_esti`

## See also

`set_bg_esti_params`,
`close_bg_esti`

## Module

Foundation
