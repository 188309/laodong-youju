# 劳动有据：公开资料与匿名社区

访问：https://188309.github.io/laodong-youju/
社区：https://188309.github.io/laodong-youju/community.html

首页法律资料无须登录。社区支持匿名文字投稿、评论回复、公司/关键词/城市/类型搜索、审核状态、撤回与举报。

## 架构与真实能力

- GitHub Pages 只托管前端，不能保存投稿。社区通过 HTTPS 调用劳动有据已有后端 `/api/community`，数据保存在 Cloudflare D1。
- 后端地址：`https://laodong-youju.merrydune18.chatgpt.site`。网络必须能访问该域名；前端打开不代表后端一定可达。断网或接口失败时显示错误，不模拟成功或伪造故事。
- 匿名社区使用独立的随机访问凭据，当前浏览器保留90天；恢复码365天。服务器只存哈希。匿名凭据无管理员及私密证据权限。
- 投稿和评论先审核后公开；管理员使用原版网站的受控后台。审核不代表违法认定。撤回内容隐藏，审核记录保留。
- 此入口仅接收脱敏文字；图片/视频上传、手机号认证、AI个案分析尚未接入。未承诺中国境内数据存储或全国网络可用性。
- 内容默认没有种子数据、虚构用户或案例；只有真实审核通过的内容进入社区。

## 发布

保持 Pages 设置：Deploy from a branch → main → / (root)。根目录的 index.html、community.html、community.css、community.js 和 .nojekyll 用于实际访问。

`python build.py` 根据 template.html 与 law-sources.json 生成首页，同时将社区文件复制到 dist。不要编辑生成后的法条内容来冒充最新核查；资料核查日期见页面。

源码不包含身份凭据、恢复码、用户投稿、私密材料或服务端密钥。社区后端独立部署，不能把后台密钥写入 JavaScript。修改域名需同步服务端精确 CORS 白名单。
