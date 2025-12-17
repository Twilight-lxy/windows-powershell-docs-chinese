---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/remove-adfsrelyingpartytrustsgroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AdfsRelyingPartyTrustsGroup
---

# 删除依赖 AdFS 的信任组（Remove-AdfsRelyingPartyTrustsGroup）

## 摘要
删除一个依赖方信任组。

## 语法

```
Remove-AdfsRelyingPartyTrustsGroup -TargetIdentifier <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-AdfsRelyingPartyTrustsGroup` cmdlet 用于删除一个依赖方信任组。

## 示例

## 参数

### -TargetIdentifier
指定要删除的组的ID。

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
在运行cmdlet之前，会提示您进行确认。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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

## 输出

## 备注

## 相关链接

[Add-AdfsRelyingPartyTrustsGroup](./Add-AdfsRelyingPartyTrustsGroup.md)

[Get-AdfsRelyingPartyTrustsGroup](./Get-AdfsRelyingPartyTrustsGroup.md)

