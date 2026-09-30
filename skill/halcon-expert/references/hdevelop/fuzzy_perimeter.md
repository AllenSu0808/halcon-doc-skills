# fuzzy_perimeter (Operator)

## Name

`fuzzy_perimeter` — Calculate the fuzzy perimeter of a region.

## Signature

`fuzzy_perimeter(Regions, Image : : Apar, Cpar : Perimeter)`

## Description

The operator `fuzzy_perimeter` is used to determine the
differences of fuzzy membership between an image point and its
neighbor points. The right and lower neighbor are taken into
account. The fuzzy perimeter is then defined as follows:
$$p(X) = \sum_{m=1}^{M-1} \sum_{n=1}^{N-1} \left| \mu_X(x_{m,n}) - \mu_X(x_{m,n+1}) \right| + \sum_{m=1}^{M-1} \sum_{n=1}^{N-1} \left| \mu_X(x_{m,n}) - \mu_X(x_{m+1,n}) \right|$$ ![figure](../assets/2dfc1c8dccb4d889.svg)
where MxN is the size of the image, and
u(x(m,n)) is the fuzzy membership function (i.e., the input
image). This implementation uses Zadeh's Standard-S function, which
is defined as follows:
$$\mu_X(x) = \begin{cases} 0, \\ 2\left(\frac{x - a}{c - a}\right)^2, \\ 1 - 2\left(\frac{x - a}{c - a}\right)^2, \\ 1, \end{cases} \quad \text{for } x \le a \text{ and } a < x \le b \text{ and } b < x \le c \text{ and } c \le x$$ ![figure](../assets/2a4cc102cd9d5110.svg)
The parameters a, b and c obey the following restrictions: $b = \frac{a + c}{2}$ ![figure](../assets/7dc90e3d0b244150.svg) is the inflection point of the
function, $\Delta b=b-a=c-b$ is the
bandwidth, and for x = b $\mu(x)=0.5$
holds. In `fuzzy_perimeter`, the parameters
*`Apar`* and *`Cpar`* are defined as follows: b is
$\frac{Apare}{Cpar}$ ![figure](../assets/829d7e0a39cfd606.svg).

## Attention

Note that for `fuzzy_perimeter`, the *`Regions`* must lie
completely within the previously defined domain. Otherwise an exception
is raised.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Regions for which the fuzzy perimeter is to be
calculated.

**`Image`** (input_object)  singlechannelimage `→` object (byte)

Input image containing the fuzzy membership values.

**`Apar`** (input_control)  integer `→`  (integer)

Start of the fuzzy function.

Default:
0

Suggested values:
0, 5, 10, 20, 50, 100

Value range:
`0
≤
Apar
≤
255` (lin)

Minimum increment:
1

Recommended increment:
5

**`Cpar`** (input_control)  integer `→`  (integer)

End of the fuzzy function.

Default:
255

Suggested values:
50, 100, 150, 200, 220, 255

Value range:
`0
≤
Cpar
≤
255` (lin)

Minimum increment:
1

Recommended increment:
5

Restriction:
`Apar <= Cpar`

**`Perimeter`** (output_control)  real(-array) `→`  (real)

Fuzzy perimeter of a region.

## Example (HDevelop)

```
* To find a Fuzzy Entropy from an Image
read_image(Image,'monkey')
fuzzy_perimeter(Trans,Trans,0,255,Per)
```

## Result

The operator `fuzzy_perimeter` returns the value 2 (
H_MSG_TRUE)
if
the parameters are correct. Otherwise an exception is raised.

## See also

`fuzzy_entropy`

## References

M.K. Kundu, S.K. Pal: “Automatic selection of object enhancement
operator with quantitative justification based on fuzzy set theoretic
measures”; Pattern Recognition Letters 11; 1990; pp. 811-829.

## Module

Foundation
