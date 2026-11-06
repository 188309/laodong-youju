# 劳动有据：公开资料与匿名社区

访问：https://188309.github.io/laodong-youju/
社区试运行：https://188309.github.io/laodong-youju/community-cn.html
原社区记录：https://188309.github.io/laodong-youju/community.html#mine

首页法律资料无须登录。社区支持匿名文字投稿、评论回复、公司/关键词/城市/类型搜索、审核状态、撤回与举报。

## 架构与真实能力

- GitHub Pages 只托管前端，不能保存投稿。新社区通过 HTTPS 调用腾讯云上海 CloudBase 后端 `/api/community`，投稿、评论、昵称、审核和举报记录保存在独立的 PostgreSQL schema。
- 新后端地址：`https://uncomfortable-trout-d4br5a14f22b-1525819918.ap-shanghai.app.tcloudbase.com`。目前使用开发测试默认域名，不承诺长期稳定服务或全国所有网络均可访问。前端打开不代表后端一定可达；失败时显示真实错误。
- 原 `community.html` 和 `community.js` 继续连接原 Cloudflare D1 服务。原记录未删除或迁移，新旧匿名凭据分别保存，恢复码不通用。
- 匿名社区使用独立的随机访问凭据，当前浏览器保留90天；恢复码365天。服务器只存哈希。匿名凭据无管理员及私密证据权限。
- 投稿和评论先审核后公开。新社区当前由管理员使用腾讯云 PostgreSQL 控制台审核，尚未提供可视化审核后台；原版网站后台只管理原社区。审核不代表违法认定。撤回内容隐藏，审核记录保留。
- 此入口仅接收脱敏文字；图片/视频上传、手机号认证、AI个案分析尚未接入。数据库位于上海不等于网页托管和所有服务商日志均位于中国境内。
- 内容默认没有种子数据、虚构用户或案例；只有真实审核通过的内容进入社区。

## 发布

保持 Pages 设置：Deploy from a branch → main → / (root)。根目录的 index.html、community-cn.html、community-cn.js、community.css 和 .nojekyll 用于新入口；保留 community.html 与 community.js 供原记录访问。

`python build.py` 根据 template.html 与 law-sources.json 生成首页，同时将社区文件复制到 dist。不要编辑生成后的法条内容来冒充最新核查；资料核查日期见页面。

源码不包含身份凭据、恢复码、用户投稿、私密材料或服务端密钥。社区后端独立部署，不能把后台密钥写入 JavaScript。修改域名需同步服务端精确 CORS 白名单。
