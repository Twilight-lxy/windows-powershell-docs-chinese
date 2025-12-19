---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.RemoteAttestation.Server.PowerShell.dll-Help.xml
Module Name: HgsAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsattestation/remove-hgsattestationhostgroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-HgsAttestationHostGroup
---

# 删除 HgsAttestationHostGroup

## 摘要
根据主机组删除一个认证策略。

## 语法

```
Remove-HgsAttestationHostGroup [-Name] <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-HgsAttestationHostGroup` cmdlet 用于从 Host Guardian Service (HGS) 中删除基于 Active Directory 主机组配置的认证策略。

## 示例

### 示例 1：删除一个主机组
```
PS C:\> Remove-HgsAttestationHostGroup -Name "TrustedADHostGroup14"
```

此命令会从认证服务中删除名为“TrustedADHostGroup14”的主机组。如果某个受保护的主机同时属于该主机组且不属于任何其他可信主机组，那么该主机将无法再获取新的认证证书。

## 参数

### -Name
指定该主机组的友好名称；此 cmdlet 将从该组中删除相应的策略。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您确认是否要继续执行。

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
展示了如果该cmdlet运行会发生的结果。不过，这个cmdlet实际上并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters (http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Add-HgsAttestationHostGroup](./Add-HgsAttestationHostGroup.md)

[Get-HgsAttestationHostGroup](./Get-HgsAttestationHostGroup.md)

