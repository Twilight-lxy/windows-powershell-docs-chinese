---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/get-iisconfigcollectionelement?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IISConfigCollectionElement
---

# Get-IISConfigCollectionElement

## 摘要
从 IIS 配置集合中获取一个配置元素对象。

## 语法

```
Get-IISConfigCollectionElement [-ConfigCollection] <ConfigurationElementCollection>
 [[-ConfigAttribute] <Hashtable>] [<CommonParameters>]
```

## 描述
`Get-IISConfigCollectionElement` cmdlet 可以获取一个属于指定 `ConfigurationCollection` 的 `ConfigurationElement` 对象。返回的该对象随后可以用于其他需要 `ConfigurationElement` 参数的 cmdlet 中。

## 示例

### 示例 1：通过将集合传递给流水线（pipeline）来获取默认网站的配置元素
```
PS C:\> Get-IISConfigSection -SectionPath "system.applicationHost/sites" | Get-IISConfigCollection | Get-IISConfigCollectionElement -ConfigAttribute @{"name"="Default Web Site"}
```

这个命令通过将集合传递给一个处理流程（pipeline），来获取默认网站的配置信息。

### 示例 2：使用配置集合作为参数来获取一个配置元素
```
PS C:\> $SiteCollection = Get-IISConfigSection -SectionPath "system.applicationHost/sites" | Get-IISConfigCollection
Get-IISConfigCollectionElement -ConfigCollection $SiteCollection -ConfigAttribute @{"name"="Default Web Site"}
```

这个命令获取默认网站的配置元素，然后将该元素存储到变量 $SiteCollection 中。

## 参数

### -ConfigAttribute
指定一个哈希表，其中包含要插入的配置元素的属性信息。如果该哈希表中缺少任何必需的属性，此cmdlet将会失败。

```yaml
Type: Hashtable
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ConfigCollection
指定用于返回集合元素的 **ConfigurationCollection** 对象。如果之前已经获取了一个 ConfigurationCollection 并将其赋值给某个变量，那么就无法通过管道将该对象传递给此 cmdlet，因为管道引擎会尝试对其进行枚举，并传递的是 ConfigurationElement 对象。您可以尝试将整个 Get-IISConfigCollection cmdlet 传递到管道中，或者将其作为参数使用，以获得正确的结果。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### Microsoft.Web.Administration.ConfigurationElementCollection

### System.Collections.Hashtable

## 输出

### System.Object

## 备注

## 相关链接

[New-IISConfigCollectionElement](./New-IISConfigCollectionElement.md)

[Remove-IISConfigCollectionElement](./Remove-IISConfigCollectionElement.md)

[适用于 Windows PowerShell 的 IIS 管理 cmdlet](./iisadministration.md)

