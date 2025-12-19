---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/clear-iisconfigcollection?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Clear-IISConfigCollection
---

# 清除 IIS 配置集合

## 摘要
清除一个 IIS 配置集合。

## 语法

```
Clear-IISConfigCollection [-ConfigCollection] <ConfigurationElementCollection> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Clear-IISConfigCollection` cmdlet 用于清除指定的 Internet Information Services (IIS) 集合，方法是通过删除所有元素并添加一个 `<clear>` 标签来实现。这样做可以防止该集合从上级集合继承任何元素（如果存在的话）。

## 示例

### 示例 1：清除默认网站的 `defaultDocument` 设置。这些设置是从服务器级别继承而来的，并在 `applicationHost.config` 文件中定义的。
```
PS C:\> Get-IISConfigSection -SectionPath "system.webServer/defaultDocument" -CommitPath "Default Web Site" | Get-IISConfigCollection -CollectionName "files" | Clear-IISConfigCollection -Confirm:$False
```

这个命令会在 `web.config` 文件中添加一些行，而 `web.config` 是默认网站的配置文件。

## 参数

### -ConfigCollection
指定要清除其集合元素的 **ConfigurationCollection** 对象。如果事先已经获取了一个 **ConfigurationCollection** 并将其赋值给某个变量，那么就无法通过管道将该对象传递给此 cmdlet，因为管道引擎会尝试对其进行遍历，并传递出 **ConfigurationElement** 对象。请尝试将整个 **Get-IISConfigCollection** cmdlet 传递到管道中，或者将其作为参数使用，以获得正确的结果。

```yaml
Type: ConfigurationElementCollection
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

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
展示了如果运行该 cmdlet 会发生什么情况。但实际上并没有运行该 cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### Microsoft.Web ADMINISTRATION.ConfigurationElementCollection

## 输出

### System.Object

## 备注

## 相关链接

[Get-IISConfigCollection](./Get-IISConfigCollection.md)

[用于 Windows PowerShell 的 IIS 管理 cmdlet](./iisadministration.md)

