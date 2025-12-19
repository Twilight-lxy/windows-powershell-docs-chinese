---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/get-iisconfigcollection?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IISConfigCollection
---

# Get-IISConfigCollection

## 摘要
从一个 IIS 配置节或配置元素中获取一个配置集合对象。

## 语法

```
Get-IISConfigCollection [-ConfigElement] <ConfigurationElement> [[-CollectionName] <String>]
 [<CommonParameters>]
```

## 描述
`Get-IISConfigCollection` cmdlet 可以从 `ConfigurationSection` 或 `ConfigurationElement` 中获取一个 `ConfigurationCollection` 对象。

建议不要将此值作为参数传递给后续的 cmdlet，因为 Windows PowerShell 无法解析该对象。这是因为 `ConfigurationCollection` 实现了 `IEnumerable` 接口，当以这种方式使用时，管道处理器会遍历其中的每个元素。因此，要么直接将整个 `Get-IISConfigCollection` cmdlet 传递到管道中，要么将其作为参数传递。

## 示例

### 示例 1：从 IIS 配置元素中获取配置集合
```
PS C:\> Get-IISConfigSection -SectionPath "system.webServer/defaultDocument" | Get-IISConfigCollection -CollectionName "files"

Attributes      : {value}
ChildElements   : {}
ElementTagName  : add
IsLocallyStored : True
Methods         :
RawAttributes   : {[value, Default.htm]}
Schema          : Microsoft.Web.Administration.ConfigurationElementSchema

Attributes      : {value}
ChildElements   : {}
ElementTagName  : add
IsLocallyStored : True
Methods         :
RawAttributes   : {[value, Default.asp]}
Schema          : Microsoft.Web.Administration.ConfigurationElementSchema
```

这个命令用于获取系统.webServer/defaultDocument部分的文件集合。

### 示例 2：从 IIS 配置部分中获取一个配置元素
```
PS C:\> Get-IISConfigSection -SectionPath "system.webServer/defaultDocument" | Get-IISConfigElement -ChildElementName "files" | Get-IISConfigCollection


Attributes      : {value}
ChildElements   : {}
ElementTagName  : add
IsLocallyStored : True
Methods         :
RawAttributes   : {[value, Default.htm]}
Schema          : Microsoft.Web.Administration.ConfigurationElementSchema

Attributes      : {value}
ChildElements   : {}
ElementTagName  : add
IsLocallyStored : True
Methods         :
RawAttributes   : {[value, Default.asp]}
Schema          : Microsoft.Web.Administration.ConfigurationElementSchema
```

这个命令从 `system.webServer/defaultDocument` 部分获取 `FilesElement` 配置对象，然后获取其默认的集合。这两种格式的输出结果是相同的。

## 参数

### -CollectionName
指定要返回的集合的名称。如果未使用该集合的名称，则会返回默认集合。或者，也可以通过 **Get-IISConfigElement** 来获取指定的集合，然后再从这个集合中获取默认集合。

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
指定返回 ConfigurationCollection 所对应的 IIS ConfigurationSection 或 ConfigurationElement。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### Microsoft.Web Adminstration.ConfigurationElement

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[Clear-IISConfigCollection](./Clear-IISConfigCollection.md)

[Get-IISConfigElement](./Get-IISConfigElement.md)

[适用于 Windows PowerShell 的 IIS 管理 cmdlet](./iisadministration.md)

