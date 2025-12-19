---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/get-iisconfigelement?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IISConfigElement
---

# Get-IISConfigElement

## 摘要
从一个 IIS 配置节或一个配置元素中获取一个配置元素对象。

## 语法

```
Get-IISConfigElement [-ConfigElement] <ConfigurationElement> [[-ChildElementName] <String>]
 [<CommonParameters>]
```

## 描述
`Get-IISConfigElement` cmdlet 可以从 `ConfigurationSection` 或 `ConfigurationElement` 中获取一个子 `ConfigurationElement` 对象。

## 示例

### 示例 1：获取 IIS 网站的配置元素
```
PS C:\> $ConfigSection = Get-IISConfigSection -SectionPath "system.applicationHost/sites"
PS C:\> $SitesCollection = Get-IISConfigCollection -ConfigElement $ConfigSection
PS C:\> $Site = Get-IISConfigCollectionElement -ConfigCollection $SitesCollection -ConfigAttribute @{"name" = "Default Web Site"}
PS C:\> $Elem = Get-IISConfigElement -ConfigElement $Site -ChildElementName "limits"
PS C:\> Get-IISConfigAttributeValue -ConfigElement $Elem -AttributeName "MaxUrlSegments"
```

该命令将“Default Web Site”的配置元素限制信息返回到Windows PowerShell变量$Elem中。

## 参数

### -ChildElementName
指定要返回的子配置元素（ConfigurationElement）的名称。如果省略此参数，则将返回给定父元素的所有子元素。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ConfigElement
指定要返回子配置元素（ConfigurationElement）所对应的 IIS ConfigurationSection 或 ConfigurationElement。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### Microsoft.WebAdministration.ConfigurationElement

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[Remove-IISConfigElement](./Remove-IISConfigElement.md)

[适用于 Windows PowerShell 的 IIS 管理 cmdlet](./iisadministration.md)

