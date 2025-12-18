---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.DeviceHealthAttestation.PowerShell.dll-Help.xml
Module Name: DeviceHealthAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/devicehealthattestation/set-dhascertificatechainpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DHASCertificateChainPolicy
---

# Set-DHASCertificateChainPolicy

## 摘要
设置证书链策略。

## 语法

### SetCertificateChainPolicy（默认值）
```
Set-DHASCertificateChainPolicy [-CertificateChainPolicy] <CertificateChainPolicy> [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### SetCertificateChainPolicyComponents
```
Set-DHASCertificateChainPolicy -RevocationFlag <String> -RevocationMode <String> -VerificationFlags <String>
 -UrlRetrievalTimeout <String> [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DHASCertificateChainPolicy` cmdlet 用于设置设备健康验证（Device Health Attestation）服务所遵循的证书链策略。该证书链策略定义了证书链验证及相关撤销行为的参数。

您可以指定一个 `CertificateChainPolicy` 对象作为输入参数，或者也可以单独指定构成 `CertificateChainPolicy` 的各个组件。需要作为输入指定的组件包括：

- RevocationFlag.
- RevocationMode.
- VerificationFlags.
- UrlRetrievalTimeout.

You must have administrator rights to run this cmdlets.

## 示例

### Example 1: Set certificate chain policy with a CertificateChainPolicy object
```
PS C:\> $policy = Get-DHASCertificateChainPolicy
PS C:\> $policy.RevocationFlag = "ExcludeRoot"
PS C:\> Set-DHASCertificateChainPolicy -CertificateChainPolicy $policy
```

The first command gets the **CertificateChainPolicy** object, and then stores it in the $policy variable.

The second command sets the RevocationFlag property of the policy to ExcludeRoot.

The third command sets the policy to include the new value for RevocationFlag.

### 示例 2：设置证书链策略及其组成部分
```
PS C:\> Set-DHASCertificateChainPolicy -RevocationFlag "ExcludeRoot" -RevocationMode "NoCheck" -VerificationFlags "NoFlag" -UrlRetrievalTimeout "00:01:00"
```

此命令通过为证书链策略的每个组成部分指定一个值来修改该策略。

## 参数

### -CertificateChainPolicy
指定要使用的证书链策略。

```yaml
Type: CertificateChainPolicy
Parameter Sets: SetCertificateChainPolicy
Aliases:

Required: True
Position: 0
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

### -Force
强制命令运行，而无需请求用户确认。

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

### -RevocationFlag
指定一个.NET [X509RevocationFlag 枚举](https://go.microsoft.com/fwlink/?LinkId=821152)。

```yaml
Type: String
Parameter Sets: SetCertificateChainPolicyComponents
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RevocationMode
指定一个.NET [X509RevocationMode 枚举](https://go.microsoft.com/fwlink/?LinkId=821153)。

```yaml
Type: String
Parameter Sets: SetCertificateChainPolicyComponents
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UrlRetrievalTimeout
指定一个.NET [TimeSpan 结构](https://go.microsoft.com/fwlink/?LinkId=821155)。

```yaml
Type: String
Parameter Sets: SetCertificateChainPolicyComponents
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VerificationFlags
用于指定一个.NET [X509VerificationFlags 枚举](https://go.microsoft.com/fwlink/?LinkId=821154)。

```yaml
Type: String
Parameter Sets: SetCertificateChainPolicyComponents
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被执行。

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

### CertificateChainPolicy

## 输出

## 备注

## 相关链接

[Get-DHASCertificateChainPolicy](./Get-DHASCertificateChainPolicy.md)

