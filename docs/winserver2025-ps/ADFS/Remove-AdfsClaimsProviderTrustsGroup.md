---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/remove-adfsclaimsprovidertrustsgroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AdfsClaimsProviderTrustsGroup
---

# 删除 AdfsClaimsProviderTrustsGroup

## 摘要
删除一个 AD FS 主张提供者信任组。

## 语法

```
Remove-AdfsClaimsProviderTrustsGroup -TargetIdentifier <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-AdfsClaimsProviderTrustsGroup` cmdlet 用于删除 Active Directory Federation Services (AD FS) 的声明提供者信任组。

## 示例

## 参数

### -TargetIdentifier
指定目标的ID。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
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
展示了如果该cmdlet被运行会发生的情景。但实际上该cmdlet并没有被运行。

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

[Add-AdfsClaimsProviderTrustsGroup](./Add-AdfsClaimsProviderTrustsGroup.md)

[Get-AdfsClaimsProviderTrustsGroup](./Get-AdfsClaimsProviderTrustsGroup.md)

