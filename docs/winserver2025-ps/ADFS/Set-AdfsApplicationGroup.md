---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfsapplicationgroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsApplicationGroup
---

# 设置 AdFS 应用程序组

## 摘要
修改应用程序组。

## 语法

### ApplicationGroupIdentifier（默认值）
```
Set-AdfsApplicationGroup [-TargetApplicationGroupIdentifier] <String> [-Name <String>]
 [-ApplicationGroupIdentifier <String>] [-Description <String>] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 名称
```
Set-AdfsApplicationGroup [-TargetName] <String> [-Name <String>] [-ApplicationGroupIdentifier <String>]
 [-Description <String>] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ApplicationGroupObject
```
Set-AdfsApplicationGroup [-TargetApplicationGroup] <ApplicationGroup> [-Name <String>]
 [-ApplicationGroupIdentifier <String>] [-Description <String>] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-AdfsApplicationGroup` cmdlet 用于修改 Active Directory Federation Services (AD FS) 中的应用程序组。

## 示例

## 参数

### -ApplicationGroupIdentifier
指定应用程序组的ID。

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

### -Name
为应用程序组指定一个名称。

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

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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
用于指定应用程序组的ID。

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
指定应用程序组的名称。

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
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

字符串对象通过 *ApplicationGroupIdentifier*、*Description*、*Name*、*TargetApplicationGroupIdentifier* 和 *TargetName* 参数被接收。

### Microsoft.IdentityServer.Management.Resources.ApplicationGroup

`ApplicationGroup` 对象是通过 `TargetApplicationGroup` 参数接收到的。

## 输出

### Microsoft.IdentityServer.Management.Resources.ApplicationGroup

当指定 `PassThru` 参数时，会返回更新后的 `ApplicationGroup` 对象。默认情况下，此 cmdlet 不生成任何输出。

## 备注

## 相关链接

[ Disable-AdfsApplicationGroup](./Disable-AdfsApplicationGroup.md)

[Enable-AdfsApplicationGroup](./Enable-AdfsApplicationGroup.md)

[Get-AdfsApplicationGroup](./Get-AdfsApplicationGroup.md)

[New-AdfsApplicationGroup](./New-AdfsApplicationGroup.md)

[Remove-AdfsApplicationGroup](./Remove-AdfsApplicationGroup.md)

