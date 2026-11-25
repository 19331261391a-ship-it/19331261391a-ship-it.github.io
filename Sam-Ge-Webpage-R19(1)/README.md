# Sam Ge Webpage — R19

- `Sam-Ge-Webpage-R19.html`：单文件版，照片已内嵌，可直接打开。
- `index.html` 与 `images/`：部署版，上传时保持目录结构。
- `collaborator-sources.json`：人物资料、核查来源与照片路径。
- `Collaborator-review.md`：本次修改说明与核查限制。

当前共 17 位 Collaborators，17 张本地人物照片，无字母占位图。Xiaoling Liang 使用用户上传的原始 JPEG。

替换照片后，在本目录运行 `python rebuild-standalone.py`（Windows 可用 `py rebuild-standalone.py`），可同步更新单文件版。
Google Scholar 数据逻辑沿用原版，部署时保留原站的 `scholar.json` 及更新配置。
