---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/remove-iisconfigattribute?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-IISConfigAttribute
---

# 移除 IIS 配置属性

## 摘要
从 IIS 配置节或配置元素属性中删除某个配置属性。

## 语法

```
Remove-IISConfigAttribute [-ConfigElement] <ConfigurationElement> [-AttributeName] <String>
 [<CommonParameters>]
```

## 描述
`Remove-IISConfigAttribute` cmdlet 用于从 Internet Information Services (IIS) 的配置部分或配置元素中删除某个配置属性。被删除的值是该 `ConfigurationElement` 对应的属性值，并不一定代表 해당站点、虚拟目录或文件夹等实际应用中的有效属性值。要获取实际的属性值，务必通过指定尽可能深的路径来检索相应的配置元素。即使该配置属性在当前层级并未定义，系统也会扫描其父级属性，并返回实际的配置元素。之后你就可以对这个配置元素进行操作，以获取、设置或删除相应的属性值。

## 示例

### 示例 1：从 IIS 网站中删除某个配置属性。
```
PS C:\> Get-IISSite "Default Web Site" | Get-IISConfigElement -ChildElementName "limits" | Remove-IISConfigAttribute -AttributeName "MaxUrlSegments"
```

此命令会删除“Default Web Site”中“MaxUrlSegment”属性的配置属性值，使其恢复为父级的默认设置或系统范围内的默认设置。

### 示例 2：从配置存储的不同部分中删除配置属性值：
```
PS C:\> Get-IISConfigSection "system.webServer/asp" | Remove-IISConfigAttribute -AttributeName "ScriptErrorMessage"
```

此命令会删除 `ScriptErrorMessage` 的全局属性值，使其恢复为模式默认值。

## 参数

### -AttributeName
指定要删除的属性的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ConfigElement
指定要从其中删除匹配属性的 IIS ConfigurationSection 或 ConfigurationElement 对象。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### Microsoft.Web.Administration.ConfigurationElement

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[Get-IISConfigAttributeValue](./Get-IISConfigAttributeValue.md)

[Set-IISConfigAttributeValue](./Set-IISConfigAttributeValue.md)

[适用于 Windows PowerShell 的 IIS 管理 cmdlet](./iisadministration.md)

