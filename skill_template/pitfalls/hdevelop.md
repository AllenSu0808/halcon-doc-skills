# HDevelop 常見陷阱

來源標示：「文件」表示可在 `references/` 查證；「經驗」表示本文件未收錄的一般使用經驗。

## 呼叫語法

1. 簽章格式為 `op (輸入物件 : 輸出物件 : 輸入控制 : 輸出控制)`；在程式中呼叫時
   所有參數依同樣順序以逗號分隔，例如 `threshold (Image, Region, 128, 255)`。（文件：Signature）
2. 所有參數都必須傳入，沒有預設值；預設值以 `params` 查 `Default`。（文件）
3. 輸出參數位置必須是變數，不能是常值或運算式。（經驗）
4. 運算子名稱與括號之間慣例有一個空白（`read_image (Image, 'fabrik')`）。（經驗）

## 字串、tuple 與運算式

5. 字串只能用單引號 `'text'`；雙引號不是字串。（經驗）
6. 字串中的反斜線要跳脫（`'C:\\images'`），路徑建議用 `/`。（經驗）
7. 指派用 `:=`；相等比較用 `==`，不等用 `!=`（或 `#`）。（經驗）
8. tuple 以 `[a, b, c]` 建立與串接（`[T1, T2]`），`[]` 是空 tuple。（經驗）
9. tuple 索引從 0 開始（`T[0]`），長度用 `|T|`；但 `select_obj` 等 iconic 物件索引從 1 開始。
   （文件：select_obj）
10. 兩個整數相除得到整數（`5 / 2` 為 2）；需要小數時寫成 `5.0 / 2`。（經驗）
11. tuple 與單一值做算術時會逐元素運算；兩個長度不同（且都大於 1）的 tuple 做運算會出錯。（經驗）
12. 角度函式：`rad(90)`、`deg(3.14)`。（經驗）

## 控制流程

13. 區塊語法：`if (...)` … `elseif (...)` … `else` … `endif`；
    `for I := 0 to N - 1 by 1` … `endfor`；`while (...)` … `endwhile`。（經驗）
14. 例外處理：`try` … `catch (Exception)` … `endtry`；錯誤碼用 `dev_get_exception_data`
    或 `Exception[0]` 取得。（文件：dev_get_exception_data）
15. 以 `*` 開頭的行是註解。（經驗）
16. 自訂 procedure 的呼叫語法與運算子相同；`check` 會把 `.hdev` 內定義的 procedure 排除，
    但外部 procedure（`.hdvp`）會被報為 `[unknown-operator]`，可忽略。（經驗）

## dev_* 運算子

17. `dev_*` 運算子只在 HDevelop 環境有效；匯出成 C# / Python 時會被省略或改寫，
    不要讓程式邏輯依賴它們。（文件：dev_* 頁面）
18. 批次處理時在程式開頭關閉畫面更新：`dev_update_window ('off')`、`dev_update_var ('off')`、
    `dev_update_pc ('off')`，避免每一步都更新而變慢（文件：dev_update_window 等）；
    常見的 `dev_update_off ()` 是包裝這三者的程序庫 procedure，不是運算子。（經驗）
19. 顯示用 `dev_display`，設定顏色與繪製方式用 `dev_set_color`、`dev_set_draw`。（文件）
20. 需要可匯出的顯示程式時，改用 `open_window` / `disp_obj` 等一般運算子。（文件）

## 物件與記憶體

21. iconic 變數可能包含多個物件，用 `count_obj` 取得數量、`select_obj` 取出單一物件。（文件）
22. 空物件用 `gen_empty_obj`，累加物件用 `concat_obj`。（文件）
23. Handle 在所有參考被覆寫後會自動清除；需要立即釋放時用 `clear_handle` 或
    `clear_shape_model` 等專用運算子，之後 handle 失效。（文件：clear_handle）
24. `reduce_domain` 只改變影像的定義域，不裁切影像；需要實際裁切時用 `crop_domain`。（文件）

## 座標、角度與單位

25. 座標順序是 (Row, Column) = (y, x)。（文件）
26. 大多數角度參數是弧度（`angle.rad`），少數是度數（`angle.deg`，例如 `rotate_image` 的
    `Phi`）；以 `params` 查看參數標頭。（文件：rotate_image）
27. 像素座標以像素中心為整數座標，左上角像素中心為 (0, 0)。（經驗）

## 字串參數

28. 字串值必須完全一致，先以 `params` 查 `List of values`；`check` 會標出不合法的字串常值。（文件）
29. `'auto'` 只能用在文件列出 `'auto'` 的參數。（文件）
30. `Suggested values` 不是完整清單；泛用參數（`GenParamName` / `GenParamValue`）以兩個
    等長 tuple 成對傳入。（文件）

## 檔案

31. `.hdev` 是 XML，程式行包在 `<l>…</l>` 中，`<` `>` 會被寫成 `&lt;` `&gt;`；
    直接編輯 XML 時要保持跳脫。（經驗）
32. `read_image` 會搜尋 `image_dir` 系統參數並自動嘗試補副檔名。（文件：read_image）
