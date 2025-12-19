---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.RemoteAttestation.Server.PowerShell.dll-Help.xml
Module Name: HgsAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsattestation/add-hgsattestationhostgroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-HgsAttestationHostGroup
---

# Add-HgsAttestationHostGroup

## 摘要
为 Active Directory 主机组配置添加一个认证策略。

## 语法

### hostGroup
```
Add-HgsAttestationHostGroup -Name <String> -HostGroup <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### sid
```
Add-HgsAttestationHostGroup -Name <String> -Identifier <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-HgsAttestationHostGroup` cmdlet 可以添加一种基于 Active Directory 主机组配置的认证策略。您可以通过名称或安全标识符（SID）来指定所需的主机组。

## 示例

### 示例 1：添加一个主机组
```
PS C:\> Add-HgsAttestationHostGroup -Name "TrustedADHostGroup14" -Identifier $Sid
```

此命令将一个来自 Active Directory 网络的主机组添加到认证服务（Attestation service）中。*Identifier* 参数指定了存储在 $Sid 变量中的 SID（安全标识符）。运行此命令后，认证服务会信任属于该主机组的所有主机来托管受保护的虚拟机。

## 参数

### -HostGroup
指定一个主机组的名称，此cmdlet将基于该组来制定策略。请包含域名。

```yaml
Type: String
Parameter Sets: hostGroup
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identifier
指定该主机组的SID（安全标识符），此cmdlet将基于该SID来制定相应的策略。

```yaml
Type: String
Parameter Sets: sid
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定主机组的友好名称。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

## 输出

## 备注

## 相关链接

[Get-HgsAttestationHostGroup](./Get-HgsAttestationHostGroup.md)

[Remove-HgsAttestationHostGroup](./Remove-HgsAttestationHostGroup.md)

