---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfswebtheme?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsWebTheme
---

# Get-AdfsWebTheme

## 摘要
可以获取网页主题（即用于设计网站的视觉样式和元素）。

## 语法

```
Get-AdfsWebTheme [-Name <String>] [<CommonParameters>]
```

## 描述
`Get-AdfsWebTheme` cmdlet 用于获取 `AdfsWebTheme` 对象。可以通过名称来指定一个网页主题；如果未指定名称，该 cmdlet 将获取所有 `AdfsWebTheme` 对象。

## 示例

### 示例 1：获取所有网页主题
```
PS C:\> Get-AdfsWebTheme

Name                    : Default
IsBuiltinTheme          : True
StyleSheet              : {[, System.Byte[]]}
RTLStyleSheet           : {42, 32, 123, 13...}
Logo                    : {[, System.Byte[]]}
Illustration            : {[, System.Byte[]]}
AdditionalFileResources : {[/adfs/portal/script/onload.js, System.Byte[]], [/adfs/portal/images/idp/localsts.png, System.Byte[]], [/adfs/portal/images/idp/idp.png,
System.Byte[]], [/adfs/portal/images/idp/otherorganizations.png, System.Byte[]]}
```

这个命令可以获取 Active Directory Federation Services (AD FS) 中所有可用的 Web 主题。

### 示例 2：获取一个已命名的网页主题
```
PS C:\> Get-AdfsWebTheme -Name "Theme01"
Name                    : Theme01
IsBuiltinTheme          : False
StyleSheet              : {[, System.Byte[]]}
RTLStyleSheet           : {42, 32, 123, 13...}
Logo                    : {[, System.Byte[]]}
Illustration            : {[, System.Byte[]]}
AdditionalFileResources : {[/adfs/portal/script/onload.js, System.Byte[]], [/adfs/portal/images/idp/localsts.png, System.Byte[]], [/adfs/portal/images/idp/idp.png,
System.Byte[]], [/adfs/portal/images/idp/otherorganizations.png, System.Byte[]]}
```

这个命令用于获取名为“Theme01”的主题。

## 参数

### -Name
指定一个名称。该cmdlet会获取具有您所指定名称的网页主题。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### Microsoft.IdentityServer.ManagementResources.AdfsWebTheme; Microsoft_identityServer.ManagementResources.AdfsWebTheme[]
此cmdlet生成一个Web自定义对象**SystemIdentityServer.Management.Resources.AdfsWebTheme**，或者这些对象的数组。该对象包含以下属性：

- Name: **System.String**
- IsBuiltinTheme: **System.Boolean**
- StyleSheet: **IDictionary\<CultureInfo, byte\[\]\>**
- RTLStyleSheet: **byte\[\]**
- Logo: **IDictionary\<CultureInfo, byte\[\]\>**
- Illustration: **IDictionary\<CultureInfo, byte\[\]\>**
- AdditionalFileResources: **IDictionary\<string, byte\[\]\>**

## 备注

## 相关链接

[Export-AdfsWebTheme](./Export-AdfsWebTheme.md)

[New-AdfsWebTheme](./New-AdfsWebTheme.md)

[Remove-AdfsWebTheme](./Remove-AdfsWebTheme.md)

[Set-AdfsWebTheme](./Set-AdfsWebTheme.md)

