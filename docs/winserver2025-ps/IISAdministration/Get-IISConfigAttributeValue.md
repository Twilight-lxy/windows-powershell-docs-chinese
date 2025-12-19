---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/get-iisconfigattributevalue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IISConfigAttributeValue
---

# Get-IISConfigAttributeValue

## 摘要
从 IIS 配置节或配置元素属性中获取配置属性值。

## 语法

```
Get-IISConfigAttributeValue [-ConfigElement] <ConfigurationElement> [-AttributeName] <String>
 [<CommonParameters>]
```

## 描述
`Get-IISConfigAttributeValue` cmdlet 用于从 Internet Information Services (IIS) 的配置部分属性或配置元素属性中获取配置属性值。返回的值是从指定的 `ConfigurationElement` 中提取出来的值，而不一定是某个站点、虚拟目录或文件夹等的实际生效值。为了获得实际的属性值，请始终通过指定尽可能深的路径来检索相应的配置元素。即使该配置属性在当前层级没有被定义，系统也会扫描其父级属性，并返回实际的配置元素。之后您就可以对这个 `ConfigurationElement` 进行操作，以获取、设置或删除配置属性值。

## 示例

### 示例 1：从 IIS 网站中获取配置属性
```
PS C:\> Get-IISSite "Default Web Site" | Get-IISConfigElement -ChildElementName "limits" | Get-IISConfigAttributeValue -AttributeName "MaxUrlSegments"
```

这个命令获取了“Default Web Site”配置属性“MaxUrl_segments”的值。

### 示例 2：从配置存储的不同部分获取配置属性的值
```
PS C:\> Get-IISConfigSection "system.webServer/asp" | Get-IISConfigAttributeValue -AttributeName "ScriptErrorMessage"
An error occurred on the server when processing the URL. Please contact the system administrator. <p/> If you are the system administrator please click <a href="https://go.microsoft.com/fwlink/?LinkID=82731">here</a> to find out more about this error.
```

这个命令用于获取 `ScriptErrorMessage` 的全局属性值。

## 参数

### -AttributeName
指定将要检索的属性的名称。

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
指定要查找属性值的 IIS ConfigurationSection 或 ConfigurationElement 对象。

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

### Microsoft.Web.Administration.ConfigurationElement

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[Set-IISConfigAttributeValue](./Set-IISConfigAttributeValue.md)

[适用于 Windows PowerShell 的 IIS 管理 cmdlet](./iisadministration.md)

