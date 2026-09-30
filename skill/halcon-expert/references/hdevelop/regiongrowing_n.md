# regiongrowing_n (Operator)

## Name

`regiongrowing_n` — Segment an image using region growing for multi-channel images.

## Signature

`regiongrowing_n(MultiChannelImage : Regions : Metric, MinTolerance, MaxTolerance, MinSize : )`

## Description

`regiongrowing_n` performs a multi-channel
region growing. The $n$ channels give
rise to an n-dimensional feature vector. Neighboring points are
aggregated into the same region if the difference of their feature
vectors with respect to the given metric lies in the interval
[*`MinTolerance`*, *`MaxTolerance`*]. Only
neighbors of the 4-neighborhood are examined. The following metrics can be
used:

Let $g_{A}$ denote the gray value in the feature vector $A$
at point $a$ of the image, and likewise be $g_{B}$ the gray
value in the feature vector $B$ at point a neighboring point
$b$. Let $g(d)$ be the gray value with index $d$.
Furthermore, let $MinT$ denote
*`MinTolerance`* and $MaxT$ denote *`MaxTolerance`*.

- ***'1-norm'*:** —

  Sum of absolute values
  $$MinT \le \frac{1}{n} \sum \limits_{A,B} |g_A - g_B| \le MaxT$$ ![figure](../assets/06b1316d1c6c33ce.svg)
- ***'2-norm'*:** —

  Euclidean distance
  $$MinT \leq \sqrt{\frac{\sum (g_A - g_B)^2}{n}} \leq MaxT$$ ![figure](../assets/4c64786535d711a0.svg)
- ***'3-norm'*:** —

  p - Norm with p = 3
  $$MinT \le^{3}\sqrt{\frac{\sum (g_A - g_B)^3}{n}} \le MaxT$$ ![figure](../assets/ee9a27ad7dc3f575.svg)
- ***'4-norm'*:** —

  p - Norm with p = 4
  $$MinT \le^{4} \sqrt{\frac{\sum (g_A - g_B)^4}{n}} \le MaxT$$ ![figure](../assets/77acf2f32a4cd23d.svg)
- ***'n-norm'*:** —

  Minkowski distance
  $$MinT \le n-th\root\of{\frac{\sum (g_A - g_B)^n}{n}} \le MaxT$$ ![figure](../assets/7a6153ebe83cd7ce.svg)
- ***'max-diff'*:** —

  Supremum distance
  $$MinT\le\max \{|g_{A}-g_{B}|\}\le MaxT$$
- ***'min-diff'*:** —

  Infimum distance
  $$MinT\le\min \{|g_{A}-g_{B}|\}\le MaxT$$
- ***'variance'*:** —

  Variance of gray value differences
  $$MinT\le Var(g_{A}-g_{B})\le MaxT$$
- ***'dot-product'*:** —

  Dot product
  $$MinT \leq \frac{1}{n} \sqrt{\sum (g_{A} g_{B})} \leq MaxT$$ ![figure](../assets/0447cb43eb837ee4.svg)
- ***'correlation'*:** —

  Correlation
  $$m_A = \frac{1}{n} \sum g_A \\ V_ar_A = \frac{1}{n} \sqrt{\sum (g_A - m_A)^2} \\ m_B = \frac{1}{n} \sum g_B \\ V_ar_B = \frac{1}{n} \sqrt{\sum (g_B - m_B)^2} \\ M_inT \leq \frac{1}{n^2} \sum \frac{(g_A - m_A)(g_B - m_B)}{(V_ar_A V_ar_B)} \leq M_axT$$ ![figure](../assets/3333838d5336f384.svg)
- ***'mean-diff'*:** —

  Difference of arithmetic means
  $$a = \frac{1}{n} \sum_A g_A \ b = \frac{1}{n} \sum_B g_B \ MinT \le |a - b| \le MaxT$$ ![figure](../assets/9338d4a65262e2da.svg)
- ***'mean-ratio'*:** —

  Ratio of arithmetic means
  $$a = \frac{1}{n}\sum_{i=1}^{n} g_A\\ b = \frac{1}{n}\sum_{i=1}^{n} g_B\\ MinT \leq \min\left\{ \frac{a}{b}, \frac{b}{a} \right\} \leq MaxT$$ ![figure](../assets/9f72487d59354551.svg)
- ***'length-diff'*:** —

  Difference of the vector lengths
  $$a = \sqrt{\frac{\sum g_{A}^{2}}{n}} \\ b = \sqrt{\frac{\sum g_{B}^{2}}{n}} \\ MinT \le |a - b| \le MaxT$$ ![figure](../assets/444cb80e35daad64.svg)
- ***'length-ratio'*:** —

  Ratio of the vector lengths
  $$a = \sqrt{\frac{\sum g_A^2}{n}} \\ b = \sqrt{\frac{\sum g_B^2}{n}} \\ MinT \leq \min\left\{ \frac{a}{b}, \frac{b}{a} \right\} \leq MaxT$$ ![figure](../assets/c429fe75b1c0c306.svg)
- ***'n-norm-ratio'*:** —

  Ratio of the vector lengths w.r.t the p-norm with
  p = n
  $$a = \sqrt[n]{\frac{\sum g_A^n}{n}} \\ b = \sqrt[n]{\frac{\sum g_B^n}{n}} \\ MinT \leq \min\left\{ \frac{a}{b}, \frac{b}{a} \right\} \leq MaxT$$ ![figure](../assets/f50deb607ff87305.svg)
- ***'gray-max-diff'*:** —

  Difference of the maximum gray values
  $$a = \max\{|g_A|\}\n b = \max\{|g_B|\}\n MinT \le |a - b| \le MaxT$$ ![figure](../assets/4ef3131544e46843.svg)
- ***'gray-max-ratio'*:** —

  Ratio of the maximum gray values
  $$a = \max\{|g_A|\}\nb = \max\{|g_B|\}\nMinT \leq \min\left\{\frac{a}{b}, \frac{b}{a}\right\} \leq MaxT$$ ![figure](../assets/081a564c8f3d940c.svg)
- ***'gray-min-diff'*:** —

  Difference of the minimum gray values
  $$a = \min\{|g_A|\}\n b = \min\{|g_B|\}\n MinT \leq |a - b| \leq MaxT$$ ![figure](../assets/c53412ac283c9de8.svg)
- ***'gray-min-ratio'*:** —

  Ratio of the minimum gray values
  $$a = \min\{|g_A|\}\nb = \min\{|g_B|\}\nMinT \leq \min\left\{\frac{a}{b}, \frac{b}{a}\right\} \leq MaxT$$ ![figure](../assets/9495ff73b7fd7b87.svg)
- ***'variance-diff'*:** —

  Difference of the variances over all gray values (channels)
  $$MinT\le|Var(g_{A})-Var(g_{B})|\le MaxT$$
- ***'variance-ratio'*:** —

  Ratio of the variances over all gray values (channels)
  $$MinT \leq \frac{Var(g_B)}{Var(g_A)} \leq MaxT$$ ![figure](../assets/d277f3a9da7273c0.svg)
- ***'mean-abs-diff'*:** —

  Difference of the sum of absolute values over all gray values (channels)
  $$a = \sum_{d,k,k<d}^{ } |g_A(d) - g_A(k)|\n b = \sum_{d,k,k<d}^{ } |g_B(d) - g_B(k)|\n MinT \le \frac{|a - b|}{\text{number of sums}} \le MaxT$$ ![figure](../assets/d469f2a5e15b8c0f.svg)
- ***'mean-abs-ratio'*:** —

  Ratio of the sum of absolute values over all gray values (channels)
  $$a = \sum_{d,k,k<d}^{ } |g_A(d) - g_A(k)| b = \sum_{d,k,k<d}^{ } |g_B(d) - g_B(k)| MinT \leq \min \left\{ \frac{a}{b}, \frac{b}{a} \right\} \leq MaxT$$ ![figure](../assets/9e773c1bd1cee4bb.svg)
- ***'max-abs-diff'*:** —

  Difference of the maximum distance of the components
  $$a = \max\{g_{A}(d),g_{A}(k)\}\n b = \max\{g_{B}(d),g_{B}(k)\}\n\min\!T \leq \min\left\{\frac{a}{b},\frac{b}{a}\right\} \leq \max\!T$$ ![figure](../assets/734f6d03278d50d5.svg)
- ***'max-abs-ratio'*:** —

  Ratio of the maximum distance of the components
  $$a = \max\{g_{A}(d),g_{A}(k)\}\n b = \max\{g_{B}(d),g_{B}(k)\}\n\min\!T \leq \min\left\{\frac{a}{b},\frac{b}{a}\right\} \leq \max\!T$$ ![figure](../assets/734f6d03278d50d5.svg)
- ***'min-abs-diff'*:** —

  Difference of the minimum distance of the components
  $$a = \min\{g_A(d), g_A(k)\}, k < d b = \min\{g_B(d), g_B(k)\}, k < d MinT \le |a - b| \le MaxT$$ ![figure](../assets/f2c54e2918864f38.svg)
- ***'min-abs-ratio'*:** —

  Ratio of the minimum distance of the components
  $$a = \min\{g_A(d), g_A(k)\}, k < d b = \min\{g_B(d), g_B(k)\}, k < d MinT \leq \min\left\{ \frac{a}{b}, \frac{b}{a} \right\} \leq MaxT$$ ![figure](../assets/baa92be093e074a8.svg)
- ***'plane'*:** —

  The following has to hold for all
  $d_{1},d_{2}\in[1,n]$:
  $$g_A(d1) > g_A(d2) ⇒ g_B(d1) > g_B(d2)\ng_A(d1) < g_A(d2) ⇒ g_B(d1) < g_B(d2)$$ ![figure](../assets/cba809a0cb44ea7d.svg)

Regions with an area less than *`MinSize`* are suppressed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`MultiChannelImage`** (input_object)  (multichannel-)image(-array) `→` object (byte)

Input image.

**`Regions`** (output_object)  region-array `→` object

Segmented regions.

**`Metric`** (input_control)  string `→`  (string)

Metric for the distance of the feature vectors.

Default:
'2-norm'

List of values:
'1-norm', '2-norm', '3-norm', '4-norm', 'correlation', 'dot-product', 'gray-max-diff', 'gray-max-ratio', 'gray-min-diff', 'gray-min-ratio', 'length-diff', 'length-ratio', 'max-abs-diff', 'max-abs-ratio', 'max-diff', 'mean-abs-diff', 'mean-abs-ratio', 'mean-diff', 'mean-ratio', 'min-abs-diff', 'min-abs-ratio', 'min-diff', 'n-norm', 'n-norm-ratio', 'plane', 'variance', 'variance-diff', 'variance-ratio'

**`MinTolerance`** (input_control)  number `→`  (real / integer)

Lower threshold for the features' distance.

Default:
0.0

Suggested values:
0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 25.0, 30.0

**`MaxTolerance`** (input_control)  number `→`  (real / integer)

Upper threshold for the features' distance.

Default:
20.0

Suggested values:
0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 25.0, 30.0

**`MinSize`** (input_control)  integer `→`  (integer)

Minimum size of the output regions.

Default:
30

Suggested values:
1, 10, 25, 50, 100, 200, 500, 1000

Value range:
`1
≤
MinSize`

Minimum increment:
1

Recommended increment:
5

## Result

`regiongrowing_n` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior with respect to the input images and output
regions can be determined by setting the values of the flags
*'no_object_result'*, *'empty_region_result'*, and
*'store_empty_region'* with [`set_system`](set_system.md).
If necessary, an exception is raised.

## Possible Predecessors

`compose2`,
`compose3`

## Alternatives

`class_2dim_sup`,
`class_ndim_norm`

## See also

`regiongrowing_mean`

## Module

Foundation
