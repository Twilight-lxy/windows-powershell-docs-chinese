---
description: 使用此主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/set-iisconfigattributevalue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-IISConfigAttributeValue
---

# 设置 IIS 配置属性值

## 摘要
为 IIS 配置节或配置元素属性设置一个配置属性值。

## 语法

```
Set-IISConfigAttributeValue [-ConfigElement] <ConfigurationElement> [-AttributeName] <String>
 [-AttributeValue] <Object> [<CommonParameters>]
```

## 描述
`Set-IISConfigAttributeValue` cmdlet 用于从 Internet Information Services (IIS) 的配置节属性或配置元素属性中设置一个配置属性值。所设置的值仅适用于指定的 `ConfigurationElement`，而不一定代表该站点、虚拟目录或文件夹等的实际生效值。若要设置实际的属性值，请务必通过指定尽可能深的路径来检索相应的配置元素。

## 示例

### 示例 1：设置配置属性的值
```
PS C:\> $ConfigSection = Get-IISConfigSection -SectionPath "system.applicationHost/sites"
PS C:\> $SitesCollection = Get-IISConfigCollection -ConfigElement $ConfigSection
PS C:\> $Site = Get-IISConfigCollectionElement -ConfigCollection $SitesCollection -ConfigAttribute @{"name" = "Default Web Site"}
PS C:\> $Elem = Get-IISConfigElement -ConfigElement $Site -ChildElementName "limits"
PS C:\> Set-IISConfigAttributeValue -ConfigElement $Elem -AttributeName "MaxUrlSegments" -AttributeValue 16
```

此命令将名为“Default Web Site”的IIS网站的配置属性“MaxUrlSegmentes”的值设置为16。

## 参数

### -AttributeName
指定将要设置值的属性的名称。

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

### -AttributeValue
指定属性的新值。

```yaml
Type: Object
Parameter Sets: (All)
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ConfigElement
指定要查找属性值的 IIS ConfigurationSection 或 ConfigurationElement。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### Microsoft.Web.Administration.ConfigurationElement

### System.String

### System.Object

## 输出

### System.Object

## 备注

## 相关链接

[Get-IISConfigAttributeValue](./Get-IISConfigAttributeValue.md)

[适用于 Windows PowerShell 的 IIS 管理cmdlet](./iisadministration.md)

