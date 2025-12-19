---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/remove-iisconfigelement?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-IISConfigElement
---

# 删除 IIS 配置元素

## 摘要
删除指定的配置元素。

## 语法

```
Remove-IISConfigElement [-ConfigElement] <ConfigurationElement> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-IISConfigElement` cmdlet 用于删除指定的配置元素。这样做会导致该配置元素继承其父元素的属性（如果存在的话），或者使用架构中规定的默认值。如果被删除的配置元素是一个集合元素，那么它将从该集合中移除；在这种情况下，其功能与 `Remove-IISConfigCollectionElement` 是等效的。

## 示例

### 示例 1：从 IIS 网站中删除一个配置元素
```
PS C:\> Get-IISConfigSection "system.webServer/defaultDocument" -CommitPath "Default Web Site" | Remove-IISConfigElement
```

此命令会从 IIS 网站“Default Web Site”中包含的网页配置文件中删除某个配置部分。

## 参数

### -ConfigElement
指定要删除的 Internet Information Services (IIS) 的 ConfigurationSection 或 ConfigurationElement 对象。

```yaml
Type: ConfigurationElement
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet运行时会发生什么情况。但实际上该cmdlet并没有被执行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于_CommonParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### Microsoft.Web ADMINISTRATION.ConfigurationElement

## 输出

### System.Object

## 备注

## 相关链接

[Get-IISConfigElement](./Get-IISConfigElement.md)

[Remove-IISConfigCollectionElement](./Remove-IISConfigCollectionElement.md)

[适用于 Windows PowerShell 的 IIS 管理 cmdlet](./iisadministration.md)

