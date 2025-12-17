---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/export-adfswebtheme?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-AdfsWebTheme
---

# 导出 AdFSWebTheme 主题

## 摘要
将一个网页主题导出到一个文件夹中。

## 语法

### IdentifierName
```
Export-AdfsWebTheme -Name <String> -DirectoryPath <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### RelyingPartyName
```
Export-AdfsWebTheme -RelyingPartyName <String> -DirectoryPath <String> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### IdentifierObject
```
Export-AdfsWebTheme -WebTheme <WebThemeBase> -DirectoryPath <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Export-AdfsWebTheme` cmdlet 将一个 Web 主题对象导出到一个文件夹中。该 cmdlet 会创建与 Web 主题设置相对应所需的文件夹。您可以使用此 cmdlet 根据现有的主题（例如 Active Directory Federation Services (AD FS) 提供的默认主题）来创建新的 Web 主题。

## 示例

#### 示例 1：导出一个网页主题
```
PS C:\> Export-AdfsWebTheme -Name "Theme01" -DirectoryPath "C:\WebTheme"
```

这个命令会将一个名为“Theme01”的网页主题导出到C:\WebTheme文件夹中。该命令会将所有文件（包括层叠样式表、JavaScript文件和图片）放入指定文件夹中的相应子文件夹中。

## 参数

### -DirectoryPath
指定一个文件夹的路径。该cmdlet会将网页主题导出到您指定的文件夹中。

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

### -Name
用于指定一个名称。该 cmdlet 会导出具有你所指定名称的网页主题。

```yaml
Type: String
Parameter Sets: IdentifierName
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -RelyingPartyName
指定依赖方的名称。

```yaml
Type: String
Parameter Sets: RelyingPartyName
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WebTheme
用于指定一个 **AdfsWebTheme** 对象。该 cmdlet 会导出您所指定的主题。若要获取一个 **AdfsWebTheme** 对象，可以使用 **Get-AdfsWebTheme** cmdlet。

```yaml
Type: WebThemeBase
Parameter Sets: IdentifierObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
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
展示了如果该 cmdlet 被运行时会发生什么情况。但实际上，这个 cmdlet 并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-AdfsWebTheme](./Get-AdfsWebTheme.md)

[New-AdfsWebTheme](./New-AdfsWebTheme.md)

[Remove-AdfsWebTheme](./Remove-AdfsWebTheme.md)

[Set-AdfsWebTheme](./Set-AdfsWebTheme.md)

