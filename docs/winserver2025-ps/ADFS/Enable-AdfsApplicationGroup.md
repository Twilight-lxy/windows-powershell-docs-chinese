---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/enable-adfsapplicationgroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-AdfsApplicationGroup
---

# 启用 AdfsApplicationGroup

## 摘要
在 AD FS 中启用一个应用程序组。

## 语法

### ApplicationGroupIdentifier（默认值）
```
Enable-AdfsApplicationGroup [-TargetApplicationGroupIdentifier] <String> [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 名称
```
Enable-AdfsApplicationGroup [-TargetName] <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ApplicationGroupObject
```
Enable-AdfsApplicationGroup [-TargetApplicationGroup] <ApplicationGroup> [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
**Enable-AdfsApplicationGroup** cmdlet 可以在 Active Directory Federation Services (AD FS) 中启用一个应用程序组。

## 示例

## 参数

### -PassThru
返回一个表示您正在操作的该项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -TargetApplicationGroup
指定目标应用程序组。

```yaml
Type: ApplicationGroup
Parameter Sets: ApplicationGroupObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetApplicationGroupIdentifier
指定目标应用程序组标识符。

```yaml
Type: String
Parameter Sets: ApplicationGroupIdentifier
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -TargetName
指定目标名称。

```yaml
Type: String
Parameter Sets: Name
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
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
展示了如果运行该 cmdlet 会发生什么情况。但实际上，这个 cmdlet 并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft IdentityServer.Management.Resources.ApplicationGroup

`ApplicationGroup` 对象是通过 `TargetApplicationGroup` 参数接收到的。

### System.String

`String` 对象通过 `TargetApplicationGroupIdentifier` 和 `TargetName` 参数被接收。

## 输出

### Microsoft IdentityServer.Management.Resources.ApplicationGroup

当指定 `PassThru` 参数时，该命令会返回一个被禁用的 `ApplicationGroup` 对象。默认情况下，此命令不会生成任何输出。

## 备注

## 相关链接

[禁用 AdfsApplicationGroup](./ Disable-AdfsApplicationGroup.md)

[Get-AdfsApplicationGroup](./Get-AdfsApplicationGroup.md)

[New-AdfsApplicationGroup](./New-AdfsApplicationGroup.md)

[Remove-AdfsApplicationGroup](./Remove-AdfsApplicationGroup.md)

[Set-AdfsApplicationGroup](./Set-AdfsApplicationGroup.md)

