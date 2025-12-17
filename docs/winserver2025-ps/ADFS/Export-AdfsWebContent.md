---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/export-adfswebcontent?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-AdfsWebContent
---

# 导出 AdFS Web 内容

## 摘要
将所有网页内容对象在特定区域设置（locale）下的属性导出到指定的文件中。

## 语法

```
Export-AdfsWebContent [[-Locale] <CultureInfo>] -FilePath <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Export-AdfsWebContent` cmdlet 可将特定区域设置（locale）下所有 Web 内容对象的属性（包括全局 Web 内容和依赖方 Web 内容）导出到指定的文件中。如果未指定区域设置，该 cmdlet 会导出使用不变区域设置的 Web 内容。`Set-AdfsGlobalWebContent` 和 `Set-AdfsRelyingPartyWebContent` cmdlets 用于添加自定义的 Web 内容。

使用此cmdlet来实现Active Directory Federation Services（AD FS）登录体验中自定义消息的本地化。将网页内容导出为.resx文件，对该文件进行本地化处理，然后使用**Import-AdfsWebContent** cmdlet导入本地化的.resx文件。

## 示例

### 示例 1：为不变的本地化设置导出网页内容
```
PS C:\> Export-AdfsWebContent -FilePath "C:\WebContent\Invariant.resx"
```

此命令会将所有为不变区域设置（invariant locale）定制的网页内容导出到指定的文件中。

### 示例 2：为指定的区域设置导出网页内容
```
PS C:\> Export-AdfsWebContent -Locale en-us -FilePath "C:\WebContent\EnUs.resx"
```

该命令会将所有针对“en-us”语言环境的自定义网页内容导出到指定的文件中。

## 参数

### -FilePath
指定一个文件路径。该cmdlet会将网页内容对象的属性导出到您指定的文件中。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Locale
用于指定一个区域设置（locale）。该cmdlet会输出与所指定的区域设置相关联的网页内容对象的属性信息。

```yaml
Type: CultureInfo
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并未运行该cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Import-AdfsWebContent](./Import-AdfsWebContent.md)

