---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/remove-iisconfigcollectionelement?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-IISConfigCollectionElement
---

# 删除 IISConfigCollectionElement

## 摘要
从 IIS 配置集合中移除一个配置元素对象。

## 语法

```
Remove-IISConfigCollectionElement [-ConfigCollection] <ConfigurationElementCollection>
 [[-ConfigAttribute] <Hashtable>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-IISConfigCollectionElement` cmdlet 用于从指定的 Internet Information Services (IIS) 配置集合中删除一个 `ConfigurationElement`。

## 示例

### 示例 1：从默认文档列表中删除一个文件名
```
PS C:\> $ConfigSection = Get-IISConfigSection -SectionPath "system.webServer/defaultDocument"
PS C:\> Get-IISConfigCollection $ConfigSection "Files" | Remove-IISConfigCollectionElement  -ConfigAttribute @{"Value" = "MyDefDoc.htm"}
```

此命令会从默认文档列表中删除一个配置条目。

## 参数

### -ConfigAttribute
指定一个哈希表，其中包含在集合中查找要删除的配置元素时需要匹配的属性。对于未指定的配置属性，将不会进行任何过滤操作。如果省略此参数，则会删除集合中的所有元素。

```yaml
Type: Hashtable
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ConfigCollection
指定要从哪个 `ConfigurationCollection` 中移除匹配的 `ConfigurationElements`。

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
在运行该 cmdlet 之前，会提示您进行确认。

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
展示了如果该cmdlet运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### Microsoft.Web.Administration.ConfigurationElementCollection

### System.Collections.Hashtable

## 输出

### System.Object

## 备注

## 相关链接

[Get-IISConfigCollectionElement](./Get-IISConfigCollectionElement.md)

[New-IISConfigCollectionElement](./New-IISConfigCollectionElement.md)

[适用于 Windows PowerShell 的 IIS 管理 cmdlet](./iisadministration.md)

