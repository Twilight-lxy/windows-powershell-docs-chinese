---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/new-adfsapplicationgroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-AdfsApplicationGroup
---

# 新的 AdfsApplicationGroup

## 摘要
创建一个应用程序组。

## 语法

```
New-AdfsApplicationGroup [-Name] <String> [[-ApplicationGroupIdentifier] <String>] [-Description <String>]
 [-Disabled] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`New-AdfsApplicationGroup` cmdlet 用于在 Active Directory Federation Services (AD FS) 中创建一个应用程序组。

## 示例

## 参数

### -ApplicationGroupIdentifier
指定应用程序组的ID。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Description
为应用程序组指定一个描述。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Disabled
表示该应用程序组是否已被禁用。

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

### -Name
为应用程序组指定一个名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不生成任何输出。

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

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

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
展示了如果该cmdlet运行会发生什么情况。但实际上该cmdlet并没有被运行。

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
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

字符串对象通过 *ApplicationGroupIdentifier*、*Description* 和 *Name* 参数被接收。

## 输出

### Microsoft.IdentityServer.Management.Resources.ApplicationGroup

当指定 `PassThru` 参数时，该命令会返回一个新的 `ApplicationGroup` 对象。默认情况下，此命令不会生成任何输出。

## 备注

## 相关链接

[ Disable-AdfsApplicationGroup ](./Disable-AdfsApplicationGroup.md)

[Enable-AdfsApplicationGroup](./Enable-AdfsApplicationGroup.md)

[Get-AdfsApplicationGroup](./Get-AdfsApplicationGroup.md)

[Remove-AdfsApplicationGroup](./Remove-AdfsApplicationGroup.md)

[Set-AdfsApplicationGroup](./Set-AdfsApplicationGroup.md)

