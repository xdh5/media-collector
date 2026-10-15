# 获取作者作品列表

实现在 media-collector 子仓库的 `core/list_author_works`。公开方法是 `list_author_works` 和 `resolve_author_profile`。

`list_author_works(profile_url, limit)` 读取作者主页最新作品，按发布时间从新到旧返回，最多 `limit` 条。每条包含 `aweme_id`、`work_url`、`title`、`author_name`、`sec_user_id`、`published_at`、`cover_url`、`is_video`。`work_url` 是 `https://www.douyin.com/video/{aweme_id}`，可交给 `download_video.download`。

`resolve_author_profile(profile_text)` 把主页链接或 `sec_user_id` 规范成 `sec_user_id` 和主页地址。短链会先跟随跳转。

## 配置

`.env` 填写 `DY_COOKIES`：登录 https://www.douyin.com 后，从任意 `/aweme/v1/web/` 请求复制完整 Cookie，必须包含 `UIFID`。
