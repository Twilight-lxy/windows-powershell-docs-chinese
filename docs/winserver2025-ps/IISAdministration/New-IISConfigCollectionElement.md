---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/new-iisconfigcollectionelement?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-IISConfigCollectionElement
---

# New-IISConfigCollectionElement

## 摘要
在 IIS 配置集合中创建一个新的配置元素对象。

## 语法

```
New-IISConfigCollectionElement [-ConfigCollection] <ConfigurationElementCollection>
 [-ConfigAttribute] <Hashtable> [[-AddAt] <UInt32>] [-Passthru] [<CommonParameters>]
```

## 描述
`New-IISConfigCollectionElement` cmdlet 用于在指定的 Internet Information Services (IIS) 配置集合中创建一个新的 `ConfigurationElement`。

## 示例

### 示例 1：将一个新的文件名添加到默认文档列表中
```
PS C:\> $ConfigSection = Get-IISConfigSection -SectionPath "system.webServer/defaultDocument"
PS C:\> $DefaultDocumentCollection = Get-IISConfigCollection -ConfigElement $ConfigSection -CollectionName "files"
PS C:\> New-IISConfigCollectionElement
  -ConfigCollection $DefaultDocumentCollection -ConfigAttribute @{"Value" = "MyDefDoc.htm"}
```

这个命令会在默认文档列表中创建一个条目。

### 示例 2：在默认文档列表的顶部添加一个新文件名
```
PS C:\> Get-IISConfigSection -SectionPath "system.webServer/defaultDocument" | Get-IISConfigCollection -CollectionName "files" | New-IISConfigCollectionElement  -ConfigAttribute @{Value = "MyDefDoc.htm"} -AddAt 0
```

这个命令会在默认文档列表中创建一个新的条目，并将这个新条目设置为集合中的第一个元素。这是通过将 *AddAt* 参数的值设置为 0 来实现的；因为集合中的第一个元素的索引始终是 0。

## 参数

### -AddAt
指定新配置元素的集合索引；默认情况下，新元素会被添加到集合的末尾。集合索引用于确定集合中各项的顺序：集合中的第一个元素是索引为 0 的项，第二个元素是索引为 1 的项，依此类推。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ConfigAttribute
指定一个哈希表，其中包含要插入的配置元素的属性信息。如果这个哈希表中缺少任何必需的属性，该cmdlet将会失败。

```yaml
Type: Hashtable
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ConfigCollection
指定新集合元素将被添加到的 **ConfigurationCollection** 对象。如果之前已经获取了一个 **ConfigurationCollection** 并将其赋值给某个变量，那么无法通过管道将该对象传递给此 cmdlet，因为管道引擎会尝试遍历该集合，从而传递出的是 **ConfigurationElement** 对象。此时，可以选择将整个 Get-IISConfigCollection cmdlet 传递到管道中，或者将其作为参数使用，以获得正确的结果。

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

### -Passthru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters (http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Web ADMINISTRATION.ConfigurationElementCollection

### System.Collections.Hashtable

### System.UInt32

## 输出

### System.Object

## 备注

## 相关链接

[Get-IISConfigCollectionElement](./Get-IISConfigCollectionElement.md)

[适用于 Windows PowerShell 的 IIS 管理 cmdlet](./iisadministration.md)

