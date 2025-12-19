---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.RemoteAttestation.Server.PowerShell.dll-Help.xml
Module Name: HgsAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsattestation/get-hgsattestationhostgroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-HgsAttestationHostGroup
---

# Get-HgsAttestationHostGroup

## 摘要
根据主机组获取认证策略。

## 语法

```
Get-HgsAttestationHostGroup [-Name <String>] [<CommonParameters>]
```

## 描述
`Get-HgsAttestationHostGroup` cmdlet 可以获取基于 Active Directory 主机组配置的认证策略。若要获取特定的主机组策略，请通过其名称进行指定。

## 示例

### 示例 1：获取所有主机组的策略
```
PS C:\> Get-HgsAttestationHostGroup
```

这个命令可以获取所有使用“Attestation服务”配置的主机组的策略信息。

### 示例 2：获取特定主机组的策略信息
```
PS C:\> Get-HgsAttestationHostGroup -Name "TrustedADHostGroup14"
```

此命令用于获取名为 TrustedADHostGroup14 的主机组的策略。

## 参数

### -Name
指定该 cmdlet 获取策略的目标主机组的友好名称。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

## 输出

### System.Collections.Specialized.StringCollection
此cmdlet返回一个**StringCollection**对象。

## 备注

## 相关链接

[Add-HgsAttestationHostGroup](./Add-HgsAttestationHostGroup.md)

[Remove-HgsAttestationHostGroup](./Remove-HgsAttestationHostGroup.md)

