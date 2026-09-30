## Drawing

List of Operators ↓

This chapter describes operators that allow the user to manually draw
geometric shapes. They require mouse interaction and in general block the
application until the mouse interaction is finished. For non-blocking
interactive creation of geometric shapes, HALCON also provides drawing
objects with the operators listed in [Graphics / Object](toc_graphics_object.md).

### General Objectives

The draw operators [`draw_region`](draw_region.md), [`draw_xld`](draw_xld.md), [`draw_xld_mod`](draw_xld_mod.md),
[`draw_nurbs`](draw_nurbs.md), [`draw_nurbs_mod`](draw_nurbs_mod.md), [`draw_nurbs_interp`](draw_nurbs_interp.md),
[`draw_nurbs_interp_mod`](draw_nurbs_interp_mod.md), as well as [`drag_region1`](drag_region1.md),
[`drag_region2`](drag_region2.md) and [`drag_region3`](drag_region3.md) return iconic objects.
All other draw operators return the geometric parameters that are needed to
create regions or contours in the respective shape (see table).
Most draw operators have a modifying variant that allows the user to
specify the initial parameters of the shown shape.

### Drawing in Buffer Windows

Because the draw operators rely on mouse interaction, they generally do
not work when used with buffer windows (see [`open_window`](open_window.md)), so you
should use drawing objects instead. Nevertheless some operators (see table)
can be used in buffer windows.
These operators are controlled through a mouse state.
In order to use these operators (and to not cause a deadlock) the
application has to provide the mouse state with the operators
[`send_mouse_double_click_event`](send_mouse_double_click_event.md), [`send_mouse_down_event`](send_mouse_down_event.md),
[`send_mouse_drag_event`](send_mouse_drag_event.md) and [`send_mouse_up_event`](send_mouse_up_event.md) as well as the
state of the modifier keys (also by using [`send_mouse_drag_event`](send_mouse_drag_event.md)),
whereas the draw operators themselves must be run in another thread.
While using the draw operator, the image section must not be changed.

| Drawing Operators | Output | Generate Object | Works in Buffer Windows |
| --- | --- | --- | --- |
| [`draw_point`](draw_point.md) | `row`, `column` | [`gen_cross_contour_xld`](gen_cross_contour_xld.md) | yes |
| [`draw_line`](draw_line.md) | `row_1`, `column_1`, `row_2`, `column_2` | [`gen_contour_polygon_xld`](gen_contour_polygon_xld.md) | yes |
| [`draw_rectangle1`](draw_rectangle1.md) | `row_1`, `column_1`, `row_2`, `column_2` | [`gen_rectangle1`](gen_rectangle1.md) | yes |
| [`draw_rectangle2`](draw_rectangle2.md) | `row`, `column`, `phi`, `length_1`, `length_2` | [`gen_rectangle2`](gen_rectangle2.md), [`gen_rectangle2_contour_xld`](gen_rectangle2_contour_xld.md) | yes |
| [`draw_circle`](draw_circle.md) | `row`, `column`, `radius` | [`gen_circle`](gen_circle.md), [`gen_circle_contour_xld`](gen_circle_contour_xld.md) | yes |
| [`draw_ellipse`](draw_ellipse.md) | `row`, `column`, `phi`, `radius_1`, `radius_2` | [`gen_ellipse`](gen_ellipse.md), [`gen_ellipse_contour_xld`](gen_ellipse_contour_xld.md) | yes |
| [`draw_xld`](draw_xld.md) | `contour` | - | yes |
| [`draw_region`](draw_region.md) | `region` | - | yes |
| [`draw_polygon`](draw_polygon.md) | `region` | - | yes |
| [`draw_nurbs`](draw_nurbs.md) | `contour`, `rows`, `columns`, `weights` | - | no |
| [`draw_nurbs_interp`](draw_nurbs_interp.md) | `contour`, `rows`, `columns`, `knots`, `tangents` | - | no |
| [`drag_region1`](drag_region1.md) | `region` | - | no |
| [`drag_region2`](drag_region2.md) | `region` | - | no |
| [`drag_region3`](drag_region3.md) | `region` | - | no |
|  |

---

#### List of Operators

- [`drag_region1`](drag_region1.md) — Interactive moving of a region.

- [`drag_region2`](drag_region2.md) — Interactive movement of a region with fixpoint specification.

- [`drag_region3`](drag_region3.md) — Interactive movement of a region with restriction of positions.

- [`draw_circle`](draw_circle.md) — Interactive drawing of a circle.

- [`draw_circle_mod`](draw_circle_mod.md) — Interactive drawing of a circle.

- [`draw_ellipse`](draw_ellipse.md) — Interactive drawing of an ellipse.

- [`draw_ellipse_mod`](draw_ellipse_mod.md) — Interactive drawing of an ellipse.

- [`draw_line`](draw_line.md) — Draw a line.

- [`draw_line_mod`](draw_line_mod.md) — Draw a line.

- [`draw_nurbs`](draw_nurbs.md) — Interactive drawing of a NURBS curve.

- [`draw_nurbs_interp`](draw_nurbs_interp.md) — Interactive drawing of a NURBS curve using interpolation.

- [`draw_nurbs_interp_mod`](draw_nurbs_interp_mod.md) — Interactive modification of a NURBS curve using interpolation.

- [`draw_nurbs_mod`](draw_nurbs_mod.md) — Interactive modification of a NURBS curve.

- [`draw_point`](draw_point.md) — Draw a point.

- [`draw_point_mod`](draw_point_mod.md) — Draw a point.

- [`draw_polygon`](draw_polygon.md) — Interactive drawing of a polygon row.

- [`draw_rectangle1`](draw_rectangle1.md) — Draw a rectangle parallel to the coordinate axis.

- [`draw_rectangle1_mod`](draw_rectangle1_mod.md) — Draw a rectangle parallel to the coordinate axis.

- [`draw_rectangle2`](draw_rectangle2.md) — Interactive drawing of any orientated rectangle.

- [`draw_rectangle2_mod`](draw_rectangle2_mod.md) — Interactive drawing of any orientated rectangle.

- [`draw_region`](draw_region.md) — Interactive drawing of a closed region.

- [`draw_xld`](draw_xld.md) — Interactive drawing of a contour.

- [`draw_xld_mod`](draw_xld_mod.md) — Interactive modification of a contour.
