---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.RemoteAttestation.Server.PowerShell.dll-Help.xml
Module Name: HgsAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsattestation/get-hgsattestationpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-HgsAttestationPolicy
---

# Get-HgsAttestationPolicy

## 摘要
获取 HGS 证明策略。

## 语法

```
Get-HgsAttestationPolicy [[-Name] <String>] [-State <AttestationPolicyState>]
 [-PolicyType <AttestationPolicyType[]>] [-PolicyVersion <PolicyVersion>] [-Stage] [<CommonParameters>]
```

## 描述
`Get-HgsAttestationPolicy` cmdlet 可用于获取 Host Guardian Service (HGS) 的认证策略。

## 示例

### 示例 1：获取所有策略
```
PS C:\> Get-HgsAttestationPolicy
```

此命令会获取当前为认证服务（Attestation service）配置的所有策略。

### 示例 2：通过名称获取保险单
```
PS C:\> Get-HgsAttestationPolicy -Name "BaselineTpmPolicy16"
```

这个命令用于获取名为 BaselineTpmPolicy16 的策略。

### 示例 3：按类型获取策略
```
PS C:\> Get-HgsAttestationPolicy -PolicyType SecureBootSettings
```

此命令用于获取类型为 Tpm 的策略。

### 示例 4：获取所有已启用的策略
```
PS C:\> Get-HgsAttestationPolicy -State Enabled
```

这个命令会获取所有已启用的策略。

## 参数

### -Name
指定此 cmdlet 所获取的策略的名称。可以使用通配符来获取多个策略。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -PolicyType
指定了此cmdlet获取的策略的类型。

```yaml
Type: AttestationPolicyType[]
Parameter Sets: (All)
Aliases:
Accepted values: Unknown, SecureBootEnabled, SecureBootSettings, CiPolicy, UefiDebugDisabled, FullBoot, VsmIdkPresent, BitLockerEnabled, IommuEnabled, PagefileEncryptionEnabled, HypervisorEnforcedCiPolicy, NoHibernation, NoDumps, DumpEncryption, DumpEncryptionKey

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PolicyVersion
保留以供将来使用。

```yaml
Type: PolicyVersion
Parameter Sets: (All)
Aliases:
Accepted values: None, PolicyVersion1503, PolicyVersion1704

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Stage
保留以供将来使用。

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

### -State
指定此cmdlet获取的政策所处的状态。该参数的可接受值为：

- Enabled
- Disabled
- Locked

```yaml
Type: AttestationPolicyState
Parameter Sets: (All)
Aliases:
Accepted values: Disabled, Enabled, Locked

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters (http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 字符串
你可以将字符串通过管道（pipe）传递给这个cmdlet。

## 输出

### AttestationPolicyInfo
此cmdlet返回身份验证策略信息。

## 备注

## 相关链接

[ Disable-HgsAttestationPolicy](./Disable-HgsAttestationPolicy.md)

[Enable-HgsAttestationPolicy](./Enable-HgsAttestationPolicy.md)

[Remove-HgsAttestationPolicy](./Remove-HgsAttestationPolicy.md)

