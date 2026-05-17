# UI Skills Collection

[English](README.md) | **中文**

这是一个个人 UI 设计库和 Codex 插件集合，用来帮助 Codex 更稳定地设计、审查、重构和打磨前端界面。

这个仓库不是把所有 UI prompt 或 skill 都塞进来。它保留的是更少但更硬的核心：产品/品牌界面的判断、官方 skill 结构范式、视觉层级、可访问性、动效克制、响应式检查，以及让界面更像成品的细节规则。

## 内容结构

```text
.agents/plugins/marketplace.json
plugins/ui-skills/.codex-plugin/plugin.json
plugins/ui-skills/skills/ui-craft/SKILL.md
plugins/ui-skills/skills/ui-audit/SKILL.md
plugins/ui-skills/docs/
demos/homepage-variants/
docs/personal-design-library-roadmap.md
scripts/validate_plugin.py
```

## Skills

- `ui-craft`：设计、构建、重构、细化和打磨 UI。
- `ui-audit`：审查现有 UI，并输出可执行的问题清单。

## 当前设计思想

当前版本已经从主动插件思想里移除了 UI/UX Pro Max、Taste、ui-skills。它们适合做对比参考，但会让这个库变得太依赖检索、太强制风格化，或者规则重复。

现在保留的是更收敛的一组：

- Impeccable 的产品/品牌 register 判断。
- Anthropic 官方 skill 的结构范式和 frontend-design 的紧凑方向选择。
- User Interface Wiki 的审核优先级。
- Make Interfaces Feel Better 的细节打磨。
- Designer Skills 里关于系统、层级、表单和评审的词汇。
- 少量 0xdesign 式多方案探索思路。

## Demo

打开 [demos/homepage-variants/index.html](demos/homepage-variants/index.html) 可以看三版基于当前设计思想做出的首页方向。

预览图：

- [产品操作台](demos/homepage-variants/product-preview.png)
- [编辑品牌页](demos/homepage-variants/editorial-preview.png)
- [沉浸工作室](demos/homepage-variants/cinematic-preview.png)
- [移动端检查](demos/homepage-variants/mobile-preview.png)

## 后续优化方向

下一步是把它从“好用的 UI plugin”变成真正的个人设计库。路线图在 [docs/personal-design-library-roadmap.md](docs/personal-design-library-roadmap.md)。

## 校验

```bash
python scripts/validate_plugin.py
```

## 仓库

远程仓库：<https://github.com/sn0wjin19/ui-skills-collection>
