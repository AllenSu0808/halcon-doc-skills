# trans_from_rgb (Operator)

## Name

`trans_from_rgb` — Transform an image from the RGB color space to an arbitrary color space.

## Signature

`trans_from_rgb(ImageRed, ImageGreen, ImageBlue : ImageResult1, ImageResult2, ImageResult3 : ColorSpace : )`

## Description

`trans_from_rgb` transforms an image from the RGB color
space to an arbitrary color space (*`ColorSpace`*).
The three channels of the image are passed as three separate images on
input and output.

The operator `trans_from_rgb` supports the image types
`byte`, `uint2`, `int4`, and `real`.
In the case of `real` images, all values should lay within
0 and 1. If not, the results of the transformation may not be reasonable.

Certain scalings are performed accordingly to the image type:

- Considering `byte` and `uint2` images, the domain of
  color space values is generally mapped to the full domain of
  [0..255] or [0..65535], respectively.
  Because of this, the origin of signed values (e.g., CIELab)
  may not be at the center of the domain.
- Hue values are represented by angles of [0..2$\pi$[
  and are coded for the particular image types differently:

  - `byte`-images map the angle domain to [0..255].
  - `uint2`/`int4`-images are coded in
    minutes of arc [0..21600[, except for the transformations
    *'cielchab'* and *'cielchuv'* for
    `int4`-images, where they are coded in
    seconds of arc [0..1296000[.
  - `real`-images are coded in radians
    [0..2$\pi$[, except for the transformations
    *'cielchab'* and *'cielchuv'*, where the
    standards ISO 11664-4:2008 and ISO 11664-5:2009 require the
    hue to be specified in degrees.
- Saturation values are represented by percentages of [0..100]
  and are coded differently for the particular image type:

  - `byte`-images map the saturation values
    to [0..255].
  - `uint2`/`int4`-images map the
    saturation values to [0..10000].
  - `real`-images map the saturation values
    to [0..1].

Supported are the transformations listed below.
Note, all domains are based on RGB values scaled to [0; 1]. To
obtain the domain of a certain image type, they must be
scaled accordingly with the value range.
Due to different precision the values obtained using the given equations
may slightly differ from the values returned by the operator.

- **'yiq'** —

  $$Y = 0.299R + 0.587G + 0.114B I = -0.27(B - Y) + 0.74(B - Y) Q = 0.41(B - Y) + 0.48(R - Y)$$ ![figure](../assets/4aa1b323e14579a6.svg)

  Value range:
  $Y\in[0;1]$,
  $I\in[-0.59947;0.59947]$,
  $Q\in[-0.52243;0.52243]$
- **'yuv'** —

  $$Y = 0.299R + 0.587G + 0.114B U = 0.493(B - Y) V = 0.877(R - Y)$$ ![figure](../assets/d3e35d9d705b399f.svg)
  Note, this implies that $\text{Y}$, $\text{U}$, and $\text{V}$ are not
  independent of each other.

  Value range:
  $Y\in[0.0;1.0]$,
  $U\in[-0.436798;0.436798]$,
  $V\in[-0.614777;0.614777]$
- **'argyb'** —

  $$\begin{pmatrix} A \\ R_q \\ Y_b \end{pmatrix} = \begin{pmatrix} 0.30 & 0.59 & 0.11 \\ 0.50 & -0.50 & 0.00 \\ 0.25 & 0.25 & -0.50 \end{pmatrix} \begin{pmatrix} R \\ G \\ B \end{pmatrix}$$ ![figure](../assets/778200bfeff81c4f.svg)

  Value range:
  $A\in[0;1]$,
  $Rg\in[-0.5;0.5]$,
  $Yb\in[-0.5;0.5]$
- **'ciexyz'** —

  $$\left(\begin{array}{c}X\\Y\\Z\end{array}\right) = \left(\begin{array}{ccc}0.412453 & 0.357580 & 0.180423\\0.212671 & 0.715160 & 0.072169\\0.019334 & 0.119193 & 0.950227\end{array}\right) \left(\begin{array}{c}R\\G\\B\end{array}\right)$$ ![figure](../assets/c17428f598854c9c.svg)
  The primary colors used correspond to sRGB respectively CIE Rec. 709.
  D65 is used as white point.

  - **Used primary colors (x, y, z):** —

    $$red:=\left(\begin{array}{c}0.6400\\0.3300\\0.0300\end{array}\right),\ green:=\left(\begin{array}{c}0.3000\\0.6000\\0.1000\end{array}\right),\ blue:=\left(\begin{array}{c}0.1500\\0.0600\\0.7900\end{array}\right),\ white_{65}:=\left(\begin{array}{c}0.3127\\0.3290\\0.3583\end{array}\right)$$ ![figure](../assets/8b56ee927304b199.svg)

  Value range:
  $X\in[0;0.950456]$,
  $Y\in[0;1]$,
  $Z\in[0;1.088754]$
- **'hls'** —

  ```
    Min := min([R, G, B])
    Max := max([R, G, B])
    L := (Min + Max) / 2
    if (Max == Min)
       H := 0
       S := 0
    else
       if (L > 0.5)
          S := (Max - Min) / (2 - Max - Min)
       else
          S := (Max - Min) / (Max + Min)
       endif
       if (R == Max)
          H := ((G - B) / (Max - Min)) * rad(60)
       elseif (G == Max)
          H := (2 + (B - R) / (Max - Min)) * rad(60)
       elseif (B == Max)
          H := (4 + (R - G) / (Max - Min)) * rad(60)
       endif
    endif
  ```

  Value range:
  $H\in[0;2\pi[$,
  $L\in[0;1]$,
  $S\in[0;1]$
- **'hsi'** —

  $$\begin{pmatrix} M1 \\ M2 \\ I1 \end{pmatrix} = \begin{pmatrix} \dfrac{2}{\sqrt{6}} & -\dfrac{1}{\sqrt{6}} & -\dfrac{1}{\sqrt{6}} \\ 0 & -\dfrac{1}{\sqrt{2}} & -\dfrac{1}{\sqrt{2}} \\ \dfrac{1}{\sqrt{3}} & \dfrac{1}{\sqrt{3}} & \dfrac{1}{\sqrt{3}} \end{pmatrix} \begin{pmatrix} R \\ G \\ B \end{pmatrix} \\ \begin{pmatrix} H \\ S \\ I \end{pmatrix} = \begin{pmatrix} \atan2(M2, M1) \\ \sqrt{M1^2 + M2^2} \\ \dfrac{I1}{\sqrt{3}} \\end{pmatrix}$$ ![figure](../assets/bbc9f50680f9ddd0.svg)

  Value range:
  $H\in[0;2\pi[$,
  $S \in [0; \sqrt{\frac{2}{3}}]$ ![figure](../assets/90ea807d5c621940.svg),
  $I\in[0;1]$

  Attention:
   `uint2`/`int4`-images map the saturation
  values to [0..65536].
- **'hsv'** —

  ```
    Min := min([R, G, B])
    Max := max([R, G, B])
    V := Max
    if (Max == Min)
       S := 0
       H := 0
    else
       S := (Max - Min) / Max
       if (R == Max)
          H := ((G - B) / (Max - Min)) * rad(60)
       elseif (G == Max)
          H := (2 + (B - R) / (Max - Min)) * rad(60)
       elseif (B == Max)
          H := (4 + (R - G) / (Max - Min)) * rad(60)
       endif
    endif
  ```

  Value range:
  $H\in[0;2\pi[$,
  $S\in[0;1]$,
  $V\in[0;1]$
- **'ihs'** —

  ```
    Min := min([R, G, B])
    Max := max([R, G, B])
    I := (R + G + B) / 3
    if (I == 0)
       H := 0
       S := 1
    else
       S := 1 - Min / I
       if (S == 0)
            H := 0
       else
          X := (R + R - G - B) / 2
          Y := (R - G) * (R - G) + (R - B) * (G - B)
          Z := sqrt(Y)
          if (Z == 0)
             H := 0
          else
             H := acos(X / Z)
          endif
          if (B > G)
             H := rad(360) - H
          endif
       endif
    endif
  ```

  Value range:
  $I\in[0;1]$,
  $H\in[0;1]$,
  $S\in[0;1]$
- **'cielab'** —

  $$\begin{pmatrix}X\\Y\\Z\end{pmatrix} = \begin{pmatrix}0.412453 & 0.357580 & 0.180423 \\ 0.212671 & 0.715160 & 0.072169 \\ 0.019334 & 0.119193 & 0.950227\end{pmatrix} \begin{pmatrix}R\\G\\B\end{pmatrix} \\ L = 116 f\left( \frac{Y}{Y_w} \right) - 16 \\ a = 500\left( f\left( \frac{X}{X_w} \right) - f\left( \frac{Y}{Y_w} \right) \right) \\ b = 200\left( f\left( \frac{Y}{Y_w} \right) - f\left( \frac{Z}{Z_w} \right) \right)$$ ![figure](../assets/990f6a5b5cfcb632.svg)
  where
  $$f(t) = {\begin{cases} t^{\tfrac{1}{3}}, \\\n\frac{841}{108} * t + \frac{4}{29}, \n\end{cases} \quad \text{if } t > \left( \tfrac{6}{29} \right)^3 \\ \text{otherwise} \n}$$ ![figure](../assets/99e23817a459dd61.svg)

  Black point B: ($R_{B}$, $G_{B}$, $B_{B}$) =
  (0, 0, 0)

  White point W (according to image type):

  - `byte`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    (255, 255, 255)
  - `uint2`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    ($2^{16}-1$, $2^{16}-1$,
    $2^{16}-1$)
  - `int4`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    ($2^{31}-1$, $2^{31}-1$,
    $2^{31}-1$)
  - `real`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    (1.0, 1.0, 1.0)

  Value range:
  $L\in[0;100]$,
  $a\in[-86.1813;98.2352]$,
  $b\in[-107.8617;94.4758]$
  (`byte` and `uint2`:
  scaled to the maximum gray value.
  `int4`:
  $\text{L}$ is scaled to the maximum gray value,
  $a$ and $\text{b}$ are scaled to the minimum gray value,
  such that the origin stays at 0.)
- **'cielchab'** —

  $$\begin{pmatrix}X\\Y\\Z\end{pmatrix}=\begin{pmatrix}0.412453&0.357580&0.180423\\0.212671&0.715160&0.072169\\0.019334&0.119193&0.950227\end{pmatrix}\begin{pmatrix}R\\G\\B\end{pmatrix}\n\nL=\;116f\left(\frac{Y}{Y_w}\right)-16\\n a=\;500\left(f\left(\frac{X}{X_w}\right)-f\left(\frac{Y}{Y_w}\right)\right)\\n b=\;200\left(f\left(\frac{Y}{Y_w}\right)-f\left(\frac{Z}{Z_w}\right)\right)\\nC_{ab}=\sqrt{a^2+b^2}\\nh_{ab}=\operatorname{atan2}(b,a)$$ ![figure](../assets/59db6b3815d574ad.svg)
  where
  $$f(t) = {\begin{cases} t^{\tfrac{1}{3}}, \\\n\frac{841}{108} * t + \frac{4}{29}, \n\end{cases} \quad \text{if } t > \left( \tfrac{6}{29} \right)^3 \\ \text{otherwise} \n}$$ ![figure](../assets/99e23817a459dd61.svg)

  $h_{ab}$ lies

  - between 0° and 90° if $a$ and $b$ are both positive,
  - between 90° and 180° if $a$ is negative and $b$ is
    positive,
  - between 180° and 270° if $a$ and $b$ are both
    negative, and
  - between 270° and 360° if $a$ is positive and $b$
    is negative.

  Black point B: ($R_{B}$, $G_{B}$, $B_{B}$) =
  (0, 0, 0)

  White point W (according to image type):

  - `byte`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    (255, 255, 255)
  - `uint2`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    ($2^{16}-1$, $2^{16}-1$,
    $2^{16}-1$)
  - `int4`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    ($2^{31}-1$, $2^{31}-1$,
    $2^{31}-1$)
  - `real`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    (1.0, 1.0, 1.0)

  Value range:
  $L\in[0;100]$,
  $C\in[0;133.8086]$,
  $h\in[0;360[$
  (`byte`:
  scaled to the maximum gray value.
  `uint2`:
  $\text{L}$ and $\text{C}$ are scaled to the maximum gray value,
  $\text{h}$ is given in minutes of arc.
  `int4`:
  $\text{L}$ and $\text{C}$ are scaled to the maximum gray value,
  $\text{h}$ is given in seconds of arc.)
- **'cieluv'** —

  $$\begin{pmatrix}X\\Y\\Z\end{pmatrix} = \begin{pmatrix}0.412453 & 0.357580 & 0.180423\\0.212671 & 0.715160 & 0.072169\\0.019334 & 0.119193 & 0.950227\end{pmatrix} \begin{pmatrix}R\\G\\B\end{pmatrix} \\ u' = \dfrac{4X}{(X + 15Y + 3Z)} \\ v' = \dfrac{9Y}{(X + 15Y + 3Z)} \\ u'_w = \dfrac{4X_w}{(X_w + 15Y_w + 3Z_w)} \\ v'_w = \dfrac{9Y_w}{(X_w + 15Y_w + 3Z_w)} \\ L = 116f\left(\dfrac{Y}{Y_w}\right) - 16 \\ u = 13L(u' - u'_w) \\ v = 13L(v' - v'_w)$$ ![figure](../assets/fba2d56c2ff41ede.svg)
  where
  $$f(t) = \begin{cases} t^{\frac{1}{3}}, \\ \frac{841}{108} * t + \frac{4}{29} & \text{if } t > \left(\frac{6}{29}\right)^{3} \\ \text{otherwise} \end{cases}$$ ![figure](../assets/4d83160613e780e2.svg)

  Black point B: ($R_{B}$, $G_{B}$, $B_{B}$) =
  (0, 0, 0)

  White point W (according to image type):

  - `byte`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    (255, 255, 255)
  - `uint2`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    ($2^{16}-1$, $2^{16}-1$,
    $2^{16}-1$)
  - `int4`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    ($2^{31}-1$, $2^{31}-1$,
    $2^{31}-1$)
  - `real`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    (1.0, 1.0, 1.0)

  Value range:
  $L\in[0;100]$,
  $u\in[-83.0774;175.0148]$,
  $v\in[-134.1008;107.3923]$
  (`byte` and `uint2`:
  scaled to the maximum gray value.
  `int4`:
  $\text{L}$ is scaled to the maximum gray value,
  $\text{u}$ and $\text{v}$ are scaled to the minimum gray value,
  such that the origin stays at 0.)
- **'cielchuv'** —

  $$\begin{pmatrix}X\\Y\\Z\end{pmatrix}=\begin{pmatrix}0.412453&0.357580&0.180423\\0.212671&0.715160&0.072169\\0.019334&0.119193&0.950227\end{pmatrix}\begin{pmatrix}R\\G\\B\end{pmatrix} u^{\prime}=\frac{4X}{(X+15Y+3Z)} v^{\prime}=\frac{9Y}{(X+15Y+3Z)} u^{\prime}_{w}=\frac{4X_{w}}{(X_{w}+15Y_{w}+3Z_{w})}\nv^{\prime}_{w}=\frac{9Y_{w}}{(X_{w}+15Y_{w}+3Z_{w})}\nL=116f\left(\frac{Y}{Y_{w}}\right)-16 u=13L(u^{\prime}-u^{\prime}_{w}) v=13L(v^{\prime}-v^{\prime}_{w}) C_{uv}=\sqrt{u^{2}+v^{2}} h_{uv}=\operatorname{atan2}(v,u)$$ ![figure](../assets/c03d9769b5f9e56a.svg)
  where
  $$f(t) = {\begin{cases} t^{\tfrac{1}{3}}, \\\n\frac{841}{108} * t + \frac{4}{29}, \n\end{cases} \quad \text{if } t > \left( \tfrac{6}{29} \right)^3 \\ \text{otherwise} \n}$$ ![figure](../assets/99e23817a459dd61.svg)

  Black point B: ($R_{B}$, $G_{B}$, $B_{B}$) =
  (0, 0, 0)

  White point W (according to image type):

  - `byte`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    (255, 255, 255)
  - `uint2`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    ($2^{16}-1$, $2^{16}-1$,
    $2^{16}-1$)
  - `int4`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    ($2^{31}-1$, $2^{31}-1$,
    $2^{31}-1$)
  - `real`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    (1.0, 1.0, 1.0)

  Value range:
  $L\in[0;100]$,
  $C\in[0;179.0402]$,
  $h\in[0;360[$
  (`byte`:
  scaled to the maximum gray value.
  `uint2`:
  $\text{L}$ and $\text{C}$ are scaled to the maximum gray value,
  $\text{h}$ is given in minutes of arc.
  `int4`:
  $\text{L}$ and $\text{C}$ are scaled to the maximum gray value,
  $\text{h}$ is given in seconds of arc.)
- **'i1i2i3'** —

  $$\begin{pmatrix}I_1\\I_2\\I_3\end{pmatrix} = \begin{pmatrix}0.333 & 0.333 & 0.333\\1.0 & 0.0 & -1.0\\-0.5 & 1.0 & -0.5\end{pmatrix} \begin{pmatrix}R\\G\\B\end{pmatrix}$$ ![figure](../assets/d5dcc29d0f841369.svg)

  Value range:
  $I1\in[0;1]$,
  $I2\in[-1;1]$,
  $I3\in[-1;1]$
- **'ciexyz2'** —

  $$\begin{pmatrix}X\\Y\\Z\end{pmatrix}=\begin{pmatrix}0.639175&0.175258&0.185567\\0.306931&0.584158&0.108911\\0.000000&0.060773&0.939227\end{pmatrix}\begin{pmatrix}R\\G\\B\end{pmatrix}$$ ![figure](../assets/b79eb42f4f76a4f9.svg)

  Value range:
  $X\in[0;1.0]$,
  $Y\in[0;1.0]$,
  $Z\in[0;1.0]$
- **'ciexyz3'** —

  $$\begin{pmatrix} X \\ Y \\ Z \end{pmatrix} = \begin{pmatrix} 0.618 & 0.177 & 0.205 \\ 0.299 & 0.587 & 0.114 \\ 0.000 & 0.056 & 0.944 \end{pmatrix} \begin{pmatrix} R \\ G \\ B \end{pmatrix}$$ ![figure](../assets/75240cd2bcd4ed07.svg)

  Value range:
  $X\in[0;1]$,
  $Y\in[0;1]$,
  $Z\in[0;1]$
- **'ciexyz4'** —

  $$\begin{pmatrix}X\\Y\\Z\end{pmatrix}=\begin{pmatrix}0.476&0.299&0.175\\0.262&0.656&0.082\\0.020&0.161&0.909\end{pmatrix}\begin{pmatrix}R\\G\\B\end{pmatrix}$$ ![figure](../assets/f39225c64c1f8fc2.svg)

  - **Used primary colors (x, y, z):** —

    $$red:=\left(\begin{array}{c}0.628\\0.346\\0.026\end{array}\right),\ green:=\left(\begin{array}{c}0.268\\0.588\\0.144\end{array}\right),\ blue:=\left(\begin{array}{c}0.150\\0.070\\0.780\end{array}\right),\ white_{65}:=\left(\begin{array}{c}0.313\\0.329\\0.358\end{array}\right)$$ ![figure](../assets/a118d7e868cf11fe.svg)

  Value range:
  $X\in[0;0.95]$,
  $Y\in[0;1]$,
  $Z\in[0;1.09]$
- **'lms'** —

  $$\begin{pmatrix}L\\M\\S\end{pmatrix}=\begin{pmatrix}0.390469&0.549910&0.008901\\0.070925&0.963118&0.001358\\0.023143&0.128013&0.935976\end{pmatrix}\begin{pmatrix}R\\G\\B\end{pmatrix}$$ ![figure](../assets/1564ba1b4fa22516.svg)
  This conceptually is a transformation from RGB to CIE XYZ
  (see *'ciexyz'* above) followed by a transformation from
  CIE XYZ to LMS.

  Value range:
  $L\in[0;0.949280]$,
  $M\in[0;1.035401]$,
  $S\in[0;1.087132]$

## Attention

As the calculations are made with a different numerical precision, the
OpenCL implementation of the cielab transformation for images of type `int4`
is slightly less accurate than the pure C version.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on domain level.

## Parameters

**`ImageRed`** (input_object)  singlechannelimage(-array) `→` object (byte / uint2 / int4 / real)

Input image (red channel).

**`ImageGreen`** (input_object)  singlechannelimage(-array) `→` object (byte / uint2 / int4 / real)

Input image (green channel).

**`ImageBlue`** (input_object)  singlechannelimage(-array) `→` object (byte / uint2 / int4 / real)

Input image (blue channel).

**`ImageResult1`** (output_object)  singlechannelimage(-array) `→` object (byte / uint2 / int4 / real)

Color-transformed output image (channel 1).

**`ImageResult2`** (output_object)  singlechannelimage(-array) `→` object (byte / uint2 / int4 / real)

Color-transformed output image (channel 1).

**`ImageResult3`** (output_object)  singlechannelimage(-array) `→` object (byte / uint2 / int4 / real)

Color-transformed output image (channel 1).

**`ColorSpace`** (input_control)  string `→`  (string)

Color space of the output image.

Default:
'hsv'

List of values:
'argyb', 'cielab', 'cielchab', 'cielchuv', 'cieluv', 'ciexyz', 'ciexyz2', 'ciexyz3', 'ciexyz4', 'hls', 'hsi', 'hsv', 'i1i2i3', 'ihs', 'lms', 'yiq', 'yuv'

List of values (for compute devices):
'cielab', 'cielchab', 'cieluv', 'cielchuv', 'hsv', 'hsi'

## Example (HDevelop)

```
* Transformation from rgb to hsv and conversely
read_image(Image,'patras')
dev_display(Image)
decompose3(Image, Image1, Image2, Image3)
trans_from_rgb(Image1,Image2,Image3,ImageH,ImageS,ImageV,'hsv')
trans_to_rgb(ImageH,ImageS,ImageV,ImageR,ImageG,ImageB,'hsv')
compose3(ImageR,ImageG,ImageB,Multichannel)
dev_display(Multichannel)
```

## Result

`trans_from_rgb` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system(::'no_object_result', <Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`decompose3`

## Possible Successors

`compose3`

## Alternatives

`linear_trans_color`,
`rgb1_to_gray`,
`rgb3_to_gray`

## See also

`trans_to_rgb`

## References

ITU-R BT.470-6: “Conventional Television Systems”, 1998.
  
ISO 11664-4:2008: “Colorimetry --- Part 4: CIE 1976 L*a*b* Colour
Space”, 2008.
  
ISO 11664-5:2009: “Colorimetry --- Part 5: CIE 1976 L*u*v* Colour
space and u',v' uniform chromaticity scale diagram”, 2009.

## Module

Foundation
